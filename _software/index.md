---
layout: single
title: "Software"
permalink: /software/
author_profile: true
excerpt: "Research software and data infrastructure packages."
entry_type: index
packages:
  - title: "MultimodalVA"
    language: "Python · pretrained language models · multimodal ML"
    status: "Research software · repository currently private"
    problem: "Automated verbal autopsy methods commonly use structured responses without incorporating the information in free-text narratives."
    role: "Developer and maintainer; designed and implemented the package's unified research workflows."
    technical_scope: "Narrative and tabular models, multimodal ensembles, training and prediction pipelines, hyperparameter optimization, evaluation, and visualization."
    links:
      - label: "Project page"
        url: "/projects/multimodalva/"
      - label: "Dissertation preprint"
        url: "https://arxiv.org/abs/2508.19274"

  - title: "Reference Data Archive software and data platform"
    language: "Julia · R · Python · APIs"
    status: "Operational research infrastructure · public platform"
    problem: "Reference mortality datasets need consistent ingestion, metadata, quality control, access, and analytics workflows across institutions."
    role: "Core developer and platform manager for the WHO-hosted RDA."
    technical_scope: "Data ingestion and curation, metadata, automated workflows, NADA and user-facing APIs, analytics environments, documentation, and user/data management."
    links:
      - label: "RDA platform"
        url: "https://data.who.int/rda"
      - label: "Project page"
        url: "/projects/reference-data-archive/"
---

<div class="page-intro">
  <p class="page-lead">I design and implement reusable research software and data systems that move population-health methods into reproducible analysis and operational infrastructure.</p>
</div>

<div class="feature-grid">
  {% for package in page.packages %}
    {% include software-card.html package=package %}
  {% endfor %}
</div>
