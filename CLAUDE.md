# Website editorial and maintenance guide

This is the current source of truth for Codex, Claude, and manual maintenance
of Yue Chu's academic website. It supersedes earlier redesign notes, including
the historical card/grid plan that previously lived in `AGENT.md`.

## Technical foundation

- Jekyll / Academic Pages / Minimal Mistakes, hosted on GitHub Pages.
- Keep the site static and compatible with GitHub Pages; do not add unsupported
  plugins or unnecessary build systems.
- Preserve public URLs when practical.
- Reusable rendering belongs in `_includes/`; shared styling belongs in the
  existing Sass structure.
- Folder landing pages inside collections use `entry_type: index`; archive
  loops must exclude those records.

## Content ownership

Each navigation section has one obvious source:

- Home: `_pages/about.md`
- Research: `_research/index.md`
- Publications: `_publications/index.md` and `_publications/*.md`
- Projects: `_projects/index.md` and `_projects/*.md`
- Software: `_software/index.md` and `_software/*.md`
- Teaching & Mentoring: `_teaching/index.md`
- Presentations: `_presentations/index.md`
- News: `_news/index.md`
- Personal: `_personal/index.md`
- Navigation: `_data/navigation.yml`
- Academic CV source: `_CV/Yue_Chu_CV.qmd`; served PDF:
  `files/Yue_Chu_CV.pdf`
- Research-resume source: `_CV/Yue_Chu_Resume.qmd`; served PDF:
  `files/Yue_Chu_Resume.pdf`

Do not create duplicate routed pages or parallel `_data` copies for these
sections. Presentations, News, and Personal remain secondary/footer
destinations. The primary job-market navigation is Research, Publications,
Projects, Software, Teaching & Mentoring, and CV.

## Audience and identity

The site presents one coherent identity to tenure-track and research-scientist
audiences in sociology, demography, population/public health, epidemiology,
survey methodology, computational social science, and adjacent applied
research settings. Do not create separate versions of the site for those
markets and do not frame the site as an industry data-science portfolio.

The central research problem is:

> How incomplete and imperfect health information becomes population evidence,
> and how measurement, validation, classification, and inference can be
> improved along the way.

The event-to-estimate backbone is:

**health event → report → record → classification → population estimate**

Use the strongest accurate framing. Make intellectual ownership, public-health
importance, demographic contribution, methodological work, and infrastructure
leadership visible. Strong framing never permits inflated authorship, status,
deployment, impact, funding, or independence claims.

The site is a broad professional profile that may be read by faculty,
collaborators, research organizations, and recruiters. It is not a substitute
for a position-specific application. Present a durable research identity and
enough concrete evidence for different readers to understand both scientific
leadership and collaborative range.

## Research architecture

Use these three scientific themes, in this order, consistently on the homepage,
Research page, and Publications page:

1. **Measurement, Reporting, and Data Quality**
   - How respondent, interviewer, instrument, collection mode, and institutional
     processes create omission, displacement, misclassification, and other bias.
   - Includes survey validation, birth/death reporting, information sufficiency,
     and adaptive questioning.

2. **Mortality Measurement, Validation, and Health Information Systems**
   - How mortality-measurement tools are designed, validated, monitored, and
     integrated into operational public-health systems.
   - Includes verbal autopsy, multimodal cause-of-death inference, MITS,
     validation and transportability, monitoring and evaluation, and integration
     with civil registration and vital statistics (CRVS).

3. **Demographic Inference Under Incomplete and Misclassified Data**
   - How fertility, mortality, and cause-of-death quantities are estimated when
     events are incompletely observed, selectively reported, or imperfectly
     classified.
   - Includes SBH-Bayes and its SVD-Bayes foundation, summary birth histories,
     fertility schedules, mortality estimation, uncertainty propagation, and
     evidence across survey, surveillance, registration, and modeled-data
     environments.

Misclassification studies connect Themes 1 and 3: the first explains how error
arises; the third asks how it changes population estimates. Assign each output
to one primary theme on the Publications page rather than duplicating it.

### Evidence selection and contribution framing

Define each theme by its scientific questions, then choose a portfolio of
evidence that supports that identity. Do not rank every output mechanically by
sole ownership, authorship position, journal prestige, or recency. Across the
site, the strongest evidence mix usually includes:

- a current or emerging agenda that shows intellectual direction and growing
  leadership;
- established lead-authored or otherwise substantial contributions that show
  the ability to deliver research; and
- selected collaborations that demonstrate methodological breadth, work on
  consequential studies, and cross-country or cross-institutional execution.

