# Security Policy & Coordinated Vulnerability Disclosure (CVD)

> **Governance Alignment:** Maintained in accordance with **ISO/IEC 27001:2022 (Controls A.5.24–A.5.28)**, **ISO/IEC 27701:2019 (PIMS A.7)**, **ISO/IEC 42001:2023 (Control A.8.4)**, and **OWASP Top 10 for LLM Applications (2025/2026)**.

---

## 1. Zero Data Retention (ZDR) & Privacy Architecture Baseline

All workstations, prototypes, and sandboxes maintained under this repository strictly enforce **Privacy-by-Design** and **Zero Data Retention (ZDR)** architectural baselines:

- **100% Volatile In-Memory Execution:** All prompt sanitization, vector math, and compliance evaluations execute exclusively within runtime memory. Closing the browser tab or process lifecycle immediately purges all states.
- **Zero Remote Telemetry & PII Ingestion:** No cookies, tracker scripts, analytics beacons, or database connections exist on static client-side endpoints. 
- **Deterministic Cryptographic Verification:** Data fixity relies strictly on client-side native `crypto.subtle` APIs (AES-GCM-256 / SHA-256) and keyless transparency log attestations (Sigstore / Rekor).
- **Regulatory Mapping:** Fully compliant with Hong Kong Personal Data (Privacy) Ordinance (Cap. 486 PDPO), EU GDPR Article 5 (Data Minimization), and the 2024 HK PCPD Model Framework.

---

## 2. Supported Versions

| System / Prototype | Release Branch | Security Support Status |
| :--- | :--- | :---: |
| **Pillar I: Governance Workstations** (*Veracity, Veritas, Laboris, PCPD Sandbox, etc.*) | `main` | :white_check_mark: Actively Supported |
| **Pillar II: Zero-Trust PWA Suites** (*LeaveWell, ScanSign, Safe-Off, etc.*) | `main` | :white_check_mark: Actively Supported |
| **Pillar III: Cognitive & Agility** (*Lawgic, Spatial Test, DISC*) | `main` | :white_check_mark: Actively Supported |
| **Pillar IV: Scientific Simulations** (*JAR Series*) | `main` | :white_check_mark: Actively Supported |
| Legacy Experimental Prototypes | Archived Tags | :x: Unsupported |

---

## 3. Vulnerability Scope & Eligible Hazards

We welcome coordinated disclosure on the following security and governance risks:

- **Cryptographic Implementation Defects:** Insecure entropy, key-recovery flaws in PBKDF2/AES-GCM implementations, or Sigstore verification bypasses.
- **Client-Side Code Integrity:** DOM-based Cross-Site Scripting (XSS), Content Security Policy (CSP) bypasses, or Subresource Integrity (SRI) discrepancies.
- **AI Safety & Policy Guardrail Failure:** Direct prompt injection vulnerabilities leading to deterministic control bypass, or unauthorized extraction of sandboxed system prompts.
- **Data Minimization Violations:** Any unintended state leakage or unencrypted client persistence across browser sessions.

*Exclusions:* Automated volumetric DoS/DDoS attacks, social engineering, and issues originating from third-party hosting infrastructures (e.g., GitHub Pages edge servers) are out of scope.

---

## 4. Coordinated Disclosure Procedure

If you identify a security flaw or an algorithmic guardrail breach:

1. **Do Not Open Public Issues:** Please refrain from publishing GitHub Issues, Discussions, or pull requests containing exploit payloads.
2. **Preferred Reporting Method (Encrypted & Private):**
   - **GitHub Private Vulnerability Advisory:** Submit privately via the repository's **[Security] -> [Advisories] -> [Report a vulnerability]** tab.
   - **Alternative Channel:** Direct outreach via encrypted professional communication on [LinkedIn (Jacky Law)](https://www.linkedin.com/in/jackylawck) with the subject header `[SECURITY DISCLOSURE - VULNERABILITY]`.
3. **Required Disclosure Details:**
   - Detailed description of the vulnerability and attack vector.
   - Step-by-step reproduction steps or minimal Proof-of-Concept (PoC).
   - Expected impact assessment on data confidentiality, integrity, or governance guardrails.

---

## 5. Remediation Service-Level Agreements (SLAs)

Adhering to ISO/IEC 27001 incident handling disciplines:

- **Initial Triage & Acknowledgment:** Within **24–48 hours** of receipt.
- **Severity Assessment & Fix Development:** Within **5 business days**.
- **Coordinated Public Patch & CVE/Advisory Release:** Within **7–14 calendar days** following successful fix verification.

---

## 6. Safe Harbor & Research Protections

We consider security and safety research conducted under this policy to be **authorized and lawful**:

- We will not pursue legal civil action or initiate law enforcement complaints against individuals who perform good-faith security testing.
- Researchers must make reasonable efforts to avoid privacy violations, data destruction, and service degradation during analysis.
- Public attribution will be gratefully acknowledged in patch release notes unless the researcher requests anonymity.
