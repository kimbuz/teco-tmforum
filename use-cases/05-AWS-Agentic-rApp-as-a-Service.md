# Use Case 05: Ericsson Agentic rApp as a Service on AWS

## Summary

Ericsson and AWS launched **rApp as a Service (rApp aaS)** — a SaaS solution hosted on AWS and available via AWS Marketplace that uses **Agentic AI** to deliver RAN automation, network operations, and optimization at scale. This is a **production-ready commercial product** deployed across 60+ CSPs managing 13 million sites and 2 billion subscribers.

---

## The Problem

CSPs face critical challenges modernizing their networks:
- Growing complexity of multi-technology (5G/6G) and multi-service environments
- Increasing operational costs due to manual interventions
- Difficulty scaling network operations to meet surging data demands
- Legacy SON (Self-Organizing Network) systems hinder AI-driven automation
- Pressure to accelerate time-to-market while ensuring reliability
- Most CSPs are at Autonomous Network Level 1–2 (TM Forum 2025 survey)

---

## The Solution Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Agentic rApp as a Service (AWS)                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │              AGENTIC AI LAYER                                    ││
│  │                                                                   ││
│  │  ┌──────────────────────────────────────────────────────────┐   ││
│  │  │           SUPERVISOR AGENT                                │   ││
│  │  │  (Reasoning, Planning, Coordination via Amazon Bedrock)   │   ││
│  │  └────────┬──────────────┬──────────────┬───────────────────┘   ││
│  │           │              │              │                        ││
│  │           ▼              ▼              ▼                        ││
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐                ││
│  │  │ Cell       │  │ Uplink     │  │ Interference│                ││
│  │  │ Anomaly    │  │ Anomaly    │  │ Optimization│                ││
│  │  │ Detection  │  │ Detection  │  │ Agent       │                ││
│  │  │ Agent      │  │ Agent      │  │             │                ││
│  │  └────────────┘  └────────────┘  └────────────┘                ││
│  │           │              │              │                        ││
│  │           ▼              ▼              ▼                        ││
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐                ││
│  │  │ Root Cause │  │ Cell       │  │ Spectral   │                ││
│  │  │ Analysis   │  │ Shaping    │  │ Efficiency │                ││
│  │  │ Agent      │  │ Agent      │  │ Agent      │                ││
│  │  └────────────┘  └────────────┘  └────────────┘                ││
│  └─────────────────────────────────────────────────────────────────┘│
│                              │                                        │
│                              ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │              AWS SERVICES                                        ││
│  │                                                                   ││
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          ││
│  │  │ Amazon   │ │ Amazon   │ │ Amazon   │ │ AWS      │          ││
│  │  │ Bedrock  │ │ SageMaker│ │ Athena   │ │ Lambda   │          ││
│  │  │ (Agents) │ │ AI       │ │(Analytics│ │(Event-   │          ││
│  │  │          │ │(ML Cycle)│ │          │ │ driven)  │          ││
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          ││
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          ││
│  │  │ ECS on   │ │ AWS Glue │ │ AWS      │ │ AWS      │          ││
│  │  │ Fargate  │ │ (ETL)    │ │PrivateLink│ │ KMS     │          ││
│  │  │(Compute) │ │          │ │(Security)│ │(Encrypt) │          ││
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          ││
│  └─────────────────────────────────────────────────────────────────┘│
│                              │                                        │
│                              ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │     INTEGRATION INTERFACES                                       ││
│  │                                                                   ││
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   ││
│  │  │ O-RAN R1 │  │ O-RAN O1 │  │   MCP    │  │ Agent2Agent  │   ││
│  │  │Interface │  │Interface │  │ Protocol │  │ (A2A)        │   ││
│  │  │(Data)    │  │(FCAPS)   │  │          │  │ Protocol     │   ││
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   ││
│  └─────────────────────────────────────────────────────────────────┘│
│                              │                                        │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│     ERICSSON INTELLIGENT AUTOMATION PLATFORM (EIAP)                  │
│     (On-premises or AWS Cloud)                                       │
│                                                                       │
│  • Central governance over network data exposure                     │
│  • Conflict resolution for multi-rApp configuration writes           │
│  • Policy-driven execution framework                                 │
│  • Southbound O1 interface to RAN                                    │
│  • Northbound R1 interface to rApps                                  │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CSP RAN INFRASTRUCTURE                             │
│     (5G, 5G-A, 4G, O-RAN — Multi-vendor, Multi-technology)          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Proven Results (Field-Validated)

| Metric | Result |
|--------|--------|
| **Accuracy** | 98% field-validated |
| **Cell issue resolution** | 54% faster |
| **Optimization time/effort** | 75% reduction |
| **Downlink throughput** (cells with issues) | 43% improvement |
| **Spectral efficiency** | 4% gains |
| **Daily AI inferences** | 100 million+ |
| **Sites managed** | 13 million+ globally |
| **Subscribers served** | 2 billion+ |
| **CSPs deployed** | 60+ |

---

## Three Integration Scenarios for CSPs

### Scenario 1: Integrate with Existing AI Strategy
- Ingest O-RAN O1/R1 data into CSP's own Data/AI solutions
- Use rApp aaS for optimized RAN operations with Ericsson expertise
- CSP maintains its own AI platform alongside rApp aaS

### Scenario 2: Shift RAN Automation to rApp aaS
- Simplify data pipelines
- Receive insights, proposals, and network intents via APIs
- Reduce computational and operational load (lower TCO)
- Interfaces: APIs, MCP (Model Context Protocol), A2A (Agent2Agent)

### Scenario 3: Enrich EIAP with New Data Sources
- Ingest additional data for advanced rApp development
- CSPs build custom rApps atop EIAP
- Consolidate network automation and data strategies

---

## Security Architecture on AWS

| Security Layer | Implementation |
|---------------|----------------|
| **Encryption at rest** | AES-256 with AWS KMS |
| **Encryption in transit** | TLS 1.2+ |
| **AI model data privacy** | Amazon Bedrock — data never shared with model providers |
| **Agentic AI guardrails** | Amazon Bedrock Guardrails for policy-based approval |
| **Multi-tenant isolation** | Dedicated resources, isolated schemas, or row-level security |
| **Data residency** | Regional deployment, data never leaves designated regions |
| **Private connectivity** | AWS Direct Connect + PrivateLink |
| **Audit trails** | CloudTrail + CloudWatch for all autonomous decisions |
| **Compliance** | 140+ global security standards |

---

## Relevance to TM Forum AN Levels

This solution directly accelerates the journey from Level 2 → Level 4/5:

| AN Level | How rApp aaS Contributes |
|----------|--------------------------|
| L2 → L3 | Automated anomaly detection, recommendations |
| L3 → L4 | Autonomous optimization, closed-loop actions |
| L4 → L5 | Intent-driven, cross-domain agentic coordination |

---

## Sources
- [AWS Blog: Accelerating Autonomous Network Optimization](https://aws.amazon.com/blogs/industries/accelerating-autonomous-network-optimization-agentic-rapp-as-a-service-powered-by-aws-and-ericsson-intelligent-automation-platform/) (Feb 17, 2026)
- [AWS Blog: Agentic AI for RAN Optimization — Pathway to Level 5](https://aws.amazon.com/blogs/industries/agentic-ai-for-ran-optimization-pathway-to-autonomous-network-level-5/) (Jul 2025)
- [Ericsson: Agentic rApp as a Service with AWS](https://www.ericsson.com/en/blog/2026/2/agentic-rapp-as-a-service) (Feb 2026)
- [Ericsson Press Release: rApp aaS Launch](https://www.ericsson.com/en/press-releases/2026/2/ericsson-launches-agentic-rapp-as-a-service-on-aws-to-accelerate-autonomous-networks-transformation)
- [AWS Marketplace: Agentic rApp as a Service](https://aws.amazon.com/marketplace/pp/prodview-nbixyvn7m3mbc)