Substantive collaborative contributions are useful evidence of potential even
when they do not establish complete independence. Keep them visible, but do
not let them carry an inaccurate claim of sole leadership. Conversely, do not
use ownership as the only reason to feature a weaker or less relevant example.
Select the combination that best explains the research identity of each theme,
then describe Yue's contribution with calibrated language.

For the summary-birth-history work, distinguish two stages accurately. The
original SVD-Bayes thesis study was co-conceived with Samuel Clark, including
the Bayesian framework and simulation-first strategy. The current SBH-Bayes
extension is being independently developed by Yue through a reformulated
likelihood, redesigned analysis, broader research questions, continued data
processing, and tests of modeling assumptions. This is evidence of a
collaborative foundation developing into an independently extended research
agenda; do not describe the original study as solely conceived by Yue.

The 2023 <em>Journal of Global Health</em> provider–mother study and the 2022
<em>Annals of Applied Statistics</em> child-mortality study remain relevant
collaborative evidence. Yue contributed to study design in the former and to
early analysis design in the latter, but did not lead their later analysis and
drafting. They may demonstrate substantive contribution, methodological range,
and collaborative execution; they should not be framed as Yue-led flagship
projects.

Applied research, methods, and infrastructure are cross-cutting modes of work,
not additional scientific themes:

- **Applied population health and demography:** consequential measurement,
  surveillance, and estimation problems in real health-data systems.
- **Statistical and computational methods:** bias assessment, validation,
  multimodal classification, demographic estimation, and uncertainty.
- **Data and research infrastructure:** reusable software, harmonized data,
  metadata, APIs, secure environments, and platforms for sustained research.

Research software and data infrastructure should therefore appear in a
cross-cutting `Research Approach` section and on the Software page. They should
not replace one of the three scientific research themes.

Do not create a section titled `Research Trajectory` or a separate speculative
future-agenda block. Instead, use one natural paragraph explaining the linked
sequence of current questions:

**bias enters data → information sufficiency → validation and transportability
→ instrument/system redesign → population inference**

Describe emerging work with language such as `current work examines`, `creates
a basis for`, and `the next question is`. Do not promise future grants,
deployment, impact, products, or timelines. Adaptive questioning and MITS are
ongoing research; distinguish preliminary/presented work from completed
validation or operational use.

## Page-specific decisions

### Homepage

- Begin with a short self-introduction, not a large occupational-title banner.
- Use `Population Health Scientist · Demographer · Epidemiologist · Data
  Scientist` as the compact identity line beneath the profile photo. In prose,
  lead with `interdisciplinary population health scientist and demographer`
  and describe epidemiology and data science as intersecting fields.
- Make interdisciplinary training, work across resource-limited and domestic
  settings, public-health relevance, and the applied/method/infrastructure span
  visible. Do not define the whole profile through global health alone.
- Use a restrained profile-highlights block and substantive/method/toolkit
  keywords. Avoid redundant publication counts and authorship counts.
- Show the three research themes in compact form, drawing their names and
  summaries from `_research/index.md`.
- Selected work should represent the three themes, not three versions of one
  MultimodalVA study.
- Do not add redundant buttons to pages already available in the primary nav.

### Research

- Provide substantially more information than the homepage.
- For each theme: substantive motivation, central questions, established work,
  current/ongoing work, and a short list of directly linked outputs.
- Include a small number of real figures only when they explain a finding or
  method. Avoid decorative diagrams and dense card layouts.
- End with `Research Approach`, covering applied work, methods, and
  infrastructure. The linked sequence of current questions appears as prose,
  without a `Research Trajectory` heading.

### Publications

- Organize the portfolio by the same three research themes, followed by a small
  additional-collaborations section when useful.
- Within themes, put relevant preprints and working papers before older
  peer-reviewed evidence so recent production remains visible.
- The paper title links directly to the DOI, journal, preprint, or authoritative
  paper page. Add a separate link only for useful code/data.
- Use a compact, borderless paper grid with high information density. Use real
  paper figures selectively; otherwise use a quiet year/venue fallback.
- Do not reproduce the CV's chronological list or create unnecessary detail
  pages for papers that already have an authoritative external page.

### Projects

- Use vertical lists under `Active Projects`, `Past Research Projects`, and
  `Consulting and Technical Assistance`.
- Do not show status or topical tag rows on the project index. The section
  heading already states status; keep outputs as inline links rather than
  tag-like buttons.
- MultimodalVA is software, not a project.
- The ALPHA Network verbal-autopsy dataset is a past ALPHA research output.
- The provider–mother interaction article is not an output of the Guinea-Bissau
  verbal-autopsy technical-assistance project; do not link them.

