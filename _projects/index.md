---
layout: single
title: "Consulting"
permalink: /consulting/
redirect_from:
  - /projects/
author_profile: true
excerpt: "Consulting, technical assistance, and capacity building for public-health data and decision systems."
entry_type: index
---

<div class="page-intro">
  <p class="page-lead">I provide technical consulting where mortality measurement, health-information systems, and applied data science meet. I help public-health partners move from data collection to validated evidence and operational systems through analysis, reproducible workflows, documentation, training, and local capacity building.</p>
</div>

{% assign projects = site.projects | where_exp: "item", "item.entry_type != 'index'" | sort: "date" | reverse %}
{% assign current_projects = projects | where: "project_group", "consulting_current" %}
{% assign consulting_projects = projects | where: "project_group", "consulting" %}
{% assign capacity_projects = projects | where: "project_group", "capacity" %}

{% if current_projects.size > 0 %}
  <h2>Current Engagement</h2>
  <div class="project-list">
    {% for project in current_projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
{% endif %}

{% if consulting_projects.size > 0 %}
  <h2>Selected Consulting and Technical Assistance</h2>
  <div class="project-list">
    {% for project in consulting_projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
{% endif %}

{% if capacity_projects.size > 0 %}
  <h2>Training and Capacity Building</h2>
  <div class="project-list">
    {% for project in capacity_projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
{% endif %}

{% if current_projects.size == 0 and consulting_projects.size == 0 and capacity_projects.size == 0 %}
  <p>No consulting engagements are published yet.</p>
{% endif %}
