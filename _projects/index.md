---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
excerpt: "Current and selected research projects."
entry_type: index
---

<div class="page-intro">
  <p class="page-lead">These projects show how my research moves from question to evidence and from method to system: multi-country studies establish population patterns, active collaborations test new measurement tools, and technical assistance carries those methods into data collection and health-information practice.</p>
</div>

{% assign projects = site.projects | where_exp: "item", "item.entry_type != 'index'" | sort: "date" | reverse %}
{% assign active_projects = projects | where: "project_group", "active" %}
{% assign consulting_projects = projects | where: "project_group", "consulting" %}
{% assign past_projects = projects | where: "project_group", "past" %}

{% if active_projects.size > 0 %}
  <h2>Active Projects</h2>
  <div class="project-list">
    {% for project in active_projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
{% endif %}

{% if past_projects.size > 0 %}
  <h2>Past Research Projects</h2>
  <div class="project-list">
    {% for project in past_projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
{% endif %}

{% if consulting_projects.size > 0 %}
  <h2 id="consulting-and-technical-assistance">Consulting and Technical Assistance</h2>
  <div class="compact-list">
    {% for project in consulting_projects %}
      <article class="compact-item">
        <h3 class="compact-item__title"><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
        {% if project.role %}<p class="compact-item__meta">{{ project.role }}</p>{% endif %}
        {% if project.excerpt %}<p class="compact-item__summary">{{ project.excerpt | markdownify | strip_html | strip | truncate: 160 }}</p>{% endif %}
        {% if project.links %}
          <p class="inline-links"><span class="inline-links__label">Related:</span> {% for link in project.links %}<a href="{{ link.url }}">{{ link.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</p>
        {% endif %}
      </article>
    {% endfor %}
  </div>
{% endif %}

{% if active_projects.size == 0 and consulting_projects.size == 0 and past_projects.size == 0 %}
  <p>No projects are published yet.</p>
{% endif %}
