---
layout: single
title: "Software"
permalink: /software/
author_profile: true
excerpt: "Research software, data infrastructure, and computing tools."
entry_type: index
packages:
  - title: "Reference Data Archive platform"
    tags:
      - "Julia"
      - "Python"
      - "R"
      - "SQL"
      - "APIs"
      - "Data engineering"
    problem: "Mortality reference datasets are difficult to discover, document, integrate, quality-check, and reuse consistently across institutions."
    deployment: "Operational public archive and secure analytics environment hosted by WHO. My contribution began with pilot development in 2023 and has continued under a formal WHO contract since June 2025."
    capabilities:
      - "Ingest and integrate mortality reference data from research sites and partner organizations."
      - "Harmonize variables and metadata, validate incoming data, and automate quality-control workflows."
      - "Publish DDI metadata to a NADA catalogue and provide programmatic access through user-facing APIs."
      - "Manage secure data access, users, and analysis workflows across collaborating institutions."
    outputs:
      - label: "WHO platform"
        url: "https://data.who.int/platforms/rda"
      - label: "RDA GitHub organization"
        url: "https://github.com/RDAORG"
      - label: "Project overview"
        url: "/projects/reference-data-archive/"

  - title: "MultimodalVA"
    tags:
      - "Python"
      - "NLP"
      - "Machine learning"
      - "Multimodal learning"
      - "LLMs"
    problem: "Automated verbal-autopsy methods commonly discard free-text narratives or evaluate narrative and structured symptom data in separate workflows."
    deployment: "Open-source, MIT-licensed Python package archived at Zenodo."
    capabilities:
      - "Prepare narrative and structured verbal-autopsy records for reproducible cause-of-death modeling."
      - "Train and compare narrative-only, indicator-only, and multimodal classifiers under consistent data splits and metrics."
      - "Run data-fusion, feature-fusion, soft-voting, and stacking models with hyperparameter optimization."
      - "Evaluate and visualize model performance, including prompt-based workflows for open-weight chat models."
    outputs:
      - label: "GitHub"
        url: "https://github.com/y-chu/MultimodalVA"
      - label: "Zenodo release"
        url: "https://doi.org/10.5281/zenodo.23036919"
      - label: "medRxiv study preprint"
        url: "https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1"
      - label: "Dissertation preprint"
        url: "https://arxiv.org/abs/2508.19274"
      - label: "Software overview"
        url: "/software/multimodalva/"
tools:
  - label: "Programming & statistical computing"
    items: "R · Python · Julia · SQL · Stata · JAGS · NIMBLE"
  - label: "Machine learning & language models"
    items: "Hugging Face · Optuna · pretrained language models · multimodal learning · prompt-based inference · Ollama"
  - label: "Data systems & delivery"
    items: "Data integration and harmonization · metadata and DDI · REST APIs · ODK · NADA · Azure · Kubeflow · Snowflake · AWS"
---

<div class="page-intro">
  <p class="page-lead">I build software and data infrastructure when a methodological contribution must remain reproducible, inspectable, and usable beyond a single study. The systems below support two parts of my research program: validating cause-of-death methods and making mortality reference data easier to discover, evaluate, and reuse.</p>
</div>

<div class="software-list">
  {% for package in page.packages %}
    {% include software-card.html package=package %}
  {% endfor %}
</div>

## Methods & Tools

<dl class="software-facts software-facts--page">
  {% for group in page.tools %}<div><dt>{{ group.label }}</dt><dd>{{ group.items }}</dd></div>{% endfor %}
</dl>
