# BA / SA document audit

3 November 2026. Documentation completeness does not establish stakeholder acceptance.

| Requested artifact | Result | Location / boundary |
|---|---|---|
| Business requirements | PASS (source-derived scope) | analysis/yuyenpensuk/acceptance.html. Not an approved stakeholder BRD or interview transcript. |
| Software requirements | PASS (source-derived catalogue) | Same document: FR01–FR07, acceptance conditions, source and verification status. |
| Use Case Diagram | PASS (simplified source-derived model) | analysis/yuyenpensuk/diagrams/use-cases.svg. Actor/scope view, not claimed as a complete formal UML model. |
| Activity Diagram | PARTIAL | Existing workflow.svg and workflow.mmd are process/activity overviews, not a newly validated formal UML activity model. |
| Sequence Diagram | PASS (design artifact) | content-sequence.svg and .mmd describe successful save and failure boundary. Not an execution trace. |
| DFD | PASS with stated scope | Existing context/data-flow diagrams and detailed flow register. SVG is an overview; Mermaid and document carry full directions/stores. |
| ERD | PASS for actual SQL schema | analysis/adoption/erd.svg and .mmd from animal-adoption/schema.sql at 8b73516a25839510d31301f7f790a416278b652b. Yuyenpensuk data-model.svg is explicitly JSON logical modeling, not SQL ERD. |
| System Architecture | PASS (source-derived) | Yuyenpensuk specification explains host dispatch, Express/EJS, JSON and upload directories. Existing flow/model figures supplement it. |
| Business Workflow | PASS (document artifact) | Existing workflow for each of five source-derived analysis projects. Not proof of execution. |
| User Story | PASS (source-derived) | Three stories and acceptance criteria in the new Yuyenpensuk specification. |
| Acceptance Criteria | PASS (test design) | FR catalogue, stories and existing traceability tables. |
| UAT Test Cases | PASS as design / NOT TESTED as execution | Explicitly unexecuted; no user sign-off invented. |
| API Documentation | PASS for route catalogue | New specification labels HTML form routes and internal image endpoints; not a versioned public REST API contract. |
| Formal stakeholder-approved BRD/SRS | NOT TESTED / unavailable | No signed approval or original meeting record was supplied. |

## Existing document review

The five analysis documents (Yuyenpensuk, Booking, GoldSense, Flood, Vending) contain non-empty scopes, functional requirements, business rules, diagrams, data dictionaries and UAT plans. Existing source baselines were retained rather than silently presenting them as newly approved specifications. SVG XML validity, nonempty files and local links are checked. Browser rendering is checked separately. The adoption schema and Yuyenpensuk routes/storage were read directly. No stakeholder approval or full implementation equivalence is inferred for the other historical documents.

- `analysis/booking/index.html`: 16200 characters; 13 section headings.

- `analysis/flood/index.html`: 18685 characters; 13 section headings.

- `analysis/gold-thai/index.html`: 16279 characters; 13 section headings.

- `analysis/index.html`: 4561 characters; 0 section headings.

- `analysis/vending/index.html`: 16683 characters; 13 section headings.

- `analysis/yuyenpensuk/acceptance.html`: 10171 characters; 11 section headings.

- `analysis/yuyenpensuk/index.html`: 17211 characters; 13 section headings.


## Gold runtime update — 4 November 2026

Supersedes Gold runtime limitations in earlier dated sections only. Actual Docker + PostgreSQL 16.15 restart persistence and all three Airflow 2.10.5 DAG tasks passed on GitHub Actions run 41788294519. Daily 13:17 Asia/Bangkok refresh first full execution 41788601769 passed, including recorded export commit and Pages rebuild. Services are ephemeral; no hosted Airflow UI or permanent PostgreSQL deployment is claimed. Latest recorded export has 2,412 observations, 4 November 2026 06:56:26 UTC.

ML remains NOT PASSED: HGB MAE 138.14 vs naive 135.47; broader 16-configuration pre-holdout validation still selected the naive baseline. No predictive accuracy or forecast promotion is claimed. Raw source logs and reproducible comparison are in intasan/gold-trading.

Gold gallery now includes five real browser captures: overview, monthly history, model evaluation, pipeline/provenance and the successful GitHub Actions runtime integration. The *-current.jpg images show the 4 November export; the Actions capture is test-run evidence, not an Airflow UI or database GUI capture. External URLs point to the author's own Gold repository. All are Real Evidence of the displayed page, with stated scope; none is an AI screenshot.

Case-study source-derived requirements, data model and architecture links remain available. Hero, theme, navigation, Orb and all animation source were unchanged. Agricultural repository was not modified.
