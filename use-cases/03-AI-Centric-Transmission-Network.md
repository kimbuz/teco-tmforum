---
tags: [use-case, MasOrange, transport, AI, self-healing]
---

# Use Case 03: AI-Centric Transmission Network Reinvention

## Summary

MasOrange is leveraging automation and AI to reinvent its **transport/transmission network**, making it intelligent and adaptive. The goal is to progress toward Level 4 autonomous operations in the transmission domain — enabling the network to learn, anticipate issues, and self-optimize.

---

## The Problem

AI workloads are reshaping transport network requirements:

- **East-west traffic explosion** — AI workloads drive heavy data exchanges between data centers
- **Unprecedented capacity demands** — Optical transmission is no longer a background utility but a key enabler
- **Complexity of merged networks** — Post-merger (Orange Spain + MASMOVIL), MasOrange must unify and optimize a massive transmission infrastructure
- **Manual operations don't scale** — 41 million lines require automated management
- **Service quality expectations** — Customers expect zero-downtime, high-bandwidth connectivity

---

## The Solution

### Strategic Vision

MasOrange treats the transmission network as a **product** — not just infrastructure. AI is pushing them to rethink how the network works and delivers value.

> "For us, Artificial Intelligence is pushing us to rethink the basics of how our network works and how we deliver value to our customer. And maybe the most important thing is that our customers use our transmission network all the days, even if they never notice."
> — **Pilar Puerta Galvan**, Transmission Director, MasOrange

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│           AI-Centric Transmission Network Architecture            │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              AUTONOMOUS OPERATIONS LAYER                   │  │
│  │                                                             │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐  │  │
│  │  │  PREDICT     │  │  DECIDE      │  │  ACT           │  │  │
│  │  │              │  │              │  │                │  │  │
│  │  │  • Failure   │  │  • Optimal   │  │  • Self-heal  │  │  │
│  │  │    forecast  │  │    routing   │  │  • Reroute    │  │  │
│  │  │  • Capacity  │  │  • Capacity  │  │  • Reconfigure│  │  │
│  │  │    planning  │  │    allocation│  │  • Scale      │  │  │
│  │  │  • Anomaly   │  │  • Energy    │  │  • Optimize   │  │  │
│  │  │    detection │  │    policy    │  │               │  │  │
│  │  └──────────────┘  └──────────────┘  └────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                    │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              AI/ML ENGINE                                   │  │
│  │                                                             │  │
│  │  • Machine Learning models for traffic prediction          │  │
│  │  • Intent-based orchestration for service lifecycle        │  │
│  │  • Pattern recognition for anomaly detection               │  │
│  │  • Reinforcement learning for optimization                 │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                    │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              TRANSMISSION INFRASTRUCTURE                    │  │
│  │                                                             │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │  OPTICAL LAYER                                        │ │  │
│  │  │  • 2 Tbps live data transmission (Madrid)             │ │  │
│  │  │  • Supports 800,000 simultaneous HD channels          │ │  │
│  │  │  • Or 160,000 4K ultra-HD channels                    │ │  │
│  │  │  • Highly redundant topology                          │ │  │
│  │  └──────────────────────────────────────────────────────┘ │  │
│  │                                                             │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │  IP/MPLS LAYER                                        │ │  │
│  │  │  • Unified post-merger architecture                   │ │  │
│  │  │  • Multi-path redundancy                              │ │  │
│  │  │  • Traffic engineering                                │ │  │
│  │  └──────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Capabilities

### 1. Predictive Operations
- Anticipate failures before they impact customers
- Forecast capacity needs based on traffic patterns
- Detect degradation trends in optical signals

### 2. Self-Optimization
- Dynamically adjust routing based on real-time conditions
- Optimize energy consumption during low-traffic periods
- Balance load across redundant paths

### 3. Self-Healing
- Automatic rerouting when failures occur
- Restoration of service without human intervention
- Minimized mean time to repair (MTTR)

### 4. Intent-Based Management
- Define desired outcomes (e.g., "maintain 99.999% availability for this service")
- Network autonomously determines how to achieve the intent
- End-to-end service lifecycle management

---

## Capacity Achievements

| Metric | Value |
|--------|-------|
| Live transmission capacity (Madrid) | **2 Tbps** |
| Simultaneous HD channels supported | **800,000** |
| Simultaneous 4K channels supported | **160,000** |
| Network redundancy | Highly redundant topology |
| Customer lines | 41 million |

---

## Level 4 Characteristics in Transmission

At Level 4, the transmission network can:

| Capability | Description |
|-----------|-------------|
| **Predict** | Forecast failures and capacity needs |
| **Decide** | Autonomously choose optimal actions |
| **Act** | Execute changes with minimal human involvement |
| **Learn** | Continuously improve from operational data |
| **Self-heal** | Restore service automatically |
| **Self-optimize** | Adjust parameters for best performance |

---

## Integration with Broader AN Strategy

The transmission network automation connects to MasOrange's overall autonomous network strategy:

```
┌─────────────────────────────────────────────┐
│         MasOrange AN Domains                 │
├─────────────────────────────────────────────┤
│                                               │
│  ┌─────────┐  ┌─────────────┐  ┌─────────┐ │
│  │  RAN    │  │ TRANSMISSION│  │  CORE   │ │
│  │  Domain │  │ DOMAIN      │  │  Domain │ │
│  │         │  │             │  │         │ │
│  │ EIAP +  │  │ AI-Centric  │  │ Unified │ │
│  │ rApps   │  │ Automation  │  │ 5G SA   │ │
│  │         │  │             │  │ Core    │ │
│  └────┬────┘  └──────┬──────┘  └────┬────┘ │
│       │              │              │        │
│       └──────────────┼──────────────┘        │
│                      ▼                        │
│         ┌────────────────────────┐           │
│         │  Cross-Domain          │           │
│         │  Orchestration         │           │
│         │  (Intent-Based)        │           │
│         └────────────────────────┘           │
│                                               │
└─────────────────────────────────────────────┘
```

---

## Why Transmission Matters for AI Era

The transmission network is becoming critical infrastructure for AI:

1. **AI training** requires massive east-west bandwidth between GPU clusters
2. **AI inference** at the edge needs low-latency, high-reliability transport
3. **Network AI** itself depends on real-time data flowing through transport
4. **5G services** (slicing, URLLC) require guaranteed transport performance

---

## Sources
- [TelecomTV: MasOrange Reinvents Transmission Network](https://www.telecomtv.com/content/5g/masorange-reinvents-its-transmission-network-for-the-ai-centric-era-55176/) (January 2026)
- [TelecomTV: Spotlight on 5G — MasOrange](https://www.telecomtv.com/content/spotlight-on-5g/masorange-reinvents-its-transmission-network-for-the-ai-centric-era-55197/)
- [Ericsson: MasOrange 5G Core Agreement](https://www.ericsson.com/en/press-releases/3/2026/ericsson-and-masorange-sign-agreement-for-5g-core) (Feb 2026)
