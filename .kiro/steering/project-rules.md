# Project Rules — TM Forum Knowledge Base

## Context

This project is a knowledge base about TM Forum, Autonomous Networks, Agentic AI, and DTW Ignite 2026. It is maintained by Telecom Argentina's Assurance Digital team. All content should serve as preparation material for industry events and internal reference.

This vault is used in **Obsidian** — all content must be Obsidian-compatible and optimized for graph view, search, and navigation.

## Subject Focus

- TM Forum standards, frameworks, and events (ODA, Open APIs, eTOM, SID, ANLET)
- Autonomous Networks (Levels 0-5, self-healing, self-optimization, closed-loop)
- Agentic AI in telecommunications (multi-agent systems, intent-based management)
- Real-world deployments and architectures (any operator, any cloud platform)
- Data architecture for AN (CFS/RFS, Data Mesh, Data Fabric, Knowledge Graphs)
- Telecom Argentina's involvement and opportunities

## File Organization Rules

1. Every folder must have a `00-<MeaningfulName>.md` as its index (e.g., `00-Knowledge-Index.md`). Never use generic names like `00-README.md`.
2. Files are numbered with two-digit prefixes (01, 02, 03...) for reading order.
3. One topic per file — do not mix unrelated subjects in a single document.
4. New use cases or operator deployments go in `use-cases/` with the next available number.
5. Telecom Argentina-specific content goes in `our-cases/`.
6. DTW event context and TM Forum theory goes in `dtw-ignite-prep/`.
7. Concepts, definitions, and educational frameworks go in `knowledge/`.
8. AN level examples with vendors and tech go in `examples/`.
9. When adding a new file, always update the corresponding folder index (`00-*.md`).

## Obsidian Compatibility Rules

### Frontmatter (YAML)
1. Every `.md` file MUST start with YAML frontmatter as the very first thing (before the title).
2. Frontmatter must include `tags` as an array.
3. Tags must include:
   - The folder category tag: `knowledge`, `use-case`, `dtw-2026`, `examples`, `telecom-argentina`
   - 2-5 topic-specific tags relevant to the content
4. Use lowercase, hyphenated tags (e.g., `fault-management`, `agentic-AI`, `data-mesh`).
5. Example:
   ```yaml
   ---
   tags: [knowledge, digital-twin, graph, real-time]
   ---
   ```

### Links
1. Use **Obsidian wiki-links** for all internal references: `[[filename|Display Text]]`
2. Use the filename without extension and without folder path: `[[01-Zero-X|Zero-X]]` (not `[Zero-X](../knowledge/01-Zero-X.md)`)
3. Keep external URLs as standard markdown links: `[Text](https://...)`
4. Cross-reference generously — every concept mention should link to its knowledge article. This makes the graph view rich and useful.

### Diagrams
1. Use **Mermaid** for all diagrams (renders natively in Obsidian).
2. Do NOT use ASCII art — it breaks with different fonts and looks bad in Obsidian.
3. Keep Mermaid diagrams simple and readable. Prefer `graph TD` or `graph LR` for architecture, `sequenceDiagram` for flows.

### Naming
1. File names must be descriptive and meaningful — they appear as node labels in the graph view.
2. Never use generic names like "README", "index", "notes".
3. Use Title-Case-With-Hyphens for filenames: `07-Knowledge-Graph.md`
4. The `00-` prefix is reserved for folder index files only.

### Structure for Graph View
1. Each document should link to at least 2-3 other documents (creates graph connections).
2. Include a "Related Concepts" or "Relationship to Other Concepts" section at the bottom of knowledge articles with wiki-links.
3. Index files (`00-*`) should link to ALL files in their folder.
4. Use tags consistently so graph filtering by tag produces useful clusters.

### Formatting
1. Use `##` headers (not `#`) for sections within a document — the `#` title is the filename in Obsidian.
2. Use callouts for important notes: `> [!info]`, `> [!warning]`, `> [!tip]`
3. Use tables for structured comparisons — they render well in Obsidian.
4. Keep paragraphs short (3-4 lines max) for readability in preview mode.
5. Use horizontal rules (`---`) to separate major sections.

## Content Rules

