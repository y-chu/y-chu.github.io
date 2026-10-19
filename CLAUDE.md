# CLAUDE.md

This file is the working guide for this website repository. It is meant to keep future edits consistent across Codex, Claude, and manual maintenance.

## Authority

- Treat this file as the current source of truth for site structure and maintenance conventions.
- `AGENT.md` is historical context from an earlier redesign pass and may reference old file locations. Use `CLAUDE.md` when the two disagree.

## Site Basics

- Framework: Jekyll / Academic Pages / Minimal Mistakes
- Hosting target: GitHub Pages
- Build constraint: static-site compatible, no unsupported plugins
- Main config: `_config.yml`
- Main navigation: `_data/navigation.yml`

## Navigation-to-Folder Mapping

Top-level navigation content should live in folders that match the nav tabs.

- Home: `_pages/about.md`
- Research: `_research/index.md`
- Projects: `_projects/index.md` plus item pages in `_projects/*.md`
- Publications: `_publications/index.md` plus structured entries in `_publications/*.md`
- Presentations: `_presentations/index.md` (full list lives in the page front matter; replaced the old `_talks/` collection)
- Software: `_software/index.md`
- Teaching & Mentoring: `_teaching/index.md`
- News: `_news/index.md`
- Personal: `_personal/index.md` (kept in secondary/footer navigation)
- CV route: `_pages/cv.md` redirects `/cv/` to `files/Yue_Chu_CV.pdf`; `_pages/resume.md` redirects `/resume/` to `files/Yue_Chu_Resume.pdf`. The primary-nav CV link opens the CV PDF directly; the homepage has separate CV and Résumé links that open the PDFs.

Primary and secondary navigation are defined in `_data/navigation.yml`. The primary job-market navigation is Research, Publications, Projects, Software, Teaching & Mentoring, and CV. Presentations, News, and Personal are secondary/footer links.
- Served CV file: `files/Yue_Chu_CV.pdf`
- Served résumé file: `files/Yue_Chu_Resume.pdf`
- CV and résumé sources: `_CV/Yue_Chu_CV.qmd`, `_CV/Yue_Chu_Resume.qmd`
- Build commands (output directly to the served files, so no manual copy/drift):
  `quarto render _CV/Yue_Chu_CV.qmd --output-dir ../files`
  `quarto render _CV/Yue_Chu_Resume.qmd --output-dir ../files`
- Legacy consulting route: `_pages/consulting.md` redirects to the consulting section on `/projects/`

## Core Principle

If a section appears in the main website navigation, there should be one obvious matching folder where its content is maintained.

That means:

- Do keep nav-owned content in its matching folder.
- Do not scatter the same section across `_pages/` and `_data/` unless there is a strong technical reason.
- Do not create duplicate routed pages for nav sections in `_pages/` if a folder-backed version already exists.

## 2026 Audience and Positioning

The site supports one unified professional identity for two related markets:

- Research Scientist roles in population health, public health, demography, survey methodology, data science, and adjacent applied research settings
- Selective TTAP / tenure-track roles in population health, public health, demography, sociology, survey methodology, and related interdisciplinary fields

Do not create separate identities, sites, or parallel versions of the same page for these audiences. The primary audiences are TTAP searches and research-scientist roles at universities, research institutes, hospitals, and research organizations. Do not frame the site toward industry data-science hiring. The shared intellectual positioning is population measurement under incomplete, heterogeneous, or imperfect information, supported by demographic, statistical, computational, and AI methods and translated through research software, data infrastructure, and collaborative implementation.

Keep the site concise. The homepage and research page should establish direction and hierarchy; publications, projects, software, GitHub, and the comprehensive CV should provide the detailed evidence.

## Research Content Architecture

Keep established research identity and future research agenda explicitly separate. Do not present planned methods or projects as completed work.

### Established Research Identity

Present these three areas in this order:

