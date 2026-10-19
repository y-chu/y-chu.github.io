---
layout: single
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Research on population measurement under incomplete and imperfect information."
entry_type: index
established:
  - title: "Population Inference with Incomplete and Heterogeneous Data"
    slug: "population-inference"
    home_summary: "Demographic, statistical, computational, and AI approaches for more reliable population estimates from incomplete, uneven, and heterogeneous evidence."
    summary: "I develop demographic, statistical, computational, and AI approaches that turn incomplete and uneven observations into population estimates with interpretable uncertainty."
    links:
      - label: "Selected evidence"
        url: "#inference-evidence"
      - label: "Publications"
        url: "/publications/"
  - title: "Measurement Processes and Data Quality"
    slug: "measurement-processes"
    home_summary: "How data collection, reporting, and classification processes shape the quality, comparability, and interpretation of population evidence."
    summary: "I treat measurement error as an outcome to be explained: how interviews, reporting, recording, and classification processes shape the evidence used for demographic and health inference."
    links:
      - label: "Selected evidence"
        url: "#measurement-evidence"
      - label: "Projects"
        url: "/projects/"
  - title: "Computational Research Tools and Data Infrastructure"
    slug: "research-infrastructure"
    home_summary: "Reusable research software and data infrastructure for reproducible analysis, collaborative research, and translation into practice."
    summary: "I translate methods into reusable software and data systems that support reproducible analysis, multi-institutional collaboration, and implementation in global health research."
    links:
      - label: "Selected evidence"
        url: "#infrastructure-evidence"
      - label: "Software"
        url: "/software/"
evidence:
  - area: "Population inference"
    slug: "inference-evidence"
    title: "From incomplete observations to population estimates"
    summary: "My work spans Bayesian and demographic estimation, mortality surveillance, and AI-assisted cause-of-death inference. It includes first- and joint-first-author studies of mortality across six African countries, India, and China, alongside a dissertation on language models and multimodal learning for verbal autopsy."
    links:
      - label: "First-author multi-country study"
        url: "/publication/Chu2024_ALPHA"
      - label: "Dissertation and arXiv preprint"
        url: "https://arxiv.org/abs/2508.19274"
      - label: "All publications"
        url: "/publications/"
  - area: "Measurement processes"
    slug: "measurement-evidence"
    title: "Making information loss and reporting error visible"
    summary: "Validation studies in Guinea-Bissau and Malawi show how survey interactions and classification processes can distort mortality measurement. Current work extends this logic to information sufficiency: identifying which parts of an interview preserve the evidence needed for reliable inference."
    links:
      - label: "Survey validation study"
        url: "/publication/helleringer-2020-neonatal-mortality-bias/"
      - label: "Information sufficiency"
        url: "/publication/working-information-sufficiency/"
  - area: "Research infrastructure"
    slug: "infrastructure-evidence"
    title: "Turning methods into durable research infrastructure"
    summary: "I am platform manager and core developer of the WHO-hosted Reference Data Archive, co-leading software development with the Africa Health Research Institute, and the developer of MultimodalVA. These systems make mortality reference data and multimodal cause-of-death workflows more reusable, auditable, and accessible to research teams."
    links:
      - label: "WHO Reference Data Archive"
        url: "/projects/reference-data-archive/"
      - label: "MultimodalVA"
        url: "/projects/multimodalva/"
      - label: "Software"
        url: "/software/"
future_agenda:
  title: "Advancing Population Measurement under Imperfect Information"
  intro: "My next stage of work moves from diagnosing measurement problems to validating and designing better measurement, while keeping completed contributions distinct from future directions."
  themes:
    - title: "Understand information, error, and uncertainty"
      summary: "Examine what population data capture and miss, how error arises in reporting and classification, and how uncertainty should carry through to estimates."
    - title: "Validate measurement across populations and settings"
      summary: "Test whether statistical and AI-based measurement tools perform reliably and equitably across populations, settings, and data sources."
    - title: "Design more effective and equitable measurement strategies"
      summary: "Use that evidence to improve data collection and analysis under limited resources and to better represent under-measured populations."
---

<div class="page-intro">
  <p class="page-lead">My research asks how a health event becomes a report, a record, a classification, and ultimately a population estimate—and where information is lost or distorted along that chain.</p>
  <p>This perspective connects demographic estimation, survey validation, cause-of-death inference, and research infrastructure within one program of population measurement under incomplete and imperfect information.</p>
</div>

## Established Research

<ol class="priorities">
  {% for item in page.established %}
    <li id="{{ item.slug }}">
      <span class="priority__title">{{ item.title }}</span>
      <span class="priority__desc">{{ item.summary }}</span>
      <span class="research-area__work">{% for link in item.links %}<a href="{{ link.url }}">{{ link.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</span>
    </li>
  {% endfor %}
</ol>

## Selected Evidence

<div class="info-rows">
  {% for item in page.evidence %}
    <article class="info-row" id="{{ item.slug }}">
      <div class="info-row__side"><p class="info-row__meta">{{ item.area }}</p></div>
      <div class="info-row__body">
        <h3 class="info-row__title">{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
        <div class="link-row">{% for link in item.links %}<a class="link-chip" href="{{ link.url }}">{{ link.label }}</a>{% endfor %}</div>
      </div>
    </article>
  {% endfor %}
</div>

## Future Research Agenda

### {{ page.future_agenda.title }}

{{ page.future_agenda.intro }}

<ol class="agenda-list">
  {% for theme in page.future_agenda.themes %}
    <li>
      <span class="priority__title">{{ theme.title }}</span>
      <span class="priority__desc">{{ theme.summary }}</span>
    </li>
  {% endfor %}
</ol>

## Additional Collaborative Research

I have also contributed to clinical evidence synthesis, including systematic reviews and meta-analyses of treatments for diabetes and osteoporosis in chronic kidney disease. These collaborations broaden the settings in which I apply rigorous evidence assessment without constituting a fourth core research area.
