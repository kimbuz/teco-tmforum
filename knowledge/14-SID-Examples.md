# SID in Practice — Concrete Examples

## How SID Looks as Data

SID is a UML model, but in practice it materializes as **JSON structures** through TM Forum Open APIs. Every API payload follows SID entity definitions. Here are real examples of how the "language" looks when you actually use it.

---

## Example 1: A Service Instance (CFS) — TMF638

This is what a Customer Facing Service looks like in the Service Inventory API:

```json
{
  "id": "svc-00142857",
  "href": "/serviceInventory/v4/service/svc-00142857",
  "name": "Internet Access 500Mbps",
  "description": "Residential broadband service",
  "state": "active",
  "serviceType": "CFS",
  "startDate": "2025-03-15T10:30:00Z",
  "serviceSpecification": {
    "id": "spec-internet-500",
    "name": "Internet_Access_500Mbps",
    "href": "/serviceCatalog/v4/serviceSpecification/spec-internet-500"
  },
  "serviceCharacteristic": [
    {
      "name": "downloadSpeed",
      "value": "500",
      "valueType": "string",
      "unitOfMeasure": "Mbps"
    },
    {
      "name": "uploadSpeed",
      "value": "250",
      "valueType": "string",
      "unitOfMeasure": "Mbps"
    },
    {
      "name": "accessTechnology",
      "value": "GPON",
      "valueType": "string"
    }
  ],
  "supportingService": [
    {
      "id": "svc-rfs-00285714",
      "href": "/serviceInventory/v4/service/svc-rfs-00285714",
      "name": "GPON_ONT_Port_Activation",
      "serviceType": "RFS"
    },
    {
      "id": "svc-rfs-00285715",
      "href": "/serviceInventory/v4/service/svc-rfs-00285715",
      "name": "Data_VLAN_Assignment",
      "serviceType": "RFS"
    },
    {
      "id": "svc-rfs-00285716",
      "href": "/serviceInventory/v4/service/svc-rfs-00285716",
      "name": "QoS_Profile_500Mbps",
      "serviceType": "RFS"
    }
  ],
  "relatedParty": [
    {
      "id": "cust-98765",
      "name": "Juan Perez",
      "role": "Customer",
      "@referredType": "Individual"
    }
  ],
  "place": [
    {
      "id": "loc-54321",
      "name": "Av. Corrientes 1234, CABA",
      "role": "installationAddress"
    }
  ],
  "@type": "Service",
  "@baseType": "Service"
}
```

### What SID Defines Here

| SID Entity | In This Example |
|-----------|-----------------|
| **Service** | The root object (id, state, name, type) |
| **ServiceSpecification** | Reference to the catalog template |
| **ServiceCharacteristic** | Key-value pairs describing the service |
| **ServiceRelationship** | `supportingService` links CFS → RFS |
| **RelatedParty** | Who this service belongs to |
| **Place** | Where the service is delivered |

---

## Example 2: A Resource Facing Service (RFS) — TMF638

This is one of the RFS instances that supports the CFS above:

```json
{
  "id": "svc-rfs-00285714",
  "href": "/serviceInventory/v4/service/svc-rfs-00285714",
  "name": "GPON_ONT_Port_Activation",
  "state": "active",
  "serviceType": "RFS",
  "serviceSpecification": {
    "id": "spec-gpon-ont-activation",
    "name": "GPON_ONT_Port_Activation_Spec"
  },
  "serviceCharacteristic": [
    {
      "name": "ontSerialNumber",
      "value": "HWTC-ABCD1234"
    },
    {
      "name": "ponPort",
      "value": "0/1/3/7"
    },
    {
      "name": "lineProfile",
      "value": "FTTH-500M"
    },
    {
      "name": "servicePort",
      "value": "1"
    }
  ],
  "supportingResource": [
    {
      "id": "res-olt-001",
      "name": "OLT-CABA-Norte-01",
      "href": "/resourceInventory/v4/resource/res-olt-001",
      "@referredType": "PhysicalResource"
    },
    {
      "id": "res-ont-98765",
      "name": "ONT-HWTC-ABCD1234",
      "href": "/resourceInventory/v4/resource/res-ont-98765",
      "@referredType": "PhysicalResource"
    }
  ],
  "@type": "Service",
  "@baseType": "Service"
}
```

