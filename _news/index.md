---
layout: single
title: "News"
permalink: /news/
author_profile: true
excerpt: "Recent updates on papers, talks, and milestones."
entry_type: index
items:
  - date: "2026-10-16"
    title: "New medRxiv preprint on multimodal AI for verbal autopsy"
    category: "Research"
    blurb: "Released a national South African benchmark comparing narrative, structured-data, multimodal, and large-language-model approaches to cause-of-death assignment from verbal autopsy records."
    url: "https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1"
    link_label: "Read the preprint"

  - date: "2026-10-13"
    title: "Multimodal cause-of-death benchmark selected as a NeurIPS 2026 poster"
    category: "Research"
    blurb: "A coauthored benchmark using child health and mortality data was selected for a NeurIPS 2026 ED Track poster, presented by the first author; the paper is available separately as a medRxiv preprint."
    url: "https://www.medrxiv.org/content/10.64898/2026.07.13.26357980v1"
    link_label: "Read the preprint"

  - date: "2026-05-21"
    title: "Presented work on AI-assisted population surveys at Yale University"
    category: "Presentation"
    blurb: "Presented *AI as Measurement Infrastructure: Adaptive Survey Design in Verbal Autopsy* at the FDS Workshop on AI for Social Science Research Methods, Yale University, New Haven, CT."
    url: "/presentations/"
    link_label: "See presentations"

  - date: "2026-05-10"
    title: "Presented work on information sufficiency in population surveys at PAA 2026"
    category: "Presentation"
    blurb: "Presented *Sufficiency of Information in Population Surveys: Evidence from Verbal Autopsy* at the Annual Meeting of the Population Association of America, St. Louis, MO."
    url: "/presentations/"
    link_label: "See presentations"

  - date: "2025-12-01"
    title: "Reference Data Archive officially launched at WHO"
    category: "Project"
    blurb: "The Reference Data Archive (RDA) is now live at data.who.int/rda. Its initial public release includes verbal autopsy data from the São Paulo mortality surveillance system and reflects collaborative infrastructure work across OSU, AHRI, WHO, and the University of São Paulo."
    url: "https://data.who.int/rda"
    link_label: "Visit the RDA"

  - date: "2025-08-25"
    title: "New preprint on multimodal AI for cause of death classification"
    category: "Research"
    blurb: "Shared a new arXiv preprint on using language models and machine learning for cause-of-death classification using verbal autopsy data."
    url: "https://arxiv.org/abs/2508.19274"
    link_label: "Read the preprint"

  - date: "2025-04-13"
    title: "Presented verbal autopsy AI work at PAA 2025"
    category: "Presentation"
    blurb: "Presented current work on pretrained language models and multimodal learning for verbal autopsy at the Population Association of America Annual Meeting in Washington, DC."
    url: "/presentations/"
    link_label: "See presentations"

  - date: "2024-11-05"
    title: "Workshop talk at Max Planck Institute for Demographic Research"
    category: "Presentation"
    blurb: "Spoke at the Demystifying Machine Learning workshop on machine learning techniques for verbal autopsy analysis."
    url: "/presentations/"
    link_label: "View presentations"

  - date: "2024-08-01"
    title: "Lancet Global Health paper published"
    category: "Publication"
    blurb: "Published a multi-country surveillance study on temporal changes in cause of death among adolescents and adults across eastern and southern Africa."
    url: "https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(24)00171-2/fulltext"
    link_label: "View publication"

  - date: "2022-10-01"
    title: "Journal of Global Health paper on adolescent mortality in China"
    category: "Publication"
    blurb: "Published national and sub-national estimates of mortality among 5-19-year-olds in China using Disease Surveillance Points System evidence."
    url: "https://pubmed.ncbi.nlm.nih.gov/36181508/"
    link_label: "Read paper"
---

<div class="page-intro">
  <p class="page-lead">A short timeline of recent research, presentation, and site updates.</p>
</div>

<div class="news-list">
  {% assign news_items = page.items | sort: "date" | reverse %}
  {% for item in news_items %}
    {% include news-item.html item=item %}
  {% endfor %}
</div>
