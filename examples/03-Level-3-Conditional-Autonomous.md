---
tags: [examples, vendors, Level-3, AI-decisions, closed-loop, predictive]
---

# Level 3 — Conditional Autonomous

## Definition

The system **makes decisions and executes within specific domains** without asking for human approval. Humans oversee and can intervene, but the system operates autonomously within its defined boundaries. This is where AI starts making real decisions — not just following rules.

---

## What L3 Looks Like in Practice

| Capability | What Happens | Human Role |
|-----------|-------------|-----------|
| AI-driven optimization | ML models decide parameter changes in real-time | Human monitors outcomes, adjusts objectives |
| Predictive maintenance | System predicts failures and schedules fixes proactively | Human reviews predictions, approves major actions |
| Closed-loop within domain | Detect → Analyze → Decide → Act cycle runs autonomously | Human handles cross-domain exceptions |
| Anomaly detection + response | AI identifies anomalies AND takes corrective action | Human reviews post-action reports |
| Dynamic resource allocation | System scales resources based on demand prediction | Human sets budget/capacity constraints |

---

## Mobile Network Examples (L3)

### 1. AI-Driven RAN Optimization (rApps)
**What:** ML models continuously analyze cell performance, predict congestion, and autonomously adjust parameters (power, tilt, handover thresholds, scheduling weights) — without human approval per change.

**Human still does:** Sets optimization objectives ("maximize throughput while keeping drop rate < 0.5%"), reviews weekly performance trends, handles multi-domain issues.

**Key difference from L2 SON:** L2 SON uses static rules ("if load > 80%, activate MLB"). L3 uses ML models that learn patterns and make novel decisions the rules never anticipated.

**Vendors:**
| Vendor | Product | Key Capability |
|--------|---------|---------------|
| Ericsson | EIAP + rApps (Cell Anomaly Detector) | AI-driven anomaly detection and auto-remediation |
| Nokia | AVA Cognitive Analytics + MantaRay | ML-based RAN optimization |
| Huawei | MAE + IntelligentRAN | AI-powered radio optimization |
| Samsung | AI-RAN | Neural network-based scheduling |
| Qualcomm (Cellwize) | CHIME AI | Multi-vendor AI optimization |
| Parallel Wireless | Open RAN AI | AI for disaggregated RAN |
| Open source | O-RAN SC Near-RT RIC + xApps | ML-based real-time control |

### 2. Predictive Cell Outage Detection
**What:** AI models analyze patterns in KPIs (gradual degradation, unusual correlations) and predict a cell will fail 2–4 hours before it happens. System automatically activates Cell Outage Compensation on neighbors.

**Human still does:** Dispatches field team for physical repair, reviews prediction accuracy.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Ericsson | Cognitive Software (predictive analytics) |
| Nokia | AVA Anomaly Detection |
| Huawei | iMaster MAE Predictive Maintenance |
| Amdocs | NEON Predictive |

### 3. Dynamic Network Slicing
**What:** System monitors slice SLA compliance in real-time. When a slice approaches SLA violation, it autonomously reallocates resources from underutilized slices — no human approval needed.

**Human still does:** Defines slice SLA contracts, handles inter-slice conflicts that exceed policy.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Ericsson | Ericsson Orchestrator + 5G Core |
| Nokia | Nokia Digital Operations Center |
| Huawei | iMaster NCE Slice Manager |
| Amdocs | Network Slice Management |
| Open source | ONAP + 5G Core (Free5GC / Open5GS) |

### 4. Automated Energy Management
**What:** AI predicts traffic patterns per cell per hour. During predicted low-traffic periods, system autonomously shuts down capacity layers (carrier shutdown, MIMO reduction, cell sleep). Reactivates before traffic rises.

**Human still does:** Sets energy saving targets, defines "never sleep" cells (hospitals, airports).

**Vendors:**
| Vendor | Product | Claimed Savings |
|--------|---------|----------------|
| Ericsson | rApp: RAN Energy Saver | 15–20% energy reduction |
| Nokia | AVA Energy Efficiency | 10–20% savings |
| Huawei | PowerStar | Up to 30% savings |
| Open source | O-RAN Energy Saving xApp | Community-developed |

---

## Fixed Network Examples (L3)

### 1. Predictive Fiber Fault Detection
**What:** AI monitors optical power levels, BER trends, and temperature across fiber links. Predicts degradation (aging splice, bending, water ingress) and schedules maintenance before service impact.

**Human still does:** Dispatches field crew, validates prediction accuracy over time.

**Vendors:**
| Vendor | Product | How |
|--------|---------|-----|
| Nokia | Altiplano + Fiber Sensing | AI on optical telemetry |
| Huawei | NCE-FAN Intelligent O&M | Predictive analytics on PON |
| Calix | Calix Cloud Analytics | ML on CPE/ONT data |
| VIAVI | ONMSi + AI Analytics | Fiber monitoring + prediction |
| Open source | Custom ML on OTDR/power data | Python + TensorFlow |

### 2. Autonomous WiFi Optimization
**What:** System continuously analyzes WiFi performance per home (interference, channel utilization, client capabilities). Autonomously changes channels, power levels, band steering — per-home, per-hour.

**Human still does:** Nothing for standard cases. Handles complex multi-AP deployments.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Nokia | WiFi Care (Corteca) |
| Calix | GigaSpire BLAST + CommandIQ |
| Plume | HomePass Adaptive WiFi |
| Airties | Smart WiFi (AI-driven mesh) |
| Open source | OpenWrt + dawn (802.11k/v/r) |

