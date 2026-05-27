---
tags: [use-case, data-model, CFS, RFS, catalog, inventory]
---

# Use Case 07: Data Architecture — From Legacy Telco Data to Autonomous Networks

## The Core Question

How do you move from actual telco data (fragmented OSS/BSS, siloed inventories, inconsistent catalogs) to the information structure needed for Autonomous Networks use cases?

---

## TM Forum Data Model: Product → Service → Resource (PSR)

The TM Forum defines a layered data model that decouples commercial offers from technical implementations:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TM Forum PSR Model                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  PRODUCT LAYER (What we sell)                              │  │
│  │                                                             │  │
│  │  Product Catalog ──→ Product Inventory                     │  │
│  │  (TMF620)             (TMF637)                             │  │
│  │                                                             │  │
│  │  • Product Offerings (bundles, plans)                      │  │
│  │  • Pricing and eligibility                                 │  │
│  │  • Customer-visible characteristics                        │  │
│  │  • Commercial lifecycle                                    │  │
│  └──────────────────────────┬────────────────────────────────┘  │
│                              │ decomposes to                      │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  SERVICE LAYER (What we deliver)                           │  │
│  │                                                             │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  CFS (Customer Facing Service)                       │  │  │
│  │  │  • Technology-agnostic                               │  │  │
│  │  │  • Reusable across products                          │  │  │
│  │  │  • Represents what customer experiences              │  │  │
│  │  │  • Example: "Internet Access 100Mbps"                │  │  │
│  │  └──────────────────────────┬──────────────────────────┘  │  │
│  │                              │ decomposes to                │  │
│  │                              ▼                              │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  RFS (Resource Facing Service)                       │  │  │
│  │  │  • Technology-specific                               │  │  │
│  │  │  • Domain-specific (IP, FTTH, HFC, RAN, etc.)       │  │  │
│  │  │  • Maps to actual network resources                  │  │  │
│  │  │  • Example: "GPON ONT Port Activation"               │  │  │
│  │  └──────────────────────────┬──────────────────────────┘  │  │
│  │                              │                              │  │
│  │  Service Catalog ──→ Service Inventory                     │  │
│  │  (TMF633)             (TMF638)                             │  │
│  └──────────────────────────┬────────────────────────────────┘  │
│                              │ maps to                            │
│                              ▼                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  RESOURCE LAYER (What we operate)                          │  │
│  │                                                             │  │
│  │  Resource Catalog ──→ Resource Inventory                   │  │
│  │  (TMF634)              (TMF639)                            │  │
│  │                                                             │  │
│  │  • Physical resources (routers, OLTs, antennas, fiber)    │  │
│  │  • Logical resources (VLANs, IP addresses, ports)         │  │
│  │  • Network functions (VNFs, CNFs)                          │  │
│  │  • Topology and connectivity                               │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## CFS vs RFS — Key Differences

| Aspect | CFS (Customer Facing Service) | RFS (Resource Facing Service) |
|--------|-------------------------------|-------------------------------|
| **Perspective** | Customer/business view | Technical/network view |
| **Technology** | Technology-agnostic | Technology-specific |
| **Domain** | Cross-domain | Domain-specific (IP, FTTH, RAN, etc.) |
| **Reusability** | Reusable across products | Specific to technology |
| **Example** | "Broadband 500Mbps" | "GPON ONT Config + VLAN Assignment" |
| **Lifecycle** | Tied to product/customer | Tied to network resources |
| **Mapping** | 1 CFS → N RFS | 1 RFS → N Resources |

### Example Decomposition

```
PRODUCT: "Home Fiber 500Mbps + TV + Phone"
    │
    ├── CFS: Internet Access 500Mbps
    │       ├── RFS: GPON ONT Port Activation
    │       ├── RFS: VLAN Assignment (data)
    │       ├── RFS: IP Address Assignment
    │       └── RFS: QoS Profile Configuration
    │
    ├── CFS: IPTV Service
    │       ├── RFS: Multicast VLAN Assignment
    │       ├── RFS: STB Provisioning
    │       └── RFS: Content Delivery Config
    │
    └── CFS: VoIP Service
            ├── RFS: SIP Registration
            ├── RFS: Voice VLAN Assignment
            └── RFS: Number Porting
```

---

## TM Forum ODA Components for Inventory & Catalog

