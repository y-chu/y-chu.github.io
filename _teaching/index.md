---
layout: single
title: "Teaching & Mentoring"
permalink: /teaching/
author_profile: true
excerpt: "Quantitative and population-health teaching, research supervision, and technical workshops."
entry_type: index
approach:
  - title: "Make reasoning visible"
    summary: "I ask students to articulate the substantive question, measure, estimand, assumptions, and limits behind an analysis—not only reproduce a procedure."
  - title: "Scaffold reproducible independence"
    summary: "Worked examples, annotated code, and structured checkpoints gradually give way to independent choices and reproducible analysis."
  - title: "Mentor toward ownership"
    summary: "In research supervision, I move from technical guidance to student-led decisions, interpretation, documentation, and communication."
teaching_experience:
  - term: "Spring 2026"
    course: "SOCIOL 8607: Causal Modeling"
    institution: "The Ohio State University"
    role: "Teaching Assistant"
    note: "Facilitated class discussion and provided coding and programming support."
  - term: "Autumn 2020"
    course: "SOCIOL 3549: Statistics in Sociology"
    institution: "The Ohio State University"
    role: "Recitation Leader"
    note: "Led synchronous recitation and lab sections with Stata examples; many students were taking their first statistics course."
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
    context: "Supervised a PhD research assistant at The Ohio State University on data-quality checks, data cleaning, and coding."
  - term: "Spring 2024"
    title: "Undergraduate research mentoring"
    context: "Mentored an undergraduate research assistant at The Ohio State University."
  - term: "Summer 2023"
    title: "Doctoral research supervision · Reference Data Archive"
    context: "Supervised a PhD research assistant on data-quality checks, data cleaning, and coding during a visiting appointment at the Africa Health Research Institute."
  - term: "2015–2018"
    title: "Graduate research supervision"
    context: "Supervised 10+ graduate research assistants at Johns Hopkins Bloomberg School of Public Health working on literature review, data extraction, data analysis, modeling support, and visualization."
  - term: "Summers 2017 & 2018"
    title: "Summer research mentoring"
    context: "Mentored two undergraduate students through the Johns Hopkins Bloomberg School of Public Health Diversity Summer Internship Program."
workshops:
  - date: "2022"
    title: "R workshops"
    context: "Hosted by the Sociology Graduate Student Association, The Ohio State University"
  - date: "2018–2020"
    title: "Verbal autopsy data analysis workshops"
    context: "Hosted by the openVA team, The Ohio State University"
teaching_areas:
  - "Quantitative Methods and Applied Statistics"
  - "Survey Methodology, Measurement, and Data Quality"
  - "Demography and Population Health"
  - "Computational Social Science and Data Science"
  - "Global Health Data and Mortality Measurement"
---

## Teaching Approach

<div class="page-intro">
  <p class="page-lead">My teaching goal is for students to move from a substantive population or public-health question to a defensible measure, estimand, dataset, method, interpretation, and statement of limits.</p>
  <p>Students should be able to explain what evidence supports a conclusion, where uncertainty enters, and what additional evidence could change the answer. I use quantitative work as a setting for making that reasoning visible and reproducible.</p>
</div>

<ol class="priorities">
  {% for principle in page.approach %}
    <li>
      <span class="priority__title">{{ principle.title }}</span>
      <span class="priority__desc">{{ principle.summary }}</span>
    </li>
  {% endfor %}
</ol>

<p>I bring this approach to causal modeling, statistics, demographic methods, population studies, research supervision, and technical workshops. I completed pedagogical training through Ohio State's Drake Institute for Teaching and Learning in 2021.</p>

## Teaching Experience

<div class="experience-list">
  {% for item in page.teaching_experience %}
    <article class="experience-item">
      <div class="experience-item__date">{{ item.term }}</div>
      <div>
        <h3>{{ item.course }}</h3>
        <p><strong>{{ item.role }}</strong> · {{ item.institution }}</p>
        {% if item.note %}<p>{{ item.note }}</p>{% endif %}
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

## Teaching Areas

<ul class="course-list">
  {% for area in page.teaching_areas %}<li>{{ area }}</li>{% endfor %}
</ul>
