---
tags: [knowledge, rApps, SMO, O-RAN, RAN-automation]
---

# rApps and SMO (Service Management & Orchestration)

## Definition

**rApps** are software applications that automate RAN (Radio Access Network) management and optimization. They run on the **SMO** (Service Management & Orchestration) platform, which is the O-RAN Alliance's framework for centralized, intelligent network management.

---

## SMO — Service Management & Orchestration

| Aspect | Detail |
|--------|--------|
| **What** | Centralized platform for managing and orchestrating RAN |
| **Standard** | O-RAN Alliance architecture |
| **Contains** | Non-Real-Time RAN Intelligent Controller (Non-RT RIC) |
| **Interfaces** | O1 (southbound to RAN), R1 (northbound to rApps) |
| **Purpose** | Enable multi-vendor RAN automation through open interfaces |

### Key Interfaces

| Interface | Direction | Purpose |
|-----------|-----------|---------|
| **O1** | SMO → RAN | FCAPS management (Fault, Configuration, Accounting, Performance, Security) |
| **R1** | rApps → SMO | Data access and actuation for rApps |
| **A1** | Near-RT RIC → RAN | Real-time policies (millisecond control) |

---

## rApps — RAN Applications

| Aspect | Detail |
|--------|--------|
| **What** | Software tools for automated RAN management and optimization |
| **Where they run** | On the Non-RT RIC within the SMO |
| **Control loop** | 1 second or longer (non-real-time) |
| **Ecosystem** | Multi-vendor — Ericsson, 3rd-party ISVs, CSP-built |
| **Deployment** | On-premises (EIAP) or cloud (rApp as a Service on AWS) |

### Examples of rApps

| rApp | Function |
|------|----------|
| Cell Anomaly Detector | Proactive detection of performance issues |
| RAN Energy Saver | Dynamic energy optimization without service impact |
| Uplink Anomaly Detection | Identify uplink interference patterns |
| Cell Shaping | Optimize cell coverage and capacity |
| Interference Optimization | Reduce inter-cell interference |
| Root Cause Analysis | Automated fault diagnosis |

---

## Ericsson EIAP (Intelligent Automation Platform)

Ericsson's implementation of the SMO/Non-RT RIC:

| Feature | Detail |
|---------|--------|
| SDK | Allows 3rd-party rApp development |
| Scale | Manages 13M+ sites globally |
| Ecosystem | Ericsson + 3rd-party rApps |
| Deployment | On-premises or AWS cloud |
| Governance | CSP controls what data rApps can access |
| Conflict resolution | Manages competing rApp configuration requests |

---

## Agentic rApps (2026 Evolution)

The latest evolution: rApps powered by **Agentic AI** where specialized AI agents coordinate through a supervisor agent:

- Natural language interactions
- Intent-based workflows
- Reasoning, planning, and autonomous action
- Available as SaaS on AWS Marketplace
- Uses Amazon Bedrock for agent coordination
- Supports MCP and A2A protocols for integration

See: [[05-AWS-Agentic-rApp-as-a-Service|Use Case 05 — AWS Agentic rApp as a Service]]

---

## How rApps Relate to AN Levels

| AN Level | rApp Role |
|----------|-----------|
| L2 | rApps provide recommendations, human decides |
| L3 | rApps decide and act within RAN domain |
| L4 | Agentic rApps coordinate across domains autonomously |
| L5 | rApps are part of fully autonomous end-to-end system |

---

## Sources
- [Ericsson: Intelligent Automation Platform](https://www.ericsson.com/en/ran/intelligent-ran-automation/intelligent-automation-platform)
- [Ericsson: rApps Software Directory](https://www.ericsson.com/en/ran/intelligent-ran-automation/intelligent-automation-platform/rapps/software)
- [AWS: Agentic rApp as a Service](https://aws.amazon.com/blogs/industries/accelerating-autonomous-network-optimization-agentic-rapp-as-a-service-powered-by-aws-and-ericsson-intelligent-automation-platform/)
- [Ericsson: Agentic AI Pathway to Level 5](https://www.ericsson.com/en/blog/2025/7/agentic-ai-pathway-to-autonomous-network-level-5)
