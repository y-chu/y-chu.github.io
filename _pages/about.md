---
permalink: /
excerpt: "Population health scientist and demographer working on population measurement under incomplete, heterogeneous, and imperfect information."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
recent_work:
  - year: "2026"
    label: "Preprint · medRxiv"
    title: "Multimodal Artificial Intelligence for Cause-of-Death Assignment From Verbal Autopsy Records: A National Benchmark Study in South Africa"
    note: "A national benchmark of narrative, structured-data, multimodal, and large-language-model approaches to cause-of-death assignment from verbal autopsy records."
    links:
      - label: "medRxiv"
        url: "https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1"
      - label: "GitHub"
        url: "https://github.com/y-chu/MultimodalVA"
      - label: "Project page"
        url: "/projects/multimodalva/"
  - year: "2026"
    label: "Open-source software"
    title: "MultimodalVA"
    note: "Python package implementing narrative, structured-data, and multimodal cause-of-death classifiers."
    links:
      - label: "GitHub"
        url: "https://github.com/y-chu/MultimodalVA"
      - label: "Project page"
        url: "/projects/multimodalva/"
  - year: "2025"
    label: "PhD dissertation · arXiv"
    title: "Leveraging Language Models and Machine Learning in Verbal Autopsy Analysis"
    note: "Language models and multimodal learning for cause-of-death classification from verbal autopsy narratives and questionnaire data."
    links:
      - label: "arXiv"
        url: "https://arxiv.org/abs/2508.19274"
---

{% assign research_page = site.research | where: "entry_type", "index" | first %}
{% assign peer_reviewed_publications = site.publications | where: "publication_type", "peer_reviewed" %}
{% assign featured_publications = peer_reviewed_publications | where: "featured", true | sort: "publication_order" %}

<div class="home-positioning">
  <h1 class="home-positioning__title">Population Health Scientist &amp; Demographer</h1>
  <p class="page-lead">I study how to measure population health when information is incomplete, heterogeneous, or imperfect, combining demographic, statistical, computational, and AI methods with research software and data infrastructure.</p>
  <div class="link-row link-row--home">
    <a class="link-chip" href="/research/">Research</a>
    <a class="link-chip" href="/publications/">Publications</a>
    <a class="link-chip" href="/files/Yue_Chu_CV.pdf">Full academic CV</a>
    <a class="link-chip" href="/files/Yue_Chu_Resume.pdf">2-page résumé</a>
  </div>
</div>

## Research Directions

<ul class="priorities">
  {% for direction in research_page.established %}
    <li>
      <span class="priority__title">{{ direction.title }}</span>
      <span class="priority__desc">{{ direction.home_summary }}</span>
    </li>
  {% endfor %}
</ul>

<div class="evidence-strip" aria-label="Selected evidence">
  <a href="/publications/"><strong>{{ peer_reviewed_publications.size }} peer-reviewed publications</strong><span>including first-, joint-first-, and corresponding-author work</span></a>
  <a href="/publications/"><strong>Lead-authored population evidence</strong><span>first, joint-first, and corresponding-author research</span></a>
  <a href="/projects/reference-data-archive/"><strong>WHO Reference Data Archive</strong><span>platform manager and core developer</span></a>
  <a href="/publication/Chu2024_ALPHA"><strong>9 surveillance sites, 6 countries</strong><span>multi-site mortality analysis, first author</span></a>
</div>

## Background

I am a Postdoctoral Fellow at the Institute for Population Research at The Ohio State University. I hold a PhD in Sociology with a minor in Statistics and Demography from Ohio State, an MSPH in Population, Family and Reproductive Health from the Johns Hopkins Bloomberg School of Public Health, and a Bachelor of Medicine in Preventive Medicine from Fudan University. I work with WHO, the Africa Health Research Institute, and international research consortia on mortality measurement, verbal autopsy, and research data infrastructure.

## Recent Work

<div class="info-rows">
  {% for item in page.recent_work %}
    <article class="info-row">
      <div class="info-row__side">
        <p class="info-row__year">{{ item.year }}</p>
        <p class="info-row__meta">{{ item.label }}</p>
      </div>
      <div class="info-row__body">
        <h3 class="info-row__title">{{ item.title }}</h3>
        <p>{{ item.note }}</p>
        <div class="link-row">{% for link in item.links %}<a class="link-chip" href="{{ link.url }}">{{ link.label }}</a>{% endfor %}</div>
      </div>
    </article>
  {% endfor %}
</div>

## Selected Publications

<div class="info-rows">
  {% for paper in featured_publications limit: 4 %}
    <article class="info-row">
      <div class="info-row__side">
        {% if paper.publication_year %}<p class="info-row__year">{{ paper.publication_year }}</p>{% endif %}
        {% if paper.venue %}<p class="info-row__meta">{{ paper.venue }}</p>{% endif %}
      </div>
      <div class="info-row__body">
        <h3 class="info-row__title">{{ paper.title }}</h3>
        {% if paper.authors %}<p class="info-row__meta publication-authors">{{ paper.authors }}</p>{% endif %}
        {% if paper.venue_details %}<p>{{ paper.venue_details }}</p>{% endif %}
        {% include publication-links.html publication=paper %}
      </div>
    </article>
  {% endfor %}
</div>

<p><a href="/publications/">Browse all publications</a></p>

## Contact

- University email: [chu.282@osu.edu](mailto:chu.282@osu.edu)
- Personal email: [ychu612@gmail.com](mailto:ychu612@gmail.com)