| Component ID | Name | Responsibility |
|-------------|------|----------------|
| **TMFC001** | Product Catalog Management | Product offerings, specifications, pricing |
| **TMFC002** | Product Inventory | Active product instances per customer |
| **TMFC006** | Service Catalog Management | Service specifications and requirements |
| **TMFC008** | Service Inventory | CFS instances + RFS definitions + CFS↔RFS mapping + resource mapping |
| **TMFC012** | Resource Inventory | Physical/logical resource instances, topology |
| **TMFC010** | Resource Catalog | Resource specifications and capabilities |

### Key Open APIs

| API | Purpose | Role in AN |
|-----|---------|-----------|
| **TMF620** | Product Catalog Management | Define what can be sold |
| **TMF633** | Service Catalog Management | Define service specifications |
| **TMF634** | Resource Catalog Management | Define resource types |
| **TMF637** | Product Inventory Management | Track active products |
| **TMF638** | Service Inventory Management | Track CFS/RFS instances |
| **TMF639** | Resource Inventory Management | Track network resources |
| **TMF641** | Service Order Management | Orchestrate service delivery |
| **TMF652** | Resource Order Management | Orchestrate resource provisioning |

---

## Why This Matters for Autonomous Networks

### The Data Foundation Problem

Autonomous Networks need **real-time, accurate, correlated data** across all layers. Without proper PSR modeling:

| Problem | Impact on AN |
|---------|-------------|
| No CFS↔RFS mapping | Can't correlate customer impact with network faults |
| Stale resource inventory | Digital twin is inaccurate → wrong AI decisions |
| No service topology | Can't predict fault propagation |
| Fragmented catalogs | Can't automate service lifecycle |
| Missing relationships | Can't do root cause analysis across domains |

### What AN Needs from Data

```
┌─────────────────────────────────────────────────────────────────┐
│         Data Requirements for Autonomous Networks                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  1. REAL-TIME RESOURCE STATE                                     │
│     • Current configuration of every network element             │
│     • Performance metrics (KPIs) per resource                    │
│     • Alarm/fault state                                          │
│     • Capacity utilization                                       │
│                                                                   │
│  2. SERVICE TOPOLOGY (CFS ↔ RFS ↔ Resource)                     │
│     • Which customers are affected by which resources            │
│     • Service dependency chains                                  │
│     • Redundancy and failover paths                              │
│     • SLA requirements per service                               │
│                                                                   │
│  3. NETWORK TOPOLOGY (Graph)                                     │
│     • Physical connectivity (fiber, radio links)                 │
│     • Logical connectivity (VLANs, tunnels, slices)              │
│     • Layer relationships (L1 → L2 → L3 → Service)              │
│     • Geographic/location data                                   │
│                                                                   │
│  4. HISTORICAL PATTERNS                                          │
│     • Past incidents and resolutions                             │
│     • Traffic patterns and trends                                │
│     • Change history (what was modified, when, by whom)          │
│     • Performance baselines                                      │
│                                                                   │
│  5. INTENT & POLICY                                              │
│     • Business intents (SLA targets, cost constraints)           │
│     • Network policies (routing, security, QoS)                  │
│     • Automation rules and guardrails                            │
│     • Compliance requirements                                    │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Transformation Roadmap: Legacy → AN-Ready Data

### Phase 1: Inventory Reconciliation
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Discovery   │────▶│  Reconcile   │────▶│  Unified     │
│  (Network    │     │  (Match OSS  │     │  Resource    │
│   Scan)      │     │   vs Reality)│     │  Inventory   │
└──────────────┘     └──────────────┘     └──────────────┘
```
- Automated network discovery to find actual resources
- Reconcile with existing OSS inventory
- Establish single source of truth (Resource Inventory)

### Phase 2: Service Modeling
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Define CFS  │────▶│  Map CFS→RFS │────▶│  Map RFS→    │
│  Catalog     │     │  Decomposition│    │  Resources   │
│              │     │  Rules        │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```
- Define technology-agnostic CFS specifications
- Create decomposition rules (CFS → RFS)
- Map RFS to actual resource configurations

### Phase 3: Graph/Topology Building
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Physical    │────▶│  Logical     │────▶│  Service     │
│  Topology    │     │  Topology    │     │  Topology    │
│  (L1/L2)     │     │  (L3/VPN)    │     │  (CFS/RFS)   │
└──────────────┘     └──────────────┘     └──────────────┘
```
- Build multi-layer topology graph
- Establish cross-layer dependencies
- Enable impact analysis and fault propagation modeling

