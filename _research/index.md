---
layout: single
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Research on how incomplete and imperfect health information becomes population evidence."
entry_type: index
established:
  - title: "Measurement, Reporting, and Data Quality"
    slug: "measurement-reporting-data-quality"
    home_summary: "How respondents, interviewers, instruments, collection modes, and institutions shape what population-health data capture, omit, and misclassify."
  - title: "Mortality Measurement, Validation, and Health Information Systems"
    slug: "mortality-measurement-validation-systems"
    home_summary: "How mortality-measurement tools can be validated, monitored, and integrated into routine surveillance and civil-registration systems."
  - title: "Demographic Inference Under Incomplete and Misclassified Data"
    slug: "demographic-inference"
    home_summary: "How fertility, mortality, and cause-of-death patterns can be estimated when events are incompletely observed, selectively reported, or imperfectly classified."
---

<div class="page-intro">
  <p class="page-lead">I study how incomplete and imperfect health information becomes population evidence. My work follows the path from a health event to a report, a record, a classification, and ultimately a population estimate.</p>
  <p>At each step, social interaction, instrument design, health-system capacity, and analytic choices determine what remains visible. I ask where bias enters the data; how measurement tools can be validated, monitored, and improved; and how demographic inference should proceed when missingness and misclassification remain. This connects the social production of data to the methods and information systems used to draw public-health conclusions.</p>
</div>

<section class="research-program" id="measurement-reporting-data-quality">
  <h2>Measurement, Reporting, and Data Quality</h2>

  <p>Population data are made, not merely collected. Respondents decide what to disclose and how to describe an event; interviewers interpret, probe, and record; questionnaires constrain the available answers; and survey modes change the interaction through which information is produced. I therefore treat bias and misclassification as outcomes to be located and explained rather than as unexplained noise.</p>

  <p>My validation research helps locate reporting error rather than treating disagreement between records as random. Studies of neonatal mortality have examined omissions, age displacement, and misclassification between stillbirths and neonatal deaths; in the collaborative provider–mother study, I contributed to the study design used to test how interview interactions shape reported birth outcomes. My current program extends that foundation from diagnosing error to asking how instruments can preserve essential information without systematically misrepresenting particular people or events.</p>

  <h3>Questions I ask</h3>
  <ul>
    <li>Where in reporting and data collection do errors arise, and which respondents, interviewers, or events are most affected?</li>
    <li>How do interview mode, question wording, probing, and instrument length change the information that is recorded?</li>
    <li>Which questions preserve essential information, and when does shortening or adapting an interview change the population being measured?</li>
  </ul>

  <h3>Current and ongoing work</h3>
  <p>Current work examines which parts of verbal-autopsy interviews carry the information needed for reliable cause-of-death inference and what adaptive questioning changes about the population being measured. This moves the research from diagnosing error to redesigning instruments: shorter or more responsive interviews should be judged not only by efficiency, but also by whether they create new forms of differential measurement error.</p>

  <h3>Selected publications and ongoing work</h3>
  <ol class="example-paper-list">
    <li><a href="https://doi.org/10.1007/s13524-020-00911-6">Biases in survey estimates of neonatal mortality: Results from a validation study in urban areas of Guinea-Bissau</a> — <em>Demography</em>.</li>
    <li><a href="https://doi.org/10.7189/jogh.13.04086">Provider-mother interactions are associated with birth outcome misclassifications in household surveys</a> — <em>Journal of Global Health</em>.</li>
    <li><a href="https://doi.org/10.1371/journal.pone.0168743">Understanding misclassification between neonatal deaths and stillbirths</a> — <em>PLOS ONE</em>.</li>
    <li><a href="/publication/working-information-sufficiency/">Sufficiency of information in population surveys: Evidence from verbal autopsy</a> — working paper; presented at PAA 2026.</li>
    <li><a href="/publication/adaptive-questioning-demographic-measurement/">What adaptive questioning does to demographic measurement</a> — ongoing research; presented at the 2026 FDS Workshop on AI for Social Science Research Methods.</li>
  </ol>
</section>

