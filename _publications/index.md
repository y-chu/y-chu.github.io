---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
entry_type: index
excerpt: "Working papers, peer-reviewed publications, dissertations and theses, and technical reports."
---

{% include base_path %}

{% assign peer_reviewed = site.publications | where: "publication_type", "peer_reviewed" | sort: "publication_order" %}
{% assign working_papers = site.publications | where: "publication_type", "working_paper" | sort: "publication_order" %}
{% assign dissertations = site.publications | where: "publication_type", "dissertation" | sort: "publication_order" %}
{% assign theses = site.publications | where: "publication_type", "thesis" | sort: "publication_order" %}
{% assign reports = site.publications | where: "publication_type", "report" | sort: "publication_order" %}

<div class="page-intro">
  <p class="page-lead">My work develops and applies demographic, statistical, computational, and AI methods to population-health measurement, with an emphasis on incomplete data, surveillance, data quality, and operational research systems.</p>
  <p><strong>{{ peer_reviewed.size }} peer-reviewed articles.</strong> Publications are listed in reverse chronological order, with Yue Chu shown in bold and joint-first authorship identified where applicable.</p>
  {% if site.author.googlescholar %}<p><a href="{{ site.author.googlescholar }}">Google Scholar profile</a> · <a href="/files/Yue_Chu_CV.pdf">Academic CV</a></p>{% endif %}
</div>

{% if working_papers.size > 0 %}
## Working Papers / Manuscripts

<div class="publication-list">
  {% for publication in working_papers %}{% include publication-list-item.html publication=publication %}{% endfor %}
</div>
{% endif %}

## Peer-Reviewed Publications

<div class="publication-list">
  {% for publication in peer_reviewed %}{% include publication-list-item.html publication=publication %}{% endfor %}
</div>

{% if dissertations.size > 0 or theses.size > 0 %}
## Dissertations & Theses

<div class="publication-list">
  {% for publication in dissertations %}{% include publication-list-item.html publication=publication %}{% endfor %}
  {% for publication in theses %}{% include publication-list-item.html publication=publication %}{% endfor %}
</div>
{% endif %}

{% if reports.size > 0 %}
## Technical Reports & Book Chapters

<div class="publication-list">
  {% for publication in reports %}{% include publication-list-item.html publication=publication %}{% endfor %}
</div>
{% endif %}
