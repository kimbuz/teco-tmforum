---
tags: [use-case, AWS, multi-agent, Bedrock, open-source]
---

# Use Case 06: AWS Multi-Agent Collaboration for Telecom Network Operations

## Summary

AWS published a reference architecture and **open-source implementation** for a multi-agent Network Operations Assistant using **Amazon Bedrock**. The solution uses specialized AI agents (Maintenance, Alarm, KPI) coordinated by a Supervisor Agent to automate NOC troubleshooting. This applies to **any network type** (mobile, fixed, transport) and is available as deployable code on GitHub.

---

## The Problem

Traditional Network Operations Centers (NOCs) suffer from:
- **Linear, manual troubleshooting** dependent on static playbooks
- **Fragmented monitoring tools** — alarms, maintenance, KPIs in different interfaces
- **Tribal knowledge** — critical insights reside with experienced engineers, rarely documented
- **High MTTR** (Mean Time to Resolve) — slow correlation of data from multiple sources
- **Human error** — inconsistencies when correlating maintenance schedules, active alarms, and performance trends

---

## Solution Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              Network Operations Assistant                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  FRONTEND (Streamlit on AWS Fargate)                       │  │
│  │  • Chat-based interface                                    │  │
│  │  • Natural language queries                                │  │
│  │  • Real-time agent tracing                                 │  │
│  │  • Amazon Cognito authentication                           │  │
│  │  • CloudFront + Lambda@Edge for security                   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                    │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  SUPERVISOR AGENT (Amazon Nova Pro)                        │  │
│  │                                                             │  │
│  │  • Receives user query                                     │  │
│  │  • Determines which sub-agents to engage                   │  │
│  │  • Coordinates parallel data gathering                     │  │
│  │  • Correlates findings across agents                       │  │
│  │  • Synthesizes comprehensive response                      │  │
│  │  • Recommends specific actions                             │  │
│  └────────┬──────────────────┬──────────────────┬────────────┘  │
│           │                  │                  │                 │
│           ▼                  ▼                  ▼                 │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐      │
│  │ MAINTENANCE    │ │ ALARM          │ │ KPI            │      │
│  │ AGENT          │ │ AGENT          │ │ AGENT          │      │
│  │ (Nova Lite)    │ │ (Nova Lite)    │ │ (Nova Lite)    │      │
│  │                │ │                │ │                │      │
│  │ • Ongoing work │ │ • Active alarms│ │ • Throughput   │      │
│  │ • Upcoming     │ │ • Severity     │ │ • Latency      │      │
│  │   maintenance  │ │ • Impact       │ │ • Packet loss  │      │
│  │ • Service      │ │ • Recommended  │ │ • Anomaly      │      │
│  │   windows      │ │   actions      │ │   detection    │      │
│  └───────┬────────┘ └───────┬────────┘ └───────┬────────┘      │
│          │                  │                  │                  │
│          ▼                  ▼                  ▼                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  AWS LAMBDA FUNCTIONS (Serverless Integration Layer)       │  │
│  │                                                             │  │
│  │  • Maintenance Checker                                     │  │
│  │  • Alarm Checker                                           │  │
│  │  • KPI Analyzer                                            │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                    │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  DATA LAYER (Amazon S3)                                    │  │
│  │                                                             │  │
│  │  s3://netops-network-data/                                 │  │
│  │  ├── data/                                                 │  │
│  │  │   ├── sites.csv          (Network site information)     │  │
│  │  │   ├── maintenance.csv    (Maintenance schedules)        │  │
│  │  │   ├── alarms.csv         (Active/historical alarms)     │  │
│  │  │   └── kpi_metrics.csv    (Performance metrics)          │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent Workflow (Step by Step)

```
User: "What is the status of site_dallas_001?"
         │
         ▼
┌─────────────────────────────────────────┐
│ 1. SUPERVISOR AGENT receives query       │
│    Analyzes intent, plans execution      │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
┌────────┐  ┌────────┐  ┌────────┐
│Maint.  │  │Alarm   │  │KPI     │
│Agent   │  │Agent   │  │Agent   │
│checks  │  │checks  │  │analyzes│
│schedule│  │active  │  │metrics │
│        │  │alarms  │  │        │
└───┬────┘  └───┬────┘  └───┬────┘
    │            │            │
    └────────────┼────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│ 2. SUPERVISOR correlates all findings    │
│    Identifies patterns and root causes   │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│ 3. RESPONSE formulated with:             │
│    • Site status summary                 │
│    • Active issues and severity          │
│    • Maintenance impact analysis         │
│    • Recommended actions                 │
└─────────────────────────────────────────┘
```

