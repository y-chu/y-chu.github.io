---
permalink: /
excerpt: "Population health scientist and demographer studying how incomplete health information becomes evidence for public-health decisions."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% assign research_page = site.research | where: "entry_type", "index" | first %}

<div class="home-positioning">
  <p class="page-lead">I am an interdisciplinary population health scientist and demographer at the intersection of epidemiology and data science, and a Postdoctoral Fellow at The Ohio State University's Institute for Population Research.</p>
  <p>I study how health events become population evidence—from reports and records through evidence integration, classification, and population inference to public-health decisions. I develop and validate methods for maternal, newborn, child, and adolescent health; mortality and disease burden; and epidemic measurement, supported by reusable software and data infrastructure.</p>
</div>

## Profile Highlights

<div class="evidence-strip evidence-strip--profile" aria-label="Profile highlights">
  <div><strong>Interdisciplinary expertise</strong><span>Bridging preventive medicine, public health, sociology, demography, applied statistics, and data science</span></div>
  <div><strong>Methods, application &amp; translation</strong><span>Developing and validating statistical methods, applying them to real-world population-health problems, and translating evidence into practice and decision-making</span></div>
  <div><strong>Cross-context research delivery</strong><span>Designing and executing collaborative population-health research across Asia, Africa, Latin America, and the United States</span></div>
  <div><strong>Research infrastructure leadership</strong><span>Leading the full lifecycle of production research systems—from architecture and protocol design to development, governance, and sustained operations</span></div>
</div>

## Current Research Themes

<p>My research program addresses a practical public-health problem: populations most affected by preventable mortality are often those for whom routine data are least complete. It connects substantive epidemiology with research on how information is produced, combined, validated, and used for population inference. This agenda has three connected themes:</p>

<ol class="priorities priorities--lettered priorities--home">
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
  <div><dt>Substantive</dt><dd>Demography; population health; epidemiology; mortality and disease burden; maternal, newborn, child, and adolescent health; epidemic measurement; verbal autopsy; civil registration and vital statistics; resource-limited settings.</dd></div>
  <div><dt>Methods</dt><dd>Bayesian hierarchical models; demographic estimation; survey validation; measurement error; evidence synthesis; natural language processing; machine learning; multimodal learning; large language models.</dd></div>
  <div><dt>Data science &amp; delivery</dt><dd>R, Python, Julia, SQL, and Stata; reproducible pipelines; data integration and harmonization; metadata and DDI; APIs; ODK; secure analytics environments.</dd></div>
</dl>

## Contact

- University email: [chu.282@osu.edu](mailto:chu.282@osu.edu)
- Personal email: [ychu612@gmail.com](mailto:ychu612@gmail.com)