### Phase 4: Digital Twin
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Real-Time   │────▶│  Graph       │────▶│  AI/ML       │
│  Telemetry   │     │  Database    │     │  Models      │
│  Ingestion   │     │  (Digital    │     │  (Prediction │
│              │     │   Twin)      │     │   & Action)  │
└──────────────┘     └──────────────┘     └──────────────┘
```
- Stream real-time data into graph-based digital twin
- Train AI models on topology-aware data
- Enable autonomous decision-making

---

## Technology Options for Implementation

| Layer | Options |
|-------|---------|
| **Graph Database** | Google Spanner Graph, Amazon Neptune, Neo4j, TigerGraph |
| **Resource Inventory** | Oracle UIM, ServiceNow TMT, Netcracker, custom (TMF639 API) |
| **Service Catalog** | Oracle Service Catalog, Amdocs, custom (TMF633 API) |
| **Digital Twin** | Google Cloud (Spanner + Vertex AI), AWS (Neptune + Bedrock), custom |
| **Data Integration** | AWS Glue, Google Dataflow, Apache Kafka, MuleSoft |
| **AI/ML Platform** | Amazon SageMaker, Google Vertex AI, Azure ML |

---

## Applies to ALL Network Types

| Network Domain | CFS Example | RFS Example | Resource Example |
|---------------|-------------|-------------|------------------|
| **Fixed (FTTH)** | Broadband 1Gbps | GPON ONT Config | OLT Port, ONT, Fiber |
| **Fixed (HFC)** | Cable Internet | DOCSIS CM Config | CMTS, Cable Modem |
| **Mobile (RAN)** | 5G Data Plan | Cell Activation | gNodeB, Antenna, Spectrum |
| **Transport** | MPLS VPN | LSP Configuration | Router, Optical Transponder |
| **Core** | Voice Service | IMS Registration | SBC, CSCF, HSS |
| **SD-WAN** | Enterprise WAN | Tunnel Config | CPE, vEdge, Controller |
| **IoT** | Fleet Tracking | Connectivity Profile | SIM, APN, Device |

---

## TM Forum Catalyst: Intelligent Fixed Broadband Operations

**ID:** C25.0.777
**Focus:** Using AI to optimize home broadband services
**Goals:**
- Reduce operating costs for fiber networks
- Improve customer experience
- Increase ROI in fiber networks

This proves AN is **not limited to mobile** — fixed broadband is an active area.

---

## The "Semantic MCP Server" Pattern (AWS)

AWS published an architecture for solving the **data ingestion problem** in telco operations:

- **Problem:** Telco data is multi-format, multi-vendor, multi-domain
- **Solution:** Deploy fine-tuned Small Language Models (SLMs) at the edge
- **Architecture:** Hybrid edge using AWS Outposts or AI Factories
- **Benefit:** Reduces cloud inference costs, ensures data sovereignty
- **Protocol:** Model Context Protocol (MCP) for standardized data access

This pattern helps transform raw telco data into structured information that AI agents can consume.

---

## Key Insight: The Data Steward Agent

Google Cloud introduced a **Data Steward Agent** — an agentic workflow that automates data governance to ensure digital twins remain accurate. This addresses the #1 problem in AN: **stale or inaccurate inventory data**.

```
Data Steward Agent Workflow:
1. Continuously monitors network changes
2. Validates inventory against live network state
3. Automatically reconciles discrepancies
4. Maintains graph relationships
5. Ensures digital twin accuracy for AI decisions
```

---

## Sources
- [TM Forum: TMFC008 Service Inventory](https://www.tmforum.org/oda/directory/components-map/production/TMFC008)
- [TM Forum: TMFC006 Service Catalog](https://www.tmforum.org/resources/technical-specification/tmfc006-service-catalog-management-v1-1-0/)
- [TM Forum: TMF639 Resource Inventory API](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5.0)
- [TM Forum: Intelligent Fixed Broadband Operations](https://www.tmforum.org/catalysts/projects/C25.0.777/intelligent-fixed-broadband-operations)
- [Oracle: PSR Models (CFS/RFS)](https://docs.oracle.com/en/industries/communications/service-catalog-design/8.3/users-guide/defining-your-psr-models1.html)
- [PassionateAboutOSS: CFS vs RFS](https://passionateaboutoss.com/differences-between-cfs-and-rfs/)
- [AWS: Semantic MCP Server for Telco](https://aws.amazon.com/blogs/industries/architecting-the-semantic-mcp-server-edge-deployment-of-fine-tuned-slms-to-solve-the-data-ingestion-problem-for-telco-operations/)
- [Google Cloud: Data Steward Agent](https://cloud.google.com/blog/topics/telecommunications/new-agents-for-the-autonomous-network-operations-framework)
