# Yue Chu — academic website

Source for [y-chu.github.io](https://y-chu.github.io), an Academic Pages/Jekyll
site presenting Yue Chu's research, publications, projects, software, teaching,
presentations, and public CV.

Before editing content or layout, read [`CLAUDE.md`](CLAUDE.md). It contains the
current research framing, information architecture, factual boundaries, page
design decisions, and release checklist. `AGENT.md` is only a pointer to that
guide.

## Local preview

```bash
bundle exec jekyll serve -l -H localhost
```

The site is then available at `http://localhost:4000`.

## Build and validation

```bash
bundle exec jekyll build
ruby scripts/check_internal_links.rb _site
git diff --check
```

## CV and research resume

The editable sources are `_CV/Yue_Chu_CV.qmd` and
`_CV/Yue_Chu_Resume.qmd`. Render directly to the public `files/` directory:

```bash
quarto render _CV/Yue_Chu_CV.qmd --output-dir ../files
quarto render _CV/Yue_Chu_Resume.qmd --output-dir ../files
```

Visually inspect the rendered PDFs before release. Do not manually maintain a
second copy of either PDF.

## Release policy

Keep the site compatible with GitHub Pages. Do not deploy, commit, stage, or
push changes unless Yue explicitly requests it.
