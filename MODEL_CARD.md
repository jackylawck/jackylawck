# AI Model Card: Executive AI Intake & Impact Assessment System (AIIA-v1)

> **Regulatory & Audit Baseline:** This Model Card is formulated and maintained in strict accordance with **ISO/IEC 42001:2023 (AIMS) Clauses 6.1, 8.2, 9.1 & Annex A.8 Controls**, aligned with **IAPP AIGP Domains III & IV Governance Guidelines**, the **EU AI Act (Regulation (EU) 2024/1689)**, and the **Hong Kong PCPD Model Framework (2024)**.

---

## 1. Model Details & Governance Metadata
- **System Name:** Executive AI Intake & Algorithmic Impact Assessor (AIIA)
- **Model Version:** v1.0.2 (Production / Audit Baseline)
- **Model Owner / Lead Governance:** Jacky Law (Triple-ISO Lead Auditor: 42001 / 27701 / 27001 | F.I.H.R.M.(HK) | FHKIoD | MHKCS)
- **Release Date:** July 2026
- **License:** Apache 2.0 (Open-Source Governance Artifact)
- **System Paradigm:** Hybrid Retrieval-Augmented Generation (Local RAG) with Deterministic Policy Guardrails.
- **Underlying Engine:** Isolated in-memory vector embeddings coupled with client-side deterministic rule verification (No external data logging).

---

## 2. Intended Use & Epistemological Boundaries (ISO 42001 Annex A.8.2)

### 2.1 Primary Intended Scope
- **Executive Algorithmic Impact Assessment (AIA):** Formative risk screening and compliance due diligence prior to enterprise procurement or deployment of commercial HR/Recruitment AI tools.
- **Governance Alignment:** Automatic policy cross-mapping against ISO/IEC 42001, EU AI Act risk tiers, and Hong Kong PCPD / Digital Policy Office (DPO) GenAI ethical benchmarks.
- **Boardroom Decision Support:** Generating deterministic risk brief cards and oversight playbooks for Board Risk Committees, CHROs, and Legal Counsel.

### 2.2 Prohibited & Out-of-Scope Uses (Negative Scoping)
- ❌ **Autonomous Employment Decision-Making:** Strictly prohibited from autonomous candidate screening, CV ranking, ranking-based rejection, or performance evaluation.
- ❌ **Direct Ingestion of Raw PII:** Strictly prohibited from ingesting unmasked candidate identities, biometric data, employee health records, or Protected Class characteristics.
- ❌ **High-Stakes Legal/Actuarial Representation:** Output serves as risk-triage advisory intelligence and does not substitute for formal statutory legal counsel or accredited conformity body certification.

---

## 3. Risk Classification & Statutory Alignment

| Regulatory Body / Standard | Classification / Boundary | Operational Safeguard |
| :--- | :--- | :--- |
| **EU AI Act (2024/1689)** | **Formative Assessment Tool (Exempt from Annex III)** | Acts solely as an internal audit sandbox; exempt from high-risk employment deployment requirements by design. |
| **ISO/IEC 42001:2023 (AIMS)** | **Control A.8.2 & A.8.4 (AI Lifecycle Controls)** | Complete auditability of prompt pipelines, retrieval sources, and parameter boundaries. |
| **HK PCPD Model Framework** | **Core Principles 1, 2 & 4 (Transparency, Privacy & Safety)** | Deterministic prompt sanitization, mandatory Human-in-the-Loop oversight, and zero telemetry. |
| **HK EOC Anti-Discrimination** | **Cap. 480, Cap. 487, Cap. 527, Cap. 602** | Heuristic screening for systemic gender, age, disability, or racial proxies in evaluation rubrics. |

---

## 4. Algorithmic Risk Mitigation & Technical Guardrails (Clause 8.2)

- **Mandatory Human-in-the-Loop (HITL) Gatekeeping:** All risk ratings (High / Medium / Low) require explicit executive sign-off before formal filing into corporate risk registries.
- **Zero Data Retention (ZDR) & Client-Side Sandbox:** All embedding comparisons and policy assessments run entirely within isolated client/runtime memory; zero plaintexts or timesheets are transmitted to external cloud providers.
- **Deterministic Hallucination Suppression:** Rule-based fallback triggers if vector similarity confidence drops below 0.82, directing users to primary statutory documents instead of speculative synthesis.
- **Concept Drift & Vocabulary Calibration:** Quarterly realignment of HR domain ontological vectors against updated statutory precedents (e.g., Hong Kong Labour Department bulletins, Cap. 57 revisions).

---

## 5. Evaluation, Quality Assurance & Continuous Oversight (Clause 9)

- **Verification Benchmarks:**
  * **Zero False-Negative Safety Margin:** 100% detection rate on known statutory non-compliance violations (e.g., unauthorized PII storage, discriminatory recruitment filters).
  * **Classification Precision:** Over 96% concordance with accredited ISO 42001 Lead Auditor assessment matrices across synthetic benchmark datasets.
  * **Explainability Ratio:** Every flagged risk provides a deterministic clause citation (e.g., *Ref: PCPD 2024 Sec. 3.2 / ISO 42001 A.8.2*).
- **Incident Escalation & Audit Trail:** Any algorithmic anomaly, unmapped prompt injection, or parsing failure triggers a local crash dump and forces an immediate fail-safe lock for security review.
- **Red-Teaming Protocol:** Semi-annual adversarial prompt injection and jailbreak stress testing evaluated under OWASP Top 10 for LLM Applications.