<section class="research-program" id="mortality-measurement-validation-systems">
  <h2>Mortality Measurement, Validation, and Health Information Systems</h2>

  <p>Where medical certification is limited, cause-of-death evidence depends on tools that translate interviews, clinical observations, and diagnostic tests into comparable classifications. Validation therefore involves more than ranking algorithms in one dataset. I study what information a method uses, whether performance travels across populations and collection settings, how individual- and population-level conclusions differ, and how performance can be monitored after implementation.</p>

  <p>In my lead-authored national South African benchmark, I compare methods that use verbal-autopsy narratives, structured symptom indicators, pretrained language models, and multimodal learning. By evaluating operational, single-modality, multimodal, and large-language-model approaches under a common design, the study tests what each source of information adds and where conclusions differ between individual cause assignment and population cause fractions. The companion <a href="https://github.com/y-chu/MultimodalVA">MultimodalVA</a> software makes those comparisons reproducible.</p>

  <h3>Questions I ask</h3>
  <ul>
    <li>How much and what kinds of information are needed for reliable individual cause assignment and population cause fractions?</li>
    <li>How should new tools be validated across sites, populations, interview modes, and changing cause distributions?</li>
    <li>Which monitoring and evaluation signals reveal when a measurement system no longer performs as intended?</li>
    <li>How can verbal autopsy and complementary evidence be integrated into routine mortality surveillance and CRVS workflows?</li>
  </ul>

  <h3>Current and ongoing work</h3>
  <p>Current studies extend this work from benchmark performance to decision-oriented validation: how much information is sufficient, what minimally invasive tissue sampling adds beyond verbal autopsy, when calibration fails across populations, and which monitoring signals reveal that a deployed system no longer performs as intended. The goal is to connect model evaluation to operational decisions without assuming that a tool validated in one setting will remain valid elsewhere.</p>

  <figure class="research-figure research-figure--wide">
    <img src="/images/research/multimodalva-main-results.png" alt="Comparison of cause-of-death classification accuracy, macro F1, and population-level CSMF accuracy across operational, unimodal, and multimodal models">
    <figcaption>The public South African benchmark compares operational, narrative-only, indicator-only, and multimodal approaches at both individual and population levels. It illustrates why validation must consider more than a single accuracy measure.</figcaption>
  </figure>

  <h3>Selected publications and outputs</h3>
  <ol class="example-paper-list">
    <li><a href="https://doi.org/10.64898/2026.10.15.26364476">Multimodal artificial intelligence for cause-of-death assignment from verbal autopsy records: A national benchmark study in South Africa</a> — first and corresponding author; medRxiv preprint; submitted.</li>
    <li><a href="https://doi.org/10.64898/2026.07.13.26357980">A multimodal benchmark for evaluating cause-of-death inference using child health and mortality data</a> — medRxiv preprint; separate NeurIPS 2026 poster presented by the first author.</li>
    <li><a href="https://doi.org/10.1080/16549716.2021.1982486">Estimating causes of death where there is no medical certification: Evolution and state of the art of verbal autopsy</a> — <em>Global Health Action</em>.</li>
    <li><a href="https://github.com/y-chu/MultimodalVA">MultimodalVA</a> — open-source Python package and reproducible modeling workflow.</li>
    <li><a href="/publication/mits-beyond-verbal-autopsy/">How much post-mortem testing does cause-of-death surveillance need?</a> — ongoing research.</li>
  </ol>
</section>

