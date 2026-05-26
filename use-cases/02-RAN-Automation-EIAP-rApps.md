# Use Case 02: RAN Automation with Ericsson EIAP & rApps

## Summary

MasOrange deployed the **Ericsson Intelligent Automation Platform (EIAP)** with AI-powered **rApps** in its commercial network to deliver automated RAN optimization and energy efficiency. This is a **production deployment** (December 2025), not a PoC.

---

## The Problem

As MasOrange scales its 5G network (one-third already O-RAN-ready, 5G Advanced in 40 cities), manual network management becomes unsustainable:

- Increasingly complex multi-vendor, multi-technology RAN
- Need for continuous optimization across thousands of cells
- Energy costs rising with network densification
- Performance anomalies hard to detect manually at scale
- Human operators cannot react fast enough to dynamic conditions

---

## The Solution

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              Ericsson Intelligent Automation Platform (EIAP)      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │         SERVICE MANAGEMENT & ORCHESTRATION (SMO)           │  │
│  │                                                             │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │              rApps ECOSYSTEM                          │  │  │
│  │  │                                                       │  │  │
│  │  │  ┌─────────────────┐    ┌─────────────────────────┐ │  │  │
│  │  │  │  Ericsson Cell  │    │  Future Connections     │ │  │  │
│  │  │  │  Anomaly        │    │  Nix RAN Energy Saver   │ │  │  │
│  │  │  │  Detector       │    │                         │ │  │  │
│  │  │  │                 │    │  • Dynamic config       │ │  │  │
│  │  │  │  • Proactive    │    │  • Monitor & optimize   │ │  │  │
│  │  │  │    detection    │    │  • Energy saving        │ │  │  │
│  │  │  │  • Automatic    │    │    features             │ │  │  │
│  │  │  │    diagnosis    │    │  • No service impact    │ │  │  │
│  │  │  │  • Reduced MTTR │    │                         │ │  │  │
│  │  │  └─────────────────┘    └─────────────────────────┘ │  │  │
│  │  │                                                       │  │  │
│  │  │  ┌─────────────────┐    ┌─────────────────────────┐ │  │  │
│  │  │  │  3rd Party      │    │  Additional Ericsson    │ │  │  │
│  │  │  │  rApps          │    │  rApps (ecosystem)      │ │  │  │
│  │  │  │  (multi-vendor) │    │                         │ │  │  │
│  │  │  └─────────────────┘    └─────────────────────────┘ │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                    │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │         ERICSSON NETWORK MANAGER (ENM)                     │  │
│  │         (Integration with commercial network)              │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                    │
└──────────────────────────────┼──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MasOrange RAN                                  │
│                                                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │  5G SA   │  │  5G Adv  │  │  4G LTE  │  │  O-RAN Ready │   │
│  │  Cells   │  │  Cells   │  │  Cells   │  │  Sites       │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│                                                                   │
│  Coverage: 40+ cities | 15M+ people | 1/3 O-RAN ready           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Deployed rApps

### 1. Ericsson Cell Anomaly Detector
**Purpose:** Proactive detection of network performance issues

| Feature | Description |
|---------|-------------|
| Detection | Automatically identifies performance anomalies across cells |
| Speed | Significantly reduces time to detect issues |
| Expertise | Reduces need for specialized human expertise |
| Scale | Manages increasingly complex networks automatically |
| Action | Triggers automated diagnosis and remediation |

### 2. Future Connections Nix RAN Energy Saver
**Purpose:** Maximize energy efficiency without impacting service

| Feature | Description |
|---------|-------------|
| Configuration | Dynamically configures energy saving features |
| Monitoring | Continuously monitors energy consumption patterns |
| Optimization | Optimizes RAN energy saving in real-time |
| Protection | Avoids any impact on service performance |
| Sustainability | Contributes to network sustainability goals |

---

## How rApps Work

