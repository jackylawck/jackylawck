# AI Model Card: Executive AI Intake & Impact Assessment System (AIIA-v1)

> **Compliance Notice:** This Model Card is maintained in accordance with **ISO/IEC 42001:2023 (AIMS) Control A.6 & A.8** and aligned with **AIGP Domain III & IV Oversight Guidelines**.

---

## 1. Model Details & Governance Metadata
* **System Name:** Executive AI Intake & Algorithmic Impact Assessor (AIIA)
* **Model Version:** v1.0.2
* **Model Owner:** Jacky Law (ISO 42001 Lead Auditor / F.I.H.R.M.)
* **Release Date:** July 2026
* **License:** Apache 2.0
* **System Architecture:** Retrieval-Augmented Generation (RAG) & Policy Guardrail Sandbox

---

## 2. Intended Use & Boundaries (ISO 42001 A.6.1)
* **Primary Intended Use:** Assisting HR executives and corporate boards in conducting algorithmic impact assessments (AIA) prior to adopting commercial AI HR/Recruitment tools.
* **Out-of-Scope Uses:** 
  * Autonomous candidate hiring or rejection without human sign-off.
  * Direct processing of unencrypted PII or sensitive personal data.
* **Target Audience:** CHROs, Risk Committees, Board Directors.

---

## 3. Risk Mitigation & Guardrails (ISO 42001 Clause 8.2)
* **Identified Risks:** Concept drift in recruitment terminology; demographic representation bias.
* **Controls Implemented:** Mandatory Human-in-the-Loop (HITL) escalation; automated compliance checks against Hong Kong PCPD guidelines.

---

## 4. Evaluation & Continuous Oversight (ISO 42001 Clause 9)
* **Performance Metrics:** Accuracy of risk tier classification (High/Medium/Low) against ISO 42001 Annex A controls.
* **Monitoring:** Quarterly audit log review and concept drift validation.
