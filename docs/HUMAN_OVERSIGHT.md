# Human Oversight, Escalation & Redress Framework

> **Regulatory & Governance Alignment:** Maintained in alignment with **ISO/IEC 42001:2023 (AIMS)** (Clauses 8.2, 8.4 & Annex A.6.2.6, A.8.2–A.8.4, A.9.2–A.9.4), **ISO 37002** (Whistleblowing Management), **EU AI Act (Regulation (EU) 2024/1689, Articles 14 & 86)**, **Hong Kong PCPD Model Personal Data Protection Framework (2024 — Areas 2 & 4)**, **Hong Kong PDPO (Cap. 486)**, **Hong Kong Mediation Ordinance (Cap. 620)**, and **IAPP AIGP Domain IV (Human Oversight & Governance)**.

---

## 1. Human Oversight Governance Tiers (HITL / HOTL / HIC)

All AI-assisted governance sandboxes, compliance advisors, and deterministic workflow prototypes in this portfolio operate under non-autonomous boundaries. Human oversight is structured across three operational tiers:

```text
+----------------------------------------------------------------------+
|                HUMAN OVERSIGHT GOVERNANCE HIERARCHY                  |
+----------------------------------------------------------------------+
| 1. Human-in-the-Loop (HITL) - Pre-Action Sign-Off                    |
|    * Systems generate draft risk classifications, statutory citations|
|      or rubric bias flags only.                                      |
|    * No binding organizational action takes effect without explicit  |
|      human review and approval.                                      |
|                                                                      |
| 2. Human-on-the-Loop (HOTL) - Operational Monitoring & Intervention  |
|    * Designated owners monitor retrieval confidence, deterministic   |
|      rule triggers, and fairness indicators during ongoing use.      |
|    * Reviewers retain immediate authority to pause execution or      |
|      route edge cases to manual inspection.                          |
|                                                                      |
| 3. Human-in-Command (HIC) - Executive Override & Decommissioning     |
|    * Ultimate governance authority rests with executive leadership   |
|      and Board Risk or Audit Committees.                             |
|    * Includes full authority to override outputs, suspend workflows, |
|      or decommission a system upon legal, ethical, or safety risk.   |
+----------------------------------------------------------------------+

2. Prohibition of Fully Automated High-Stakes Decisions
 * Non-ADM Boundary: No prototype or reference workflow in this repository is authorized for deployment as a sole automated decision-making (ADM) mechanism for candidate rejection, disciplinary action, contract termination, compensation adjustment, or statutory entitlement determination.
 * Advisory & Workflow Accountability: AI-assisted prototypes (such as local RAG compliance advisors and vendor rubric sandboxes) serve strictly as advisory decision support, while deterministic workflows (such as SpeakUp-Mediation and DailyStaffAppraisal) enforce mandatory human evaluation. Legal and managerial accountability rests 100% with designated human decision-makers.
3. Escalation, Blind Review & Conflict-of-Interest (COI) Protocol
[ Automated Triage / Deterministic Rule Check ]
       |
       v (Confidence < 0.82, Boundary Margin, or Proxy-Bias Flag)
[ Tier 1: Independent Human Blind Review ]
       | (Primary documents reviewed with system rationale masked)
       |
       +--> [ COI Gate: Implicates Reviewing HR Owner? ]
       |         |
       |         +--> YES --> [ Direct Bypass to Managing Director / Audit Committee ]
       |
       v (Contested Finding or Residual Compliance Risk)
[ Tier 2: Governance & Compliance Review ]
       | (Verification against HK PDPO, Cap. 57, EOC Cap. 480/487/527/602 & ISO 42001)
       v (Unresolved Workplace or Governance Dispute)
[ Tier 3: Voluntary ADR & Workplace Mediation ] (HK Mediation Ordinance Cap. 620)

 * Threshold & Anomaly Escalation: Any advisory output falling below the configured retrieval confidence threshold (0.82), landing within a borderline grading margin, or flagging a statutory protected-ground proxy automatically halts synthesis and routes to manual review.
 * De-Biased Blind Review: To mitigate automation bias and anchoring bias, Tier 1 reviewers inspect primary source documents or submissions before viewing system-generated summaries or tags.
 * Conflict-of-Interest (COI) Bypass: Consistent with ISO 37002 and the SpeakUp-Mediation reference architecture, any escalated HR or governance matter implicating the reviewing HR function automatically bypasses HR queues and routes directly to executive leadership or an independent oversight committee.
4. Individual Explanation, Re-Evaluation & Mediation Redress
To uphold procedural fairness across applicable jurisdictions — including EU AI Act Article 86 and GDPR Article 22 (where EU scope applies), and Hong Kong PDPO (Cap. 486, DPP1, DPP2, DPP6) alongside HK PCPD Model Framework (2024, Area 4) in Hong Kong:
 * Clear Human Explanation: Affected individuals are entitled to plain-language explanations of the evaluation criteria, rule weights, and statutory or policy clauses relied upon in any decision affecting them.
 * Formal Human Re-Evaluation:
   * Individuals may request a manual review within 14 calendar days of receiving an assessed outcome.
   * Re-evaluation must be conducted by an independent human reviewer who was not involved in the initial review cycle.
 * Voluntary Mediation Pathway (ADR):
   * For contested workplace or governance matters, organizations adopting these reference frameworks should provide a voluntary, neutral workplace mediation option prior to formal disciplinary or legal escalation.
   * Consistent with the Hong Kong Mediation Ordinance (Cap. 620), mediation communications operate on a confidential, "without prejudice" basis and are kept strictly separate from formal HR personnel files.
5. Auditability & Execution-Tier Logging Boundaries (ISO/IEC 27001 & ISO/IEC 42001)
Logging and retention of oversight actions follow each architecture's execution boundary, consistent with SECURITY.md and docs/DATA_LINEAGE.md:
 * Enterprise Tenant Deployments (M365 Workflows & Azure Audit Gateways): Human overrides, approval timestamps, and escalation outcomes are recorded within the adopting organization's own tenant using tamper-evident mechanisms (such as read-only SharePoint audit lists, SHA-256 hash-chained logs in MCD Privacy Audit Gateway, broken-inheritance RBAC, and Power Automate Secure Outputs redaction). Override patterns are reviewed semi-annually to detect systematic rubric drift or recurring control gaps.
 * Client-Side Zero-Data-Retention Sandboxes: Static browser tools execute strictly in local volatile memory and retain no server-side logs. Where formal corporate audit trails are required, reviewers export sanitized assessment summaries into their internal enterprise risk or compliance registers under corporate retention policies.

