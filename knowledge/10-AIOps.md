# AIOps — AI for IT/Network Operations

## Definition

AIOps (Artificial Intelligence for Operations) applies machine learning and data analytics to automate and enhance IT and network operations. It processes large volumes of operational data (logs, metrics, events, traces) to detect anomalies, correlate events, identify root causes, and trigger remediation.

---

## Core Capabilities

| Capability | What It Does |
|-----------|-------------|
| **Anomaly detection** | Identifies unusual patterns in metrics/behavior |
| **Event correlation** | Groups related alarms into a single incident |
| **Root cause analysis** | Determines the underlying cause of a problem |
| **Noise reduction** | Filters false positives, reduces alarm fatigue |
| **Predictive analytics** | Forecasts failures before they happen |
| **Automated remediation** | Triggers fixes without human intervention |
| **Capacity planning** | Predicts resource needs based on trends |

---

## Traditional AIOps vs. Graph-Based AIOps

| Aspect | Traditional AIOps | Graph-Based AIOps (GNN) |
|--------|-------------------|------------------------|
| Data model | Time-series, flat vectors | Network topology graph |
| Correlation | Statistical (correlation != causation) | Deterministic (follows physical paths) |
| Topology awareness | None (topology-blind) | Native (structure-aware) |
| False positives | High | Drastically reduced |
| Explainability | Black box | Explainable (graph paths) |
| Root cause | Guesses based on patterns | Traces through known dependencies |

See: [Knowledge Graph](./07-Knowledge-Graph.md) and [Use Case 01 — GraphML AIOps](../use-cases/01-GraphML-AIOps-Root-Cause-Analysis.md)

---

## AIOps in the AN Context

| AN Level | AIOps Role |
|----------|-----------|
| L1–L2 | Assists humans with detection and recommendations |
| L3 | Makes decisions within a domain (closed-loop) |
| L4 | Cross-domain autonomous operations |
| L5 | Fully autonomous, self-evolving operations |

---

## Key Metrics AIOps Improves

| Metric | Meaning | Impact |
|--------|---------|--------|
| **MTTR** | Mean Time to Repair | Reduced from hours to minutes |
| **MTTI** | Mean Time to Identify | Reduced from minutes to seconds |
| **False positive rate** | Incorrect alerts | Reduced by 80%+ with GNNs |
| **Alarm volume** | Total alerts per day | Reduced through correlation |
| **Proactive detection** | Issues found before impact | Enabled by predictive models |

---

## Sources
- [Google Cloud: What is AIOps](https://cloud.google.com/discover/what-is-aiops)
- [NetAI: GNN-Powered AIOps](https://netai.ai/)
- [AWS: Multi-Agent Collaboration for Telecom Network Operations](https://aws.amazon.com/blogs/industries/multi-agent-collaboration-using-amazon-bedrock-for-telecom-network-operations/)
