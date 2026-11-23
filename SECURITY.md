# Security Policy & Coordinated Vulnerability Disclosure (CVD)

> **Governance Alignment:** Maintained in alignment with **ISO/IEC 27001:2022** (Controls A.5.24–A.5.28, A.8.8), **ISO/IEC 27701** (Privacy by Design and Default, Annex A.7.4), **ISO/IEC 42001:2023** (Control A.8.4), and the **OWASP Top 10 for LLM Applications**.

---

## 1. Privacy Architecture & Zero Server-Side Retention Baseline

All workstations, client-side tools, and reference architectures maintained under `jackylawck` follow **Privacy-by-Design** and **Zero Server-Side Data Retention** principles across three operational tiers:

- **Volatile In-Memory Tools:** Prompt sanitizers, document diff engines, media transcoders, and compliance sandboxes (such as *Prompt-Off*, *ClauseDiff*, *SlimVid*, and *SpeakFlow*) process inputs strictly within browser runtime memory. Closing the tab or terminating the worker immediately purges session state.
- **Local-First Browser Storage Tools:** Personal learning and journaling PWAs (such as *KidsPrepDictate* and *PauseWell*) persist user-initiated progress exclusively inside local browser storage (`localStorage` / `sessionStorage`) under user control, with zero remote synchronization or server uploads.
- **Tenant-Isolated Enterprise Templates:** Microsoft 365 reference architectures (such as *SpeakUp-Mediation* and *DailyStaffAppraisal*) are designed to run entirely inside the adopting organization's own M365 tenant, utilizing broken-inheritance SharePoint RBAC and Power Automate `Secure Outputs` log redaction.
- **Zero Remote Telemetry & Cryptographic Integrity:** Static endpoints contain no tracking cookies, analytics beacons, or external logging databases. Client-side encryption and integrity verification rely on native `crypto.subtle` APIs (PBKDF2, AES-GCM-256, ECDSA P-256, SHA-256), strict Content Security Policies (CSP), and Sigstore/Rekor transparency attestations.
- **Regulatory Alignment:** Architected to align with the Hong Kong Personal Data (Privacy) Ordinance (Cap. 486, PDPO), EU GDPR Articles 5 and 25, and the Hong Kong PCPD Model Personal Data Protection Framework (2024).

---

## 2. Supported Versions

| Portfolio Pillar | Release Branch | Security Support Status |
| :--- | :--- | :--- |
| **Pillar I: AI Governance & Decision Support** (*Veracity, Veritas, Laboris, TalentBridge, PCPD/DPO Sandboxes*) | `main` | Actively Supported |
| **Pillar II: Zero-Trust Client Tools** (*SlimVid, KidsPrepDictate, SpeakFlow, LeaveWell, ScanSign, Safe-Off*) | `main` | Actively Supported |
| **Pillar III: Organizational Agility & Cognitive Tools** (*Lawgic, Nature Compass, Spatial Test, DISC*) | `main` | Actively Supported |
| **Pillar IV: Joint Applied Research** (*JAR QubitLab, JAR Black Hole, JAR Fusion Core, etc.*) | `main` | Actively Supported |
| **Pillar V: Enterprise M365 & Low-Code Workflows** (*SpeakUp-Mediation, DailyStaffAppraisal, DOIS, NOTAS, TAP*) | `main` | Actively Supported |
| Archived Experimental Prototypes | Archived Tags | Unsupported |

---

## 3. Vulnerability Scope & Eligible Risks

Coordinated disclosure is welcomed for verifiable security, privacy, or governance defects within repositories owned by `jackylawck`:

- **Cryptographic & Supply-Chain Integrity:** Weak entropy, key-derivation or AES-GCM flaws, Sigstore/Rekor attestation bypasses, or vendor SHA-256 checksum mismatches.
- **Client-Side Security Controls:** DOM-based Cross-Site Scripting (XSS), Content Security Policy (CSP) bypasses, `innerHTML` injection sinks, or unintended outbound network requests violating zero-upload guarantees.
- **Governance & AI Guardrail Failures:** Prompt-injection bypasses in local RAG prototypes, deterministic rule-engine logic bypasses, or unintended RBAC/COI routing flaws in M365 reference flow definitions.
- **Privacy & State Leakage:** Unintended cross-session data persistence in volatile tools, unredacted sensitive outputs in workflow templates, or unencrypted exposure of secrets designed to be protected.

**Out of Scope:** Volumetric DoS/DDoS testing, social engineering, theoretical issues without a reproducible proof of concept, and vulnerabilities in third-party infrastructure providers (such as GitHub Pages, Cloudflare, or Microsoft 365 cloud services).

---

## 4. Coordinated Disclosure Procedure

If you discover a security defect or governance control bypass:

1. **Keep Reports Private:** Do not open public GitHub Issues, Discussions, or pull requests containing exploit payloads or unpatched vulnerability details.
2. **Primary Channel (GitHub Private Vulnerability Reporting):** Submit a confidential report via the affected repository's **Security -> Advisories -> Report a vulnerability** tab.
3. **Encrypted Alternative (PGP / Keybase):** For cross-repository issues or encrypted correspondence, contact via [keybase.io/jackylawck](https://keybase.io/jackylawck) encrypted to GPG Key ID `FFA3E47793F1CA32`. For initial non-sensitive coordination only, you may reach out via [LinkedIn](https://www.linkedin.com/in/jackylawck) using the subject `[SECURITY DISCLOSURE]`.
4. **Recommended Report Contents:**
   - Affected repository name, commit hash or URL, and component.
   - Clear reproduction steps or a minimal Proof-of-Concept (PoC).
   - Assessment of potential impact on confidentiality, integrity, or governance boundaries.

---

## 5. Target Response & Remediation Timelines

Following ISO/IEC 27001 incident-handling practices on a best-effort basis for open-source maintenance:

- **Initial Acknowledgment:** Within **48–72 hours** of receipt.
- **Triage & Remediation Plan:** Within **5 business days**.
- **Patch Release & Coordinated Advisory:** Target **7–14 calendar days** after fix verification, depending on severity and scope.

---

## 6. Safe Harbor

Good-faith security research conducted in accordance with this policy is considered authorized with respect to repositories and static pages hosted under `github.com/jackylawck` and `jackylawck.github.io`:

- No legal action or law enforcement complaint will be initiated against researchers conducting good-faith, non-destructive testing within the scope defined above.
- Researchers must avoid privacy violations, data destruction, or disruption of third-party hosting services during testing.
- This safe harbor applies solely to `jackylawck` project assets and does not authorize testing against third-party platforms (including GitHub, Cloudflare, or external Microsoft 365 tenants).
- Credit will be acknowledged in release notes or advisories upon remediation unless the researcher prefers to remain anonymous.
