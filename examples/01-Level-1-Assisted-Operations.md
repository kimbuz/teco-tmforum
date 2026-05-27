# Level 1 — Assisted Operations

## Definition

The system provides information and assistance, but **humans execute all tasks and make all decisions**. The network gives you better visibility and reduces manual data gathering, but you still drive.

---

## What L1 Looks Like in Practice

| Capability | What Happens | Human Role |
|-----------|-------------|-----------|
| Monitoring dashboards | System collects and displays KPIs | Human reads and interprets |
| Alerting | System generates alarms when thresholds are crossed | Human decides what to do |
| Zero Touch Provisioning (ZTP) | New device auto-registers and gets base config | Human triggers deployment, system assists |
| Inventory discovery | System scans network and reports what exists | Human validates and corrects |
| Report generation | System produces performance/fault reports | Human analyzes and acts |

---

## Mobile Network Examples (L1)

### 1. Cell Site Auto-Configuration (ZTP)
**What:** A new gNodeB is powered on. It automatically contacts the management system, downloads its base configuration, and registers itself.

**Human still does:** Decides where to deploy, validates config is correct, activates the cell for traffic.

**Vendors:**
| Vendor | Product | How It Works |
|--------|---------|-------------|
| Ericsson | ENM (Ericsson Network Manager) | Auto-integration of new RAN nodes |
| Nokia | NetAct | Plug-and-play site commissioning |
| Huawei | iManager U2000/MAE | Auto-discovery and base config push |

### 2. Performance Dashboards
**What:** Real-time KPI visualization across all cells — throughput, latency, drop rates, availability.

**Human still does:** Identifies degraded cells, decides priority, assigns engineers.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Ericsson | Ericsson Expert Analytics (EEA) |
| Nokia | Nokia AVA (Analytics) |
| Huawei | SmartCare CEM |
| Open source | Grafana + Prometheus + SNMP/Streaming telemetry |

### 3. Alarm Forwarding and Enrichment
**What:** System collects alarms from all elements, enriches with topology context, forwards to NOC.

**Human still does:** Correlates alarms mentally, identifies root cause, dispatches fix.

---

## Fixed Network Examples (L1)

### 1. ONT Zero Touch Provisioning
**What:** Customer plugs in ONT. It auto-registers with the OLT, gets a management VLAN, and reports its serial number to the provisioning system.

**Human still does:** Triggers service activation, assigns VLAN/speed profile, validates connectivity.

**Vendors:**
| Vendor | Product | Protocol |
|--------|---------|----------|
| Huawei | NCE-FAN (Fixed Access Network) | OMCI, TR-069 |
| Nokia | Altiplano Access Controller | NETCONF/YANG |
| Calix | Calix Cloud | AXOS auto-provisioning |
| ZTE | ZXAN NMS | Auto-discovery |

### 2. Fiber Network Inventory Discovery
**What:** System scans OLTs and reports connected ONTs, power levels, distances, port utilization.

**Human still does:** Reconciles with planned inventory, identifies discrepancies, updates records.

### 3. CPE Remote Diagnostics
**What:** System collects CPE stats (WiFi channels, signal strength, connected devices) and presents to support agent.

**Human still does:** Interprets data, decides if issue is CPE, access, or core, guides customer.

**Vendors:**
| Vendor | Product |
|--------|---------|
| Nokia | WiFi Care / Corteca |
| Calix | CommandIQ + Support Cloud |
| Huawei | CloudCampus |
| Open source | TR-069/TR-369 (USP) + GenieACS |

---

## Technologies at L1

| Technology | Role | Open Source? |
|-----------|------|-------------|
| **SNMP** | Basic device monitoring | Yes (protocol) |
| **NETCONF/YANG** | Structured device config and state | Yes (IETF standard) |
| **TR-069/TR-369** | CPE remote management | Yes (Broadband Forum standard) |
| **Streaming telemetry** | Real-time metrics from devices | Yes (gNMI, gRPC) |
| **Syslog** | Event/log collection | Yes |
| **Grafana + Prometheus** | Dashboards and alerting | Yes |
| **Zabbix / Nagios** | Infrastructure monitoring | Yes |
| **ELK Stack** | Log aggregation and search | Yes |

---

## What's Missing to Reach L2

| L1 Has | L2 Needs |
|--------|----------|
| Dashboards (human reads) | Automated recommendations |
| Alarms (human correlates) | Automated correlation and grouping |
| ZTP (base config only) | Policy-driven full service provisioning |
| Manual troubleshooting | Scripted/playbook-driven remediation |
| Static thresholds | Dynamic baselines |

---

## Sources
- [Nokia: Zero Touch Provisioning](https://infocenter.nokia.com/public/7750SR205R1A/topic/com.sr.basic/html/ztp.html)
- [Cisco: Crosswork Zero-Touch Provisioning](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/crosswork-network-automation/datasheet-c78-743677.html)
- [Huawei: NCE Fixed Access Network Automation](https://carrier.huawei.com/en/products/fixed-network/nce/NCE-FAN/Access-automation)
- [Nokia: Simplify Mobile Transport Rollouts with ZTP](https://www.nokia.com/blog/simplify-mobile-transport-network-rollouts/)