1. **Population Inference with Incomplete and Heterogeneous Data** — demographic, statistical, computational, and AI approaches for reliable population estimates from incomplete, uneven, or heterogeneous evidence.
2. **Measurement Processes and Data Quality** — how data collection, reporting, and classification shape the quality, comparability, and interpretation of population evidence.
3. **Computational Research Tools and Data Infrastructure** — reusable research software and data infrastructure for reproducible analysis, collaboration, and translation into practice.

Keep these descriptions high-level. Do not turn them into inventories of every method, application, or project. Detailed evidence belongs in publications, projects, software, GitHub, and the CV. `Health Outcomes Research` may remain only as additional collaborative research, not as a fourth co-equal core area.

### Future Research Agenda

Use the umbrella title **Advancing Population Measurement under Imperfect Information**. The supporting copy may express the goal of producing better evidence and supporting consequential research, policy, epidemiologic, or public-health decisions, without limiting the agenda to a single discipline or employment sector.

Organize the future agenda around three high-level themes:

1. Understanding information, error, and uncertainty
2. Validating measurement across populations and settings
3. Designing more effective and equitable measurement strategies

Maintain the progression **understand → validate → design**. Keep the website language open and durable: do not name speculative methods such as knowledge graphs, specific future interview technologies, or other planned techniques unless they become documented projects or outputs. Adaptive data collection currently has workshop-poster evidence only and must be framed as a future direction, not an established research contribution.

### Public/Private Research Boundary

- Do not publish, link, title, summarize results from, or otherwise expose the unpublished writing-sample manuscript. This is the South African multimodal verbal-autopsy manuscript (`Job 2026/TTAP/sample_RSA`; formerly listed as "Multimodal Artificial Intelligence for Cause-of-Death Assignment From Verbal Autopsy Records"). Its held-out-province, calibration, and cross-setting results are private.
- The dissertation-chapter excerpt (`sample_MMVA`) is public through the dissertation, and the ALPHA writing sample is the published Lancet Global Health paper.
- The multimodal cause-of-death benchmark is publicly listed by NeurIPS 2026 and may be described as accepted. Yue Chu is fourth of 21 authors and is not a corresponding author on this paper. Retain the public medRxiv preprint link (Yang et al. 2026, DOI 10.64898/2026.07.13.26357980).
- Broad research questions already supported by public work may appear without disclosing unpublished manuscript details.
- MultimodalVA repository: https://github.com/y-chu/MultimodalVA. Yue confirmed on 2026-09-19 that it goes public no later than the week of 2026-09-21, and the link is already on the site, CV, and résumé. If it still returns 404 after that week, remove the links or ask Yue. Do not link `docs/index.html` via GitHub as "Docs" until a rendered documentation site exists.
- Website-wide methods language may include pretrained language models, LLMs, prompt engineering, machine learning, and multimodal learning when supported by documented work. Describe the stack of a specific project only with methods actually used in that project.

## Current Structure Pattern

There are two patterns in use:

1. Single-file section pages
- Used for `research`, `software`, `teaching`, `news`, and `personal`
- The section lives in that folder's `index.md`
- Structured lists for that section live in front matter arrays on the same file

2. Collection-backed sections
- Used for `projects` and `publications`
- The section landing page lives at that folder's `index.md`
- Individual items live as separate Markdown files in the same folder
- Consulting and technical assistance entries are part of `_projects/*.md` and should use `project_group: consulting`

## Important Implementation Detail

Folder landing pages inside collections use:

```yaml
entry_type: index
```

This matters because archive loops must exclude the index document.

Examples:

- `_projects/index.md`
- `_publications/index.md`
- `_teaching/index.md`

When filtering collection items, always exclude `entry_type: index`.

## Editing Rules