<section class="research-program" id="demographic-inference">
  <h2>Demographic Inference Under Incomplete and Misclassified Data</h2>

  <p>Many demographic quantities cannot be observed directly. Summary birth histories compress a woman's full fertility and child-survival experience; household surveys omit or misclassify events; surveillance sites cover selected populations; and registration systems vary in completeness. I develop and apply methods that recover fertility, mortality, and cause-of-death patterns while making the limits of the underlying evidence explicit.</p>

  <p>I bring together demographic models, Bayesian inference, epidemiologic evidence synthesis, and uncertainty propagation to recover population patterns without hiding the limits of the underlying evidence. This includes estimation from summary birth histories, age patterns of fertility and mortality, multi-country surveillance analyses, and national or subnational mortality estimation. The aim is not to erase differences among survey, surveillance, registration, and modeled data, but to determine when their selection and error processes change the conclusion.</p>

  <h3>Questions I ask</h3>
  <ul>
    <li>How can fertility and child-mortality schedules be jointly estimated from compressed or incomplete reproductive histories?</li>
    <li>How should uncertainty from reporting and cause classification propagate into mortality rates and population cause fractions?</li>
    <li>How can survey, surveillance, registration, and modeled evidence be compared or combined without erasing their different selection and error processes?</li>
  </ul>

  <h3>Current and ongoing work</h3>
  <p><strong>SBH-Bayes</strong> illustrates this agenda by jointly estimating fertility and child mortality schedules from summary birth histories, which compress a woman's full reproductive history into a small set of counts. The original SVD-Bayes study was co-conceived with Samuel Clark, including its Bayesian framework and simulation-first strategy. I am now independently extending that foundation through a reformulated likelihood, redesigned empirical analysis, broader research questions, continued data processing, and tests of modeling assumptions.</p>

  <p>Related work examines changing age at last birth during fertility decline and cause-specific mortality patterns across heterogeneous surveillance and national data systems. In a collaborative <em>Annals of Applied Statistics</em> study of age- and cause-specific child mortality, I contributed to the early analysis design. Together, these projects show how the same inferential problem recurs across different demographic quantities: the observed data are partial, but their limitations can be represented rather than ignored.</p>

  <figure class="research-figure research-figure--wide">
    <img src="/images/research/svdbayes-fertility-schedules.png" alt="Estimated age-specific fertility schedules using one to four SVD components across example populations">
    <figcaption>SVD-derived components reconstruct flexible age-specific fertility schedules from compressed demographic information and provide the foundation for joint Bayesian estimation from summary birth histories.</figcaption>
  </figure>

  <h3>Selected publications and ongoing work</h3>
  <ol class="example-paper-list">
    <li><a href="/publication/joint-fertility-child-mortality-summary-birth-histories/">Joint estimation of fertility and child mortality schedules from summary birth histories: A Bayesian model in the Brass tradition</a> — manuscript in preparation.</li>
    <li><a href="https://doi.org/10.1016/S2214-109X(24)00171-2">Temporal changes in cause of death among adolescents and adults in six countries in eastern and southern Africa</a> — first and corresponding author, <em>Lancet Global Health</em>.</li>
    <li><a href="https://doi.org/10.1016/S2214-109X(19)30080-4">National, regional, and state all-cause and cause-specific under-five mortality in India</a> — joint first author, <em>Lancet Global Health</em>.</li>
    <li><a href="https://doi.org/10.1214/21-AOAS1489">A flexible Bayesian framework to estimate age- and cause-specific child mortality over time</a> — <em>Annals of Applied Statistics</em>.</li>
    <li><a href="/publication/casterline-age-at-last-birth/">Changes in age at last birth over the course of contemporary fertility declines</a> — manuscript under review.</li>
  </ol>
</section>

<p class="research-sequence">These themes form one research program rather than three separate topics. I trace how bias enters population-health data; determine when the available information is sufficient for a decision; test whether an inference remains valid across populations and collection settings; redesign instruments, validation studies, and monitoring systems in response; and assess when the remaining uncertainty changes a demographic or public-health conclusion.</p>

## Research Approach

<dl class="research-approach">
  <div><dt>Applied population health and demography</dt><dd>I begin with consequential measurement, surveillance, and estimation problems in real health-data systems, especially where routine information is incomplete.</dd></div>
  <div><dt>Statistical and computational methods</dt><dd>I develop and apply methods for bias assessment, survey validation, Bayesian demographic estimation, multimodal classification, calibration, and uncertainty propagation.</dd></div>
  <div><dt>Data and research infrastructure</dt><dd>I build reusable software, harmonized data resources, metadata and APIs, and secure collaborative environments when a research question requires methods and data to remain usable beyond a single analysis.</dd></div>
</dl>

The <a href="https://data.who.int/platforms/rda">WHO-hosted Reference Data Archive</a> and <a href="https://github.com/y-chu/MultimodalVA">MultimodalVA</a> are the principal infrastructure examples. The former supports the curation, documentation, access, and reuse of mortality reference data; the latter turns multimodal cause-of-death methods into a reproducible research workflow.

## Additional Collaborative Research

I have also contributed to Bayesian prevalence estimation and clinical evidence synthesis, including statewide COVID-19 seroprevalence and systematic reviews of treatments for diabetes and osteoporosis in chronic kidney disease. These collaborations broaden the settings in which I apply rigorous evidence assessment without constituting a fourth core research line.
