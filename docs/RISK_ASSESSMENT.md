# Algorithmic Impact & Risk Assessment Baseline (AIA / RMF)

> **Audit Standard Alignment:** Maintained in alignment with **ISO/IEC 42001:2023 (AIMS)** (Clauses 6.1, 8.2, 8.3, 8.4, 9.1 & Annex A.5, A.6, A.7, A.8, A.9), **ISO/IEC 27001:2022** (Controls A.8.10, A.8.28, A.8.32), **ISO/IEC 27701** (Annex A.7.4), **NIST AI RMF 1.0 (GOVERN, MAP, MEASURE, MANAGE)**, **EU AI Act (Regulation (EU) 2024/1689)**, and the **Hong Kong PCPD Model Personal Data Protection Framework (2024)**.

---

## 1. Context, Architectural Scope & Regulatory Classification (NIST MAP 1.1 / ISO/IEC 42001 Clauses 6.1 & 8.4)

- **Target Scope:** AI-assisted governance workstations, local RAG compliance advisors, and vendor rubric evaluation sandboxes (including *AIIA* and synthetic bias-testing demonstrators such as *TalentScout*).
- **Non-AI Portfolio Exclusion:** Purely deterministic software, media codecs, and rule-based enterprise workflows (including *SlimVid*, *KidsPrepDictate*, *SpeakFlow*, *SpeakUp-Mediation*, and *DailyStaffAppraisal*) contain zero machine learning or probabilistic inference models and are formally out of scope of ISO/IEC 42001 and EU AI Act Article 3(1), as documented in `llms.txt`.
- **Core Technology Paradigm:** Localized Hybrid Retrieval-Augmented Generation (Local RAG) paired with deterministic rule verification and strict client-side execution boundaries.
- **Regulatory Scope Assessment:**
  - **EU AI Act (Regulation (EU) 2024/1689):**
    - *AIIA / Governance Compliance Sandboxes:* Operate strictly as internal regulatory lookup and vendor due-diligence tools affecting no natural-person employment outcomes; therefore outside **Annex III Point 4 (Employment)**.
    - *Synthetic HR Bias Sandboxes (e.g., TalentScout):* Restricted strictly to synthetic training and fairness demonstration. Live enterprise deployment for candidate screening or natural-person profiling is explicitly prohibited; any real-world deployment performing natural-person profiling would constitute a **High-Risk AI System** under Annex III Point 4 and cannot rely on **Article 6(3)** procedural derogations.
  - **Hong Kong PCPD (2024) & HK DPO Alignment:** Evaluated against the four core areas of the 2024 PCPD Model Framework (Governance, Risk & Human Oversight, System Management, Stakeholder Communication) and HK Digital Policy Office (DPO) risk-tiering principles, enforcing Privacy-by-Design, Zero Server-Side Data Retention, and mandatory Human-in-the-Loop sign-off.

---

## 2. Risk Appetite & Scoring Methodology (NIST GOVERN 1.2 / ISO/IEC 42001 Clause 8.2)

Risk is evaluated across a standard 5×5 matrix as the product of **Severity (1–5)** and **Likelihood (1–5)**:

$$\text{Risk Score} = \text{Severity} \times \text{Likelihood}$$

| Risk Rating | Score Band | Governance Action & Acceptance Criteria |
| :--- | :---: | :--- |
| **Low** | **1–4** | Acceptable under standard technical controls; reviewed during periodic governance cycles. |
| **Medium** | **5–9** | Tolerable only with documented procedural controls and human verification. |
| **High** | **10–14** | Requires active risk-treatment controls, pre-action HITL gatekeeping, and periodic audit testing. |
| **Critical** | **15–25** | Unacceptable for deployment; triggers fail-closed halt until architectural controls reduce residual risk. |

---

## 3. Risk Assessment & Control Matrix (ISO/IEC 42001 Clauses 8.2–8.4, Annex A.5 & NIST MEASURE / MANAGE)

