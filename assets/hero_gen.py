#!/usr/bin/env python3
"""Generate assets/hero.svg: a grid-locked, two-ink editorial header.

Grid (Müller-Brockmann tokens): 12 columns, 24px gutters, 72px margins, 1296px content width,
8px baseline, 24px leading. Every ink edge lands on a column line and every baseline on the 8px grid;
the script prints a verification table and exits with GRID VERIFY: PASS/FAIL.

Inks (mono-color): substrate Cool Gray #E9E9E5, Charcoal #30343A (type plate, with a 78% tint for the
data strip), Signal Red #C83232 (image plate: a halftone-screened dependency graph). Text is shaped with
HarfBuzz and converted to outlines, so the SVG renders identically without any fonts installed.

Usage:  python3 hero_gen.py <fonts_dir> <out_dir> [--grid]
    fonts_dir must contain Inter-Variable.ttf (Inter[opsz,wght].ttf from github.com/google/fonts/tree/main/ofl/inter)
    and IBMPlexMono-Regular.ttf + IBMPlexMono-Medium.ttf (github.com/google/fonts/tree/main/ofl/ibmplexmono).
    --grid also writes hero-grid.svg with the column/baseline overlay for checking alignment.
Deps:   pip install fonttools uharfbuzz
"""
import hashlib, io, math, sys, json
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb

args = [a for a in sys.argv[1:] if not a.startswith("--")]
FONTS = args[0] if args else "fonts"
OUT = args[1] if len(args) > 1 else "."
WITH_GRID = "--grid" in sys.argv

# ---------- grid tokens (single source of truth) ----------
T = dict(cols=12, bl=8, lh=24, gutter=24, margin=72, maxw=1296, W=1440, H=480)
COL_W = (T["maxw"] - (T["cols"] - 1) * T["gutter"]) / T["cols"]  # 86
def col_start(i): return T["margin"] + (i - 1) * (COL_W + T["gutter"])
def col_end(i): return col_start(i) + COL_W
assert col_end(12) == T["W"] - T["margin"]

# ---------- palette ----------
SUBSTRATE = "#E9E9E5"   # Cool Gray (mono-color substrate_cool_gray)
INK_TYPE = "#30343A"     # Charcoal
INK_IMAGE = "#C83232"    # Signal Red

# ---------- content (all user-supplied facts) ----------
NAME = "Zachary Zhang"
LABEL = "AI PRODUCT ENGINEER"
STRIP = [
    ["New York, NY", "Building in AI since 2019"],
    ["New York University", "M.S. Electrical Engineering", "M.S. Project Management"],
    ["Co-founder & CTO", "GiraStyle AI, Aedylon, KOIN", "Omarchy Chinese maintainer"],
    ["Kigi CLI · Agent Company", "Elydora · Tessovis · CityOS"],
]
INK_SOFT = "#5B5F64"     # 78% tint of Charcoal on the substrate (grid-system "soft ink"); a density change, not a third ink

# ---------- typography ----------
class Face:
    def __init__(self, tt, data):
        self.tt = tt
        self.upem = tt["head"].unitsPerEm
        self.gs = tt.getGlyphSet()
        self.order = tt.getGlyphOrder()
        self.hbfont = hb.Font(hb.Face(data))
        self.hbfont.scale = (self.upem, self.upem)

    def shape(self, text):
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {"kern": True, "liga": True})
        return list(zip(buf.glyph_infos, buf.glyph_positions))

    def layout(self, text, size, x, baseline, tracking=0.0):
        """Return (path_d, ink_left, ink_right). tracking is in em."""
        sc = size / self.upem
        pen = SVGPathPen(self.gs)
        pen_x = 0.0
        ink_l = ink_r = None
        for info, pos in self.shape(text):
            g = self.order[info.codepoint]
            gx = x + (pen_x + pos.x_offset) * sc
            gy = baseline - pos.y_offset * sc
            self.gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, gx, gy)))
            bp = BoundsPen(self.gs); self.gs[g].draw(bp)
            if bp.bounds:
                l = gx + bp.bounds[0] * sc; r = gx + bp.bounds[2] * sc
                ink_l = l if ink_l is None else min(ink_l, l)
                ink_r = r if ink_r is None else max(ink_r, r)
            pen_x += pos.x_advance + tracking * self.upem
        return pen.getCommands(), ink_l, ink_r

    def aligned(self, text, size, target_x, baseline, tracking=0.0):
        """Place text so the first glyph's INK edge lands on target_x."""
        _, l0, _ = self.layout(text, size, 0.0, baseline, tracking)
        return self.layout(text, size, target_x - l0, baseline, tracking)