### 3. Automated Fault Isolation (Fixed Access)
**What:** Customer reports "no internet." System automatically tests ONT reachability, optical power, VLAN connectivity, DHCP, DNS — isolates fault to specific layer (fiber, ONT, OLT, aggregation, core) and either auto-fixes or dispatches with precise diagnosis.

**Human still does:** Handles physical layer faults requiring field visit.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Nokia | Altiplano Diagnostics |
| Huawei | NCE-FAN Intelligent Diagnosis |
| Calix | Support Cloud (AI-driven) |
| EXFO | Nova Fiber (automated testing) |
| Open source | TR-369 (USP) + custom diagnostic agents |

---

## Technologies at L3

| Technology | Role | Open Source? |
|-----------|------|-------------|
| **Machine Learning (supervised)** | Prediction models (failure, traffic, anomaly) | Yes (scikit-learn, TensorFlow, PyTorch) |
| **Reinforcement Learning** | Optimization decisions (RAN parameters) | Yes (Ray RLlib, Stable Baselines) |
| **Time-series analysis** | Trend detection, forecasting | Yes (Prophet, ARIMA, DeepAR) |
| **Graph Neural Networks** | Topology-aware fault analysis | Yes (tf-GNN, PyG) |
| **MLOps platforms** | Model training, deployment, monitoring | Yes (MLflow, Kubeflow) |
| **Feature stores** | Real-time feature serving for ML | Yes (Feast) |
| **Event streaming** | Real-time data for ML inference | Yes (Apache Kafka, Pulsar) |
| **Near-RT RIC** | Real-time RAN control (10ms–1s) | Yes (O-RAN SC) |
| **Digital Twin (basic)** | Network state for simulation | Partial (custom builds) |

---

## Key Vendors Pushing L3

| Vendor | Strength | Key Products |
|--------|----------|-------------|
| **Ericsson** | RAN AI, rApps ecosystem | EIAP, Cognitive Software, rApps |
| **Nokia** | Fixed + mobile AI, broadband | AVA, Altiplano, MantaRay, Corteca |
| **Huawei** | End-to-end AI, scale | MAE, iMaster NCE, PowerStar |
| **Samsung** | AI-native RAN | AI-RAN, vRAN |
| **Cisco** | Transport + enterprise | Crosswork, ThousandEyes, NSO |
| **Juniper** | Intent-based networking | Apstra, Mist AI |
| **Amdocs** | BSS/OSS + AI | NEON, amAIz |
| **Netcracker** | Digital OSS/BSS | Autonomous Operations |
| **Google Cloud** | AI/ML platform, digital twin | Vertex AI, Spanner Graph |
| **AWS** | AI/ML platform, agents | Bedrock, SageMaker |

---

## Key Open Source Projects at L3

| Project | What It Does | Relevance |
|---------|-------------|-----------|
| **O-RAN SC Near-RT RIC** | Real-time RAN control platform | Hosts xApps for L3 RAN decisions |
| **ONAP (Holmes/DCAE)** | Analytics and closed-loop framework | Policy-driven automation with ML |
| **Acumos AI** | AI model marketplace and deployment | Share/deploy ML models across telco |
| **Magma** | Open mobile core | Programmable core for automation |
| **Free5GC / Open5GS** | Open 5G core | Enables slice management automation |
| **Apache Kafka** | Event streaming | Real-time data pipeline for ML |
| **Kubeflow** | ML pipeline orchestration | Train and deploy telco ML models |
| **MLflow** | ML experiment tracking | Manage model lifecycle |
| **TensorFlow / PyTorch** | ML frameworks | Build prediction/optimization models |

---

## What's Missing to Reach L4

| L3 Has | L4 Needs |
|--------|----------|
| Autonomous within ONE domain | Autonomous across MULTIPLE domains |
| Domain-specific closed loops | Cross-domain closed loops |
| AI decides within boundaries | AI decides in complex, novel scenarios |
| Human handles exceptions | System handles most exceptions autonomously |
| Reactive to predictions | Proactive end-to-end (anticipate before any signal) |
| Per-domain digital twin | Unified cross-domain digital twin |
| Vendor-specific AI | Multi-vendor agent collaboration (A2A) |

---

## Sources
- [Ericsson: Telecom Network Automation](https://www.ericsson.com/en/network-automation)
- [Ericsson: From SON to Centralized Automation](https://www.ericsson.com/en/blog/2022/5/from-son-to-centralized-automation)
- [Nokia: Fixed Access Network Automation](https://www.nokia.com/broadband-access/network-automation/)
- [Nokia: Agentic AI for Home and Broadband](https://www.telecomtv.com/content/network-automation/nokia-launches-agentic-ai-for-home-and-broadband-networks-55449/)
- [O-RAN Software Community](https://o-ran-sc.org/)
- [Cisco: Autonomous Networks for Service Providers](https://www.cisco.com/c/en/us/solutions/collateral/networking/auton-ntwk-sp-wp.html)
- [Bain: Accelerating Autonomous Networks](https://www.bain.com/insights/accelerating-autonomous-networks-a-reality-check-for-telcos/)
- [Verdict: Level 4 Automation Advantages](https://www.verdict.co.uk/level-4-autonomous-network-advantages/)
