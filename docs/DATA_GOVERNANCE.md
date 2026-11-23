# Data Lineage, Provenance & Retention Baseline

> **Audit Standard Alignment:** Maintained in alignment with **ISO/IEC 42001:2023 (AIMS)** (Annex A.7: Data for AI Systems — Controls A.7.2 to A.7.6), **ISO/IEC 27701** (PIMS Annex A.7.4: Data Minimization, Retention & Disposal), **ISO/IEC 27001:2022** (Control A.8.10: Information Deletion), **IAPP AIGP Domain III (Data Governance)**, and **NIST AI RMF 1.0 (GOVERN, MAP & MEASURE)**.

---

## 1. Authoritative Data Sources & Provenance (ISO/IEC 42001 Annex A.7.3 & A.7.5)

All reference corpora, lexical datasets, and compliance mappings used across `jackylawck` repositories are strictly partitioned and sourced from verifiable public-domain or statutory authorities:

1. **Primary Legislation & Statutory Texts:**
   - Laws of the Hong Kong SAR (including Employment Ordinance Cap. 57, PDPO Cap. 486, Prevention of Bribery Ordinance Cap. 201, Mediation Ordinance Cap. 620, and EOC anti-discrimination ordinances Cap. 480, 487, 527, 602) retrieved via Hong Kong e-Legislation (HKeL).
   - Cross-border and international statutes: Regulation (EU) 2024/1689 (EU AI Act) via EUR-Lex and Mainland China Personal Information Protection Law (PIPL) official statutory texts.
2. **Regulatory Frameworks & Professional Standards:**
   - Hong Kong PCPD *Artificial Intelligence: Model Personal Data Protection Framework* (2024).
   - Hong Kong Digital Policy Office (DPO) *Ethical Artificial Intelligence Framework* and *Hong Kong Generative Artificial Intelligence Technical and Application Guideline*.
   - Professional governance references aligned with HKIHRM, HKIoD, ICPM, and CMI management standards.
3. **Public Declassification & Forensics Archives (*The Veracity* & *The Veil*):**
   - Official public-domain releases across 74 national and international archives (including US NARA/FRUS, UK National Archives, UNTS, and Archives nationales de France), scoped to declassified public records (1945–1996 historical window).
4. **Regulator Enforcement & Threat Feeds (*Veritas*):**
   - Public scam and impersonation alerts issued by 20+ statutory authorities (including HKMA, SFC, HKPF CSTCB, MAS, FBI IC3, CFTC, and FCA), normalized into OASIS STIX 2.1 bundles.
5. **Clean-Room Lexical & Educational Datasets (*KidsPrepDictate* & *KidsWriteTC*):**
   - Precompiled stroke-order and character-vector datasets (1,464 Hong Kong primary standard characters) built via an auditable offline ETL pipeline aligned with Hong Kong Education Bureau (EDB) lexical references.

**Corpus Exclusion Rule:** No synthetic training data, unverified web scrapes, or crowdsourced forum content are ingested into authoritative compliance or reference corpora.

---

## 2. Deterministic Ingestion Pipeline & Quality Controls (ISO/IEC 42001 Annex A.7.4 & A.7.6)

```text
+----------------------------------------------------------------------+
|                DETERMINISTIC DATA INGESTION PIPELINE                 |
+----------------------------------------------------------------------+
| 1. Authoritative Fetch (HTTPS Native Adapters / Verified Local ETL)  |
|         |                                                            |
|         v                                                            |
| 2. Deterministic Normalization (Schema Check & Pattern PII Masking)  |
|         |                                                            |
|         v                                                            |
| 3. Layer-1 Bitstream Fixity (SHA-256 Digest & Checksum Verification) |
|         |                                                            |
|         v                                                            |
| 4. Provenance Attestation (Sigstore Keyless Rekor Anchoring)         |
|         |                                                            |
|         v                                                            |
| 5. Static Artifact Publication / Client-Side In-Memory Execution     |
+----------------------------------------------------------------------+
