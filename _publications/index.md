---
layout: publication-index
title: "Publications"
permalink: /publications/
author_profile: false
entry_type: index
excerpt: "Research portfolio organized by substantive and methodological themes."
themes:
  - title: "Measurement, Reporting, and Data Quality"
    summary: "How respondents, interviewers, instruments, and collection settings generate omission, displacement, misclassification, and other bias in population-health data."
    outputs:
      - "/publication/adaptive-questioning-demographic-measurement/"
      - "/publication/working-information-sufficiency/"
      - "/publication/damerow-2023-birth-outcome-misclassification/"
      - "/publication/helleringer-2020-neonatal-mortality-bias/"
      - "/publication/Li2016"
  - title: "Mortality Measurement, Validation, and Health Information Systems"
    summary: "Designing, validating, monitoring, and integrating cause-of-death measurement tools across research, surveillance, and civil-registration environments."
    outputs:
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
      - "/publication/wahl-2020-pneumonia-india/"
      - "/publication/mcallister-2019-pneumonia-global/"
      - "/publication/wahl-2019-pneumococcal-hib-india/"
      - "/publication/choudhary-2019-diarrhea-mortality-india/"
      - "/publication/black-2019-diarrhea-mortality/"
      - "/publication/wahl-2018-pneumococcal-hib-global/"
      - "/publication/countdown-2018-universal-coverage/"
      - "/publication/Li2016_China"
      - "/publication/liu-2016-global-under-five-mortality/"
      - "/publication/song-2016-child-mortality-china/"
      - "/publication/liu-2016-dcp3-child-mortality/"
      - "/publication/afghanistan-health-survey-2018/"
  - title: "Additional Collaborative Epidemiology and Evidence Synthesis"
    summary: "Selected collaborations applying epidemiologic, Bayesian, and evidence-synthesis methods beyond the three core research lines."
    outputs:
      - "/publication/turner-2022-covid-ohio/"
      - "/publication/Kline2021"
      - "/publication/wilson-2017-osteoporosis-ckd/"
      - "/publication/maruthur-2016-diabetes-medications/"
      - "/publication/bolen-2015-ahrq-diabetes-report/"
---

{% include base_path %}

<div class="page-intro">
  <p class="page-lead">This portfolio is organized by scientific problem rather than chronology. The three core sections mirror my research program, showing how individual studies contribute to better measurement, stronger health-information systems, and demographic inference under incomplete data.</p>
  <p>Recent and ongoing work appears alongside established evidence within each theme. Paper titles and figures link directly to the DOI or publication page; publication status is shown inline. Yue Chu is shown in bold, with first, joint-first, and corresponding authorship identified where applicable. {% if site.author.googlescholar %}<a href="{{ site.author.googlescholar }}">Google Scholar</a> · {% endif %}<a href="/files/Yue_Chu_CV.pdf">Full academic CV</a></p>
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
