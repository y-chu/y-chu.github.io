---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
entry_type: index
excerpt: "Preprints and manuscripts, peer-reviewed publications, dissertations and theses, and technical reports."
---

{% include base_path %}

{% assign preprints = site.publications | where: "publication_type", "preprint" %}
{% assign manuscripts = site.publications | where: "publication_type", "manuscript" %}
{% assign working_papers = site.publications | where: "publication_type", "working_paper" %}
{% assign early_work = preprints | concat: manuscripts | concat: working_papers | sort: "publication_order" %}
{% assign peer_reviewed = site.publications | where: "publication_type", "peer_reviewed" | sort: "publication_order" %}
{% assign dissertations = site.publications | where: "publication_type", "dissertation" | sort: "publication_order" %}
{% assign theses = site.publications | where: "publication_type", "thesis" | sort: "publication_order" %}
{% assign reports = site.publications | where: "publication_type", "report" | sort: "publication_order" %}

<div class="page-intro">
  <p><strong>{{ peer_reviewed.size }} peer-reviewed publications</strong>, listed with preprints, manuscripts, dissertation work, and technical reports in reverse chronological order. Yue Chu is shown in bold; joint-first and corresponding authorship are noted where applicable.</p>
  {% if site.author.googlescholar %}<p><a href="{{ site.author.googlescholar }}">Google Scholar profile</a> · <a href="/files/Yue_Chu_CV.pdf">Academic CV</a></p>{% endif %}
</div>

{% if early_work.size > 0 %}
## Preprints and Manuscripts

<div class="publication-list">
  {% for publication in early_work %}{% include publication-list-item.html publication=publication %}{% endfor %}
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