```
┌─────────────────────────────────────────────────┐
│                rApp Lifecycle                     │
├─────────────────────────────────────────────────┤
│                                                   │
│  1. DATA COLLECTION                              │
│     │  Rich network data (KPIs, counters,        │
│     │  configuration, topology)                  │
│     ▼                                            │
│  2. AI/ML PROCESSING                            │
│     │  Machine learning models analyze           │
│     │  patterns, detect anomalies, predict       │
│     ▼                                            │
│  3. DECISION                                     │
│     │  Automated decision based on               │
│     │  optimization objectives                   │
│     ▼                                            │
│  4. ACTION                                       │
│     │  Configuration changes pushed to           │
│     │  network via SMO/ENM                       │
│     ▼                                            │
│  5. VERIFICATION                                 │
│     │  Closed-loop: verify action achieved       │
│     │  desired outcome                           │
│     ▼                                            │
│  6. LEARN                                        │
│        Reinforcement learning improves           │
│        future decisions                          │
│                                                   │
└─────────────────────────────────────────────────┘
```

---

## Key Technical Details

### SMO (Service Management & Orchestration)
- Standardized O-RAN architecture
- Enables multi-vendor interoperability
- Provides interfaces for rApp integration
- Supports both Ericsson and 3rd-party rApps

### Open RAN Ecosystem
- One-third of MasOrange's 5G network is O-RAN-ready
- Flexibility to integrate solutions from multiple suppliers
- Boosts interoperability and innovation
- Dynamic vendor ecosystem

### Integration Path
```
EIAP ←→ ENM (Ericsson Network Manager) ←→ Commercial RAN
```

---

## Results & Benefits

| Metric | Impact |
|--------|--------|
| **Operational efficiency** | Up to 80% OPEX savings (proven in Ericsson deployments) |
| **Detection speed** | Significantly reduced time to identify anomalies |
| **Energy savings** | Dynamic optimization without service degradation |
| **User experience** | Higher bitrates, capacity, and responsiveness |
| **Automation level** | Moves toward zero-touch RAN management |

---

## Broader Context

This deployment is part of MasOrange's journey toward a **highly programmable network**:

| Year | Milestone |
|------|-----------|
| 2024 | Programmable network integration announced |
| Dec 2025 | EIAP + rApps production deployment |
| 2026 | Foundation for fully programmable capabilities at scale |

### Other Operators Using EIAP
- AT&T
- Vodafone
- Swisscom
- Telstra
- One NZ

---

## Relevance to TM Forum AN Levels

| AN Capability | How EIAP Delivers |
|--------------|-------------------|
| Self-optimization | rApps continuously optimize RAN parameters |
| Self-healing | Cell Anomaly Detector identifies and triggers fixes |
| Closed-loop | Automated detect → decide → act → verify cycle |
| Multi-domain | SMO orchestrates across RAN domains |
| Intent-based | rApps translate performance intents into actions |

---

## Key Quote

> "rApps are the future of network management, with intelligent automation empowering service providers to deliver superior service quality with greater speed and precision. By collaborating closely with MasOrange, we are able to tailor our solutions to real-world environments and gather invaluable insights that will inform broader adoption of autonomous networks across the industry."
> — **Jean-Christophe Laneri**, Head of Cognitive Network Solutions, Ericsson

---

## Sources
- [Ericsson Press Release: MasOrange EIAP Deployment](https://www.ericsson.com/en/press-releases/3/2025/ericsson-and-masorange-advance-autonomous-networks-with-ai-driven-automation-platform-and-rapps) (Dec 10, 2025)
- [SDxCentral: Ericsson Helps MasOrange](https://www.sdxcentral.com/news/ericsson-helps-masorange-advance-autonomous-networks/)
- [TelecomTV: Spain's MasOrange Automates RAN](https://www.telecomtv.com/content/network-automation/spain-s-m-sorange-automates-its-ran-with-ericsson-54496/)
- [RCR Wireless: MasOrange O-RAN](https://www.rcrwireless.com/20251212/5g/masorange-5g-o-ran)
- [Ericsson EIAP Product Page](https://www.ericsson.com/en/ran/intelligent-ran-automation/intelligent-automation-platform)
