---
tags: [examples, vendors, Level-2, SON, orchestration, playbooks]
---

# Level 2 — Partial Autonomous

## Definition

The system **executes specific tasks under human supervision**. Humans still make the decisions, but the system carries out defined workflows automatically based on policies and rules. Think of it as "automation with a human approving."

---

## What L2 Looks Like in Practice

| Capability | What Happens | Human Role |
|-----------|-------------|-----------|
| Policy-based provisioning | System provisions services based on predefined rules | Human designs policies, system executes |
| SON (Self-Organizing Networks) | System auto-tunes RAN parameters within bounds | Human sets boundaries, monitors results |
| Scripted remediation | Playbooks execute when specific alarms trigger | Human approves or reviews after execution |
| Automated testing | System runs post-change validation automatically | Human reviews results |
| Workflow orchestration | Multi-step processes execute end-to-end | Human triggers, system orchestrates |

---

## Mobile Network Examples (L2)

### 1. SON — Self-Organizing Networks (RAN)
**What:** The system continuously adjusts RAN parameters (handover thresholds, power levels, antenna tilts, neighbor lists) based on traffic patterns and KPIs.

**Human still does:** Sets optimization objectives, defines boundaries, reviews weekly reports, handles exceptions.

**SON Functions:**
| Function | What It Does | Abbreviation |
|----------|-------------|-------------|
| Automatic Neighbor Relations | Discovers and maintains neighbor cell lists | ANR |
| Mobility Robustness Optimization | Reduces handover failures | MRO |
| Mobility Load Balancing | Distributes traffic across cells | MLB |
| Coverage and Capacity Optimization | Adjusts tilts/power for coverage | CCO |
| Random Access Optimization | Tunes RACH parameters | RACH Opt |
| Inter-Cell Interference Coordination | Manages interference between cells | ICIC |
| Energy Saving | Shuts down capacity layers during low traffic | ES |
| Cell Outage Compensation | Adjusts neighbors when a cell fails | COC |

**Vendors:**
| Vendor | Product | Deployment |
|--------|---------|-----------|
| Ericsson | SON features in ENM + EIAP | Embedded in RAN management |
| Nokia | AVA SON (Autonomous Optimization) | Centralized SON platform |
| Huawei | MAE (Mobile Automation Engine) | AI-assisted SON |
| Cellwize (now Qualcomm) | CHIME | Multi-vendor centralized SON |
| Amdocs | NEON (Network Optimization) | Vendor-agnostic SON |
| Open source | O-RAN SC (Near-RT RIC) | xApps for RAN control |

### 2. Automated Alarm Correlation
**What:** System groups related alarms into a single incident, identifies probable root cause from rules, and suggests resolution.

**Human still does:** Validates the correlation, approves the fix, dispatches if needed.

**Vendors:**
| Vendor | Product |
|--------|---------|
| IBM | Netcool/OMNIbus + Impact |
| BMC | Helix Operations Management |
| Moogsoft | AIOps platform |
| ServiceNow | ITOM Event Management |
| Open source | Zabbix correlation + custom rules |

### 3. Automated Service Provisioning (Orchestrated)
**What:** Customer orders a service → orchestrator decomposes into tasks → executes across multiple systems (BSS, OSS, network elements) automatically.

**Human still does:** Designs the workflow, handles exceptions/failures, approves complex orders.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Nokia | Nokia NSP (Network Services Platform) |
| Cisco | NSO (Network Services Orchestrator) |
| Huawei | iMaster NCE |
| Netcracker | Digital OSS |
| Amdocs | Service Orchestration |
| Open source | ONAP (Open Network Automation Platform) |
| Open source | Apache ServiceComb |

---

## Fixed Network Examples (L2)

### 1. Automated FTTH Service Activation
**What:** Customer order triggers automatic ONT provisioning — VLAN assignment, speed profile, QoS, IP allocation — all executed without manual CLI commands.

**Human still does:** Handles exceptions (wrong ONT, fiber not connected), validates complex orders.

