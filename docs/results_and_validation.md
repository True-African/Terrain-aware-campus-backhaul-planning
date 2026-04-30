# Results and Validation

## Radio Mobile Matrix

The 30-scenario matrix was run at 5825 MHz using the corrected Nyarugenge and Remera campus sites. The completed rows are saved in:

- `data/radio_mobile_expanded_results.csv`
- `data/radio_mobile_expanded_with_model.csv`

Raw Radio Mobile HTML pages are saved in:

- `data/raw_radio_mobile_html/`

## Feasibility Summary

- 30 completed Radio Mobile scenarios.
- 23 scenarios meet a 20 dB fade-margin threshold.
- 13 scenarios meet a 30 dB fade-margin threshold.
- Fade-margin range: 0.23 dB to 53.68 dB.

## Recommended Designs

Using the normalized deployment-burden objective:

- 20 dB fade-margin target: `RP_5825_H05_G10`, height 5 m, gain 10 dBi, fade margin 21.86 dB.
- 30 dB fade-margin target: `RP_5825_H05_G16`, height 5 m, gain 16 dBi, fade margin 33.86 dB.

## Validation Metrics

| Model | Required fade margin (dB) | MAE Rx (dB) | RMSE Rx (dB) | MAE fade margin (dB) | Feasibility agreement |
|---|---:|---:|---:|---:|---:|
| FSPL only | 20 | 8.337 | 12.030 | 8.337 | 0.767 |
| FSPL only | 30 | 8.337 | 12.030 | 8.337 | 0.633 |
| FSPL plus average terrain/statistical correction | 20 | 6.574 | 8.673 | 6.574 | 0.767 |
| FSPL plus average terrain/statistical correction | 30 | 6.574 | 8.673 | 6.574 | 0.833 |
| FSPL plus height-calibrated correction | 20 | 0.043 | 0.043 | 0.043 | 1.000 |
| FSPL plus height-calibrated correction | 30 | 0.043 | 0.043 | 0.043 | 1.000 |

The height-calibrated correction is a simulation calibration against Radio Mobile, not field validation.

## Generated Figures

- `figures/received_signal_vs_height.png`
- `figures/fade_margin_vs_height.png`
- `figures/fade_margin_heatmap.png`
- `figures/model_error_by_height.png`
- `figures/cost_vs_fade_margin.png`

