# Project Rules — TM Forum Knowledge Base

## Context

This project is a knowledge base about TM Forum, Autonomous Networks, Agentic AI, and DTW Ignite 2026. It is maintained by Telecom Argentina's Assurance Digital team. All content should serve as preparation material for industry events and internal reference.

## Subject Focus

- TM Forum standards, frameworks, and events (ODA, Open APIs, eTOM, SID, ANLET)
- Autonomous Networks (Levels 0-5, self-healing, self-optimization, closed-loop)
- Agentic AI in telecommunications (multi-agent systems, intent-based management)
- Real-world deployments and architectures (any operator, any cloud platform)
- Data architecture for AN (CFS/RFS, Data Mesh, Data Fabric, Knowledge Graphs)
- Telecom Argentina's involvement and opportunities

## File Organization Rules

1. Every folder must have a `00-README.md` as its index and entry point.
2. Files are numbered with two-digit prefixes (01, 02, 03...) for reading order.
3. One topic per file — do not mix unrelated subjects in a single document.
4. New use cases or operator deployments go in `use-cases/` with the next available number.
5. Telecom Argentina-specific content goes in `our-cases/`.
6. DTW event context and TM Forum theory goes in `dtw-ignite-prep/`.
7. Concepts, definitions, and educational frameworks go in `knowledge/`.
8. When adding a new file, always update the corresponding `00-README.md` index.

## Content Rules

1. Every document must have sources with links at the bottom.
2. Include publication dates on references so we know what is current.
3. Use tables and bullet lists over long prose — these are reference docs.
4. Keep folder README titles general (describe the category, not one company).
5. Individual case files can be company-specific (e.g., MasOrange, BT, Telkomsel).
6. Architecture diagrams should use Mermaid when possible for proper rendering. If ASCII is used, keep it simple and use basic characters (+, -, |, >) to avoid font alignment issues.
7. Do not duplicate content across files — link to the relevant document instead.

## When Researching

1. Always search for the latest information (prioritize 2025-2026 sources).
2. Verify claims with multiple sources when possible.
3. Distinguish between PoC/demo and production deployments — mark status clearly.
4. Note which cloud platform (AWS, Google Cloud, Azure) is involved.
5. Track TM Forum document IDs (e.g., IG1356, TMF620) for precise referencing.

## Project Structure Reference

```
teco-tmforum/
|-- README.md              Project-level navigation and contributing rules
|-- dtw-ignite-prep/       DTW Ignite 2026 event prep and TM Forum theory
|-- use-cases/             Real-world deployments and architecture patterns
|-- our-cases/             Telecom Argentina's own involvement
+-- knowledge/             Concepts, definitions, and frameworks (educational)
```
