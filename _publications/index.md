---
layout: publication-index
title: "Publications"
permalink: /publications/
author_profile: false
entry_type: index
excerpt: "Research portfolio organized by substantive and methodological themes."
themes:
  - title: "Measurement, Reporting, and the Production of Health Data"
    summary: "How respondents, providers, interviewers, instruments, and institutions generate omission, displacement, misclassification, and other bias in population-health data."
    outputs:
      - "/publication/damerow-2023-birth-outcome-misclassification/"
      - "/publication/helleringer-2020-neonatal-mortality-bias/"
      - "/publication/Li2016"
  - title: "Integrating and Validating Heterogeneous Evidence"
    summary: "Combining and validating interviews, narratives, clinical records, laboratory findings, and administrative evidence for individual and population-health inference."
    outputs:
      - "/publication/adaptive-questioning-demographic-measurement/"
      - "/publication/working-information-sufficiency/"
      - "/publication/chu-2026-multimodal-ai-verbal-autopsy/"
      - "/publication/yang-2026-multimodal-cod-benchmark/"
      - "/publication/multimodalva-software/"
      - "/publication/mits-beyond-verbal-autopsy/"
      - "/publication/chandramohan-2021-verbal-autopsy/"
  - title: "Demographic Inference Under Incomplete and Misclassified Data"
    summary: "Estimating fertility, mortality, and cause-of-death patterns from incomplete histories and heterogeneous survey, surveillance, registration, and modeled evidence."
    outputs:
      - "/publication/joint-fertility-child-mortality-summary-birth-histories/"
      - "/publication/casterline-age-at-last-birth/"
      - "/publication/Chu2024_ALPHA"
      - "/publication/liu-2022-adolescent-mortality-china/"
      - "/publication/schumacher-2022-bayesian-child-mortality/"
      - "/publication/Perin2022"
      - "/publication/Li2019_India"
      - "/publication/countdown-2018-universal-coverage/"
      - "/publication/Li2016_China"
      - "/publication/liu-2016-global-under-five-mortality/"
      - "/publication/song-2016-child-mortality-china/"
      - "/publication/liu-2016-dcp3-child-mortality/"
      - "/publication/afghanistan-health-survey-2018/"
  - title: "Applied Epidemiology and Evidence Synthesis"
    summary: "Population-based research on infectious disease, maternal and child health, disease prevalence and burden, together with evidence synthesis for public-health and treatment decisions."
    outputs:
      - "/publication/turner-2022-covid-ohio/"
      - "/publication/Kline2021"
      - "/publication/wahl-2020-pneumonia-india/"
      - "/publication/mcallister-2019-pneumonia-global/"
      - "/publication/wahl-2019-pneumococcal-hib-india/"
      - "/publication/choudhary-2019-diarrhea-mortality-india/"
      - "/publication/black-2019-diarrhea-mortality/"
      - "/publication/wahl-2018-pneumococcal-hib-global/"
      - "/publication/wilson-2017-osteoporosis-ckd/"
      - "/publication/maruthur-2016-diabetes-medications/"
      - "/publication/bolen-2015-ahrq-diabetes-report/"
---

{% include base_path %}

<div class="page-intro">
  <p class="page-lead">This portfolio is organized by scientific problem rather than chronology, showing contributions to health-data production, heterogeneous evidence, demographic inference, and applied epidemiology.</p>
  <p>Recent and ongoing work appears alongside established evidence within each theme. Paper titles and figures link directly to the DOI or publication page; publication status is shown inline, and Yue Chu is shown in bold in each author list. {% if site.author.googlescholar %}<a href="{{ site.author.googlescholar }}">Google Scholar</a> · {% endif %}<a href="/files/Yue_Chu_CV.pdf">Full academic CV</a></p>
</div>

{% for theme in page.themes %}
<section class="publication-theme">
  <h2>{{ theme.title }}</h2>
  <p class="publication-theme__summary">{{ theme.summary }}</p>
  <div class="paper-grid">
    {% for output_path in theme.outputs %}
      {% assign publication = site.publications | where: "permalink", output_path | first %}
      {% if publication %}{% include publication-list-item.html publication=publication %}{% endif %}
    {% endfor %}
  </div>
</section>
{% endfor %}
