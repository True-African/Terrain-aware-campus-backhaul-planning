# Terrain-Aware Campus Wireless Backhaul Planning

This repository contains the paper, data, code, and figures for:

**Terrain-Aware Multi-Objective Optimization of Campus Wireless Backhaul Links Using Link-Budget Modeling and Radio Mobile Validation**

The study evaluates a 7.159 km point-to-point 5.8 GHz campus backhaul link between the Nyarugenge and Remera sites. It combines analytical link-budget modeling with Radio Mobile terrain-aware simulations to choose antenna height and gain while satisfying fade-margin constraints and minimizing deployment burden.

## Authors

- Simeon Nsabiyumva, corresponding author
- Samuel Babalola
- David Tuyishimire
- Isaac Museveni

Faculty of Software Engineering, African Leadership University, Kigali, Rwanda.

## Repository Contents

- `draft_paper.tex`: LaTeX manuscript source.
- `draft_paper.pdf`: compiled manuscript.
- `references.bib`: BibTeX references.
- `analyze_radio_mobile_results.py`: Python analysis script.
- `data/`: raw and processed Radio Mobile data.
- `figures/`: generated plots used in the paper.
- `CODEBOOK.md`: description of data files and fields.
- `DATA_AVAILABILITY.md`: data-sharing notes and DOI placeholder.

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

## Build the Paper

With a LaTeX distribution installed:

```bash
latexmk -pdf draft_paper.tex
```

or:

```bash
pdflatex draft_paper.tex
bibtex draft_paper
pdflatex draft_paper.tex
pdflatex draft_paper.tex
```

## Citation

After creating a Zenodo DOI, update `CITATION.cff` and cite the repository using the DOI.

