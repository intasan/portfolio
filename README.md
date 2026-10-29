# Panupong Intasan — Business / Systems / Data

Portfolio for Business Analyst, System Analyst and Data Analyst opportunities.

Website: https://intasan.github.io/portfolio/

## Design

A cinematic introduction uses original, pre-rendered 3D ring artwork scrubbed on a canvas by native scroll. Two art-directed asset sets (desktop and mobile), lo/hi loading tiers, a static poster, reduced-motion support, and an explicit motion toggle provide progressive enhancement. The site uses native scrolling; no Lenis or additional easing is layered over it.

All 17 projects also have standalone HTML case-study pages. Project links open native dialogs when JavaScript is available and remain navigable HTML links when it is not. Visual summaries are labeled separately from real project screenshots.

## Structure

- `index.html`: editorial layout, featured work, experience, skills, project archive, education, contact.
- `brand.css`: theme tokens only.
- `engine/base.css`: shared layout, responsive rules, motion and print styling.
- `engine/scroll-film.js`: scroll-to-frame rendering, tiered local loading, poster fallback and visibility/context recovery handlers.
- `engine/site.js`: navigation, search/filtering, motion preferences, dialogs, gallery and route behavior.
- `projects.json`: authoritative project records.
- `projects.js`, `case-studies/`: generated browser data and 17 standalone case studies.
- `tools/build_project_pages.py`: regenerate case studies, project JS and sitemap from `projects.json`.
- `tools/render_film.py`: reproduce the original geometric 3D artwork; requires Python, NumPy and Pillow.
- `assets/film-v1/`: 48 high frames and 16 low frames per orientation, posters, manifest, and an original four-second motion export. Runtime loads only one orientation. The MP4 is a source export and is not loaded by the website.
- `CV_Panupong_Intasan.pdf`, `ppe-case-study.html`: downloadable CV and a proposed BA assignment excerpt.
- `QA.md`: verification scope and limitations.

## Content maintenance

Edit `projects.json` and run:

```bash
python3 tools/build_project_pages.py
```

Update featured editorial copy in `index.html` when its featured project's scope changes. Update the website and CV together when education, experience, availability or contact details change. Keep source-status disclosures: several legacy repositories contain reconstructed examples rather than complete original archives. Do not invent project screenshots, performance figures, employer names or internship dates.

## Hosting

Static files are served from the repository root by GitHub Pages. No framework or JavaScript build step is required. Google Fonts are optional enhancements; system fonts remain available as fallbacks. `brand.css` contains no component selectors.
