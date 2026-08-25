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
- CV route: `_pages/cv.md`

Primary and secondary navigation are defined in `_data/navigation.yml`. The primary job-market navigation is Research, Publications, Projects, Software, Teaching & Mentoring, and CV. Presentations, News, and Personal are secondary/footer links.
- Served CV file: `files/Yue_Chu_CV.pdf`
- CV source materials: `_CV/`
- CV build command (outputs the source directly to the served file, so no manual copy/drift):
  `quarto render _CV/Yue_Chu_CV.qmd --output-dir ../files`
- Legacy consulting route: `_pages/consulting.md` redirects to the consulting section on `/projects/`

## Core Principle

If a section appears in the main website navigation, there should be one obvious matching folder where its content is maintained.

That means:

- Do keep nav-owned content in its matching folder.
- Do not scatter the same section across `_pages/` and `_data/` unless there is a strong technical reason.
- Do not create duplicate routed pages for nav sections in `_pages/` if a folder-backed version already exists.

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

- `publication_type`: `peer_reviewed`, `working_paper`, `dissertation`, `thesis`, or `report`
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
- The CV remains a direct PDF experience. `/cv/` redirects to `files/Yue_Chu_CV.pdf`.
- Publication records live in the publications collection; homepage selections use `featured: true`.
- Presentations remain available as a secondary/footer destination, with legacy `/talks/` routes redirected to `/presentations/`.
- Teaching & Mentoring is a primary-navigation page backed by `_teaching/index.md`.
- Consulting is no longer a standalone navigation tab; consulting and technical assistance work now lives inside the projects collection.
- Research, news, and personal currently use single landing files with front matter arrays instead of one-file-per-item. This keeps the nav-to-folder mapping clean without generating unwanted extra pages.

## Current Progress

Completed in the current structure pass:

- Moved nav-owned section content into matching folders
- Added folder-level `index.md` files for all top-level nav sections except Home and CV
- Removed redundant `_pages/` duplicates for nav sections
- Removed the replacement `_data/*.yml` files that had become an extra maintenance surface
- Updated the homepage to read featured research and publication content from the new folder-backed sources
- Merged consulting into projects and removed consulting from the main navigation

## Known Follow-Ups

- The active served CV remains the April 1, 2026 version until a newer job-market CV is added.
- No Research Résumé is currently present, so the site exposes only the Academic CV.
- MultimodalVA has no verified public repository or documentation URL; keep the private-repository status until a public release exists.
- Working-paper statuses and links should be updated only from an authoritative CV or manuscript record.

## Safe Next Steps

If we continue improving the site, these are good next tasks:

1. Replace `files/Yue_Chu_CV.pdf` when the next dated job-market CV is ready.
2. Convert `/cv/` into a two-document landing page if a Research Résumé is added.
3. Add verified repository or documentation links when MultimodalVA or RDA packages become public.
4. Refresh working-paper status labels as manuscripts move through review.
