---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
entry_type: index
---

{% include base_path %}

{% assign teaching_archive = site.teaching | where_exp: "item", "item.entry_type != 'index'" | reverse %}
{% for post in teaching_archive %}
  {% include archive-single.html %}
{% endfor %}
