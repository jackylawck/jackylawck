# Human Oversight & Redress Framework (HITL / HOTL / HIC)

> **Regulatory & Governance Alignment:** Formulated in strict accordance with **ISO/IEC 42001:2023 (Controls A.8.4 & A.7)**, **EU AI Act (Regulation (EU) 2024/1689 Articles 14 & 86)**, **Hong Kong PCPD Model Framework (2024 Principles 2 & 4)**, and **IAPP AIGP Domain IV (Human Agency & Oversight)**.

---

## 1. Human Agency & Oversight Governance Hierarchy (人類監督三階梯模型)

All AI-assisted governance workstations, intake assessors, and decision-support sandboxes operate under strict non-autonomous boundaries. Automation is categorized into three distinct layers of operational oversight:

```text
┌────────────────────────────────────────────────────────────────────────┐
│               HUMAN AGENCY & OVERSIGHT GOVERNANCE TIERS                │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Human-in-the-Loop (HITL) - Pre-Execution Sign-Off                  │
│    • AI models generate formative candidate scores, risk tags, or     │
│      compliance briefs only.                                          │
│    • Zero binding corporate decisions take effect without explicit    │
│      affirmative human authorization.                                 │
│                                                                        │
│ 2. Human-on-the-Loop (HOTL) - Real-Time Supervisory Gatekeeping        │
│    • Live monitoring of algorithmic drift, unexpected bias surges,    │
│      or heuristic scoring anomalies during batch evaluations.         │
│    • Human supervisors retain real-time intervention privileges.      │
│                                                                        │
│ 3. Human-in-Command (HIC) - Executive Sovereign Kill-Switch           │
│    • Ultimate managerial authority held by CHRO and Board Committees. │
│    • Immediate operational override, model rollback, or sandbox       │
│      disconnection upon ethical or statutory breach.                  │
└────────────────────────────────────────────────────────────────────────┘

```

---

## 2. Prohibition of Fully Automated Employment Decisions (高利害決策排他性排除)

* **Negative Scope Declaration:** Under no circumstances shall any tool within this repository be deployed as a sole, automated decision-making system (ADM) for candidate rejection, contract termination, compensation adjustment, or statutory entitlement calculation.
* **Decision Support Mandate:** All outputs are legally classified as advisory analytical telemetry. Responsibility for workforce decisions rests 100% with accredited human executives (F.I.H.R.M. / Board of Directors).

---

## 3. End-to-End Escalation & Discrepancy Protocol (異常升級處置協定)

```text
[ Algorithmic Triage ] 
         │
         ▼ (Discrepancy / Margin Flag: ΔConfidence < 0.85 OR Protected Class Proxy Alert)
[ Tier 1: HR Executive Blind Audit ] 
         │ (Manual review of unmasked credentials; AI reasoning masked to prevent anchor bias)
         ▼ (Contested Decision / Residual Impact)
[ Tier 2: Governance & Compliance Committee Review ]
         │ (Alignment check against HK PCPD, Cap. 57, and ISO 42001 registers)
         ▼ (Statutory Dispute / External Appeal)
[ Tier 3: Independent ADR & Mediation Recourse ] (APCAM / GBA Mediator Oversight)

```

1. **Threshold Borderline Escalation:** Any assessment score falling within a $\pm 10\%$ borderline margin or triggering algorithmic fairness warnings automatically locks the profile and routes it to manual review.
2. **De-Biased Human Audit:** To combat automation bias and confirmation bias, reviewers evaluate raw qualifications without viewing initial AI score recommendations.
3. **Executive Governance Escalation:** Disputed findings escalate directly to the Corporate Governance Advisor and Board Risk Committee.

---

## 4. Individual Redress & Statutory Rights of Explanation (權利救濟與反向解釋機制)

To ensure procedural fairness under EU AI Act Article 86, GDPR Article 22, and Hong Kong Personal Data (Privacy) Ordinance (Cap. 486):

* **Right to Human Explanation (實質可解釋性要求):** Affected individuals are entitled to receive clear, human-understandable explanations regarding the key parameters, weighting criteria, and reasoning logic contributing to their assessment.
* **Formal Request for Human Re-Evaluation (強制人工覆核申請):**
* Individuals may submit a formal request for human reconsideration within 14 calendar days of receiving an evaluated outcome.
* Re-evaluation must be executed by a human manager who was not involved in the original automated screening run.


* **Alternative Dispute Resolution (ADR) Integration:**
* Consistent with professional cross-border dispute resolution standards, contested governance or workforce evaluations provide an expedited mediation option before formal administrative or legal litigation is pursued.



---

## 5. Auditability & Evidence Provenance (ISO/IEC 27001 & ISO 42001)

* **Tamper-Evident Incident Logging:** Every human override, manual score adjustment, and appeal resolution is cryptographically appended with timestamped operator signatures into an immutable audit trail.
* **Retention & Retrospective Review:** Override logs are audited semi-annually by the Lead Auditor to detect systemic algorithmic bias trends and inform model recalibration.
