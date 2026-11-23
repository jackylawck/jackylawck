# System Lifecycle, Change Management & Continuous Assurance

> **Audit Standard Alignment:** Maintained in alignment with **ISO/IEC 42001:2023 (AIMS)** (Clauses 6.3, 8.1, 8.4, 9.1 & Annex A.6: AI System Life Cycle), **ISO/IEC 27001:2022** (Controls A.8.25, A.8.29 & A.8.32), **IAPP AIGP Domains III & IV**, and benchmarked against robustness and post-market monitoring principles in **EU AI Act (Regulation (EU) 2024/1689, Articles 15 & 72)**.

---

## 1. Lifecycle Architecture & Stage Gates (ISO/IEC 42001 Annex A.6)

Every governance workstation, AI-assisted prototype, deterministic client tool, and enterprise M365 reference template progresses through five stage-gated phases. Promotion to the next phase requires meeting defined exit criteria:

```text
+----------------------------------------------------------------------+
|                  SYSTEM LIFECYCLE QUALITY GATEWAYS                   |
+----------------------------------------------------------------------+
| [ Phase 1: Intake, Scoping & Regulatory Triage ]                     |
|   - Deliverables: Scope boundary, Non-AI check, MODEL_CARD.md draft  |
|   - Gate 1 Exit: Scope classification & impact baseline approved     |
|          |                                                           |
|          v                                                           |
| [ Phase 2: Design, Build & Deterministic Verification ]              |
|   - Deliverables: Source code, pinned/hashed deps, unit test suite   |
|   - Gate 2 Exit: Automated tests pass + CSP / XSS / checksum audit   |
|          |                                                           |
|          v                                                           |
| [ Phase 3: Governance Validation & Adversarial Testing ]             |
|   - Deliverables: Compliance review, rubric & prompt red-teaming     |
|   - Gate 3 Exit: Control sign-off & documented limitation review     |
|          |                                                           |
|          v                                                           |
| [ Phase 4: Controlled Release & Cryptographic Provenance ]           |
|   - Deliverables: PGP-signed commits, SHA-256 manifest, Rekor log    |
|   - Gate 4 Exit: Clean-room CI/CD pass & zero-telemetry validation   |
|          |                                                           |
|          v                                                           |
| [ Phase 5: Ongoing Monitoring, Calibration & End-of-Life (EOL) ]     |
|   - Ongoing: Quarterly statutory review, security patches, archival  |
+----------------------------------------------------------------------+

2. Stage-Gate Accountability & Exit Criteria
In open-source maintenance, the repository maintainer executes technical and governance verification directly. Where organizations adopt these reference architectures internally, accountability maps to the enterprise roles below:
| Lifecycle Phase | Enterprise Reference Role | Mandatory Exit Criteria |
|---|---|---|
| Phase 1: Intake & Scoping | Governance / Legal Owner | Clear intended-use and prohibited-use boundaries documented; formal deterministic non-AI scope-out check under EU AI Act Art. 3(1) where applicable. |
| Phase 2: Build & Verification | Technical Lead | Exact pinned or self-hosted dependencies; domain-specific automated tests passing; zero inline scripts violating strict CSP (default-src 'none' / 'self'). |
| Phase 3: Governance Validation | ISO Lead Auditor / Compliance | Alignment review against HK PCPD (2024), HK DPO, and statutory checklists; prompt-injection or boundary testing completed for AI-assisted prototypes. |
| Phase 4: Controlled Release | Security Lead | Clean-room CI/CD gate passing; SHA-256 vendor/dataset checksums verified; PGP-signed release commits (Key ID FFA3E47793F1CA32) and Sigstore Rekor attestation where configured. |
| Phase 5: Monitoring & EOL | Risk / Audit Committee | Quarterly statutory and dependency reviews; timely vulnerability handling per SECURITY.md; orderly archival upon end-of-life. |
3. Change Control & Semantic Versioning (ISO/IEC 27001 A.8.32 & ISO/IEC 42001 Clause 6.3)
All codebases, rule tables, statutory corpora, and enterprise flow schemas follow semantic versioning (vMAJOR.MINOR.PATCH):
3.1 Modification Tiers
 * Major Releases (vX.0.0 - Structural or Regulatory Shifts):
   * Triggers: Enactment of new primary legislation (such as Hong Kong Cap. 57 threshold revisions or EU AI Act enforcement milestones), breaking schema migrations, or core engine replacements.
   * Controls: Full review and update of MODEL_CARD.md, compliance scope boundaries, and regression test baselines prior to release.
 * Minor Releases (vX.Y.0 - Regulatory Calibration & Feature Additions):
   * Triggers: Updated regulatory guidance (HK PCPD advisories, HK DPO guidelines), new archival adapters (The Veracity / Veritas), expanded lexical sets (KidsPrepDictate), or additional enterprise workflow controls (SpeakUp-Mediation).
   * Controls: Full automated test pass, bilingual parity check, and updated governance documentation (README.md, llms.txt, sitemap.xml).
 * Patch Releases (vX.Y.Z - Security Hardening & Defect Fixes):
   * Triggers: Security or CSP hardening, prompt-injection mitigations, UI defects, dependency checksum refreshes, or documentation corrections.
   * Controls: Expedited review and best-effort patch deployment aligned with target timelines in SECURITY.md.
4. Automated CI/CD Verification & Regression Gates (ISO/IEC 27001 A.8.29)
Before merging changes into main or publishing to GitHub Pages, repository pipelines enforce verification gates tailored to each project's architecture:
 * Domain-Specific Functional Regression:
   * HR & Statutory Prototypes (e.g., Laboris, Cap. 57 Advisors): Deterministic calculation checks covering statutory leave, continuous-contract thresholds, and rule citations to prevent calculation drift.
   * Client-Side PWAs (e.g., SlimVid, KidsPrepDictate, SpeakFlow): Automated unit tests (node --test / Vitest), strict TypeScript or ES module syntax checks, bilingual i18n key-parity checks, and zero-innerHTML XSS guards.
   * Enterprise M365 Templates (e.g., SpeakUp-Mediation, DailyStaffAppraisal): JSON schema validation, Conflict-of-Interest (COI) routing verification, and sanitized placeholder audits ensuring zero live tenant credentials or GUIDs enter source control.
 * Non-AI Scope-Out & Zero-Telemetry Guard: Verifies that deterministic repositories introduce no unapproved machine learning runtimes, external analytics beacons, or unauthorized network requests.
 * Supply-Chain & Cryptographic Integrity: Verifies SHA-256 checksums for self-hosted vendor bundles and precompiled datasets, alongside PGP commit signatures and Sigstore Rekor attestations where enabled.
5. Decommissioning & End-of-Life (EOL) Protocol (ISO/IEC 42001 Clause 8.1)
When a prototype or reference architecture reaches end-of-life:
 * Deprecation Notice: Active web portals slated for retirement display an on-screen deprecation banner and repository notice for at least 60 calendar days prior to archival.
 * Tiered Data Wind-Down:
   * Volatile In-Memory Tools: No server-side data exists; retirement requires no backend purge or database migration.
   * Local-First Browser Storage PWAs: Deprecation notices remind users to export or clear any locally stored browser data (localStorage) before decommissioning.
   * Enterprise M365 Reference Templates: Adopting organizations retain full responsibility for exporting audit records and decommissioning SharePoint lists and Power Automate flows inside their own tenants under internal retention policies (aligned with HK PDPO DPP2).
 * Read-Only Archival: Upon formal EOL, the repository is marked archived (read-only) with its final commit history, release manifest, and transparency log proofs preserved for retrospective audit reference.

