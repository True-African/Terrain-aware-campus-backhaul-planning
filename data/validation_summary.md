# Validation Summary

Rows analyzed: 30
Average terrain/statistical correction: 8.38 dB

## Best feasible designs using normalized deployment burden

- Minimum-cost design for 20 dB fade margin: RP_5825_H05_G10, height 5 m, gain 10 dBi, fade margin 21.86 dB, cost 0.279.
- Minimum-cost design for 30 dB fade margin: RP_5825_H05_G16, height 5 m, gain 16 dBi, fade margin 33.86 dB, cost 0.392.

## Model validation metrics

| Model | Required fade margin (dB) | MAE Rx (dB) | RMSE Rx (dB) | MAE fade margin (dB) | Feasibility agreement |
|---|---:|---:|---:|---:|---:|
| FSPL only | 20 | 8.337 | 12.030 | 8.337 | 0.767 |
| FSPL only | 30 | 8.337 | 12.030 | 8.337 | 0.633 |
| FSPL plus average terrain/statistical correction | 20 | 6.574 | 8.673 | 6.574 | 0.767 |
| FSPL plus average terrain/statistical correction | 30 | 6.574 | 8.673 | 6.574 | 0.833 |
| FSPL plus height-calibrated correction | 20 | 0.043 | 0.043 | 0.043 | 1.000 |
| FSPL plus height-calibrated correction | 30 | 0.043 | 0.043 | 0.043 | 1.000 |

The height-calibrated correction is expected to fit Radio Mobile closely because the Radio Mobile terrain/statistical loss is constant across gain at a fixed height. This should be reported as simulation calibration, not field validation.
