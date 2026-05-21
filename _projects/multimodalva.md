---
title: "MultimodalVA"
collection: projects
permalink: /projects/multimodalva/
redirect_from:
  - /projects/automating-verbal-autopsy/
  - /projects/2025Ensem_VA.md
date: 2025-01-01
status: active
project_group: active
role: "Developer and maintainer"
excerpt: "A Python package for cause-of-death classification from verbal autopsy data using text, tabular, and ensemble multimodal pipelines."
tags:
  - "Python"
  - "Machine Learning"
  - "Verbal Autopsy"
  - "Multimodal Learning"
links:
  - label: "GitHub repository"
    url: "https://github.com/y-chu/MultimodalVA"
  - label: "Research page"
    url: "/research/"
---

MultimodalVA is a Python package I developed for cause-of-death classification using verbal autopsy data. The package supports text-only, tabular-only, and ensemble workflows so researchers can work with narrative responses, structured questionnaire data, or both together in a unified modeling pipeline.

The package was built to make verbal autopsy modeling more reproducible and more extensible. It includes end-to-end training and prediction workflows, hyperparameter optimization support, evaluation tools, and multiple ensemble strategies for combining modalities.

## Package scope

- Text classification for verbal autopsy narratives
- Tabular classification for structured symptom-response data
- Ensemble and multimodal pipelines for combining text and tabular information
- Shared utilities for splitting data, training models, scoring predictions, and visualizing results

## Why it matters

Verbal autopsy data often contains both structured symptom questions and free-text narratives. MultimodalVA is designed to bring those information sources together in a practical research workflow, making it easier to experiment with models that better reflect the richness of the underlying data.

## Current focus

The package continues to support my broader work on AI for global health and verbal autopsy analysis, including model development, benchmarking, and more accessible tooling for research collaborators.
