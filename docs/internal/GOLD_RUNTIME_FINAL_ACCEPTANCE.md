# Gold runtime and gallery acceptance — 4 November 2026

| Item | Status | Actual evidence |
|---|---|---|
| Docker + PostgreSQL | PASS in isolated CI | Integration 41789917954; original replay/restart outputs preserved in Gold evidence/runtime |
| Airflow tasks | PASS in Docker | Real DAG CLI execution of extract, model and export; metadata SQLite, analytical data PostgreSQL |
| Automation | PASS first full path / daily cron enabled | Refresh run 41788601769; daily 13:17 Asia/Bangkok; future timed trigger not yet observed |
| Persistent hosted services | NOT DEPLOYED | GitHub Actions containers are ephemeral; validated observations persist in Git |
| Current recorded data | PASS | 2,412 observations, export 4 November 2026 06:56:26 UTC; monthly coverage through October 2026 |
| ML | NOT PASSED | HGB MAE 138.14 vs naive 135.47; 16-configuration validation still selects naive; no forecast |
| Forecast guard | PASS | At least 5% lower MAE and RMSE and two winning annual folds required; evaluated again on each refresh |
| Gallery | PASS | Five real screenshots load; all thumbnails and image lightbox tested on deployed site |
| Responsive | PASS in browser viewports | 28 pages × 360/390/768/1440 CSS pixels = 112 checks; no overflow, broken loaded images or H1 issues |
| Console | PASS for application | Only browser-extension metadata errors observed |
| Design preservation | PASS | Hero/navigation prefix byte-identical; engine/site.js, effects.js, scroll-film.js and six CSS files unchanged |
| Scope protection | PASS | No mutation of agricultural repo or Yuyenpensuk production |

The 112-check run covers the deployed gallery release. A final small text refinement adds PostgreSQL/Airflow to the role and featured summary; targeted main/Gold page checks are available at tools/qa-gold.html. No layout or effects source changed. Evidence screenshots of the deployed Portfolio are in evidence/acceptance/gold-gallery-*.jpg; the gold-runtime-portfolio-responsive.json file contains raw browser results. Physical device testing was not performed.

Public Gold dashboard: https://intasan.github.io/gold-trading/
Runtime report: https://github.com/intasan/gold-trading/blob/main/docs/RUNTIME_ACCEPTANCE.md

ML cannot honestly be guaranteed to pass by repeated tuning of a known holdout. Existing results are disclosed as reused retrospective evidence. Better future-data performance remains outstanding; the site does not present the model as an accepted forecasting tool.
