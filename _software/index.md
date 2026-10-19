---
layout: single
title: "Software"
permalink: /software/
author_profile: true
excerpt: "Research software, data infrastructure, and computing tools."
entry_type: index
packages:
  - title: "Reference Data Archive platform"
    language: "Julia · Python · R · SQL"
    status: "Operational · public WHO-hosted platform"
    problem: "Reference mortality datasets need consistent ingestion, metadata, quality control, access, and analytics workflows across institutions."
    role: "Platform manager and core developer; co-lead of software development with the Africa Health Research Institute; sole data manager; author of the platform documentation."
    technical_scope: "Data ingestion and curation, metadata, automated quality-control workflows, NADA and user-facing APIs, a secure analytics environment, and user and data management."
    links:
      - label: "RDA platform"
        url: "https://data.who.int/platforms/rda"
      - label: "RDAIngest.jl"
        url: "https://github.com/RDAORG/RDAIngest.jl"
      - label: "juRDA.jl"
        url: "https://github.com/RDAORG/juRDA.jl"
      - label: "Project page"
        url: "/projects/reference-data-archive/"

  - title: "MultimodalVA"
    language: "Python · pretrained language models · machine learning · multimodal learning"
    status: "Research software · open source"
    problem: "Automated verbal autopsy methods commonly use structured responses without the information in free-text narratives."
    role: "Developer and maintainer; designed and implemented the package."
    technical_scope: "Narrative, structured-data, and multimodal classifiers; training and prediction pipelines; hyperparameter optimization; evaluation and visualization."
    links:
      - label: "GitHub"
        url: "https://github.com/y-chu/MultimodalVA"
      - label: "Preprint (medRxiv)"
        url: "https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1"
      - label: "Project page"
        url: "/projects/multimodalva/"
      - label: "Dissertation preprint"
        url: "https://arxiv.org/abs/2508.19274"

  - title: "ALPHA Network verbal-autopsy dataset (AHRI/uMkhanyakude)"
    language: "Demography · epidemiology · verbal autopsy · HDSS"
    status: "Data product · licensed access"
    problem: "Comparative mortality research across ALPHA Network sites required harmonized demographic-surveillance and verbal-autopsy data."
    role: "one of four named primary investigators in the catalogue record"
    technical_scope: "Curated and anonymised verbal-autopsy, residency, HIV-surveillance, hospital-death, and physician-coded cause-of-death data from South Africa, 2000–2020."
    links:
      - label: "AHRI catalogue record"
        url: "https://data.ahri.org/index.php/catalog/1030"
tools:
  - label: "Core research computing"
    items: "R · Python · Julia · SQL · Stata"
  - label: "Additional experience"
    items: "SPSS · JMP · Bayesian modeling with JAGS and NIMBLE"
  - label: "Machine learning and data platforms"
    items: "Hugging Face · Optuna · prompt engineering · Azure · Kubeflow · Snowflake · AWS"
---

<div class="page-intro">
  <p class="page-lead">Research software and data infrastructure I have built for reproducible analysis and shared use.</p>
</div>

<div class="feature-grid">
  {% for package in page.packages %}
    {% include software-card.html package=package %}
  {% endfor %}
</div>

## Methods & Tools

<dl class="software-facts">
  {% for group in page.tools %}<div><dt>{{ group.label }}</dt><dd>{{ group.items }}</dd></div>{% endfor %}
</dl>