**Vendors:**
| Vendor | Product | How |
|--------|---------|-----|
| Nokia | Altiplano Access Controller | NETCONF/YANG to OLTs, policy-driven |
| Huawei | NCE-FAN + iMaster NCE | Automated workflow orchestration |
| Calix | Calix Cloud + AXOS | Cloud-managed provisioning |
| Adtran | Mosaic Cloud Platform | Intent-based access automation |
| Open source | Netbox + Ansible + NETCONF | Custom automation stack |

### 2. Automated Bandwidth Upgrades
**What:** Customer requests speed upgrade via app → system validates capacity → changes QoS profile → confirms in seconds.

**Human still does:** Nothing for standard upgrades; handles capacity-constrained cases.

### 3. Scheduled Maintenance Automation
**What:** System executes maintenance windows automatically — traffic rerouting, config backup, firmware upgrade, validation, traffic restoration.

**Human still does:** Approves the maintenance window, reviews post-change report.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Cisco | Crosswork Change Automation |
| Nokia | NSP Workflow Manager |
| Juniper | Apstra (intent-based) |
| Open source | Ansible AWX/Tower + custom playbooks |
| Open source | StackStorm (event-driven automation) |

---

## Technologies at L2

| Technology | Role | Open Source? |
|-----------|------|-------------|
| **Ansible** | Playbook-driven automation | Yes |
| **Terraform** | Infrastructure as Code | Yes |
| **NETCONF/YANG** | Structured config management | Yes (IETF) |
| **ONAP** | Telco orchestration platform | Yes (Linux Foundation) |
| **Cisco NSO** | Network service orchestrator | No (commercial) |
| **StackStorm** | Event-driven automation | Yes |
| **Camunda / Flowable** | BPMN workflow engines | Yes |
| **OpenConfig** | Vendor-neutral device models | Yes |
| **gNMI** | Streaming telemetry | Yes |
| **O-RAN SC** | Open RAN software community | Yes |
| **ONOS / OpenDaylight** | SDN controllers | Yes |

---

## Key Open Source Projects at L2

| Project | What It Does | Backed By |
|---------|-------------|-----------|
| **ONAP** | End-to-end orchestration, policy, closed-loop | Linux Foundation, AT&T, China Mobile |
| **O-RAN SC** | Open RAN software (Near-RT RIC, xApps) | O-RAN Alliance |
| **OpenDaylight** | SDN controller | Linux Foundation |
| **ONOS** | SDN controller (carrier-grade) | Open Networking Foundation |
| **Ansible** | Automation engine | Red Hat |
| **StackStorm** | Event-driven automation | Extreme Networks |
| **Netbox** | Network source of truth (IPAM/DCIM) | DigitalOcean |
| **Nautobot** | Network automation platform | Network to Code |
| **nornir** | Python automation framework | Community |
| **Batfish** | Network config analysis/validation | Intentionet |

---

## What's Missing to Reach L3

| L2 Has | L3 Needs |
|--------|----------|
| Rule-based decisions (if X then Y) | ML-based decisions (predict and act) |
| Human approves actions | System acts autonomously within domain |
| Static policies | Adaptive policies that learn |
| Alarm correlation (rules) | AI-driven root cause analysis |
| Scheduled optimization | Continuous real-time optimization |
| Single-domain workflows | Cross-system awareness (still within domain) |

---

## Sources
- [Ericsson: From SON to Centralized Automation](https://www.ericsson.com/en/blog/2022/5/from-son-to-centralized-automation)
- [SNS Telecom: RAN Automation, SON, RIC, xApps & rApps](https://www.snstelecom.com/son)
- [Nokia: Fixed Access Network Automation](https://www.nokia.com/broadband-access/network-automation/)
- [ONAP: Open Network Automation Platform](https://www.onap.org/)
- [O-RAN Software Community](https://o-ran-sc.org/)
- [Cisco: NSO Network Services Orchestrator](https://www.cisco.com/c/en/us/products/cloud-systems-management/network-services-orchestrator/index.html)
