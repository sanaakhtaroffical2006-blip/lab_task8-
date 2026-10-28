# Defect Taxonomy for Requirements

| # | Category | Definition | Example (PSVS) |
|---|----------|------------|----------------|
| 1 | Ambiguity | Statement admits more than one interpretation. | S10: "20% of its boxes per year": of boxes held now, or at start of year? Calendar or rolling year? |
| 2 | Vagueness | Uses imprecise terms with no measurable meaning. | S6: "safe temperature" |
| 3 | Incompleteness | Missing information needed to implement or verify (actors, conditions, error cases). | S8: no duration, authorization or handling of boxes during maintenance |
| 4 | Contradiction | Two statements cannot both be satisfied. | S7 "never above -18°C" vs S8 "warmed to 0°C" |
| 5 | Non-verifiability | No finite objective test or proof can show satisfaction. | S12: "good audit trail" |
| 6 | Redundancy | Same content stated more than once; risk of divergence. | S6 is subsumed by S7 |
| 7 | Infeasibility | Cannot be achieved with realistic technical, legal or physical constraints. | S7: "never" is absolute, impossible under total power failure |
| 8 | Untraceability | No source, rationale or ID linking it to a stakeholder need or downstream artifact. | S3: 50,000 / 20,000 limits have no stated rationale |

**Severity scale:** High = could cause a wrong/unsafe system or blocks design; Medium = causes rework or interpretation disputes; Low = cosmetic / maintainability.