---

## Key Technical Details

### Foundation Models Used
| Agent | Model | Rationale |
|-------|-------|-----------|
| Supervisor | Amazon Nova Pro | Complex reasoning and coordination |
| Sub-agents | Amazon Nova Lite | Efficient, focused tasks |

*Note: Any Amazon Bedrock FM can be used (Claude Sonnet, Haiku, etc.)*

### Extensibility via MCP (Model Context Protocol)
The solution can be extended with real-time external integrations:
- **Power outage APIs** — correlate network issues with utility outages
- **Fiber cut detection** — "Call Before You Dig" databases
- **Weather impact** — predict network disruptions from weather data
- **Traffic/road work** — link network issues with infrastructure damage

### Agent2Agent (A2A) Protocol Support
Enables agents from different vendors/systems to communicate and collaborate.

---

## Why This Matters: Not Just Mobile

This architecture is **network-type agnostic**. The same multi-agent pattern works for:

| Network Type | Example Use Cases |
|-------------|-------------------|
| **Mobile (RAN)** | Cell anomaly detection, capacity optimization |
| **Fixed Broadband** | Fiber fault detection, CPE management |
| **Transport/Optical** | Path optimization, signal degradation |
| **Core Network** | UPF orchestration, slice management |
| **Enterprise/SD-WAN** | SLA monitoring, traffic engineering |

---

## Open Source & Deployment

### GitHub Repository
```
https://github.com/aws-samples/sample-multi-agent-collaboration-using-bedrock-for-telco-network-ops
```

### Deployment (15–20 minutes)
```bash
git clone https://github.com/aws-samples/sample-multi-agent-collaboration-using-bedrock-for-telco-network-ops.git
cd sample-multi-agent-collaboration-using-bedrock-for-telco-network-ops
./build_and_deploy.sh [stack-name] [region] [profile]
```

### What Gets Deployed
- Lambda layer with pandas/numpy
- Amazon Bedrock Agents with permissions
- Lambda functions for each AI agent
- S3 bucket with synthetic network data
- Streamlit app on Fargate
- Cognito for authentication
- ALB + CloudFront for access
- IAM roles and policies

---

## Other AWS Telecom Case Studies

| Customer | Solution | Status |
|----------|----------|--------|
| **BT Group** | Self-healing network with AWS + agentic AI for 5G SA (30M subscribers) | Production |
| **Telkomsel** | CELYNA — GenAI incident analysis with Amazon Nova Pro (hours → minutes) | Production |
| **NEC** | Agentic AI-driven autonomous UPF orchestration | Demonstrated at MWC 2026 |
| **Tech Mahindra** | AI-powered autonomous operations for European CSP (5G + IoT) | Production |
| **Ericsson** | rApp aaS on AWS (60+ CSPs, 13M sites) | Production |

---

## Sources
- [AWS Blog: Multi-Agent Collaboration for Telecom](https://aws.amazon.com/blogs/industries/multi-agent-collaboration-using-amazon-bedrock-for-telecom-network-operations/) (Sep 17, 2025)
- [AWS Blog: Shaping Future of Telco Operations](https://aws.amazon.com/blogs/industries/shaping-the-future-of-telco-operations-with-an-agentic-ai-collaboration-approach/) (Aug 2025)
- [GitHub: Multi-Agent Telco Network Ops](https://github.com/aws-samples/sample-multi-agent-collaboration-using-bedrock-for-telco-network-ops)
- [AWS: Telkomsel CELYNA Case Study](https://aws.amazon.com/solutions/case-studies/telkomsel-case-study/)
- [AWS Marketplace: RCA Network Operations Agent](https://aws.amazon.com/marketplace/pp/prodview-dgxz7ibjein4e)
- [BT Self-Healing Network with AWS](https://www.telcotitans.com/btwatch/bt-seeks-to-bring-self-healing-network-vision-to-life-with-a-little-help-from-aws/9974.article)