### Software

- Use vertical entries organized as Problem, Deployment/Use, Capabilities, and
  Related Outputs.
- Describe delivered capabilities (ingestion, integration, harmonization,
  validation, metadata, APIs, access, analysis), not a list of technologies.
- Technology tags may show language/method stack. Do not repeat `my role` on
  every entry.
- Link RDA to the full `https://github.com/RDAORG` organization rather than
  presenting individual packages as the whole platform.

### Presentations

- Keep one secondary `/presentations/` page; do not create a second talks page.
- Curate invited talks/seminars, Yue-presented conference work, and selected
  collaborative presentations. Explicitly identify work presented by a coauthor
  or first author.
- The academic CV remains the comprehensive and authoritative record.

### CV and resume

- The website CV is the comprehensive public record, not a tailored TTAP CV.
- Use `Preprints and Working Papers` before peer-reviewed articles; retain the
  precise status in each entry.
- Dissertations and theses belong under Education with links, rather than as a
  publications section once their related manuscripts are represented.
- A short research resume may be linked from the homepage but does not receive
  its own primary-navigation slot.
- A verified WHO contractor appointment may appear separately in the CV; it
  does not need homepage emphasis.
- Render PDFs directly to `files/` after source changes and visually verify them.

## Publication metadata and verified claim boundaries

Publication records may use:

- `publication_type`: `peer_reviewed`, `preprint`, `manuscript`,
  `working_paper`, `dissertation`, `thesis`, or `report`
- `publication_status`: the precise verified state; never infer or upgrade it
- `publication_order`, `publication_year`, `authors`, `venue_details`
- `paper_page_url`, `doi`, `doi_url`, `pdf_url`, `code_url`, `poster_url`
- `thumbnail` and `thumbnail_alt` for a genuinely informative figure
- `paperurl` may remain for compatibility with older helpers

Verified high-risk records:

- **Multimodal Artificial Intelligence for Cause-of-Death Assignment From
  Verbal Autopsy Records: A National Benchmark Study in South Africa** is a
  public 2026 medRxiv preprint, DOI `10.64898/2026.10.15.26364476`, submitted for
  publication. Yue Chu is first and corresponding author.
- **A Multimodal Benchmark for Evaluating Cause-of-Death Inference Using Child
  Health and Mortality Data** is a separate 2026 medRxiv preprint, DOI
  `10.64898/2026.07.13.26357980`. Its NeurIPS 2026 ED Track record is a poster
  presented by the first author. Yue Chu is fourth author and is not a
  corresponding author. Do not call NeurIPS the paper's publication venue.
- MultimodalVA is a public MIT-licensed Python package with a Zenodo release.
- Public RDA role wording: `platform manager and core developer; co-lead of
  software development with the Africa Health Research Institute; sole data
  manager`. Do not collapse this into the stronger and less precise `lead
  developer` claim.
- RDA timeline: the funded project runs 2022--2026, but Yue's documented pilot
  contribution began in 2023 and continued through May 2025 at Ohio State. Her
  formal WHO contractor role began in June 2025 and continues to the present.
  Do not use the 2022 grant start as Yue's personal work or WHO appointment
  start date.
- The ALPHA catalogue record may state: `one of four named primary investigators
  in the catalogue record`; access status is `Data product · licensed access`.
- Do not infer corresponding authorship, presenter identity, grant PI status,
  deployed impact, or public availability from collaboration alone.

## Design and writing rules

- Aim for a clean academic site with high information density, strong
  typography, restrained color, and readable whitespace.
- Prefer natural vertical reading. Avoid heavy boxes, excessive pills/tags,
  redundant buttons, decorative dashboards, and low-information grids.
- Use hierarchy and thin rules instead of shadows and ornament.
- Preserve responsive behavior and check desktop and narrow mobile widths.
- Homepage establishes identity; Research explains the program; Publications
  supplies evidence; Projects shows research settings; Software shows durable
  delivery; CV supplies the complete record. Do not repeat the same paragraph
  across all six surfaces.
- Use direct, substantive language. Avoid generic claims such as `innovative`,
  `impactful`, or `cutting-edge` when evidence can be named instead.

## Validation before release

1. Build the Jekyll site successfully.
2. Run `ruby scripts/check_internal_links.rb _site`.
3. Check that all publication paths listed on the Publications page resolve.
4. Search for retired research-theme titles and obsolete factual notes.
5. Check homepage, Research, Publications, Projects, Software, and
   Presentations at desktop and mobile widths.
6. Run `git diff --check` and inspect the final diff.
7. Do not deploy, commit, stage, or push unless Yue explicitly requests it.
