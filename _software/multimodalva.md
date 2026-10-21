---
layout: single
title: "MultimodalVA"
collection: software
permalink: /software/multimodalva/
redirect_from:
  - /projects/multimodalva/
  - /projects/automating-verbal-autopsy/
date: 2025-01-01
excerpt: "A Python package for cause-of-death classification from verbal autopsy data using narrative, structured, and multimodal models."
---

Verbal autopsy interviews record both structured symptom questions and a free-text narrative of the circumstances before a death. MultimodalVA brings the two sources together in one reproducible workflow, so researchers can train and compare narrative-only, structured-data, and multimodal cause-of-death classifiers under consistent data splits and evaluation metrics.

[GitHub](https://github.com/y-chu/MultimodalVA) · [Zenodo release](https://doi.org/10.5281/zenodo.23036919) · [Preprint (medRxiv)](https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1) · [Dissertation preprint](https://arxiv.org/abs/2508.19274)

## What it enables

- Prepare narrative and structured verbal-autopsy records for reproducible modeling
- Train narrative-only, indicator-only, and multimodal cause-of-death classifiers
- Compare data fusion, feature fusion, soft voting, and stacking under shared data splits and metrics
- Run hyperparameter optimization, evaluation, and visualization workflows
- Use prompt-based pipelines for open-weight chat models through Hugging Face or local serving with Ollama
