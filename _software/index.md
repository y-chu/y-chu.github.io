---
layout: single
title: "Software"
permalink: /software/
author_profile: true
excerpt: "Research software and data infrastructure packages."
entry_type: index
packages:
  - title: "MultimodalVA"
    language: "Python"
    summary: "A Python package for multimodal automated cause-of-death classification from verbal autopsy data. It supports narrative, tabular, and ensemble workflows so researchers can build and evaluate models using one or both modalities in a unified pipeline."
    links:
      - label: "GitHub"
        url: "https://github.com/y-chu/MultimodalVA"
      - label: "Project page"
        url: "/projects/multimodalva/"
    placeholders:
      - "Docs"

  - title: "RDA Packages"
    language: "Julia, R, Python"
    summary: "A Julia package suite for creating and managing the Reference Data Archive (RDA), together with user-facing API packages in Julia, R, and Python for easier dataset loading, browsing, and navigation through the RDA ecosystem."
    links:
      - label: "RDA project site"
        url: "https://data.who.int/platforms/rda"
      - label: "RDA user guide"
        url: "https://data.who.int/platforms/rda"
    placeholders:
      - "GitHub"
      - "Docs"
---

<div class="page-intro">
  <p class="page-lead">This page highlights software packages and package suites that support my work in verbal autopsy, mortality measurement, and data infrastructure.</p>
</div>

<div class="feature-grid">
  {% for package in page.packages %}
    {% include software-card.html package=package %}
  {% endfor %}
</div>
