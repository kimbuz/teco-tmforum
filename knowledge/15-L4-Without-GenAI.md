---
tags: [knowledge, an-levels, Level-4, GenAI, AI, clarification]
---

# Can You Achieve L4 Without GenAI?

## Short Answer

Yes. Level 4 Autonomous Networks do not require Generative AI or LLMs. The L4 criteria were defined in 2019–2020, years before GenAI became available. Operators have achieved L4 certification using classical ML, GNNs, policy engines, and well-designed closed-loops.

GenAI is an **accelerator**, not a prerequisite.

---

## L4 Criteria (What's Actually Required)

| Criteria | What It Means | GenAI Needed? |
|----------|--------------|---------------|
| Autonomous decision-making | System decides without asking humans | No — classical ML, RL, policy engines work |
| Cross-domain coordination | Actions span RAN + transport + core | No — orchestrators + event-driven architecture |
| Predictive/proactive operations | Anticipate failures before impact | No — time-series ML, GNNs |
| Minimal human intervention | Humans handle exceptions only | No — closed-loop automation |
| Continuous learning | System improves over time | No — reinforcement learning, online ML |

---

## Technologies That Deliver L4 Without GenAI

| Capability | Technology (No GenAI) | Examples |
|-----------|----------------------|----------|
| Anomaly detection | Random forests, LSTM, autoencoders | Ericsson Cell Anomaly Detector |
| Root cause analysis | Graph traversal, GNN, rule correlation | NetAI GraphML, Nokia AVA |
| Predictive maintenance | ARIMA, Prophet, DeepAR, time-series ML | Huawei iMaster predictive |
| Closed-loop automation | Policy engines, BPMN workflows, SON | ONAP, Ericsson EIAP |
| Cross-domain orchestration | Event-driven architecture, orchestrators | Cisco NSO, Nokia NSP |
| Energy optimization | Reinforcement learning | Ericsson RAN Energy Saver rApp |
| Decision-making | Decision trees, RL, Bayesian networks | Classical AIOps platforms |

---

## Real L4 Certifications — What They Used

| Operator | Year | Core Technology | GenAI Role |
|----------|------|----------------|-----------|
| MasOrange | 2026 | GNN (NetAI) + rApps (Ericsson) + policy orchestration | PoC for explainability only |
| Ooredoo Kuwait | 2025 | AIOps + analytics + automation platforms | Not mentioned |
| China Mobile | 2025 | Huawei MAE + iMaster NCE | Not core to certification |
| Ericsson rApp aaS | Production | Supervised ML, anomaly detection models | Agentic layer added later (2026) |

---

## What GenAI Actually Adds (Accelerator, Not Requirement)

| Without GenAI (still L4) | With GenAI (easier L4, path to L5) |
|--------------------------|-------------------------------------|
| Rules + ML make decisions | Agents reason about novel situations |
| Engineers write automation logic | Natural language intent → workflows |
| Fixed playbooks for known scenarios | Dynamic planning for unknown scenarios |
| Structured APIs for integration | MCP/A2A for flexible agent communication |
| Dashboard-based observability | Conversational network operations |
| Custom code per use case | Reusable agents across use cases |

---

## When GenAI Becomes Essential

| Level | GenAI Role |
|-------|-----------|
| L1–L3 | Not needed at all |
| L4 | Helpful but not required |
| L5 | Likely required — full end-to-end autonomy across all domains, including novel business decisions, probably needs agentic reasoning |

---

## Why This Matters

1. **Don't wait for GenAI to start the AN journey** — classical ML + good data + closed-loops can get you to L4
2. **Don't let vendors sell GenAI as mandatory** — it's a tool, not a prerequisite
3. **Invest in data quality first** — any AI (classical or generative) needs good data
4. **GenAI accelerates, not enables** — it makes L4 faster to achieve and easier to maintain
5. **Plan for GenAI at L5** — full autonomy likely needs agentic reasoning for truly novel situations

---

## Related Concepts

- [[02-Autonomous-Networks-Levels\|AN Levels (L0–L5)]]
- [[03-Closed-Loop-Automation\|Closed-Loop Automation]]
- [[07-Knowledge-Graph\|Knowledge Graph / GNN]]
- [[10-AIOps\|AIOps]]
- [[08-rApps-and-SMO\|rApps and SMO]]

---

## Sources
- [TM Forum: IG1218 AN Business Requirements v3.0](https://www.tmforum.org/resources/introductory-guide/autonomous-networks-business-requirements-and-framework-v3-0-0-ig1218/) — L4 defined without GenAI dependency
- [Bain: Accelerating Autonomous Networks](https://www.bain.com/insights/accelerating-autonomous-networks-a-reality-check-for-telcos/) — 20% at L4/L5 already
- [Ericsson: From SON to Centralized Automation](https://www.ericsson.com/en/blog/2022/5/from-son-to-centralized-automation) — classical ML path
- [Telecompaper: MasOrange L4 Certification](https://telecompaper.com/news/masorange-achieves-tm-forum-level-4-autonomous-network-certification--1572065)
