# Algorithmic Impact & Risk Assessment Report (AIA / RMF)

> **Audit Standard Alignment:** Formulated and maintained in strict accordance with **ISO/IEC 42001:2023 (Clause 6.1, Clause 8.2 & Annex A.5 Impact Assessment)**, **NIST AI RMF 1.0 (GOVERN, MAP, MEASURE, MANAGE Core Functions)**, **EU AI Act (Regulation (EU) 2024/1689 Articles 6, 9 & 14)**, and **Hong Kong PCPD Model Framework (2024)**.

---

## 1. Context, Boundary & Statutory Scope (NIST MAP 1.1 / ISO 42001 Clause 6.1)

- **Target System:** Executive AI Intake, Policy Advisory & Pre-Screening Governance Sandbox (AIIA-v1 / TalentScout).
- **Core Technology Paradigm:** Localized Retrieval-Augmented Generation (Local RAG) with Deterministic Client-Side Rule Verifiers.
- **Statutory Risk Classification:**
  * **EU AI Act (Regulation (EU) 2024/1689):** Governed under **Article 6 & Annex III(4) (Employment & HR)** principles. Because this tool is engineered strictly as an *internal pre-audit and formative due-diligence sandbox* (prohibiting autonomous employment rejection), it qualifies under **Article 6(3) narrow procedural exceptions**. Mandatory conformity and Human-in-the-Loop guardrails are enforced by design.
  * **Hong Kong PCPD / DPO Benchmark:** Classified as a **High-Attention Governance Workstation**, mandating end-to-end Algorithmic Transparency, Zero Data Retention (ZDR), and Privacy-by-Design.

---

## 2. Risk Appetite & Assessment Methodology (NIST GOVERN 1.2)

Risk is evaluated deterministically as a product of **Severity (1–5)** and **Likelihood (1–5)**:
$$\text{Risk Score} = \text{Severity} \times \text{Likelihood}$$
- **Low / Acceptable:** Score 1–6 (Standard automated controls)
- **Medium / Tolerable:** Score 8–12 (Mandatory procedural controls + logging)
- **High / Unacceptable:** Score 15–25 (Pipeline freeze + mandatory Human-in-the-Loop escalation)

---

## 3. Comprehensive Risk Control Matrix (ISO 42001 Annex A.5 & NIST MEASURE/MANAGE)

| Risk ID | Hazard / Failure Mode | Inherent Risk (S × L) | Control Mechanism & Algorithmic Guardrail | ISO 42001 / NIST Mapping | Residual Risk |
| :--- | :--- | :---: | :--- | :--- | :---: |
| **R-01** | **Algorithmic Demographic Bias:** Disproportionate scoring against protected classes (Gender, Race, Disability, Age). | **High**<br>(4 × 4 = 16) | • Four-Fifths Rule (Disparate Impact Ratio $> 0.80$) automated monitoring.<br>• Strip demographic proxies (e.g., graduation year, school names).<br>• Mandatory blind human review for borderline scores. | ISO A.5.2<br>NIST MEASURE 2.11<br>HK EOC Guidelines | **Low**<br>(2 × 2 = 4) |
| **R-02** | **Statutory Hallucination:** Inaccurate advice on labor law, severance, or Cap. 57 "418" continuous contract rules. | **High**<br>(4 × 3 = 12) | • Grounded RAG with strict semantic threshold ($\cos \theta \ge 0.82$).<br>• Fallback to static statutory text if confidence score drops.<br>• Citation pegging down to specific ordinance sub-clauses. | ISO A.8.2<br>NIST MANAGE 2.2 | **Very Low**<br>(2 × 1 = 2) |
| **R-03** | **Prompt Injection & Guardrail Bypass:** Malicious input overriding ethical guardrails or forcing data exposure. | **High**<br>(4 × 3 = 12) | • Deterministic regex sanitizer prior to vector embedding.<br>• Dual-prompt isolation (separating system context from user input).<br>• Zero external API execution privileges. | ISO A.8.4<br>OWASP LLM01<br>NIST MANAGE 1.3 | **Low**<br>(2 × 2 = 4) |
| **R-04** | **PII & Confidentiality Leakage:** Unintended persistence of candidate identities or internal company records. | **Critical**<br>(5 × 3 = 15) | • 100% Volatile in-memory execution (Zero Data Retention).<br>• Automated regex redaction of HKID, phone, and addresses.<br>• Zero cloud database persistence or remote telemetry. | ISO 27001 A.8.10<br>ISO 27701 A.7.2<br>HK PDPO Cap. 486 | **Negligible**<br>(1 × 1 = 1) |
| **R-05** | **Automation Bias & Rubber-Stamping:** HR managers unquestioningly accepting AI scores without critical appraisal. | **Medium**<br>(3 × 4 = 12) | • Model outputs presented strictly with explicit confidence intervals.<br>• Mandatory randomized blind audits of accepted recommendations.<br>• Mandatory rationale sign-off required for executive filing. | ISO A.8.4<br>EU AI Act Art. 14<br>NIST GOVERN 3.1 | **Low**<br>(2 × 2 = 4) |
| **R-06** | **Concept & Regulatory Drift:** Statutory reforms (e.g., Cap. 57 418 threshold revisions) invalidating models. | **Medium**<br>(3 × 3 = 9) | • Scheduled quarterly ontology recalibration against HK Gazette.<br>• Automated regression test suite covering 50 standard test cases.<br>• Automated semantic versioning deprecation alerts. | ISO A.8.4<br>NIST MEASURE 2.6 | **Low**<br>(2 × 2 = 4) |

---

## 4. Continuous Monitoring & Threshold Assurance (ISO 42001 Clause 9)

1. **Disparate Impact Thresholds:** Any evaluation run where the Selection Rate for a demographic group falls below 80% of the highest group triggers an immediate algorithmic lock (`CIRCUIT_BREAKER_TRIGGERED`).
2. **Audit Trail Immutability:** Risk assessments, human override logs, and disparity telemetry are hashed via SHA-256 and appended to tamper-evident local logs.
3. **Executive Escalation:** Any unresolved High-Risk residual event escalates automatically to the Board Risk Committee and the Lead AI Governance Auditor.
