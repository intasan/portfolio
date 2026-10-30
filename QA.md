# Portfolio redesign QA — 30 October 2026

## Scope and content

Rebuilt the site using the supplied Scroll Film design guidance while retaining the 17 previously reviewed project records, contact details and source-status disclosures. After factual review, graduation status is explicitly awaiting official confirmation, with November 2026 availability listed as intended. The former CV PDF was removed and replaced with an online summary.

Created original procedural 3D artwork for the introductory scene. It is explicitly described as abstract artwork, not a project screenshot. Yuyenpensuk's featured visual is labeled as a website asset from its repository; Agricultural Prices uses its actual dashboard screenshot; PPE and MotoInsight show clearly labeled requirement/workflow summaries. No demonstration video is claimed for a project without original footage.

## Responsive checks

Chrome using viewport iframe fixtures, not physical devices:

320×568, 360×800, 390×844, 430×932, 700×900, 768×1024, 1024×768, 1440×900, 1920×1080.

- Main page and PPE document: 18 page/viewport checks.
- 17 standalone HTML case studies: 153 page/viewport checks; each contains its expected heading.
- 17 native project dialogs: 153 dialog/viewport checks.
- No document/dialog horizontal overflow in these checks. Standard desktop scrollbars reduce the available fixture content width by 15 pixels.
- Visually reviewed desktop hero, portrait hero, selected-work layout, source artwork and the updated online CV source.

## Interaction checks

- All six filters: All 17, BA 7, SA 11, Data Analyst 6, Application 2, Interactive 3. Multi-category membership is intentional.
- Search for Airflow returns Agricultural Prices and Gold Trading Analytics; a nonmatching query returns a truthful empty state; clearing restores the list.
- Project links progressively enhance to dialogs while updating their fragment routes; standalone page links and return-to-archive links work.
- Gallery thumbnail/caption update, nested image modal, Escape to close the image then the project, and return of keyboard focus to the originating project link.
- Mobile menu opens and closes with Escape, an outside click, and navigation. After layout settles at desktop width its state resets before returning to mobile.
- Navigation active indicator corresponds to the selected-work section; reading progress is updated without a global per-frame CSS custom property.
- Motion on: scroll reaches rendered hi frame 47, reverses to hi frame 2 near the hero; motion off: frame 0 remains displayed while scrolling.
- No-JavaScript sandbox: all 17 static project links remain present, the portrait poster loads, and an appropriate explanatory message is visible. Every project has a standalone HTML destination.
- Both featured remote images loaded with nonzero natural dimensions. The original Agricultural gallery images were verified in the preceding content revision and its gallery interaction was retested here.
- The previous CV PDF was removed due to unsupported internship content. The replacement online CV was reviewed in source but has not been revalidated in every browser or printed to PDF.

## Asset and static checks

- 48 valid hi WebP frames and 16 valid lo frames per orientation; lo = ceil(hi / 3). All image files decode.
- Approximate decoded hi-image footprint: landscape 161.1 MiB, portrait 91.4 MiB; this excludes canvas, low tier, browser, fonts and other page resources. It is a size estimate, not measured peak device memory.
- All local links, image sources, scripts, stylesheets and section IDs are checked; project links map to real HTML pages.
- JavaScript syntax checked with Node.
- Theme text contrast checked against its dark and light section backgrounds.

## Limits

No physical iPhone/Safari, Firefox or Edge test was performed. No measured first-frame latency, Core Web Vitals, exhaustive slow-network test, browser memory profile or simulated GPU context-loss test is claimed. The renderer includes poster, visibility and context-restoration handling, reviewed in source. Native scroll is used without a second smoothing layer. GitHub Pages controls response cache headers; versioned frame paths are used, but custom immutable headers cannot be imposed by these static files.

Project repository links describe source/documentation, not public running demos. Operational uptime, underlying application runtimes, forecast performance and hydrological accuracy were not recertified during this visual redesign.
