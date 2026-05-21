---
layout: single
title: "Yue Chu"
permalink: /profile/
author_profile: false
excerpt: "Population health researcher working at the intersection of demography, epidemiology, and data science."
entry_type: index
---

{% assign publications_page = site.publications | where: "entry_type", "index" | first %}

<div class="profile-hero">
  <div class="profile-hero__main">
    <h1 class="profile-hero__title">Yue Chu</h1>
    <p class="profile-hero__role">Postdoctoral Fellow</p>
    <p class="profile-hero__org">The Ohio State University</p>
    <p class="page-lead">I develop statistical and computational methods for population health, with a particular focus on mortality measurement, verbal autopsy, disease surveillance, and data quality in low-resource settings.</p>
    <p>I work at the intersection of demography, epidemiology, and data science, connecting Bayesian methods, language models, and practical health data systems. My recent work includes multimodal verbal autopsy analysis, mortality estimation, and infrastructure projects that make reference data more accessible for research and policy.</p>
  </div>

  <aside class="profile-sidebar-card">
    <img class="profile-sidebar-card__image" src="/images/headshot_YC.jpg" alt="Yue Chu">
    <dl class="profile-sidebar-card__list">
      <dt>Affiliation</dt>
      <dd>The Ohio State University</dd>
      <dt>CV</dt>
      <dd><a href="/files/Yue_Chu_CV.pdf">Download PDF</a></dd>
      <dt>Website</dt>
      <dd><a href="/">y-chu.github.io</a></dd>
      <dt>GitHub</dt>
      <dd><a href="https://github.com/y-chu">y-chu</a></dd>
      <dt>Google Scholar</dt>
      <dd><a href="https://scholar.google.com/citations?user=35jZ0usAAAAJ&hl=en&oi=ao">Profile</a></dd>
      <dt>Email</dt>
      <dd><a href="mailto:chu.282@osu.edu">chu.282@osu.edu</a></dd>
    </dl>
  </aside>
</div>

## Bio

My research focuses on how to measure health and mortality when data are incomplete, noisy, or difficult to collect. A central thread across my work is making population health evidence more reliable and more useful for real-world decision-making, especially in global health settings where data systems are uneven or resource-constrained.

I am particularly interested in verbal autopsy, cause-of-death classification, mortality estimation, survey data quality, and data infrastructure for public health research. Alongside methodological work, I collaborate on practical systems such as the Reference Data Archive and on AI-enabled approaches to cause-of-death determination.

## Selected Papers

<div class="feature-grid">
  {% for paper in publications_page.featured_publications %}
    {% include selected-paper-card.html paper=paper %}
  {% endfor %}
</div>

<p><a href="/publications/">See the full publications list</a></p>

## Contact

Department of Sociology  
The Ohio State University  
Columbus, Ohio, USA

Email: [chu.282@osu.edu](mailto:chu.282@osu.edu)
