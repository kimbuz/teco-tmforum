---
tags: [knowledge, knowledge-graph, GNN, topology, AI]
---

# Knowledge Graph (for Telecom)

## Definition

A knowledge graph is a data structure that represents information as entities (nodes) and relationships (edges), capturing the meaning and context of how things connect. In telecom, it models the network as an interconnected system rather than isolated tables.

---

## Why Graphs for Telecom

Networks ARE graphs. Every device is a node, every link is an edge, every service is a path through the graph. Traditional relational databases force this natural structure into flat tables with foreign keys — losing the relationship context that AI needs.

| Question | Relational DB | Knowledge Graph |
|----------|--------------|-----------------|
| "What customers are affected by this fiber cut?" | Multiple JOINs across 5+ tables | Traverse edges from fiber → services → customers |
| "What's the root cause of this alarm storm?" | Manual correlation by engineer | Follow propagation paths in the graph |
| "What happens if this router fails?" | Custom simulation code | Remove node, observe disconnected paths |

---

## Graph vs. Relational for Network Data

| Aspect | Relational (SQL) | Graph |
|--------|------------------|-------|
| Relationships | Implicit (foreign keys, JOINs) | Explicit (first-class edges) |
| Traversal | Expensive (multi-table JOINs) | Native (follow edges) |
| Schema changes | Rigid (ALTER TABLE) | Flexible (add edge types) |
| Path queries | Very complex SQL | Natural (shortest path, reachability) |
| AI/ML readiness | Requires feature engineering | Direct input to GNNs |
| Topology modeling | Awkward | Natural |

---

## What a Telecom Knowledge Graph Contains

| Entity Type | Examples |
|-------------|---------|
| **Devices** | Routers, switches, OLTs, gNodeBs, firewalls |
| **Links** | Fiber spans, radio links, logical tunnels |
| **Services** | CFS instances, RFS instances |
| **Customers** | Accounts, subscriptions, SLAs |
| **Locations** | Sites, racks, geographic coordinates |
| **Configurations** | Running configs, policies, parameters |
| **Metrics** | KPIs attached to nodes/edges as properties |
| **Events** | Alarms, changes, incidents (temporal) |

---

## Graph Neural Networks (GNNs)

GNNs are AI models designed to learn from graph-structured data. They understand topology natively:

| Capability | How GNNs Use It |
|-----------|-----------------|
| Message passing | Propagate information along edges (like faults propagate in real networks) |
| Neighbor aggregation | Understand a node's context from its connections |
| Structural awareness | Distinguish local anomaly from structural failure |
| Deterministic reasoning | Follow known paths rather than statistical correlation |

See: [[01-GraphML-AIOps-Root-Cause-Analysis|Use Case 01 — GraphML AIOps]] for MasOrange's implementation with Google tf-GNN.

---

## Technology Options

| Product | Vendor | Strength |
|---------|--------|----------|
| Spanner Graph | Google Cloud | Scalable, temporal, integrated with Vertex AI |
| Amazon Neptune | AWS | Managed, integrates with Bedrock |
| Neo4j | Neo4j Inc. | Mature, rich query language (Cypher) |
| TigerGraph | TigerGraph | High-performance analytics |
| JanusGraph | Open source | Distributed, scalable |

---

## Relationship to Other Concepts

| Concept | Connection |
|---------|-----------|
| [[05-Digital-Twin|Digital Twin]] | A digital twin IS a knowledge graph with real-time state |
| [[08-Data-Mesh-Fabric-Unified-Knowledge-Layer|Data Fabric]] | Knowledge graph is the semantic backbone of a data fabric |
| [[01-GraphML-AIOps-Root-Cause-Analysis|Root Cause Analysis]] | GNNs on knowledge graphs enable deterministic RCA |
| [[07-Data-Model-CFS-RFS-Catalog-for-AN|CFS/RFS]] | Service topology is a subgraph within the knowledge graph |

---

## Sources
- [Google Cloud: GraphML and Digital Twins](https://cloud.google.com/blog/topics/telecommunications/graphml-and-digital-twins-enable-autonomous-networks)
- [NetAI: GNN-Powered AIOps](https://netai.ai/)
- [Google Research: Graph Neural Networks in TensorFlow](https://research.google/blog/graph-neural-networks-in-tensorflow/)
- [Orange Research: NORIA — Network Anomaly Detection Using Knowledge Graphs](https://hellofuture.orange.com/en/noria-network-anomaly-detection-using-knowledge-graphs/)
