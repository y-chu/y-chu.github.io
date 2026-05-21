---
layout: single
title: "Selected Talks and Presentations"
permalink: /talks/
author_profile: true
entry_type: index
featured_talks:
  - title: "Automating cause of death classification from verbal autopsy: using pretrained language models and multi-modal learning"
    date: "2025-04-13"
    venue: "Population Association of America Annual Meeting"
    location: "Washington, DC, USA"
    type: "Conference presentation"
    description: "A presentation on using pretrained language models and multimodal pipelines to classify causes of death from verbal autopsy data."
    page_url: "/talks/2025PAA.md"

  - title: "Leveraging machine learning techniques for verbal autopsy analysis"
    date: "2024-11-05"
    venue: "Demystifying Machine Learning Workshop, Max Planck Institute for Demographic Research"
    location: "Rostock, Germany"
    type: "Workshop talk"
    description: "A workshop talk focused on how machine learning methods can support verbal autopsy analysis and downstream mortality estimation."
    page_url: "/talks/2024MaxPlanck.md"

  - title: "Temporal changes in cause of death among adults in six countries in Eastern and Southern Africa: a multi-country cohort study using verbal autopsy data"
    date: "2023-04-14"
    venue: "Population Association of America Annual Meeting"
    location: "New Orleans, USA"
    type: "Conference presentation"
    description: "A presentation highlighting long-run changes in adult mortality patterns across HDSS sites in eastern and southern Africa."
    page_url: "/talks/2023PAA.md"

  - title: "Indirect estimation of age-specific fertility and mortality: SVD-Bayes model"
    date: "2021-05-09"
    venue: "Population Association of America Annual Meeting"
    location: "Virtual"
    type: "Conference presentation"
    description: "A methods talk introducing SVD-Bayes for recovering detailed fertility and mortality age schedules from summary birth history data."
    page_url: "/talks/2021PAA.md"

  - title: "Understanding Misclassification between Neonatal Deaths and Stillbirths: Empirical Evidence from Malawi"
    date: "2017-04-23"
    venue: "Population Association of America Annual Meeting"
    location: "Washington, DC, USA"
    type: "Conference presentation"
    description: "A presentation on classification error between stillbirths and neonatal deaths, and why that distinction matters for survey-based measurement."
    page_url: "/talks/2017PAA.md"
---

<div class="page-intro">
  <p class="page-lead">Selected conference presentations, invited talks, and workshop contributions.</p>
</div>

<div class="feature-grid">
  {% for talk in page.featured_talks %}
    {% include talk-card.html talk=talk %}
  {% endfor %}
</div>

{% if site.talkmap_link == true %}
  <p><a href="/talkmap.html">See a map of all the places I have given a talk</a></p>
{% endif %}

<h2>Archive</h2>
{% assign talks_archive = site.talks | where_exp: "item", "item.entry_type != 'index'" | reverse %}
{% for post in talks_archive %}
  {% include archive-single-talk.html %}
{% endfor %}