- When updating a nav section, edit the matching folder first.
- For curated research themes, edit `_research/index.md`.
- For software listings, edit `_software/index.md`.
- For curated news items, edit `_news/index.md`.
- For curated personal sections and fun updates, edit `_personal/index.md`.
- For publications used on the landing page and homepage, edit the structured entries in `_publications/*.md`; use `featured: true` sparingly for homepage selections.
- For presentations, edit `_presentations/index.md`.
- For project cards and project detail pages, edit `_projects/*.md`.
- For consulting and technical assistance entries, create or edit `_projects/*.md` with `project_group: consulting`.
- For publication detail pages, edit `_publications/*.md`.
- For Teaching & Mentoring content, edit `_teaching/index.md`.

## Publication Schema

Publication entries in `_publications/*.md` should use these fields when available:

- `publication_type`: `peer_reviewed`, `preprint`, `manuscript`, `working_paper`, `dissertation`, `thesis`, or `report`
- `publication_status`: optional precise status such as `Accepted`, `Under review`, `Preprint`, or `Working paper`; never infer or upgrade status. The landing page shows `publication_status`, falling back to the legacy `status` field, then `venue`.
- Preprints, manuscripts, and working papers render together under "Preprints and Manuscripts"
- `publication_order`: numeric display order within its type (ascending, newest first)
- `publication_year`: display year
- `authors`: compact HTML-ready author string with Yue Chu emphasized using `<strong>` when named
- `venue_details`: journal/report details shown on the landing page
- `featured`: optional boolean for the small homepage selection
- `detail_page`: boolean controlling whether the landing-page title links to the detail page

- `paper_page_url`: external landing page for the paper
- `doi`: DOI string without extra prose
- `doi_url`: DOI resolver URL
- `pdf_url`: direct PDF URL, either local or external
- `code_url`: code repository or download link
- `code_label`: optional custom label such as `Code and data`
- `poster_url`: poster PDF URL when available

Legacy compatibility:

- Keep `paperurl` populated for now because some older helper scripts still read it.

## Publication Assets

Recommended local asset folders:

- Publication PDFs: `assets/pdfs/publications/`
- Posters: `assets/pdfs/posters/`

Current status:

- Some older paper PDFs still live in `files/`. That is acceptable for now.
- New local publication assets should prefer the `assets/pdfs/...` structure unless there is a specific reason to keep them in `files/`.

## Design / UX Principles

- Keep the site academically professional but not visually cold.
- Prefer clear hierarchy, restrained color, and readable spacing over heavy decoration.
- Reuse includes for repeated cards and summary blocks.
- Preserve mobile responsiveness.
- Preserve existing public URLs whenever practical.

## Do

- Keep reusable display logic in `_includes/`
- Keep styling changes in the existing Sass/CSS structure
- Keep the homepage lightweight and directional
- Keep the GitHub Pages build compatible
- Add new nav sections only with a matching folder and clear ownership

## Do Not

- Do not reintroduce nav-owned content into `_data/research.yml`, `_data/news.yml`, etc.
- Do not create a second copy of a nav page in `_pages/` after a folder-backed version exists.
- Do not remove `entry_type: index` from collection landing pages without updating the archive logic.
- Do not add unsupported plugins or build steps that break GitHub Pages.
- Do not change public permalinks casually.

## Current Decisions

