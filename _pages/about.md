---
permalink: /
excerpt: "Population health scientist and demographer studying how incomplete health information becomes evidence for public-health decisions."
author_profile: true
redirect_from:
  - /about/
  - /about.html
selected_work:
  - period: "2026"
    theme: "Measurement, reporting, and data quality"
    title: "Information sufficiency in population surveys"
    note: "Identifies which parts of verbal-autopsy interviews preserve the evidence needed for reliable cause-of-death inference, creating a basis for shorter and adaptive instruments while testing whether efficiency introduces new measurement error."
    links:
      - label: "Working-paper record"
        url: "/publication/working-information-sufficiency/"
  - period: "2026"
    theme: "Mortality measurement and health information systems"
    title: "Multimodal AI for cause-of-death assignment"
    note: "Benchmarks narrative-only, symptom-indicator, multimodal, and large-language-model approaches using national South African data, with an open-source workflow for reproducible evaluation."
    links:
      - label: "medRxiv preprint"
        url: "https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1"
      - label: "Code"
        url: "https://github.com/y-chu/MultimodalVA"
  - period: "In preparation"
    theme: "Demographic inference"
    title: "SBH-Bayes: joint estimation from summary birth histories"
    note: "Extends a Bayesian framework co-conceived with Samuel Clark into an independently developed model that jointly estimates fertility and child mortality from compressed birth-history data."
    links:
      - label: "Working-paper record"
        url: "/publication/joint-fertility-child-mortality-summary-birth-histories/"
      - label: "MA thesis"
        url: "https://rave.ohiolink.edu/etdc/view?acc_num=osu1609638415015896"
---

{% assign research_page = site.research | where: "entry_type", "index" | first %}

<div class="home-positioning">
  <p class="page-lead">I am an interdisciplinary population health scientist and demographer working at the intersection of epidemiology and data science. I am currently a Postdoctoral Fellow at the Institute for Population Research at The Ohio State University.</p>
  <p>My research follows the path from a health event to a report, a record, a classification, and ultimately a population estimate. I examine where information is lost or distorted, develop methods to improve measurement and inference, and build software and data infrastructure so those methods can be evaluated and reused. My training spans preventive medicine, public health, sociology, demography, and statistics; my work includes research in resource-limited settings across sub-Saharan Africa and Asia as well as domestic population health research in the United States.</p>
</div>

## Profile Highlights

<div class="evidence-strip evidence-strip--profile" aria-label="Profile highlights">
  <div><strong>Interdisciplinary training</strong><span>Preventive medicine, public health, sociology, demography, and statistics</span></div>
  <div><strong>Research across settings</strong><span>Population-health research in resource-limited settings across Africa and Asia and in the United States, including statewide COVID-19 seroprevalence</span></div>
  <div><strong>Research across disciplines</strong><span>Population health, demography, epidemiology, statistics, and computational social science</span></div>
  <div><strong>Methods translated into infrastructure</strong><span>Research software, data harmonization, APIs, and platforms that support shared and reproducible research</span></div>
</div>

## Current Research Themes

<p>My research program addresses a practical public-health problem: populations most affected by preventable mortality are often those for whom routine data are least complete. I study where information is lost or distorted, how measurement systems can be validated and improved, and how population quantities can still be estimated. This agenda has three connected themes:</p>

<ol class="priorities priorities--lettered">
  {% for direction in research_page.established %}
    <li>
      <span class="priority__title">{{ direction.title }}</span>
      <span class="priority__desc">{{ direction.home_summary }}</span>
    </li>
  {% endfor %}
</ol>

<p>Together, these themes connect applied population-health and demographic research, statistical and computational methods, and research software and data infrastructure. I build infrastructure when answering a research question requires data and methods to remain usable beyond a single analysis.</p>

## Research Keywords

<dl class="keyword-groups">
  <div><dt>Substantive</dt><dd>Demography; population health; epidemiology; mortality; maternal, child, and adolescent health; verbal autopsy; civil registration and vital statistics; resource-limited settings.</dd></div>
  <div><dt>Methods</dt><dd>Bayesian hierarchical models; demographic estimation; survey validation; measurement error; evidence synthesis; natural language processing; machine learning; multimodal learning; large language models.</dd></div>
  <div><dt>Data science &amp; delivery</dt><dd>R, Python, Julia, SQL, and Stata; reproducible pipelines; data integration and harmonization; metadata and DDI; APIs; ODK; secure analytics environments.</dd></div>
</dl>

## Selected Current and Recent Work

<div class="info-rows">
  {% for item in page.selected_work %}
    <article class="info-row">
      <div class="info-row__side">
        <p class="info-row__year">{{ item.period }}</p>
        <p class="info-row__meta">{{ item.theme }}</p>
      </div>
      <div class="info-row__body">
        <h3 class="info-row__title">{{ item.title }}</h3>
        <p>{{ item.note }}</p>
        <p class="inline-links">{% for link in item.links %}<a href="{{ link.url }}">{{ link.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</p>
      </div>
    </article>
  {% endfor %}
</div>

## Contact

- University email: [chu.282@osu.edu](mailto:chu.282@osu.edu)
- Personal email: [ychu612@gmail.com](mailto:ychu612@gmail.com)
