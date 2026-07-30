# AI Algorithmic Risk Assessment Report (ISO 42001 Clause 8.2 & NIST AI RMF)

## 1. Context & Scope (MAP 1.1)
* **Target System:** Generative AI HR Policy & Candidate Screening Assistant.
* **Risk Classification:** Minimal Risk (under EU AI Act classification rules when restricted to decision support).

## 2. Risk Control Matrix

| Risk ID | Hazard / Risk Description | Severity | Likelihood | Control Mechanism (ISO 42001 / NIST) | Residual Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R-01** | **Concept Drift / Terminology Shift:** Model output degrades due to changing resume keywords. | High | Medium | Continuous post-deployment monitoring; quarterly model re-validation protocol. | Low |
| **R-02** | **Algorithmic Bias:** Disproportionate rejection rates for demographic sub-groups. | High | Low | Disparate Impact Ratio testing; mandatory Human-in-the-Loop override. | Low |
| **R-03** | **Hallucination in Employment Law:** AI providing outdated labor compliance advice. | Medium | Medium | RAG boundary constraints pegged strictly to verified HK Employment Ordinance documents. | Very Low |