- The homepage remains in `_pages/about.md` because it is the root route and is not part of the main nav list.
- The CV remains a direct PDF experience: `/cv/` and the nav open `files/Yue_Chu_CV.pdf`. The Research Résumé has no nav slot or landing page; it is linked from the homepage and `/resume/`.
- Publication records live in the publications collection; homepage selections use `featured: true`.
- Presentations remain available as a secondary/footer destination, with legacy `/talks/` routes redirected to `/presentations/`.
- Teaching & Mentoring is a primary-navigation page backed by `_teaching/index.md`.
- Consulting is no longer a standalone navigation tab; consulting and technical assistance work now lives inside the projects collection.
- Research, news, and personal currently use single landing files with front matter arrays instead of one-file-per-item. This keeps the nav-to-folder mapping clean without generating unwanted extra pages.
- Preserve the current layouts and visual identity. Job-market updates should primarily improve content hierarchy and factual completeness, not redesign the research, projects, publications, or software pages.
- Keep the homepage simple and non-repetitive: concise identity, the three established research areas, a restrained evidence strip, a three-item Recent Work row (the NeurIPS 2026 multimodal benchmark, MultimodalVA, and the dissertation), and selected peer-reviewed publications.
- Teaching & Mentoring should remain brief and evidence-based. Do not publish mentee names. Use `Autumn 2020` for the Sociology course. Describe teaching areas broadly rather than publishing a highly tailored department-specific course menu.
- Keep GitHub, ResearchGate, and LinkedIn (`sophiaychu`) in the professional-profile metadata when valid; none replaces another.
- Reference Data Archive role is verified as lead developer and platform manager: Yue Chu is fourth author in WHO's recommended platform citation (after the partner PIs), is named in the tutorials, is listed as the RDA representative, manager, and administrator in the data repository, wrote all platform documentation including the user guide, and is the primary contributor and administrator of the GitHub repository. Formal grant role: Key Personnel. The platform currently holds only the São Paulo, Brazil reference deaths; do not imply that pending CHAMPS, COMSA, or MITS data are available.
- CODA role (confirmed by Yue 2026-09-19): core team member who tests multimodal fusion performance, contributes to discussions of model choice, development, and interpretation with recommendations, and coauthors consortium papers. Do not describe it as leading the consortium or its algorithm development.
- Presentation and manuscript author orders can legitimately differ. The 2021 PAA age-at-last-birth presentation lists Hayford, Casterline, Chu; the manuscript lists Casterline, Hayford, Chu. Do not "reconcile" them.

## CV Strategy

- The website CV is the comprehensive public record. Maintain its source at `_CV/Yue_Chu_CV.qmd` and render it directly to `files/Yue_Chu_CV.pdf`.
- TTAP application CVs under the separate `Job 2026/TTAP` workspace are targeted application documents, not the master source for the website CV. They may be shorter or reordered for a specific search, but verified factual updates should be reconciled with the comprehensive website CV.
- The currently served website CV is dated October 13, 2026. Do not describe it with an earlier date.
- The two-page Research Résumé (`_CV/Yue_Chu_Resume.qmd`) targets research-scientist roles. Keep it consistent with the comprehensive CV and limited to verified claims; do not add Nationwide internship details without confirmation.
- Public CV and website mentoring descriptions must omit student names. Keep any identifying names commented out or removed from rendered public output.
- Keep skill claims precise. Core tools are R, Python, Julia, SQL, and Stata (Stata was the main language at JHSPH and for released publication code). Additional experience may include SPSS, RJAGS/JAGS, RNIMBLE/NIMBLE, and JMP, with context where useful. Do not imply that a complete software package was developed in every listed language.

## Current Progress

Completed in the current structure pass:

- Moved nav-owned section content into matching folders
- Added folder-level `index.md` files for all top-level nav sections except Home and CV
- Removed redundant `_pages/` duplicates for nav sections
- Removed the replacement `_data/*.yml` files that had become an extra maintenance surface
- Updated the homepage to use a concise positioning statement, evidence strip, research priorities, and featured publication content
- Merged consulting into projects and removed consulting from the main navigation
- Reframed the research page around the event-to-estimate measurement chain, three established areas, three compact evidence blocks, and a separate understand-to-validate-to-design future agenda
- Reframed Teaching & Mentoring around visible reasoning, reproducible independence, and mentoring toward ownership
- Removed the template blog posts, portfolio examples, demo/archive pages, and generic privacy copy from the public build; `/sitemap/` is now a curated directory of professional content
- Excluded internal maintenance documents, build scripts, generator notebooks, and unused template images from the deployed site; repository guidance such as this file must never be copied into `_site`
- Replaced the homepage programming-language evidence block with research-ownership evidence and prioritized first-, joint-first-, and corresponding-author work

