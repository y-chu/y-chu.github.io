# AGENT.md

## Objective

Upgrade an existing **AcademicPages (Jekyll + GitHub Pages)** personal academic website to a more modern research-oriented layout with:

- A **research overview page** (Zehang Li–style)
- A **projects index + individual project pages** (Zhenke Wu–style)
- A **cleaner homepage with improved hierarchy**

The site must remain compatible with **GitHub Pages constraints** (no unsupported plugins, static build only).

---

## Environment Context

- Framework: **Jekyll (AcademicPages / Minimal Mistakes fork)**
- Hosting: **GitHub Pages**
- Content format: Markdown + YAML front matter
- Rendering: Liquid templates
- Build constraint: Only GitHub Pages–supported plugins allowed

---

## High-Level Tasks

### 1. Fix CV Page

Update the current CV page so it directly opens the PDF instead of sending visitors to a GitHub link.

**Behavior:**
- `/cv/` should resolve directly to the hosted PDF asset
- Keep navigation label as “CV”
- Preserve a clean user flow for downloading or opening the PDF in-browser

---

### 2. Add Research Page

Create a structured research overview page.

**File:**
```
_pages/research.md
```

**Requirements:**
- Render 4–6 research themes
- Each theme includes:
  - title
  - short description (2–4 sentences)
  - keywords/tags
  - optional links
- Layout should support card/grid display
- Add a section for selected publications
- Each selected publication should include:
  - short blurb
  - downloadable paper link
  - GitHub link for code and/or data when available

**Data source (preferred):**
```
_data/research.yml
```

---

### 3. Add Projects Collection

Create a Jekyll collection for projects.

**Update `_config.yml`:**
```yaml
collections:
  projects:
    output: true
    permalink: /projects/:path/
```

**Directory:**
```
_projects/
```

Each project file must include front matter:
```yaml
---
title: "Project Title"
excerpt: "1–2 sentence summary"
date: 2025-01-01
status: ongoing
tags: [LLM, Bayesian, Global Health]
links:
  - label: "Paper"
    url: ""
  - label: "Code"
    url: ""
---
```

---

### 4. Create Projects Index Page

**File:**
```
_pages/projects.md
```

**Behavior:**
- Automatically iterate through `site.projects`
- Display:
  - title
  - short description
  - tags
  - link to project page

---

### 5. Add Talks Page

Create a page for selected presentations and talks.

**File:**
```
_pages/talks.md
```

**Behavior:**
- Highlight selected invited talks, conference presentations, workshops, or guest lectures
- Each item should support:
  - title
  - venue/event
  - date
  - short description or takeaway
  - optional slides/video/recording link

**Preferred approach:**
- Reuse existing talks content if already present in the site
- If needed, create a lightweight data source for selected talks

---

### 6. Add News Page

Create a page for academic and professional updates.

**File:**
```
_pages/news.md
```

**Behavior:**
- Display news items in reverse chronological order
- Support concise updates such as papers, awards, talks, grants, teaching, collaborations, or media mentions
- Keep the layout lightweight and easy to update

**Data source (preferred):**
```
_data/news.yml
```

---

### 7. Add Personal Page

Create a page about personal interests and fun updates outside formal research.

**File:**
```
_pages/personal.md
```

**Behavior:**
- Introduce hobbies, interests, side projects, travel, photos, or other light personal content
- Include a “fun news” or life updates section
- Keep tone warm and human while still fitting the broader academic site

---

### 8. Improve Homepage

Modify:
```
_pages/about.md
```

**Changes:**
- Shorten biography (≤150 words intro)
- Add:
  - research statement (2–3 lines)
  - links: CV / Google Scholar / GitHub
- Add section:
  - “Selected Research Areas” (link to research page)
  - “Selected Projects” (link to projects)
  - quick links to talks, news, and personal page if they improve navigation

---

### 9. UI / Layout Enhancements

Override theme defaults where needed.

**Edit or create:**
```
_layouts/
_includes/
assets/css/custom.scss
```

**Add components:**
- `research-card.html`
- `project-card.html`
- `publication-card.html`
- `news-item.html`
- `talk-card.html`

**Styling goals:**
- clean academic look
- grid-based layout
- subtle borders (no heavy shadows)
- responsive design
- restrained color palette

---

## Constraints

- Do NOT introduce unsupported Jekyll plugins
- Do NOT break existing collections (publications, talks, etc.)
- Maintain compatibility with GitHub Pages build system
- Preserve existing URLs where possible

---

## Preferred Implementation Patterns

### Research (data-driven)
```
_data/research.yml → rendered via include
```

### News (data-driven)
```
_data/news.yml → rendered via include or page loop
```

### Projects (collection-driven)
```
_projects/*.md → auto-indexed
```

### Layout reuse
- Use includes for repeatable UI components
- Avoid duplicating HTML

---

## Example Research YAML

```yaml
- title: "AI for Population Health"
  description: "Developing multimodal ML models for population health insights."
  tags: ["LLM", "Multimodal", "Health Data"]

- title: "Data Quality in Surveys"
  description: "Measuring and modeling information sufficiency in survey and surveillance systems."
  tags: ["Survey Methods", "Data Quality"]
```

---

## Example Include (Project Card)

```html
<div class="project-card">
  <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
  <p>{{ project.excerpt }}</p>
  <div class="tags">
    {% for tag in project.tags %}
      <span class="tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>
```

---

## Acceptance Criteria

- `/cv/` opens the PDF directly
- `/research/` page exists and renders structured themes
- `/research/` includes selected publications with downloadable links and code/data links where available
- `/projects/` page lists all projects dynamically
- Each project has its own page
- `/talks/` page exists and highlights selected presentations
- `/news/` page exists and displays updates cleanly
- `/personal/` page exists and presents personal interests/fun updates
- Homepage is visually cleaner and shorter
- Site builds successfully on GitHub Pages
- No broken links or layout regressions

---

## Non-Goals

- Do NOT migrate away from Jekyll
- Do NOT introduce React/Vue or dynamic frameworks
- Do NOT redesign publications/talks sections unless necessary

---

## Execution Strategy

1. Create new pages and collections
2. Add minimal working layouts
3. Populate with placeholder content
4. Apply styling improvements
5. Refactor for reuse and cleanliness

---

## Notes for Codex

- Prefer **small, atomic commits**
- Validate Liquid syntax carefully (common failure point)
- Test locally with:
  ```
  bundle exec jekyll serve
  ```
- Ensure compatibility with GitHub Pages build pipeline
