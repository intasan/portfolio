# Gold implementation update — 4 November 2026

Supersedes only Gold concept-only claims in the historical 3 November acceptance records. Other project audits remain historical evidence and are retained.

Gold repository now contains executable ingestion, SQLite persistence, read-only API, dashboard and evaluated monthly ML. Real recorded data: 2,406 observations. Candidate MAE 133.60 vs naive 129.53; forecast withheld. PostgreSQL/Docker/Airflow runtime not tested.

Evidence: https://github.com/intasan/gold-trading/blob/main/evidence/IMPLEMENTATION_ACCEPTANCE.md

Image provenance: external URL points to this author's Gold repository, evidence/dashboard-desktop.jpg; actual deployed-site browser capture on 4 November 2026, classified Real Evidence. No generated image. Underlying market values are a recorded export, not live prices.

Only Gold project metadata, case-study article, featured card content and content-generation helpers changed. Hero, stylesheets, navigation, Orb and animation source remain unchanged. Backup branch: backup/before-gold-pipeline-20261104. Agricultural repository was not modified.


## Gold runtime update — 4 November 2026

Supersedes Gold runtime limitations in earlier dated sections only. Actual Docker + PostgreSQL 16.15 restart persistence and all three Airflow 2.10.5 DAG tasks passed on GitHub Actions run 41788294519. Daily 13:17 Asia/Bangkok refresh first full execution 41788601769 passed, including recorded export commit and Pages rebuild. Services are ephemeral; no hosted Airflow UI or permanent PostgreSQL deployment is claimed. Latest recorded export has 2,412 observations, 4 November 2026 06:56:26 UTC.

ML remains NOT PASSED: HGB MAE 138.14 vs naive 135.47; broader 16-configuration pre-holdout validation still selected the naive baseline. No predictive accuracy or forecast promotion is claimed. Raw source logs and reproducible comparison are in intasan/gold-trading.

Gold gallery now includes five real browser captures: overview, monthly history, model evaluation, pipeline/provenance and the successful GitHub Actions runtime integration. The *-current.jpg images show the 4 November export; the Actions capture is test-run evidence, not an Airflow UI or database GUI capture. External URLs point to the author's own Gold repository. All are Real Evidence of the displayed page, with stated scope; none is an AI screenshot.

Case-study source-derived requirements, data model and architecture links remain available. Hero, theme, navigation, Orb and all animation source were unchanged. Agricultural repository was not modified.
