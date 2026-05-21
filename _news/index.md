---
layout: single
title: "News"
permalink: /news/
author_profile: true
excerpt: "Recent updates on papers, talks, and milestones."
entry_type: index
items:
  - date: "2026-05-21"
    title: "Attending the FDS Workshop at Yale"
    category: "Presentation"
    blurb: "Presenting a poster, AI as Measurement Infrastructure: Adaptive Survey Design in Verbal Autopsy, at the FDS Workshop on AI for Social Science Research Methods, Yale University, New Haven, CT."
    url: "/presentations/"
    link_label: "See presentations"

  - date: "2026-05-10"
    title: "Presented work on information sufficiency in verbal autopsy at PAA 2026"
    category: "Presentation"
    blurb: "Presented a poster, Sufficiency of Information in Population Surveys: Evidence from Verbal Autopsy, at the Annual Meeting of the Population Association of America, St. Louis, MO."
    url: "/presentations/"
    link_label: "See presentations"

  - date: "2025-08-25"
    title: "New preprint on AI for verbal autopsy analysis"
    category: "Research"
    blurb: "Shared a new arXiv preprint on using language models and machine learning for verbal autopsy analysis and cause-of-death classification."
    url: "https://arxiv.org/abs/2508.19274"
    link_label: "Read the preprint"

  - date: "2025-04-13"
    title: "Presented verbal autopsy AI work at PAA 2025"
    category: "Talk"
    blurb: "Presented current work on pretrained language models and multimodal learning for verbal autopsy at the Population Association of America Annual Meeting."
    url: "/talks/"
    link_label: "See talks"

  - date: "2024-11-05"
    title: "Workshop talk at Max Planck Institute for Demographic Research"
    category: "Talk"
    blurb: "Spoke at the Demystifying Machine Learning workshop on machine learning techniques for verbal autopsy analysis."
    url: "/talks/"
    link_label: "View presentations"

  - date: "2024-08-01"
    title: "Lancet Global Health paper published"
    category: "Publication"
    blurb: "Published a multi-country surveillance study on temporal changes in cause of death among adolescents and adults across eastern and southern Africa."
    url: "https://pubmed.ncbi.nlm.nih.gov/39030059/"
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