| Risk ID | Hazard / Failure Mode | Inherent Risk (S × L) | Control Mechanism & Technical Guardrail | Standard & Statutory Mapping | Residual Risk (S × L) |
| :--- | :--- | :---: | :--- | :--- | :---: |
| **R-01** | **Rubric & Proxy Bias:** Disproportionate scoring patterns disadvantaging protected groups across HK EOC statutory grounds (Sex, Disability, Family Status, Race) or broader fairness proxies (such as age). | **Critical**<br>(4 × 4 = 16) | • Strictly prohibits live autonomous candidate screening.<br>• Strips demographic proxy fields during synthetic rubric testing.<br>• Runs pre-deployment Four-Fifths Rule (Disparate Impact Ratio $\ge 0.80$) checks on synthetic benchmark datasets.<br>• Requires blind human review for borderline cases. | ISO 42001 A.5.2, A.5.4, A.7.4<br>NIST MEASURE 2.11<br>HK EOC (Cap. 480, 487, 527, 602) | **Low**<br>(2 × 2 = 4) |
| **R-02** | **Statutory Hallucination & Citation Error:** Unsupported or inaccurate compliance summaries on Hong Kong labor law (e.g., Cap. 57 continuous contract rules) or AI regulations. | **High**<br>(4 × 3 = 12) | • Local RAG grounded exclusively in authoritative statutory corpora.<br>• Deterministic confidence threshold ($\cos \theta \ge 0.82$); suppresses synthesis below threshold and links directly to primary legislation.<br>• Mandatory clause-level citations for independent human verification. | ISO 42001 A.6.2.4, A.8.2<br>NIST MANAGE 2.2 | **Low**<br>(2 × 1 = 2) |
| **R-03** | **Prompt Injection & Guardrail Bypass:** Crafted inputs attempting to override policy instructions, extract system prompts, or bypass deterministic rule checks. | **High**<br>(4 × 3 = 12) | • Deterministic input sanitization prior to retrieval.<br>• Structural separation between system instructions and user inputs.<br>• Strict CSP (`default-src 'none'` / `'self'`) and zero outbound API privileges.<br>• Semi-annual red-teaming against OWASP Top 10 for LLM Applications. | ISO 42001 A.6.2.5, A.6.2.6<br>ISO 27001 A.8.28<br>OWASP LLM01<br>NIST MANAGE 1.3 | **Low**<br>(2 × 2 = 4) |
| **R-04** | **PII Exposure & Unintended Retention:** Accidental entry or persistence of raw personal identifiers or confidential corporate records. | **Critical**<br>(5 × 3 = 15) | • Volatile in-memory client execution with zero remote servers or analytics telemetry.<br>• Pattern-based regex redaction for structured identifiers (HKID, phone, email, bank formats), paired with explicit user boundaries prohibiting raw PII input.<br>• Fail-closed error handling without writing raw memory dumps to disk. | ISO 27001 A.8.10<br>ISO 27701 A.7.4<br>HK PDPO (Cap. 486 DPP2, DPP4) | **Low**<br>(2 × 1 = 2) |
| **R-05** | **Automation Bias & Uncritical Reliance:** Reviewers rubber-stamping system risk tags or draft summaries without independent legal or HR judgment. | **High**<br>(3 × 4 = 12) | • Outputs clearly labeled as provisional advisory drafts with confidence indicators.<br>• Tier 1 blind review of primary documents prior to viewing system tags.<br>• Mandatory human rationale and sign-off before entry into corporate risk registers.<br>• COI bypass routing per ISO 37002 where reviewing HR owners are implicated. | ISO 42001 A.9.2, A.9.3<br>EU AI Act Art. 14<br>HK PCPD 2024 Area 2<br>NIST GOVERN 3.1 | **Low**<br>(2 × 2 = 4) |
| **R-06** | **Statutory & Regulatory Drift:** Legislative amendments (e.g., Cap. 57 revisions, EU AI Act enforcement milestones, updated PCPD/DPO guidance) rendering local corpora stale. | **Medium**<br>(3 × 3 = 9) | • Scheduled quarterly corpus review against HKeL, EUR-Lex, PCPD, and DPO updates.<br>• Domain-specific automated regression test suites gated in CI/CD.<br>• Semantic versioning (`vMAJOR.MINOR.PATCH`) and 60-day deprecation notices for obsolete prototypes. | ISO 42001 Clause 9.1, A.6.2.6<br>ISO 27001 A.8.32<br>NIST MEASURE 2.6 | **Low**<br>(2 × 2 = 4) |

---

## 4. Continuous Monitoring, Benchmarking & Escalation (ISO/IEC 42001 Clause 9.1)

1. **Pre-Deployment & Periodic Bias Benchmarking:** Because client-side tools do not collect live demographic attributes, fairness validation (including the Four-Fifths Rule $\ge 0.80$ threshold across synthetic cohorts) is executed during pre-release verification and quarterly regression cycles. Any benchmark failure halts release promotion until root-cause remediation is verified.
2. **Tiered Auditability & Evidence Logging:**
   - *Enterprise Tenant Deployments (M365 Workflows & Azure Audit Gateways):* Risk overrides, approvals, and gateway checks are logged inside the adopting organization's own tenant using tamper-evident mechanisms (such as read-only SharePoint audit lists, SHA-256 hash chains in *MCD Privacy Audit Gateway*, and Power Automate `Secure Outputs`).
   - *Static Zero-Retention Browser Sandboxes:* No server-side telemetry or logs are retained; reviewers export sanitized assessment briefs into internal corporate risk registers where audit preservation is required.
3. **Residual Risk Escalation:** Any confirmed High or Critical residual risk finding, guardrail bypass, or statutory discrepancy halts system use immediately and escalates to the repository maintainer (in open-source maintenance) or the adopting organization's Risk Committee and Lead Governance Auditor, following the disclosure and oversight protocols in `SECURITY.md` and `docs/HUMAN_OVERSIGHT.md`.
