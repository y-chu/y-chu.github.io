---
layout: single
title: "Personal"
permalink: /personal/
author_profile: true
excerpt: "Personal interests, informal notes, and fun updates."
entry_type: index
intro: "This page is a home for the parts of life that do not fit neatly into a CV: curiosity, everyday observations, side quests, and small moments worth remembering."
sections:
  - title: "Why this page exists"
    description: "Academic websites often flatten a person into publications and positions. I wanted one corner of the site to feel more human, with space for informal notes, gratitude, photos, travel memories, and the kinds of interests that shape how I work."
  - title: "What you might find here"
    description: "Over time I will use this page to share light updates from workshops and travel, books or ideas I am enjoying, side projects, and a few fun snapshots from daily life."
  - title: "How it connects back to research"
    description: "Much of my research is motivated by real people, local contexts, and collaborative fieldwork. Keeping a lighter personal page helps preserve that sense of texture and connection."
fun_news:
  - date: "2026-04-09"
    title: "Personal page launched"
    blurb: "This new section of the site is live and ready for future notes, stories, and informal updates."
  - date: "2026-04-09"
    title: "Website refresh in progress"
    blurb: "The site now includes dedicated spaces for research themes, projects, presentations, news, and a more personal side of the story."
---

<div class="page-intro">
  <p class="page-lead">{{ page.intro }}</p>
</div>

<div class="feature-grid feature-grid--compact">
  {% for section in page.sections %}
    <article class="feature-card feature-card--compact">
      <h2 class="feature-card__title">{{ section.title }}</h2>
      <p class="feature-card__summary">{{ section.description }}</p>
    </article>
  {% endfor %}
</div>

<h2>Fun News</h2>
<div class="news-list">
  {% assign fun_news = page.fun_news | sort: "date" | reverse %}
  {% for item in fun_news %}
    {% include news-item.html item=item %}
  {% endfor %}
</div>
