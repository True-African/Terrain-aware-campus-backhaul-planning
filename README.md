# Terrain-Aware Campus Backhaul Planning Dataset

This repository contains the data, analysis code, and generated figures for a terrain-aware wireless backhaul planning study.

The project evaluates a 7.159 km point-to-point 5.8 GHz campus backhaul link between the Nyarugenge and Remera sites. It uses Radio Mobile simulation outputs and a link-budget analysis script to compare antenna-height and antenna-gain configurations under fade-margin constraints.

## Repository Contents

- `analyze_radio_mobile_results.py`: Python script for processing Radio Mobile results, computing validation metrics, and generating figures.
- `data/`: raw and processed Radio Mobile data.
- `figures/`: generated plots from the analysis.
- `CODEBOOK.md`: description of data files and fields.
- `DATA_AVAILABILITY.md`: notes for public data archiving and DOI replacement.
- `requirements.txt`: Python dependency list.

## Data

The main processed datasets are:

- `data/radio_mobile_expanded_results.csv`
- `data/radio_mobile_expanded_with_model.csv`
- `data/validation_metrics.csv`

The raw Radio Mobile HTML exports are in:

- `data/raw_radio_mobile_html/`

## Reproduce the Analysis

Install the required Python dependency:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python analyze_radio_mobile_results.py
```

This regenerates the model-augmented CSV, validation metrics, summary file, and figures.

## Suggested Repository Description

A reproducible dataset and analysis workflow for optimizing antenna height and gain on a 5.8 GHz campus backhaul link using Radio Mobile outputs and link-budget validation.