### Key Difference: CFS vs. RFS

| Aspect | CFS (Example 1) | RFS (Example 2) |
|--------|-----------------|-----------------|
| `serviceType` | "CFS" | "RFS" |
| Characteristics | Business terms (speed, technology) | Technical terms (port, serial, profile) |
| Links down to | `supportingService` (RFS) | `supportingResource` (physical devices) |
| Links up to | Product (via product inventory) | CFS (via `supportingService`) |

---

## Example 3: A Physical Resource — TMF639

This is the OLT that the RFS references:

```json
{
  "id": "res-olt-001",
  "href": "/resourceInventory/v4/resource/res-olt-001",
  "name": "OLT-CABA-Norte-01",
  "description": "Huawei MA5800-X17, Site CABA Norte",
  "resourceStatus": "available",
  "administrativeState": "unlocked",
  "operationalState": "enable",
  "category": "PhysicalResource",
  "resourceSpecification": {
    "id": "rspec-huawei-ma5800",
    "name": "Huawei_MA5800-X17"
  },
  "resourceCharacteristic": [
    {
      "name": "vendor",
      "value": "Huawei"
    },
    {
      "name": "model",
      "value": "MA5800-X17"
    },
    {
      "name": "softwareVersion",
      "value": "V800R021C10"
    },
    {
      "name": "totalPonPorts",
      "value": "128"
    },
    {
      "name": "usedPonPorts",
      "value": "87"
    },
    {
      "name": "managementIP",
      "value": "10.200.1.50"
    }
  ],
  "place": {
    "id": "site-caba-norte",
    "name": "Central CABA Norte",
    "role": "installationSite"
  },
  "relatedParty": [
    {
      "id": "org-telecom-ar",
      "name": "Telecom Argentina",
      "role": "Owner"
    }
  ],
  "@type": "PhysicalResource",
  "@baseType": "Resource"
}
```

---

## Example 4: A Service Specification (Catalog Entry) — TMF633

This is the **template** in the catalog that defines what "Internet 500Mbps" means:

```json
{
  "id": "spec-internet-500",
  "href": "/serviceCatalog/v4/serviceSpecification/spec-internet-500",
  "name": "Internet_Access_500Mbps",
  "description": "Residential FTTH broadband, 500Mbps down / 250Mbps up",
  "lifecycleStatus": "Active",
  "isBundle": false,
  "serviceType": "CFS",
  "specCharacteristic": [
    {
      "name": "downloadSpeed",
      "description": "Maximum download speed",
      "valueType": "string",
      "configurable": false,
      "characteristicValueSpecification": [
        { "value": "500", "unitOfMeasure": "Mbps", "isDefault": true }
      ]
    },
    {
      "name": "uploadSpeed",
      "description": "Maximum upload speed",
      "valueType": "string",
      "configurable": false,
      "characteristicValueSpecification": [
        { "value": "250", "unitOfMeasure": "Mbps", "isDefault": true }
      ]
    },
    {
      "name": "accessTechnology",
      "description": "Access network technology",
      "valueType": "string",
      "configurable": false,
      "characteristicValueSpecification": [
        { "value": "GPON", "isDefault": true },
        { "value": "XGS-PON" }
      ]
    }
  ],
  "resourceSpecification": [
    {
      "id": "rspec-huawei-ma5800",
      "name": "Huawei_MA5800-X17",
      "role": "OLT"
    },
    {
      "id": "rspec-ont-generic",
      "name": "Generic_GPON_ONT",
      "role": "CPE"
    }
  ],
  "serviceLevelSpecification": [
    {
      "id": "sla-residential-gold",
      "name": "Residential Gold SLA",
      "objective": [
        { "name": "availability", "target": "99.5%" },
        { "name": "maxRepairTime", "target": "24h" }
      ]
    }
  ],
  "@type": "ServiceSpecification"
}
```

