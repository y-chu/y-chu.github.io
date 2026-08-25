---
layout: single
title: "Teaching & Mentoring"
permalink: /teaching/
author_profile: true
excerpt: "Quantitative and computational teaching, research mentoring, and technical workshops."
entry_type: index
teaching_experience:
  - term: "Spring 2026"
    course: "SOCIOL 8607: Causal Modeling"
    institution: "The Ohio State University"
    role: "Teaching Assistant"
  - term: "Autumn 2021"
    course: "SOCIOL 3549: Statistics in Sociology"
    institution: "The Ohio State University"
    role: "Recitation Leader"
  - term: "Autumn 2016–Autumn 2017"
    course: "380.651: Methods and Measures in Population Studies"
    institution: "Johns Hopkins Bloomberg School of Public Health"
    role: "Teaching Assistant"
  - term: "Autumn 2013–Autumn 2014"
    course: "380.603: Demographic Methods in Public Health"
    institution: "Johns Hopkins Bloomberg School of Public Health"
    role: "Teaching Assistant"
mentoring:
  - term: "Autumn 2025"
    title: "Doctoral research supervision · Reference Data Archive"
    context: "Provided day-to-day technical supervision to a PhD research assistant at The Ohio State University on data-quality assessment, data cleaning, and coding"
  - term: "Spring 2024"
    title: "Undergraduate research mentoring"
    context: "Mentored an undergraduate research assistant at The Ohio State University"
  - term: "Summer 2023"
    title: "Doctoral research supervision · Reference Data Archive"
    context: "Provided day-to-day technical supervision to a PhD research assistant during a visiting appointment at the Africa Health Research Institute on data-quality assessment, data cleaning, and coding"
  - term: "2015–2018"
    title: "Graduate research supervision"
    context: "Provided day-to-day research supervision and technical mentoring to 10+ graduate research assistants at Johns Hopkins Bloomberg School of Public Health across literature reviews, data extraction, data analysis, modeling support, and data visualization"
  - term: "Summers 2017 & 2018"
    title: "Summer research mentoring"
    context: "Mentored two undergraduate students through the Johns Hopkins Bloomberg School of Public Health Diversity Summer Internship Program"
workshops:
  - date: "2022"
    title: "R workshops"
    context: "Hosted by the Sociology Graduate Student Association"
  - date: "2018–2020"
    title: "Verbal autopsy data analysis workshops"
courses:
  - "Demography / Population Studies"
  - "Population Health"
  - "Quantitative Methods"
  - "Statistics / Applied Statistical Methods"
  - "Computational Social Science"
  - "Data Science for Population Research"
  - "AI / Machine Learning Applications in Population Health"
---

## Teaching Approach

<div class="page-intro">
  <p class="page-lead">My teaching connects quantitative concepts to applied research questions, with an emphasis on demographic reasoning, statistical interpretation, and reproducible computational work.</p>
  <p>Formal teaching and recitation roles span causal modeling, statistics, population studies, and demographic methods. I also provide research supervision and technical mentoring to undergraduate and graduate researchers and have completed pedagogical training through Ohio State's Drake Institute for Teaching and Learning.</p>
</div>

## Teaching Experience

<div class="experience-list">
  {% for item in page.teaching_experience %}
    <article class="experience-item">
      <div class="experience-item__date">{{ item.term }}</div>
      <div>
        <h3>{{ item.course }}</h3>
        <p><strong>{{ item.role }}</strong> · {{ item.institution }}</p>
      </div>
    </article>
  {% endfor %}
</div>

## Research Supervision & Mentoring

<div class="experience-list">
  {% for item in page.mentoring %}
    <article class="experience-item">
      <div class="experience-item__date">{{ item.term }}</div>
      <div>
        <h3>{{ item.title }}</h3>
        <p>{{ item.context }}</p>
      </div>
    </article>
  {% endfor %}
</div>

<p>Across these roles, I have supported students in developing applied quantitative, data-analysis, and population-health research skills.</p>

## Workshops & Training

<div class="experience-list">
  {% for item in page.workshops %}
    <article class="experience-item">
      <div class="experience-item__date">{{ item.date }}</div>
      <div>
        <h3>{{ item.title }}</h3>
        {% if item.context %}<p>{{ item.context }}</p>{% endif %}
      </div>
    </article>
  {% endfor %}
</div>

## Courses I Can Teach

Based on my training, research, and instructional record:

<ul class="course-list">
  {% for course in page.courses %}<li>{{ course }}</li>{% endfor %}
</ul>