def inter(wght, opsz):
    vf = TTFont(FONTS + "/Inter-Variable.ttf")
    inst = instantiateVariableFont(vf, {"wght": wght, "opsz": opsz}, inplace=False)
    b = io.BytesIO(); inst.save(b)
    return Face(inst, b.getvalue())

def plex(path):
    tt = TTFont(path)
    return Face(tt, open(path, "rb").read())

display = inter(700, 32)
mono = plex(FONTS + "/IBMPlexMono-Regular.ttf")
mono_md = plex(FONTS + "/IBMPlexMono-Medium.ttf")

# ---------- placement (every y is a baseline multiple, every x a column line) ----------
placed = []   # for verification
def put(name, d, ink_l, ink_r, baseline, col_from, col_to, fill=INK_TYPE, extra=""):
    placed.append(dict(name=name, ink_l=ink_l, ink_r=ink_r, baseline=baseline, col_from=col_from, col_to=col_to))
    return f'<path d="{d}" fill="{fill}"{extra}/>'

charcoal = []

# Label, top-left, mono medium 18px, tracked caps
LABEL_SIZE = 18
d, l, r = mono_md.aligned(LABEL, LABEL_SIZE, col_start(1), 96, tracking=0.10)
charcoal.append(put("label", d, l, r, 96, 1, 3))

# Name: size chosen so the ink spans from col 1 to just inside col 12
NAME_BASE = 280
NAME_TRACK = -0.032
target_w = col_end(10) - col_start(1) - 68   # ink ends around x=1090; the disc crosses the last letters
_, l0, r0 = display.layout(NAME, 100.0, 0.0, 0.0, NAME_TRACK)
NAME_SIZE = math.floor(target_w / (r0 - l0) * 100.0)
d, l, r = display.aligned(NAME, NAME_SIZE, col_start(1), NAME_BASE, NAME_TRACK)
charcoal.append(put("name", d, l, r, NAME_BASE, 1, 12))
name_ink_right = r
name_d = d

# Rule: one charcoal rule across all 12 columns
RULE_Y = 328
charcoal.append(f'<rect x="{col_start(1)}" y="{RULE_Y}" width="{T["maxw"]}" height="2" fill="{INK_TYPE}"/>')
placed.append(dict(name="rule", ink_l=col_start(1), ink_r=col_end(12), baseline=RULE_Y, col_from=1, col_to=12))

# Data strip: 4 cells x 3 columns, mono 18px, baselines 352/376/400
STRIP_SIZE = 18
for ci, cell in enumerate(STRIP):
    c0 = 1 + ci * 3
    for li, line in enumerate(cell):
        base = 352 + li * T["lh"]
        d, l, r = mono.aligned(line, STRIP_SIZE, col_start(c0), base)
        charcoal.append(put(f"strip{ci+1}.{li+1}", d, l, r, base, c0, c0 + 2, fill=INK_SOFT))