1. Every document must have sources with working links at the bottom.
2. Include publication dates on references so we know what is current.
3. Use tables and bullet lists over long prose — these are reference docs.
4. Keep folder index titles general (describe the category, not one company).
5. Individual case files can be company-specific (e.g., MasOrange, BT, Telkomsel).
6. Do not duplicate content across files — link to the relevant document instead.
7. Mark deployment status clearly: `Production`, `PoC`, `Demo`, `Announced`.

## Language Rules

1. **All documents are written in English** — knowledge, use-cases, examples, dtw-ignite-prep, our-cases.
2. **Only the `listen/` folder is in Spanish** — these are audio scripts for TTS (text-to-speech).
3. In `listen/` files, do NOT translate technical English terms that sound bad in Spanish TTS. Keep them in English:
   - Zero Wait, Zero Touch, Zero Trouble, Zero-X
   - Self-healing, self-optimization, self-configuration
   - CFS, RFS, Customer Facing Service, Resource Facing Service
   - Knowledge graph, digital twin, closed-loop, intent-based
   - Machine learning, throughput, downlink, uplink, dashboard, playbook
   - Root cause analysis, Mean Time to Repair (MTTR)
   - Open source, cloud-native, SaaS, vendor/vendors
   - Graph Neural Networks (GNN), Large Language Models (LLM)
   - Any acronym or proper noun (ODA, SID, eTOM, ANLET, MCP, A2A, rApps, SMO, EIAP)
4. The `listen/` text should read as natural Spanglish — Spanish narrative with English technical terms, as telecom professionals speak in Latin America.

## Listen Folder Rules

1. Episodes are designed to be read aloud by TTS — no tables, no diagrams, no markdown formatting. Pure narrative text.
2. Episode ordering: foundational concepts first (01, 02, 03...), then specific technical topics, then **vendor cases (98) and DTW briefing (99) always at the end**.
3. Closing episodes use numbers **98** and **99** so they always sort last. New episodes use the next available number after the last topic episode (08, 09, 10...) — no need to renumber the closing ones.
4. When adding new listen episodes: just use the next number. The 98/99 files stay in place permanently.

## When Researching

1. Always search for the latest information (prioritize 2025-2026 sources).
2. Verify claims with multiple sources when possible.
3. Distinguish between PoC/demo and production deployments — mark status clearly.
4. Note which cloud platform (AWS, Google Cloud, Azure) is involved.
5. Track TM Forum document IDs (e.g., IG1356, TMF620) for precise referencing.
6. When adding new content, identify which existing knowledge articles it relates to and add wiki-links.

## Project Structure Reference

```
teco-tmforum/
|-- README.md              Project-level navigation
|-- dtw-ignite-prep/       DTW Ignite 2026 event prep and TM Forum theory
|-- use-cases/             Real-world deployments and architecture patterns
|-- our-cases/             Telecom Argentina's own involvement
|-- knowledge/             Concepts, definitions, and frameworks (educational)
|-- examples/              AN Levels L1-L3 with vendors and open source
|-- listen/                Audio episodes in Spanish for TTS (Spanglish)
|-- .obsidian/             Vault configuration (do not edit manually)
+-- .kiro/                 Kiro steering rules
```

## Tag Reference

| Folder Tag | Used In |
|-----------|---------|
| `knowledge` | All files in knowledge/ |
| `use-case` | All files in use-cases/ |
| `dtw-2026` | All files in dtw-ignite-prep/ |
| `examples` | All files in examples/ |
| `telecom-argentina` | All files in our-cases/ |

| Topic Tags (use as needed) |
|---------------------------|
| `fault-management`, `self-healing`, `AIOps`, `root-cause` |
| `agentic-AI`, `multi-agent`, `MCP`, `A2A` |
| `autonomous-networks`, `an-levels`, `Level-4`, `ANLET` |
| `closed-loop`, `intent`, `zero-touch`, `zero-x` |
| `digital-twin`, `knowledge-graph`, `GNN`, `topology` |
| `ODA`, `open-apis`, `SID`, `CFS`, `RFS`, `catalog`, `inventory` |
| `data-mesh`, `data-fabric`, `integration`, `protocols` |
| `rApps`, `SMO`, `O-RAN`, `RAN-automation` |
| `AWS`, `Google-Cloud`, `Ericsson`, `Nokia`, `Huawei` |
| `MasOrange`, `production`, `PoC`, `open-source` |
