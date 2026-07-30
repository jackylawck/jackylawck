# Data Lineage & Lifecycle Management (ISO 42001 Annex A.7)

## 1. Data Provenance & Source Legitimacy
All context data ingested into governance prototypes is sourced exclusively from:
* Statutory Hong Kong Ordinances (e.g., Employment Ordinance Cap. 57).
* Official Guidance Notes published by PCPD and HKIHRM.
* International AI Standards (ISO/IEC 42001, NIST AI RMF 1.0).

## 2. Data Cleaning & Minimization Rules
* **Noise Reduction:** Automated filtering of incomplete context segments (< 50 words).
* **Anonymization:** Strict removal of direct identifiers (Names, HKID numbers, addresses) prior to embedding generation.
* **Lineage Tracking:** Every RAG output retains metadata citations linking back to original statutory document clauses.