# ---------- red plate: screened graph (abstract symbol extraction) ----------
seed = int(hashlib.sha256(f"graph|{NAME}|charcoal+signal_red|type-led".encode()).hexdigest()[:8], 16)
s1 = (seed % 1000) / 1000 * math.tau; s2 = ((seed // 1000) % 1000) / 1000 * math.tau

C = (1140.0, 88.0); R = 170.0         # dominant node, cropped by the top edge; crosses the tail of the name
HL = (C[0] - 0.05 * R, C[1] + 0.35 * R)  # highlight inside the visible part: paper shows through where the name crosses
PITCH = 7.0; THETA = math.radians(22.5)
red = []
dots = []
ct, st = math.cos(THETA), math.sin(THETA)
n = int(2 * R / PITCH) + 4
for i in range(-n, n + 1):
    for j in range(-n, n + 1):
        x = C[0] + (i * PITCH * ct - j * PITCH * st)
        y = C[1] + (i * PITCH * st + j * PITCH * ct)
        if math.hypot(x - C[0], y - C[1]) > R + PITCH: continue
        if y < -PITCH or x > T["W"] + PITCH: continue
        dh = math.hypot(x - HL[0], y - HL[1])
        t = max(0.0, min(1.0, (dh - 0.15 * R) / (0.90 * R)))
        rad = 0.5 * PITCH * 1.14 * math.sqrt(t)
        rad *= 1 + 0.07 * math.sin(0.021 * x + s1) * math.cos(0.017 * y + s2)   # halftone density drift 7%
        if rad < 0.55: continue
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad:.2f}"/>')
red.append(f'<clipPath id="disc"><circle cx="{C[0]}" cy="{C[1]}" r="{R}"/></clipPath>')
red.append(f'<g clip-path="url(#disc)" fill="{INK_IMAGE}">' + "".join(dots) + "</g>")

# worker nodes + directed edges from the dominant node
NODES = [((860.0, 96.0), 13.0), ((1384.0, 176.0), 11.0), ((1240.0, 300.0), 10.0), ((768.0, 40.0), 8.0)]
EDGE_FROM = [C, C, C, (860.0, 96.0)]
edges = []
for (nc, nr), src in zip(NODES, EDGE_FROM):
    sr = R if src == C else 13.0
    dx, dy = nc[0] - src[0], nc[1] - src[1]; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    ax, ay = src[0] + ux * (sr + 8), src[1] + uy * (sr + 8)          # leave a paper gap at the rim
    tipx, tipy = nc[0] - ux * (nr + 6), nc[1] - uy * (nr + 6)        # arrow tip stops before the node
    bx, by = tipx - ux * 16, tipy - uy * 16; px, py = -uy * 6.5, ux * 6.5
    edges.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{INK_IMAGE}" stroke-width="3"/>')
    edges.append(f'<polygon points="{tipx:.1f},{tipy:.1f} {bx+px:.1f},{by+py:.1f} {bx-px:.1f},{by-py:.1f}" fill="{INK_IMAGE}"/>')
    edges.append(f'<circle cx="{nc[0]}" cy="{nc[1]}" r="{nr}" fill="{INK_IMAGE}"/>')
red.append("".join(edges))

# ---------- guides (debug only) ----------
guides = []
for i in range(1, 13):
    guides.append(f'<rect x="{col_start(i)}" y="0" width="{COL_W}" height="{T["H"]}" fill="rgba(0,150,140,0.10)" stroke="rgba(0,150,140,0.5)" stroke-width="1"/>')
for y in range(0, T["H"] + 1, T["bl"]):
    strong = (y % T["lh"] == 0)
    guides.append(f'<line x1="{T["margin"]}" y1="{y}" x2="{T["W"]-T["margin"]}" y2="{y}" stroke="rgba(0,150,140,{0.45 if strong else 0.15})" stroke-width="1"/>')
guides.append(f'<line x1="{T["margin"]}" y1="0" x2="{T["margin"]}" y2="{T["H"]}" stroke="#e4002b" stroke-width="1"/>')
guides.append(f'<line x1="{T["W"]-T["margin"]}" y1="0" x2="{T["W"]-T["margin"]}" y2="{T["H"]}" stroke="#e4002b" stroke-width="1"/>')

def svg(with_guides):
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{T["W"]}" height="{T["H"]}" viewBox="0 0 {T["W"]} {T["H"]}" role="img" aria-labelledby="t d">\n'
            f'<title id="t">Zachary Zhang</title>\n<desc id="d">Zachary Zhang, AI product engineer. Two-ink editorial header: charcoal type and a signal-red halftone dependency graph on cool gray paper.</desc>\n')
    body = (f'<rect width="{T["W"]}" height="{T["H"]}" fill="{SUBSTRATE}"/>\n'
            f'<mask id="ko"><rect width="{T["W"]}" height="{T["H"]}" fill="#fff"/><path d="{name_d}" fill="#000" stroke="#000" stroke-width="9" stroke-linejoin="round"/></mask>\n'
            f'<g id="plate-red" mask="url(#ko)">{"".join(red)}</g>\n'
            f'<g id="plate-charcoal">{"".join(charcoal)}</g>\n')
    if with_guides: body += f'<g id="guides">{"".join(guides)}</g>\n'
    return head + body + "</svg>\n"

open(OUT + "/hero.svg", "w").write(svg(False))
if WITH_GRID: open(OUT + "/hero-grid.svg", "w").write(svg(True))

# ---------- verification ----------
ok = True
print(f"name size {NAME_SIZE}px  ink {placed[1]['ink_l']:.1f}..{name_ink_right:.1f}  (content 72..1368)  scale jump {NAME_SIZE/STRIP_SIZE:.1f}x")
for p in placed:
    cs, ce = col_start(p["col_from"]), col_end(p["col_to"])
    dx = p["ink_l"] - cs
    over = p["ink_r"] - ce
    bl_ok = p["baseline"] % T["bl"] == 0
    good = abs(dx) <= 1.0 and over <= 0.5 and bl_ok
    ok &= good
    print(f"  {'ok ' if good else 'BAD'} {p['name']:<10} ink-left {p['ink_l']:8.2f} col{p['col_from']:>2} start {cs:7.1f} (dx {dx:+.2f})  ink-right {p['ink_r']:8.1f} <= col{p['col_to']:>2} end {ce:7.1f} (over {over:+.1f})  baseline {p['baseline']} {'on-grid' if bl_ok else 'OFF-GRID'}")
print("dots:", len(dots), " | GRID VERIFY:", "PASS" if ok else "FAIL")