---

## The Full Chain Visualized

```
CATALOG (Templates)                    INVENTORY (Instances)
========================              ========================

ServiceSpecification                   Service (CFS)
"Internet_Access_500Mbps"    ------>   "Internet Access 500Mbps"
  - specCharacteristic:                  - state: "active"
    downloadSpeed: 500Mbps               - customer: Juan Perez
    uploadSpeed: 250Mbps                 - serviceCharacteristic:
    accessTechnology: GPON                   downloadSpeed: 500Mbps
                                         - supportingService: [RFS...]
         |                                        |
         v                                        v
ServiceSpecification                   Service (RFS)
"GPON_ONT_Port_Activation"   ------>   "GPON_ONT_Port_Activation"
  - specCharacteristic:                  - state: "active"
    ontSerialNumber (template)           - ontSerialNumber: HWTC-ABCD1234
    ponPort (template)                   - ponPort: 0/1/3/7
                                         - supportingResource: [OLT, ONT]
         |                                        |
         v                                        v
ResourceSpecification                  Resource (Physical)
"Huawei_MA5800-X17"          ------>   "OLT-CABA-Norte-01"
  - vendor: Huawei                       - operationalState: enable
  - totalPonPorts: 128                   - usedPonPorts: 87
                                         - managementIP: 10.200.1.50
```

---

## SID Patterns You'll See Everywhere

### 1. The Spec/Instance Pattern
Every SID entity has a **Specification** (template) and **Instance** (real thing):
- `ServiceSpecification` → `Service`
- `ResourceSpecification` → `Resource`
- `ProductSpecification` → `Product`

### 2. The Characteristic Pattern
Instead of fixed columns, SID uses flexible key-value pairs:
```json
"serviceCharacteristic": [
  { "name": "downloadSpeed", "value": "500", "unitOfMeasure": "Mbps" }
]
```
This means you can model ANY service without changing the schema.

### 3. The Relationship Pattern
Entities link to each other through typed relationships:
- `supportingService` — CFS links to its RFS
- `supportingResource` — RFS links to its resources
- `relatedParty` — anything links to who's involved
- `place` — anything links to where it is

### 4. The @type / @baseType Pattern
Polymorphism — a Resource can be `PhysicalResource` or `LogicalResource`:
```json
"@type": "PhysicalResource",
"@baseType": "Resource"
```

---

## Why This Structure Enables Autonomous Networks

| SID Pattern | AN Capability It Enables |
|------------|--------------------------|
| Spec/Instance | Automated provisioning (instantiate from spec) |
| Characteristics (key-value) | Flexible modeling without schema changes |
| Relationships (supportingService) | Impact analysis (traverse CFS→RFS→Resource) |
| State management | Lifecycle automation (active, suspended, terminated) |
| @type polymorphism | Multi-technology support (same API, different resource types) |
| Place references | Geographic fault correlation |
| RelatedParty | Customer impact analysis |

---

## Sources
- [TM Forum: TMF638 Service Inventory API](https://www.tmforum.org/resources/specification/tmf638-service-inventory-api-rest-specification-r18-5-0/)
- [TM Forum: TMF639 Resource Inventory API](https://www.tmforum.org/resources/specification/tmf639-resource-inventory-management-api-rest-specification-r17-0-1/)
- [TM Forum: TMF633 Service Catalog API](https://www.tmforum.org/resources/technical-specification/tmfc006-service-catalog-management-v1-1-0/)
- [TM Forum: SID Clarification Documents (IG1163)](https://www.tmforum.org/resources/standard/ig1163-information-framework-sid-clarification-documents-r17-5-0/)
- [TM Forum: Open APIs GitHub](https://github.com/tmforum-apis)
- [Oracle UIM: TMF638 Implementation](https://docs.oracle.com/en/industries/communications/uim/7.6.0/rest-api/op-service-post.html)
