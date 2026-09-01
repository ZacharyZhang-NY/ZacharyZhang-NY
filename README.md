<img alt="Zachary Zhang — AI Product Engineer" src="assets/hero.svg" width="100%" />

[zacharyzhang.com](https://zacharyzhang.com) · [LinkedIn](https://www.linkedin.com/in/zacharyzhangee/) · [yang@zacharyzhang.com](mailto:yang@zacharyzhang.com)

## About

Hi, I'm Zachary Zhang, an AI product engineer with an electrical engineering background and dual master's degrees from NYU (Electrical Engineering and Project Management). I've been building in AI since 2019, as a co-founder, core investor, and full-time engineer, shipping ten-plus products and independent projects across fintech, pharmaceutical compliance, consumer AI, and industrial edge computing. I work at the intersection of product and engineering, taking end-to-end ownership of the full product lifecycle.

## Projects

### AI agents and infrastructure

**[Kigi CLI](https://kigicli.dev)** · `Rust` `Multi-agent` `TUI` · [source](https://github.com/ZacharyZhang-NY/Kigi-CLI)  
AI coding agent written in Rust for complex software engineering tasks, usable as a terminal TUI, in headless CI, or inside editors through ACP. Its core is Graph Engineering: a Planner agent turns a high-level goal into a DAG of dependent tasks, checks it for cycles, missing nodes, and duplicates, and runs independent tasks in parallel with each Worker agent in its own Git worktree; a Verifier agent checks every finished node and sends failures back, a Final Verifier re-checks the overall goal, and the graph can be replanned mid-run and resumed across sessions. An Agent Swarm mode applies the same machinery to large refactors, migrations, reviews, and test writing, and one multi-model runtime works with Kimi Code, Claude, OpenAI Codex, GitHub Copilot, Grok, and API providers including OpenAI, Anthropic, Gemini, DeepSeek, Qwen, MiniMax, Z.AI, and Moonshot. Runs on macOS, Linux, and Windows with a single-file install, auto-update, and zero telemetry.

**[Agent Company](https://agent-company.dev)** · `Electron` `TypeScript` `SQLite`  
Desktop platform that runs multiple AI agents as a long-lived organization: you create a company, departments, roles, and agents, a top-level goal is broken down into Department → Role → Agent → Task, each agent gets context and tool permissions from its position, and a pixel-art office shows what every agent is doing. Built with Electron, SQLite, and Zod-validated IPC, with locally encrypted credentials, an audit log for every important state change, and a Policy Engine and Approval Flow that decide whether a high-privilege action runs automatically, waits for human approval, or is blocked once agents connect to real AI providers, browsers, enterprise services, and social media accounts.

**[Elydora Infra](https://elydora.com)** · `Ed25519` `Hash chain` `Protocol`  
Accountability and audit infrastructure for autonomous AI agents: every key action becomes a verifiable, tamper-evident, traceable record, signed with Ed25519 and linked into a hash chain so that changing any historical record breaks verification of everything after it. The Elydora Responsibility Protocol (ERP) defines this as an open protocol independent of any model, framework, or application, with four core structures: EOR (operation records), ECH (chain hashes), EAR (acknowledgement receipts), and EER (epoch roots). Built for coding agents, enterprise and financial agents, multi-agent systems, and autonomous organizations that hold real assets and execution rights.

**[Tessovis](https://tessovis.com)** · `Ontology` `Action Engine` `Simulation`  
Self-hosted ontology runtime for enterprises that maps data spread across ERP, MES, WMS, databases, files, and event streams into business objects with explicit semantics, relationships, permissions, and behavior, so people and AI agents work on one enterprise model. An Ontology Kernel turns tables, fields, and APIs into Object, Property, Link, Function, and Action; reads go through the Object Runtime and writes through an Action Engine that validates parameters, checks permissions, runs approvals, records audits, and handles transactions before writing back to the source systems. AI agents act as permission-bounded operators with high-risk actions routed to human approval, and an Observed World / Simulated World design forks the current state into an isolated sandbox for optimization, causal analysis, and multi-agent or discrete-event simulation before a validated plan becomes real actions. Includes process mining, a model runtime, an application builder, and a type-safe OSDK, and supports private and offline deployment.

**CityOS** · `Multi-agent` `Ontology` `Simulation`  
AI city operating system for city governance and government decision making, built on a DataOS + AgentOS architecture: population, traffic, business, industry, public facilities, events, and public opinion data are mapped into city digital objects linked by an ontology, and a city-level multi-agent system covering industry and economy, traffic, public services, safety, enterprise services, and public opinion answers natural-language questions such as why a district's consumption changed or what is causing congestion, mapping results back to specific objects and areas. Prediction and simulation compare options for population and traffic shifts, holiday crowds, investment policy, resource allocation, extreme weather, and public events before a policy is executed, and an Action layer turns analysis into tasks for departments, agents, IoT devices, and third-party systems. Completed a POC for the Kuala Lumpur city government in Malaysia and placed third in a CityOS hackathon.

### Products

**[KOIN AI](https://koin.ai)** · `Swift` `Kotlin` `Next.js` `Multi-agent`  
AI investment analysis and automated asset management platform for the US market, built from zero as co-founder, CTO, and core investor: native iOS and Android apps, a web product, and a financial data platform that continuously processes data, computes indicators, and runs AI analysis for about 20,000 US stocks and 20,000+ ETFs. KOIN Brain, a 7×24 multi-agent market monitoring system, watches prices, company data, news, events, and user portfolios for analysis, risk identification, and decision support, and connects to users' brokerage accounts for real-time analysis and automated portfolio management. I also worked on brokerage and trading-system integration and the SEC/FINRA-related qualifications that allow AI-automated management of user securities accounts, one of the earlier platforms in the US to reach that model.

**[GiraStyle AI](https://girastyleai.com)** · `SwiftUI` `React` `TypeScript` `TanStack`  
AI fashion platform with a consumer-facing native iOS app and an enterprise web platform. I handled product requirements, interaction flows, and UI/UX, built the iOS app in SwiftUI with AI-driven outfit recommendations, style understanding, and personalization, built the enterprise platform in React, TypeScript, and TanStack as one interface for business, data, and AI features, and own the system architecture, API design, data models, and permission system that connect the mobile app, enterprise console, and AI services.

**[Aedylon](https://aedylon.com)** · `Rust` `Workflow` `Payments`  
AI advertising production and delivery platform built from zero: the website, client portal, internal admin, and review platform on the front end, and a Rust backend covering project management, permissions, files, tasks, review, version management, and payments. Each ad project runs through a state machine, from client onboarding, quote, and deposit through production, internal review, client review, revisions, final payment, and delivery of the final HD assets, with dynamic quotes and deposit ratios, payment callbacks, automatic stage unlocking, and asset versioning replacing a process that used to be spread across manual communication, file transfers, and payment platforms.

**[Stablelance](https://stablelance.com)** · `Next.js` `Web3` `Stablecoins`  
Freelance services marketplace settled in stablecoins, similar in shape to Fiverr: service listings, matching, orders, project collaboration, file delivery, real-time chat, and settlement. I designed and built it end to end, including Web3 wallet creation and the account system, stablecoin deposits and withdrawals, the full order lifecycle, real-time messaging, permissions, data models, APIs, and production deployment. It launched and has since stopped operating.

**[Ask the Greatest](https://the-greatest.win)** · `iOS` `Android` `HarmonyOS` `Web`  
Consumer AI app for ongoing natural-language conversations with historical figures, combining each figure's background and body of thought with AI generation. I built it alone, from requirements and UI/UX through the iOS, Android, HarmonyOS, and web clients, deployment, launch, and monetization, then validated growth on Xiaohongshu with low-cost content: the first post drew close to 2,000 interactions, followed by 500+ registered users and 50+ paying users without a marketing team.

**[MedReg AI](https://www.medical-regulation.com)** · `RAG` `Next.js`  
AI-driven regulatory compliance for medical devices, pharmaceuticals, and dietary supplements.

**[Anti-PUA](https://anti-pua.org)** · `React Native`  
Cross-platform app that helps users identify and protect themselves from manipulation tactics.

### Open source

**[Omarchy](https://omarchy.org)** · `Linux` `Localization` `Fcitx5` · Chinese maintainer  
I started OmarchyCN independently to make Omarchy work for Chinese users and the network environment in China: Chinese localization, Fcitx5 input method and desktop adaptation, mirrors and install, update, and dependency flows tuned for networks in China, integration of locally available AI tools and model services, plus mirror downloads, update scripts, and documentation; it reached close to 10,000 system downloads within two days of launch. The Omarchy team noticed, and I joined as the official Chinese maintainer, handling localization, compatibility testing and patches against upstream, Chinese community issues and feedback, cross-language coordination with the core team, and contributing generally useful changes back upstream.

### Industrial edge AI

**Production line defect detection (PinOn Inc.)** · `NVIDIA Jetson` `Computer vision` `Edge inference`  
Industrial computer vision and edge AI on NVIDIA Jetson: cameras, sensors, and production equipment connect to edge compute nodes for on-device inference and device control, with cloud-side management, data sync, and remote operations forming an Edge + Cloud architecture. The system delivered to a Japanese listed company, a global leader in its industry, covers a continuous production line over 100 meters long with 20+ vision inspection points detecting quality issues, surface defects, and production anomalies in real time; I owned the full chain from site survey and inspection design through the vision algorithms, integration, deployment, and final delivery.

Other independent projects: Vigil, Ely-Novel, ELY-Browser.

## Experience

- **GiraStyle AI** · Co-founder &amp; CTO · Nov 2025 – present. Own product design, architecture, and core development for the AI fashion platform, including the native SwiftUI iOS app and the React/TypeScript enterprise web platform.
- **Aedylon** · Co-founder &amp; CTO · Feb 2024 – present. Built the AI ad production and delivery platform from zero: website, client portal, internal admin, review platform, Rust backend, and the full quote-to-delivery workflow.
- **American Health Formulations Inc.** · Project Manager · Mar 2023 – present. Lead internal digital systems, AI applications, and process automation, including an SOP and employee training system (React, Node.js, PostgreSQL), project management for the SEDDS product line, supplier coordination, and the rebuild of the company, lab, and ingredient sourcing websites.
- **KOIN** · Co-founder, CTO &amp; core investor · Jun 2020 – present. Led product, architecture, engineering, and team building for the AI investment platform, from the financial data platform and KOIN Brain to the native apps, brokerage integration, and SEC/FINRA-related qualifications.
- **Stablelance** · CTO/CIO · Jul 2024 – Oct 2025. Designed and built a stablecoin-settled freelance marketplace end to end; launched, now discontinued.
- **PinOn Inc.** · Co-founder, CTO &amp; core investor · Dec 2019 – Jun 2022. Built the company's AI and industrial automation products from zero on NVIDIA Jetson and delivered the production line defect detection project above.

## Education

- **New York University** · M.S. Project Management · 2020 – 2022
- **New York University** · M.S. Electrical Engineering · 2018 – 2020
- **Rose-Hulman Institute of Technology** · B.S. Electrical Engineering · 2014 – 2018

## Skills

- **AI agents:** multi-agent systems, agent runtimes, planning and verification loops, ontology and simulation, RAG, workflow automation
- **Languages:** Rust, Swift, TypeScript, Python, Kotlin, C, MATLAB, Verilog
- **Mobile:** native iOS (SwiftUI), native Android, HarmonyOS, React Native
- **Web and desktop:** React, Next.js, TanStack, Node.js, Electron
- **Data:** PostgreSQL, SQLite
- **Vision and edge:** NVIDIA Jetson, computer vision, edge inference, digital signal processing
- **Product and delivery:** product definition, UI/UX design (Figma), API and data model design, Agile, Six Sigma

## Contact

[zacharyzhang.com](https://zacharyzhang.com) · [LinkedIn](https://www.linkedin.com/in/zacharyzhangee/) · [yang@zacharyzhang.com](mailto:yang@zacharyzhang.com)
