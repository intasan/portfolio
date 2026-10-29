# Verification — 30 October 2026

## Content grounding

Reviewed the original portfolio, current project READMEs, Agricultural Prices integration evidence, the existing BA resume, and the PPE assignment. Updated employment intent to BA / SA / Data Analyst, education year to 2026, and availability to November 2026 using the user's latest stated availability. No employer names or internship dates were invented.

Separated GoldSense (Thai gold / SQLite / Linear Regression) from Gold Trading Analytics (Airflow / PostgreSQL / experimental models). Updated Yuyenpensuk's description to its current Docker and persistent CMS storage documentation. Agricultural Prices' 398 records are explicitly tied to the October verification dataset, not a live count. PPE is a proposed take-home solution; flood analytics is in development without certified flood predictions or a hosted deployment.

## Browser layout checks

Chrome, with iframe viewport fixtures (not physical devices):

| Viewport | Main page | PPE page | 17 project dialogs |
| --- | --- | --- | --- |
| 320 × 568 | Pass | Pass | Pass |
| 360 × 800 | Pass | Pass | Pass |
| 390 × 844 | Pass | Pass | Pass |
| 430 × 932 | Pass | Pass | Pass |
| 700 × 900 | Pass | Pass | Pass |
| 768 × 1024 | Pass | Pass | Pass |
| 1024 × 768 | Pass | Pass | Pass |
| 1440 × 900 | Pass | Pass | Pass |
| 1920 × 1080 | Pass | Pass | Pass |

Measured document/dialog scrollWidth against clientWidth; no horizontal overflow. Dialogs were opened through their shareable fragment routes: 17 × 9 = 153 dialog layout checks. Standard desktop scrollbar width reduces the available content width inside each fixture by 15px. Main and PPE pages add 18 page layout checks.

## Interaction checks

- All six filters: All 17, BA 7, SA 11, Data 6, Application 2, Interactive 3. A project may belong to multiple categories.
- Opening a project from the list, title rendering, closing, and fragment routing.
- All 17 project dialogs render project-specific role, scope, tools, result, and limitation fields.
- Agricultural gallery: all three actual repository images loaded with nonzero natural dimensions.
- Thumbnail selection updates the displayed image/caption.
- Nested image dialog opens above the project dialog; Escape closes the image first, then the project.
- 320px mobile menu exposes all five navigation links and collapses after navigation.
- PPE destination contains all seven sections; its return link opens the PPE project in the portfolio.
- CV generated and visually reviewed as one A4 page; opened successfully in Chrome's PDF viewer. Automated download-event capture timed out in the cloud browser; it is not counted as a successful automated file-save check.
- Local destination files exist; section fragment targets resolve; JavaScript syntax passes `node --check`.
- The 13 unique linked GitHub repositories were retrieved through GitHub and their current README destinations inspected. Links are source/documentation links, not claims of deployed demos.
- Email and telephone URIs match the published contact details; sending email or placing a call was not performed.

## Limits

This is Chrome viewport QA, not an exhaustive test of every browser, screen dimension, operating system, or physical device. Repository accessibility does not establish that each underlying application runs successfully; no such claim is made. Several older projects have descriptions but no verified public screenshots; their galleries are omitted instead of showing fabricated interfaces. Live counts, financial prediction performance, production server uptime, and hydrological accuracy were not re-certified as part of portfolio editing.
