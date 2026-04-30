# Terrain-Aware Campus Backhaul Planning Dataset

This project evaluates a 7.159 km point-to-point 5.8 GHz campus backhaul link between the Nyarugenge and Remera sites (in Rwanda). It uses Radio Mobile simulation outputs and a link-budget analysis script to compare antenna-height and antenna-gain configurations under fade-margin constraints.

The repository is organized as a reproducibility package: raw simulation exports, processed datasets, analysis code, and generated figures are kept together so the results can be inspected or regenerated.

## Preprint

Find full paper at:

[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=REPLACE_SSRN_ID](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=REPLACE_SSRN_ID)

Replace `REPLACE_SSRN_ID` with the SSRN abstract ID after the preprint is published.

## Structure

- [analyze_radio_mobile_results.py](analyze_radio_mobile_results.py): processes the Radio Mobile data, computes validation metrics, and regenerates the figures.
- [data/radio_mobile_expanded_results.csv](data/radio_mobile_expanded_results.csv): processed Radio Mobile results for all simulated height/gain scenarios.
- [data/radio_mobile_expanded_with_model.csv](data/radio_mobile_expanded_with_model.csv): processed results with link-budget model predictions added.
- [data/validation_metrics.csv](data/validation_metrics.csv): model error and feasibility-agreement metrics.
- [data/validation_summary.md](data/validation_summary.md): short text summary of the validation results.
- [data/raw_radio_mobile_html/](data/raw_radio_mobile_html/): raw Radio Mobile HTML exports.
- [figures/](figures/): generated plots.
- [CODEBOOK.md](CODEBOOK.md): field descriptions for the main datasets.
- [requirements.txt](requirements.txt): Python dependency list.

## Reproduce the Analysis

Install the Python dependency:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python analyze_radio_mobile_results.py
```

The script regenerates the model-augmented dataset, validation metrics, validation summary, and figures.

## Repository Description

A reproducible dataset and analysis workflow for optimizing antenna height and gain on a 5.8 GHz campus backhaul link using Radio Mobile outputs and link-budget validation.
