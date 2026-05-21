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
- Profile: `_profile/index.md`
- Research: `_research/index.md`
- Software: `_software/index.md`
- Projects: `_projects/index.md` plus item pages in `_projects/*.md`
- Publications: `_publications/index.md` plus item pages in `_publications/*.md`
- Talks: `_talks/index.md` plus item pages in `_talks/*.md`
- News: `_news/index.md`
- Personal: `_personal/index.md`
- Teaching: `_teaching/index.md` plus item pages in `_teaching/*.md`
- CV route: `_pages/cv.md`
- Served CV file: `files/Yue_Chu_CV.pdf`
- CV source materials: `_CV/`
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
- Used for `profile`, `research`, `software`, `news`, and `personal`
- The section lives in that folder's `index.md`
- Structured lists for that section live in front matter arrays on the same file

2. Collection-backed sections
- Used for `projects`, `publications`, `talks`, and `teaching`
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
- `_talks/index.md`
- `_teaching/index.md`

When filtering collection items, always exclude `entry_type: index`.

## Editing Rules

- When updating a nav section, edit the matching folder first.
- For curated research themes, edit `_research/index.md`.
- For software listings, edit `_software/index.md`.
- For curated news items, edit `_news/index.md`.
- For curated personal sections and fun updates, edit `_personal/index.md`.
- For featured publications used on the home and profile pages, edit `_publications/index.md`.
- For featured talks used on the talks landing page, edit `_talks/index.md`.
- For project cards and project detail pages, edit `_projects/*.md`.
- For consulting and technical assistance entries, create or edit `_projects/*.md` with `project_group: consulting`.
- For publication detail pages, edit `_publications/*.md`.
- For talk detail pages, edit `_talks/*.md`.
- For teaching entries, edit `_teaching/*.md`.

## Publication Schema

Publication entries in `_publications/*.md` should use these fields when available:

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
- Featured papers are stored with the publications landing page because they belong to the publications section.
- Featured talks are stored with the talks landing page because they belong to the talks section.
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

- Some talk item permalinks still end with `.md` in `_talks/*.md`; this is functional but not especially polished.
- Some talk front matter uses inconsistent `collection` labels such as `Presentation` or `Poster`; the pages still render, but normalization would be a good cleanup pass.
- If desired later, Home could also be moved to a dedicated `_home/index.md` pattern for total symmetry.

## Safe Next Steps

If we continue improving the site, these are good next tasks:

1. Normalize talk permalinks to cleaner URLs.
2. Normalize talk front matter fields across all talk entries.
3. Decide whether news should stay curated in one file or become one-file-per-update with a custom non-output workflow.
4. Add a lightweight maintenance note to the README pointing editors to `CLAUDE.md`.
