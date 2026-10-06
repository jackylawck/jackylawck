# AI System Lifecycle, Change Management & Continuous Assurance

> **Audit Standard Alignment:** Formulated and maintained in strict accordance with **ISO/IEC 42001:2023 (Clauses 6.3, 8.1 & Annex A.8 Controls)**, **ISO/IEC 27001:2022 (Control A.8.32)**, **EU AI Act (Articles 15 & 72 Post-Market Monitoring)**, and **IAPP AIGP Domains III & IV Frameworks**.

---

## 1. AI System Lifecycle Architecture & Quality Gateways (ISO 42001 Annex A.8)

Every governance workstation, RAG prototype, and actuarial engine progresses through five deterministic, stage-gated lifecycle phases. Advancement requires formal satisfaction of predefined exit criteria:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   AI SYSTEM LIFECYCLE QUALITY GATEWAYS                 │
├────────────────────────────────────────────────────────────────────────┤
│ [ Phase 1: Intake & Scoping ]                                         │
│   ├── Deliverables: Problem boundary, negative clearing classification │
│   └── Gateway 1 Exit: Pre-Assessment sign-off & MODEL_CARD.md draft   │
│            │                                                           │
│            ▼                                                           │
│ [ Phase 2: Design, Development & Verification ]                       │
│   ├── Deliverables: Deterministic code, zero-PII regex, synthetic test │
│   └── Gateway 2 Exit: Regression suite pass (100%) + CSP/SRI audit    │
│            │                                                           │
│            ▼                                                           │
│ [ Phase 3: Ethical & Regulatory Red-Teaming ]                         │
│   ├── Deliverables: Bias mitigation (EOC), prompt injection stress-test│
│   └── Gateway 3 Exit: Lead Auditor formal clearance & Rekor log anchor │
│            │                                                           │
│            ▼                                                           │
│ [ Phase 4: Production Deployment & Runtime Guardrails ]               │
│   ├── Deliverables: Client-side volatile execution, ZDR verification   │
│   └── Gateway 4 Exit: Zero telemetry validation & CSP enforcement     │
│            │                                                           │
│            ▼                                                           │
│ [ Phase 5: Post-Market Monitoring, Recalibration & Retirement ]        │
│   └── Ongoing: Quarterly drift audits, statutory diffs, graceful EOL   │
└────────────────────────────────────────────────────────────────────────┘

```

---

## 2. Hard Gatekeeping & Exit Criteria (階段准入與門禁準則)

| Lifecycle Stage | Lead Accountability | Mandatory Exit Criteria |
| --- | --- | --- |
| **Phase 1: Intake & AIA** | Corporate Governance Advisor | Legal scope confirmation; negative clearance declaration under EU AI Act Art. 3(1) if deterministic. |
| **Phase 2: Development** | Technical Lead / WASM Core | Zero external unpinned dependencies; passing all unit tests across 50+ benchmark governance scenarios. |
| **Phase 3: Validation** | Triple-ISO Lead Auditor | Formal clearance on Hong Kong PCPD and DPO compliance checklists; zero false-negative statutory violations. |
| **Phase 4: Release** | Security Officer | CI/CD cryptographic attestation via Sigstore Cosign; immutable SHA-256 manifest published. |
| **Phase 5: Oversight** | Board Risk Committee | Continuous monitoring against concept drift, regulatory changes, and incident disclosure SLAs. |

---

## 3. Change Control Protocol & Versioning Taxonomy (ISO 27001 A.8.32)

All code, algorithmic weights, and statutory ontology modifications follow strict semantic versioning (`vMAJOR.MINOR.PATCH`):

### 3.1 Tiered Modification Hierarchy

* **Major Releases (`vX.0.0` - Substantive Architecture Shifts):**
* *Triggers:* Enactment of major new primary legislation (e.g., EU AI Act enforcement phases, Cap. 57 statutory threshold amendments), structural schema migrations, or fundamental model engine replacements.
* *Requirements:* Full re-certification of `MODEL_CARD.md`, end-to-end Algorithmic Impact Assessment (AIA) re-baseline, and Board Committee review.


* **Minor Releases (`vx.Y.0` - Regulatory Calibration & Feature Extensions):**
* *Triggers:* Regulatory guidance updates (e.g., PCPD case precedents, DPO checklist iterations), new sovereign ingestion adapters (*The Veracity* / *Veritas*), or psychometric construct refinements.
* *Requirements:* Automated regression pass across the 50 standardized HR test benches and updated documentation.


* **Patch Releases (`vx.y.Z` - Hotfixes & Emergency Hardening):**
* *Triggers:* Prompt injection vulnerabilities, UI rendering bugs, dependency hash updates, or typo corrections.
* *Requirements:* Expedited emergency review and immediate redeployment within SLA parameters (< 48 hours).



---

## 4. Regression & Continuous Verification Suite

Before merging any change into the production `main` branch, the automated CI/CD pipeline enforces the following deterministic verification checks:

1. **Deterministic Regulatory Regression Test:** Executes 50 standardized employment law scenarios (covering Cap. 57 sick leave calculations, severance, 418 thresholds, and maternity provisions) to verify zero calculation drift.
2. **Negative Clearance Sanity Check:** Verifies that no probabilistic ML models or unauthorized third-party tracking scripts have been inadvertently introduced into deterministic tool repos.
3. **Cryptographic Integrity & Subresource Attestation:** Validates that all vendor dependencies match pinned SHA-256 hashes and that the Sigstore signing workflow completes successfully.

---

## 5. Decommissioning, Sunset & Graceful End-of-Life (EOL)

In accordance with ISO 42001 Clause 8.1 lifecycle completion mandates:

* **Deprecation Notice:** Prototypes marked for obsolescence will display an on-screen sunset advisory for at least 60 calendar days prior to archival.
* **Volatile State Expiration:** Because all systems enforce Zero Data Retention (ZDR), repository retirement requires zero complex database migrations or data purging workflows.
* **Repository Archival:** Upon formal EOL, the codebase is transitioned to a read-only cryptographic archive with its final Sigstore Rekor attestation immutably recorded for historical audit defense.

