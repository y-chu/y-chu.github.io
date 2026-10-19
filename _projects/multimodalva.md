---
title: "MultimodalVA"
collection: projects
permalink: /projects/multimodalva/
redirect_from:
  - /projects/automating-verbal-autopsy/
date: 2025-01-01
status: active
project_group: active
role: "Developer and maintainer"
excerpt: "A Python package for cause-of-death classification from verbal autopsy data using narrative, structured, and multimodal models."
problem: "Most automated verbal autopsy algorithms use only structured questionnaire responses and leave the free-text narrative unused."
contribution: "Designed and implemented a unified Python package for narrative-only, structured-data, and multimodal models, with shared training, prediction, optimization, evaluation, and visualization workflows."
technical_scope: "Python, pretrained language models, machine learning, multimodal learning (data fusion, feature fusion, soft voting, stacking), hyperparameter optimization, and model evaluation."
outputs: "Open-source research software underlying my dissertation research on verbal autopsy."
tags:
  - "Python"
  - "Language Models"
  - "Multimodal Learning"
  - "Verbal Autopsy"
links:
  - label: "GitHub"
    url: "https://github.com/y-chu/MultimodalVA"
  - label: "Preprint (medRxiv)"
    url: "https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1"
  - label: "Dissertation preprint"
    url: "https://arxiv.org/abs/2508.19274"
---

Verbal autopsy interviews record both structured symptom questions and a free-text narrative of the circumstances before a death. MultimodalVA brings the two sources together in one reproducible workflow, so researchers can train and compare narrative-only, structured-data, and multimodal cause-of-death classifiers under consistent data splits and evaluation metrics.

[GitHub](https://github.com/y-chu/MultimodalVA) · [Preprint (medRxiv)](https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1) · [Dissertation preprint](https://arxiv.org/abs/2508.19274)

## Package scope

- Text classification of verbal autopsy narratives with pretrained language models
- Classification of structured symptom-response data with machine learning models
- Multimodal pipelines that combine narratives and structured responses
- Shared utilities for data splitting, training, hyperparameter optimization, scoring, and visualization
