# GitHub Upload Checklist

Upload the `research_paper` folder as the repository root.

## Include

- `draft_paper.tex`
- `draft_paper.pdf`
- `references.bib`
- `analyze_radio_mobile_results.py`
- `requirements.txt`
- `README.md`
- `GITHUB_README.md`
- `DATA_AVAILABILITY.md`
- `CODEBOOK.md`
- `CITATION.cff`
- `.gitignore`
- `data/baseline_radio_mobile_results.csv`
- `data/radio_mobile_expanded_results.csv`
- `data/radio_mobile_expanded_with_model.csv`
- `data/validation_metrics.csv`
- `data/validation_summary.md`
- `data/raw_radio_mobile_html/*.html`
- `figures/*.png`

## Optional but Useful

- `literature_review.md`
- `mathematical_model.md`
- `novelty_matrix.md`
- `paper_outline.md`
- `radio_mobile_experiment_plan.md`
- `research_gap_and_contribution.md`
- `results_and_validation.md`

## Do Not Upload Unless Needed

- LaTeX temporary files: `.aux`, `.bbl`, `.blg`, `.fdb_latexmk`, `.fls`, `.log`, `.synctex.gz`
- `drafts/` if it contains rough private notes
- `extracted_notes/` if the source lecture/assignment text should not be redistributed
- `research_gpt_prompt.md` unless you want to disclose the full prompting history

## After Uploading

1. Rename `GITHUB_README.md` to `README.md` if you want the concise GitHub page to be the landing page.
2. Add a license. Recommended: MIT for code and CC BY 4.0 for data/paper materials, if your team/instructor allows it.
3. Create a GitHub release.
4. Archive the release on Zenodo to get a DOI.
5. Replace the placeholder DOI in `draft_paper.tex`, `DATA_AVAILABILITY.md`, and `CITATION.cff`.

