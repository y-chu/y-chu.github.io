---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
entry_type: index
featured_publications:
  - title: "Leveraging language models and machine learning in verbal autopsy analysis"
    authors: "Yue Chu"
    year: "2025"
    venue: "arXiv preprint"
    summary: "A methodological paper on using language models and machine learning for verbal autopsy analysis and cause-of-death classification."
    paper_url: "https://doi.org/10.48550/arXiv.2508.19274"

  - title: "Temporal changes in cause of death among adolescents and adults in six countries in eastern and southern Africa in 1995-2019"
    authors: "Yue Chu, Mary Marston, and collaborators"
    year: "2024"
    venue: "The Lancet Global Health"
    summary: "A multi-country surveillance study using verbal autopsy data to examine long-run changes in cause-specific mortality across eastern and southern Africa."
    paper_url: "https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(24)00171-2/fulltext"
  - title: "Estimating seroprevalence of SARS-CoV-2 in Ohio: A Bayesian multilevel poststratification approach with multiple diagnostic tests"
    authors: "David Kline, Zehang Li, Yue Chu, and collaborators"
    year: "2021"
    venue: "PNAS"
    summary: "A Bayesian framework for statewide COVID-19 seroprevalence estimation under low positivity, imperfect testing, and survey nonresponse."
    paper_url: "https://doi.org/10.1073/pnas.2023947118"
---

{% if site.author.googlescholar %}
  You can also find my articles on <u><a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<div class="publication-list">
  {% assign publication_archive = site.publications | where_exp: "item", "item.entry_type != 'index'" | reverse %}
  {% for post in publication_archive %}
    {% include publication-list-item.html publication=post %}
  {% endfor %}
</div>