## Known Follow-Ups

- The active served CV is the October 13, 2026 comprehensive Academic CV (content reconciled with the generic TTAP academic CV dated 2026-10-09 and the confirmed multimodal-benchmark status update dated 2026-10-13). Reconcile future verified additions from targeted application CVs without replacing it with a narrower TTAP version.
- MultimodalVA repository link is live on the site ahead of the public release (no later than the week of 2026-09-21); verify it resolves publicly after that week.
- Working-paper statuses and links should be updated only from an authoritative CV or manuscript record.
- The multimodal benchmark is listed as accepted at NeurIPS 2026 with a public medRxiv preprint; Yue Chu is the fourth author and must not be marked as a corresponding author.

## Safe Next Steps

If we continue improving the site, these are good next tasks:

1. Keep the comprehensive website CV synchronized with verified publications, reports, presentations, mentoring, and technical work, then render it directly to `files/Yue_Chu_CV.pdf`.
2. Keep the Research Résumé synchronized with the comprehensive CV after each CV update.
3. Confirm the MultimodalVA repository link resolves publicly after the week of 2026-09-21, and add a documentation link only if a rendered docs site is published.
4. Refresh working-paper status labels as manuscripts move through review.

## GitHub Profile Checklist

Yue's own to-do list for github.com/y-chu. Revisit, do, and check off. The website links only the main GitHub profile, so this profile is what reviewers see.

- [ ] Rewrite the profile README (`y-chu/y-chu`) to match the site positioning: Population Health Scientist & Demographer; three established research areas in one line each; links to the website, CV, and Google Scholar. Remove the emoji list, "multilingual data analyst / scientist / engineer", and the broken "R, Python, Julia, Stata, SPSS, ...." line.
- [ ] Make MultimodalVA public by the week of 2026-09-21 (the site, CV, and résumé already link github.com/y-chu/MultimodalVA). Before flipping to public, check the README (install, quick start, supported models, citation to the dissertation preprint), confirm the license, and remove `build/`, `catboost_info/`, and any data or private results from the repository.
- [ ] Decide whether the RDA code repository can be linked publicly. If it is under a WHO or OSU organization and public, add it to the RDA project and software entries; if private, leave it unlinked.
- [ ] Pin 4-6 repositories: MultimodalVA, the RDA repository (if public), `AfricaAdmin2-U5MR` or `China_5-19COD` (if the code is clean and documented), and `Stats-resource-for-social-science`.
- [ ] Add a README, description, and topics to every pinned repository; add a short description to `AfricaAdmin2-U5MR`, `China_5-19COD`, and `SOC8802_Final`, or archive the ones that are not worth showing.
- [ ] Review `Stats-resource-for-social-science` before pinning: remove the `Some books` folder if it contains copyrighted PDFs, remove `.DS_Store`, and confirm the Stata examples are your own recitation materials. It could then be linked from the Teaching page as teaching evidence.
- [ ] Hide or delete stale forks that dilute the profile (`2019-nCoV`, `covid-19-data`, `Deep_COVID_Exposition`, `Sabaki`, `starter-hugo-academic`, `bilm-tf`, `Model_Omicron_China`, `child_welfare_projections`, `diagnostic-testing`, `pyCrossVA`). Keep a fork only if you contributed changes to it.
- [ ] Decide whether `git_claude_workshop` should stay public and, if so, give it a README that explains the research workflow it demonstrates.
- [ ] Set the profile name, bio ("Population health scientist & demographer"), affiliation, website, and LinkedIn fields.
- [ ] After MultimodalVA is public: confirm the repository URL loads while logged out; enable GitHub Pages for `docs/` if you want a Docs link on the site; add a Zenodo DOI (a `CITATION.cff` already exists).
