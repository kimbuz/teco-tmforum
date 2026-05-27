---
tags: [use-case, MasOrange, Google-Cloud, GNN, AIOps, root-cause]
---

# Use Case 01: GraphML-Powered AIOps & Root Cause Analysis

## Summary

MasOrange partnered with **Google Cloud** and **NetAI** to build a Graph Neural Network (GNN)-powered AIOps system that uses a real-time network digital twin for deterministic, explainable root cause analysis. Demonstrated as a Proof of Concept at **MWC Barcelona 2026**.

---

## The Problem

Modern telecom networks are multi-layer ecosystems spanning 5G radio access, transport fiber, edge compute, and centralized cloud cores. Traditional AIOps approaches fail because:

- **Topology-blind models** don't understand physical connections between devices
- **Symptom-based detection** identifies anomalies but can't explain *why*
- **Correlation ≠ Causality** — statistical correlation in complex networks is often coincidental
- **Fragmented data lakes** where topology is just another table, not a living model
- **False positives** overwhelm operations teams

---

## The Solution

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    GraphML AIOps Architecture                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                   MANAGED AIOps (NetAI)                    │  │
│  │                                                             │  │
│  │  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐  │  │
│  │  │ Automated   │  │  GNN-Based   │  │  Root Cause     │  │  │
│  │  │ Network     │  │  Fault       │  │  Analysis &     │  │  │
│  │  │ Discovery   │  │  Propagation │  │  Auto-Remediate │  │  │
│  │  │ & Graph     │  │  Prediction  │  │                 │  │  │
│  │  │ Construction│  │              │  │                 │  │  │
│  │  └──────┬──────┘  └──────┬───────┘  └────────┬────────┘  │  │
│  └─────────┼────────────────┼────────────────────┼───────────┘  │
│            │                │                    │               │
│            ▼                ▼                    ▼               │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              GOOGLE CLOUD AI PLATFORM                       │  │
│  │                                                             │  │
│  │  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐  │  │
│  │  │ Spanner     │  │  Vertex AI   │  │  BigQuery       │  │  │
│  │  │ Graph       │  │  (tf-GNN     │  │  (Federated     │  │  │
│  │  │ (Digital    │  │   Training)  │  │   Graph         │  │  │
│  │  │  Twin)      │  │              │  │   Analytics)    │  │  │
│  │  └──────┬──────┘  └──────┬───────┘  └────────┬────────┘  │  │
│  └─────────┼────────────────┼────────────────────┼───────────┘  │
│            │                │                    │               │
│            ▼                ▼                    ▼               │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              NETWORK DATA SOURCES                           │  │
│  │                                                             │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │  │
│  │  │  Alarms  │  │  Perf    │  │  Config  │  │  Topology│  │  │
│  │  │  & Events│  │  Metrics │  │  Changes │  │  Data    │  │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### 1. Network Digital Twin (Google Spanner Graph)
- Moves from static inventory to a **dynamic, temporal graph**
- Explicitly models live network relations and topology
- Captures **billions of dependencies** — e.g., how a specific optical transponder supports a particular IP interface, which supports a customer's 5G slice
- Supports **"time travel" queries** — inspect the network as it looked hours or days ago for instant RCA

### 2. Graph Neural Networks (Google tf-GNN + NetAI)
- **Google tf-GNN**: Open-source, production-tested library for building GNNs at massive scale (same class used in Google's own products)
- **NetAI fine-tuning**: Specialized models for telecom behaviors (BGP session flaps, optical signal degradation, congestion-induced latency)
- **Message passing**: Mathematically propagates fault signals along known physical paths

### 3. Unified Graph Data Layer
- **Spanner Graph** for real-time digital twin operations
- **BigQuery** for federated graph analytics and historical analysis
- No complex ETL processes between operational and analytical data

### 4. ML.PREDICT (Spanner)
- Real-time predictions using trained GNN models directly on live digital twin data
- Moves from monitoring to **predicting** failure propagation

---

## Why GNNs Beat Traditional ML for Networks

| Capability | Traditional ML | Graph Neural Networks |
|-----------|---------------|----------------------|
| Topology awareness | ❌ Topology-blind | ✅ Native graph processing |
| Reasoning type | Correlation-based | Deterministic (message passing) |
| Failure propagation | Cannot model | Mathematically tracks paths |
| Anomaly classification | Single-point only | Distinguishes local vs. structural |
| False positives | High | Drastically reduced |
| Explainability | Black box | Explainable (follows graph paths) |

---

## How It Works (Operational Flow)

```
1. DISCOVER    → Automated network discovery builds graph model
                 (every device, connection, dependency in real-time)

2. INGEST      → Real-time alarms, metrics, config changes flow in

3. CORRELATE   → GNN processes the graph structure
                 (not just node data, but connections between them)

4. PROPAGATE   → If fiber cut occurs, model mathematically propagates
                 fault signal along known physical paths

5. IDENTIFY    → Deterministic root cause identified
                 (one root cause → all correlated alarms cleared)

6. REMEDIATE   → Automated corrective action triggered
                 (or recommendation to operator)
```

---

## Key Quotes

> "As we scale our operations, the ability to pinpoint root causes across millions of interconnected components is no longer optional. Partnering with Google Cloud and NetAI on this GraphML-driven approach allows us to explore and transform our observability into a proactive engine for service reliability."
> — **Roberto González Librán**, Head of Observability and Automation, MasOrange

> "By integrating GraphML capabilities with partners like NetAI, we are providing CSPs with the deterministic reasoning they need to run truly autonomous, self-healing networks."
> — **Muninder Sambi**, VP & GM of Networking, Google Cloud

---

## Status & Maturity

| Aspect | Status |
|--------|--------|
| **Stage** | Proof of Concept (demonstrated at MWC 2026) |
| **Demo** | Live at NetAI Stand 8.1C64 + Google Cloud Booth, MWC 2026 |
| **Focus** | Deterministic RCA for multi-vendor networks |
| **Next step** | Production pilot with MasOrange |

---

## Relevance to TM Forum AN Levels

This use case directly enables **Level 4 → Level 5** progression:
- **Self-healing**: Autonomous fault detection and resolution
- **Predictive**: Anticipates failures before customer impact
- **Cross-domain**: Works across multi-layer, multi-vendor networks
- **Explainable**: Deterministic reasoning (not black-box ML)

---

## Sources
- [Google Cloud Blog: GraphML and Digital Twins Enable Autonomous Networks](https://cloud.google.com/blog/topics/telecommunications/graphml-and-digital-twins-enable-autonomous-networks) (March 4, 2026)
- [Google Cloud Blog: Autonomous Networks at MWC 2026](https://cloud.google.com/blog/topics/telecommunications/autonomous-networks-at-mwc-2026) (March 2, 2026)
- [NetAI — GNN-Powered AIOps](https://netai.ai/)
- [Google tf-GNN Library](https://research.google/blog/graph-neural-networks-in-tensorflow/)
