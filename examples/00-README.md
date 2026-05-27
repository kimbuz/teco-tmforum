# Examples — AN Levels in the Real World (L1 to L3)

Concrete examples of what Autonomous Network Levels 1, 2, and 3 look like in production today. Covers mobile and fixed networks, with focus on architecture, technologies, and vendors involved.

---

## Documents

| # | Level | Focus | What You'll Learn |
|---|-------|-------|-------------------|
| 01 | [Level 1 — Assisted Operations](./01-Level-1-Assisted-Operations.md) | ZTP, dashboards, basic alerting | What most telcos already have |
| 02 | [Level 2 — Partial Autonomous](./02-Level-2-Partial-Autonomous.md) | SON, policy-based automation, scripted workflows | Where most telcos are today |
| 03 | [Level 3 — Conditional Autonomous](./03-Level-3-Conditional-Autonomous.md) | Domain-specific AI decisions, closed-loop within domains | The frontier before L4 |

---

## Why This Matters

Everyone talks about L4 and L5. But understanding L1–L3 is critical because:
- It's where **your network probably is right now**
- It shows the **gap** between current state and target
- It reveals which **technologies and vendors** are already deployed
- It helps identify **what's missing** to reach the next level

---

## Quick Comparison

| Aspect | L1 | L2 | L3 |
|--------|----|----|-----|
| Who decides | Human | Human (system recommends) | System (human oversees) |
| Who executes | Human (system assists) | System (under human control) | System (within a domain) |
| Automation type | Task automation | Policy-based workflows | AI-driven domain decisions |
| Typical tech | ZTP, dashboards, scripts | SON, orchestrators, playbooks | ML models, closed-loop per domain |
| Fixed network | Auto-provisioning ONT | Automated VLAN assignment | Predictive fiber fault detection |
| Mobile network | Auto-config new cell | SON parameter tuning | AI-driven RAN optimization |
