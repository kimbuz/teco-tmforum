# TM Forum & Autonomous Networks — Knowledge Base

Research and reference material for TM Forum, Autonomous Networks, Agentic AI, and DTW Ignite 2026.
Maintained by Telecom Argentina's Assurance Digital team.

---

## Structure

```
teco-tmforum/
|
|-- README.md                        <- You are here
|
|-- dtw-ignite-prep/                 <- DTW Ignite 2026 event preparation
|   |-- 00-DTW-Ignite-2026.md        Overview and key takeaways
|   |-- 01-TM-Forum-Overview.md      What TM Forum is, frameworks, standards
|   |-- 02-DTW-Ignite-2026-Event-Guide.md  Event details, agenda, formats
|   |-- 03-Autonomous-Networks.md    AN levels L0-L5, industry status
|   |-- 04-Agentic-AI-in-Telco.md   Multi-agent systems, Agentic ODA
|   |-- 05-Catalyst-Projects-2025-2026.md  15 active innovation projects
|   |-- 06-Publications-and-Reports.md    All relevant publications
|   +-- 07-My-Agenda-AI-Fault-Management.md  Curated sessions + 3-day calendar
|
|-- use-cases/                       <- Real-world deployments and architectures
|   |-- 00-Use-Cases-Index.md        Index, key questions answered
|   |-- 01-GraphML-AIOps-Root-Cause-Analysis.md     MasOrange + Google + NetAI
|   |-- 02-RAN-Automation-EIAP-rApps.md             MasOrange + Ericsson
|   |-- 03-AI-Centric-Transmission-Network.md       MasOrange transport
|   |-- 04-TM-Forum-Level4-Certification.md         MasOrange L4 certified
|   |-- 05-AWS-Agentic-rApp-as-a-Service.md         Ericsson + AWS (60+ CSPs)
|   |-- 06-AWS-Multi-Agent-Network-Operations.md    AWS Bedrock open-source
|   |-- 07-Data-Model-CFS-RFS-Catalog-for-AN.md    TM Forum PSR model
|   +-- 08-Data-Mesh-Fabric-Unified-Knowledge-Layer.md  Data architecture
|
|-- our-cases/                       <- Telecom Argentina's own involvement
|   +-- 00-Telecom-Argentina.md      AN Manifesto, publications, partnerships
|
|-- knowledge/                       <- Concepts and definitions
|   |-- 00-Knowledge-Index.md        Index of knowledge articles
|   |-- 01-Zero-X.md                 Zero Wait, Zero Touch, Zero Trouble
|   |-- 02-Autonomous-Networks-Levels.md  L0-L5 definitions and assessment
|   |-- 03-Closed-Loop-Automation.md Observe-Analyze-Decide-Act-Verify
|   |-- 04-Intent-Based-Management.md  Declare outcomes, not configs
|   |-- 05-Digital-Twin.md           Real-time virtual network replica
|   |-- 06-Open-Digital-Architecture-ODA.md  TM Forum modular blueprint
|   |-- 07-Knowledge-Graph.md        Network as nodes and edges
|   |-- 08-rApps-and-SMO.md          RAN automation on O-RAN platform
|   |-- 09-MCP-and-A2A-Protocols.md  Agent-to-data and agent-to-agent
|   |-- 10-AIOps.md                  AI for operations
|   |-- 11-CFS-RFS-Catalog-Inventory.md  Product-Service-Resource model
|   |-- 12-SID-Information-Framework.md  TM Forum common data model
|   |-- 13-One-View-All-Layers.md    How all concepts fit together
|   +-- 14-SID-Examples.md           Concrete JSON examples
|
+-- examples/                        <- AN Levels L1-L3 in production
    |-- 00-AN-Levels-Examples.md     Overview and comparison
    |-- 01-Level-1-Assisted-Operations.md    ZTP, dashboards, alerting
    |-- 02-Level-2-Partial-Autonomous.md     SON, orchestrators, playbooks
    +-- 03-Level-3-Conditional-Autonomous.md AI decisions within domains
```

---

## Quick Navigation

| Folder | What's Inside | Start Here |
|--------|---------------|------------|
| [dtw-ignite-prep/](./dtw-ignite-prep/00-DTW-Ignite-2026.md) | TM Forum background, event details, theory, publications | Event context |
| [use-cases/](./use-cases/00-Use-Cases-Index.md) | Real deployments, AWS architectures, data models | How it works in practice |
| [our-cases/](./our-cases/00-Telecom-Argentina.md) | Telecom Argentina's TM Forum involvement | Our company's position |
| [knowledge/](./knowledge/00-Knowledge-Index.md) | Concepts and definitions (Zero-X, AN Levels, etc.) | Learn the fundamentals |
| [examples/](./examples/00-AN-Levels-Examples.md) | AN Levels L1–L3 in production today (vendors, tech, open source) | What exists before L4 |
| [listen/](./listen/00-Listen-Index.md) | Audiolibro en español — 9 episodios para escuchar viajando | Aprender en el camino |
| [calendar/](./calendar/00-Calendar-Index.md) | DTW Ignite 2026 full calendar — all sessions by day | Plan your attendance |

---

## Key Themes

| Theme | Summary |
|-------|---------|
| Autonomous Networks | L4 is production-ready. L5 is the next target. |
| Agentic AI | Multi-agent systems replacing siloed automation. |
| Data Architecture | Data Mesh/Fabric + Knowledge Graphs + MCP/A2A = unified knowledge layer. |
| Not Just Mobile | Fixed broadband, transport, core, enterprise — all domains in scope. |
| Cloud Platforms | AWS and Google Cloud both have production telco deployments. |
| Standards | TM Forum ODA, Open APIs, SID ontology, ANLET certification. |
| Telecom Argentina | AN Manifesto signatory, Huawei AI Fabric deployed, 5G Core blueprint. |

---

## DTW Ignite 2026

| Field | Detail |
|-------|--------|
| Dates | 23-25 June 2026 |
| Location | Bella Center, Copenhagen, Denmark |
| Theme | "The Future. Faster." |
| Website | https://dtw.tmforum.org/ |
| My Agenda | [AI for Fault Management — 3-Day Plan](./dtw-ignite-prep/07-My-Agenda-AI-Fault-Management.md) |

---

## Contributing to This Repo

When adding or updating content, follow these rules:

1. **One topic per file.** Each markdown covers a single use case, concept, or reference.
2. **Number files** with a two-digit prefix (01, 02...) to maintain reading order.
3. **00-README.md** in every folder acts as the index and entry point.
4. **Sources at the bottom** of every document with working links.
5. **Keep titles general** — folder READMEs describe the category, not a single company.
6. **New operators or cases** get their own numbered file inside `use-cases/`.
7. **Telecom Argentina-specific** content goes in `our-cases/`.
8. **Update the folder README** whenever you add a new file to that folder.
9. **Use tables and lists** over long prose. These are reference docs, not essays.
10. **Date your findings** — include publication dates so we know what's current.
