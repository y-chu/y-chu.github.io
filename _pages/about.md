---
permalink: /
excerpt: "Population health scientist and demographer working on measurement under incomplete, heterogeneous, and imperfect data."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% assign research_page = site.research | where: "entry_type", "index" | first %}
{% assign peer_reviewed_publications = site.publications | where: "publication_type", "peer_reviewed" %}
{% assign featured_publications = peer_reviewed_publications | where: "featured", true | sort: "publication_order" %}

<div class="home-positioning">
  <p class="home-positioning__kicker">Population Health Scientist &amp; Demographer</p>
  <h1 class="home-positioning__title">Measurement under imperfect information</h1>
  <p class="page-lead">I study how incomplete and uneven data shape what we know about population health, and develop demographic, statistical, computational, and AI methods to improve measurement and decision-making.</p>
  <p class="home-positioning__descriptor">AI, statistical methods, and data systems for population health measurement</p>
  <div class="link-row link-row--home">
    <a class="link-chip" href="/research/">Research agenda</a>
    <a class="link-chip" href="/publications/">Publications</a>
    <a class="link-chip" href="/files/Yue_Chu_CV.pdf">Academic CV</a>
  </div>
</div>

<div class="evidence-strip" aria-label="Selected evidence">
  <a href="/publications/"><strong>{{ peer_reviewed_publications.size }}</strong><span>peer-reviewed articles</span></a>
  <a href="/projects/reference-data-archive/"><strong>WHO</strong><span>global research infrastructure</span></a>
  <a href="/research/"><strong>Demographic + statistical + AI</strong><span>measurement methods</span></a>
  <a href="/software/"><strong>R · Python · Julia · SQL</strong><span>research software and data systems</span></a>
</div>

<p>Across mortality, fertility, verbal autopsy, survey data quality, and research infrastructure, the work follows a common path from measurement problem to methodological innovation, operational system, and practical use.</p>

<ul class="priorities">
  <li>
    <span class="priority__title">Reliable population health estimates</span>
    <span class="priority__desc">Developing interpretable estimates of mortality, fertility, disease burden, and health disparities when observations are sparse, incomplete, or uneven.</span>
  </li>
  <li>
    <span class="priority__title">Stronger data systems</span>
    <span class="priority__desc">Improving survey and surveillance data quality, curation, and usability while examining how reporting processes and measurement choices shape observed patterns.</span>
  </li>
  <li>
    <span class="priority__title">Research translated into practice</span>
    <span class="priority__desc">Building validation studies, reusable software, and research infrastructure that move new methods into collaborative population-health systems and decision-making.</span>
  </li>
</ul>

## Background

I am a Postdoctoral Fellow at the Institute for Population Research at The Ohio State University. My training spans clinical medicine, population health, demography, sociology, epidemiology, and applied statistics. I hold a PhD in Sociology with a minor in Statistics and Demography from Ohio State and an MSPH in Population, Family and Reproductive Health from the Johns Hopkins Bloomberg School of Public Health. Collaborative work with WHO, the Africa Health Research Institute, and other international partners connects methodological research with population-health measurement, research infrastructure, and implementation.

## Selected Research Areas

<div class="info-rows">
  {% for theme in research_page.agenda %}
    <article class="info-row">
      <div class="info-row__side">
        <h3 class="info-row__title">{{ theme.title }}</h3>
      </div>
      <div class="info-row__body">
        <p>{{ theme.summary }}</p>
        <div class="tag-row tag-row--sm">
          {% for tag in theme.methods limit: 3 %}
            <span class="tag-pill">{{ tag }}</span>
          {% endfor %}
        </div>
      </div>
    </article>
  {% endfor %}
</div>

<p><a href="/research/">Explore the full research page</a></p>

## Selected Publications

<div class="info-rows">
  {% for paper in featured_publications limit: 3 %}
    <article class="info-row">
      <div class="info-row__side">
        {% if paper.publication_year %}<p class="info-row__year">{{ paper.publication_year }}</p>{% endif %}
        {% if paper.venue %}<p class="info-row__meta">{{ paper.venue }}</p>{% endif %}
      </div>
      <div class="info-row__body">
        <h3 class="info-row__title">{{ paper.title }}</h3>
        {% if paper.authors %}<p class="info-row__meta publication-authors">{{ paper.authors }}</p>{% endif %}
        {% if paper.venue_details %}<p>{{ paper.venue_details }}</p>{% endif %}
        {% include publication-links.html publication=paper %}
      </div>
    </article>
  {% endfor %}
</div>

<p><a href="/publications/">Browse all publications</a></p>

## Contact

- University email: [chu.282@osu.edu](mailto:chu.282@osu.edu)
- Personal email: [ychu612@gmail.com](mailto:ychu612@gmail.com)
