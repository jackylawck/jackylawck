# Model Card: Executive AI Intake & Impact Assessment System (AIIA)

> **Governance & Audit Baseline:** Maintained in alignment with **ISO/IEC 42001:2023 (AIMS)** (Clauses 6.1, 8.2, 8.4, 9.1 and Annex A.5, A.6, A.8, A.9), **IAPP AIGP Domains III & IV**, the **EU AI Act (Regulation (EU) 2024/1689)**, and the **Hong Kong PCPD Model Personal Data Protection Framework (2024)**.

---

## 1. System Details & Governance Metadata

- **System Name:** Executive AI Intake & Algorithmic Impact Assessor (AIIA)
- **Version:** v1.0.2 (Reference Governance Baseline)
- **System Owner:** Jacky Law (羅子淇) | F.I.H.R.M.(HK) · FHKIoD · MHKCS · Triple-ISO Lead Auditor (ISO 42001 / 27701 / 27001)
- **Initial Release:** July 2026 (Last Reviewed: November 2026)
- **License:** Apache 2.0 (Open-Source Governance Artifact)
- **Architecture Paradigm:** Local Hybrid Retrieval-Augmented Generation (RAG) paired with deterministic rule-based policy guardrails
- **Execution Environment:** Isolated client-side / local in-memory vector retrieval with deterministic rule verification and zero external data logging

---

## 2. Intended Use & Scope Boundaries (ISO/IEC 42001 Annex A.8.2 & A.9.4)

### 2.1 Intended Scope
- **Pre-Procurement & Pre-Deployment Impact Screening:** Structured algorithmic impact screening and compliance due diligence prior to acquiring or deploying commercial HR and enterprise AI systems.
- **Regulatory Cross-Mapping:** Deterministic mapping of proposed AI use cases against ISO/IEC 42001 controls, EU AI Act risk tiers, Hong Kong PCPD 2024 guidelines, and Digital Policy Office (DPO) ethical AI benchmarks.
- **Governance Decision Support:** Producing structured risk summaries and oversight checklists for Boards, Risk Committees, HR leadership, and Legal Counsel.

### 2.2 Prohibited & Out-of-Scope Uses
- **No Autonomous Employment Decisions:** Strictly prohibited from screening job applicants, ranking CVs, automating rejections, monitoring employee behavior, or scoring individual staff performance.
- **No Direct Ingestion of Raw PII:** Strictly prohibited from processing unmasked personal identifiers, biometric templates, employee health records, or sensitive personal attributes.
- **No Legal Advice or Conformity Certification:** Outputs provide structured risk-triage guidance only and do not constitute formal legal advice or accredited third-party conformity assessment.

---

## 3. Regulatory Alignment & Risk Classification

| Standard / Legislation | Classification / Applicable Scope | Operational Control |
| :--- | :--- | :--- |
| **EU AI Act (Regulation (EU) 2024/1689)** | **Out of Scope of Annex III Point 4 (Employment)** | Operates strictly as an internal governance and documentation sandbox; performs no recruitment filtering, worker evaluation, or automated decision-making affecting natural persons. |
| **ISO/IEC 42001:2023 (AIMS)** | **Clauses 6.1, 8.2, 8.4, 9.1 & Annex A.5, A.6, A.8.2, A.9.4** | Enforces documented impact assessment criteria, lifecycle version controls, user boundary disclosure, and auditable prompt/retrieval traceability. |
| **HK PCPD Model Framework (2024)** | **Four Core Areas (Governance, Risk & Oversight, System Management, Stakeholder Communication)** | Applies deterministic input sanitization, mandatory Human-in-the-Loop sign-off, local-only execution, and explicit transparency notices. |
| **HK EOC Statutory Ordinances** | **Cap. 480 (Sex), Cap. 487 (Disability), Cap. 527 (Family Status), Cap. 602 (Race)** | Flags potential proxy bias across statutory protected grounds during vendor rubric review, alongside broader ethical fairness checks (such as age-related proxies). |

---

## 4. Technical Guardrails & Risk Controls (ISO/IEC 42001 Clauses 8.2–8.4 & Annex A.6)

- **Mandatory Human-in-the-Loop (HITL) Sign-Off:** All generated risk classifications (High, Medium, Low) remain provisional drafts until reviewed and approved by designated governance or HR owners before entry into corporate risk registers.
- **Zero Data Retention (ZDR) & Local Isolation:** Embedding comparisons and rule evaluations execute solely within volatile runtime memory. No prompts, policy drafts, or assessment records are transmitted to external model providers or persisted on remote servers.
- **Confidence-Threshold Fallback:** If retrieval similarity drops below the configured confidence threshold (`0.82`), the system suppresses synthesis and directs reviewers to primary statutory texts to prevent unsupported outputs.
- **Quarterly Regulatory Calibration:** Retrieval corpora and rule tables are reviewed quarterly against updated statutory and regulatory publications (including Hong Kong Labour Department updates, Cap. 57 amendments, PCPD advisories, and DPO guidelines).

---

## 5. Verification, Limitations & Incident Handling (ISO/IEC 42001 Clause 9.1 & Annex A.6.2.4, A.8.4)

### 5.1 Verification & Quality Assurance
- **Deterministic Rule Verification:** Evaluated against internal synthetic compliance test cases covering prohibited PII patterns, missing human oversight controls, and discriminatory rubric criteria prior to each version release.
- **Auditor Rubric Calibration:** Scoring templates and risk-tier mappings are periodically cross-checked against ISO/IEC 42001 Lead Auditor assessment checklists.
- **Clause-Level Traceability:** Every flagged risk item outputs a specific statutory or standard reference (for example, *ISO/IEC 42001:2023 Annex A.5.4* or *HK PCPD Model Framework 2024, Section 2*) so human reviewers can verify findings independently.

### 5.2 Known Limitations
- **Corpus Currency Dependency:** Assessment accuracy depends on the latest quarterly update of the local statutory corpus; newly gazetted regulations or case law require manual corpus synchronization.
- **Jurisdictional Focus:** Rule mappings are calibrated primarily for Hong Kong SAR, the Greater Bay Area (PIPL cross-border contexts), and EU AI Act benchmarks; deployments in other jurisdictions require localized legal review.

### 5.3 Incident Handling & Adversarial Testing
- **Fail-Closed Execution:** Any parsing failure, schema violation, or detected prompt-injection pattern halts output generation immediately and records a sanitized, PII-free error code without writing raw memory dumps to disk.
- **Periodic Red-Teaming:** Prompt-injection, boundary-bypass, and citation-integrity stress tests are conducted semi-annually against the OWASP Top 10 for LLM Applications checklist.
