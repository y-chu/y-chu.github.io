---
permalink: /
excerpt: "Population health, demography, and data-driven research"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% assign research_page = site.research | where: "entry_type", "index" | first %}
{% assign publications_page = site.publications | where: "entry_type", "index" | first %}

<div class="page-intro">
  <p class="page-lead">I am a population health expert, demographer, and data scientist working at the intersection of global health, demographic estimation, and applied AI.</p>
  <p>My research examines how <strong>advanced statistical, demographic, and AI-driven methods</strong> can help close persistent <strong>data and evidence gaps</strong> in low- and middle-income countries and other resource-limited settings.</p>
  <p>Across work on mortality, fertility, disease burden, data quality, evaluation, and research infrastructure, I focus on three priorities:</p>
</div>

<ul class="priorities">
  <li>
    <span class="priority__title">Reliable population health estimates</span>
    <span class="priority__desc">More accurate, interpretable, and decision-ready estimates of mortality, fertility, disease burden, and health disparities.</span>
  </li>
  <li>
    <span class="priority__title">Stronger data systems</span>
    <span class="priority__desc">Improving the quality and usability of survey and surveillance data, and examining how social determinants, data gaps, and measurement choices shape the evidence.</span>
  </li>
  <li>
    <span class="priority__title">Research translated into practice</span>
    <span class="priority__desc">Validation studies, evaluation frameworks, and practical data tools that turn research and measurement into usable evidence and public health action in underserved populations.</span>
  </li>
</ul>

## Background

I am a Postdoctoral Fellow in the Health and Environment Modeling Co-Laboratory at The Ohio State University. My training spans clinical medicine, population health, demography, sociology, epidemiology, and applied statistics. I hold a PhD in Sociology with a minor in Statistics from The Ohio State University and an MSPH in Population, Family and Reproductive Health from the Johns Hopkins Bloomberg School of Public Health, with earlier clinical training that grounds my work in the practical realities of health systems and patient care. Across graduate training and collaborative research, I have worked with WHO, AHRI, Swiss TPH, and other public health partners on projects that connect methodological research with real-world population health measurement, evidence generation, and decision-making in resource-limited settings.

## Selected Research Areas

<div class="info-rows">
  {% for theme in research_page.themes limit: 3 %}
    <article class="info-row">
      <div class="info-row__side">
        <h3 class="info-row__title">{{ theme.title }}</h3>
      </div>
      <div class="info-row__body">
        <p>{{ theme.summary }}</p>
        <div class="tag-row tag-row--sm">
          {% for tag in theme.tags limit: 3 %}
            <span class="tag-pill">{{ tag }}</span>
          {% endfor %}
        </div>
      </div>
    </article>
  {% endfor %}
</div>

<p><a href="/research/">Explore the full research page</a></p>

## Selected Papers

<div class="info-rows">
  {% for paper in publications_page.featured_publications limit: 3 %}
    <article class="info-row">
      <div class="info-row__side">
        {% if paper.year %}<p class="info-row__year">{{ paper.year }}</p>{% endif %}
        {% if paper.venue %}<p class="info-row__meta">{{ paper.venue }}</p>{% endif %}
      </div>
      <div class="info-row__body">
        <h3 class="info-row__title">{{ paper.title }}</h3>
        {% if paper.authors %}<p class="info-row__meta">{{ paper.authors }}</p>{% endif %}
        {% if paper.summary %}<p>{{ paper.summary }}</p>{% endif %}
        {% if paper.paper_url or paper.code_url %}
          <div class="link-row">
            {% if paper.paper_url %}<a class="link-chip" href="{{ paper.paper_url }}">Paper</a>{% endif %}
            {% if paper.code_url %}<a class="link-chip" href="{{ paper.code_url }}">{{ paper.code_label | default: "Code" }}</a>{% endif %}
          </div>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>

<p><a href="/publications/">Browse all publications</a></p>

## Contact

- University email: [chu.282@osu.edu](mailto:chu.282@osu.edu)
- Personal email: [ychu612@gmail.com](mailto:ychu612@gmail.com)
