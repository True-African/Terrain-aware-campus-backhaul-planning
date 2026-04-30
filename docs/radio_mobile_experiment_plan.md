# Radio Mobile Experiment Plan

## Purpose

The current four scenarios are pilot evidence. The journal paper needs an expanded matrix so the analytical model can be validated against Radio Mobile outputs with error metrics and feasibility classification.

## Fixed Sites

| Site | Latitude | Longitude | Elevation |
|---|---:|---:|---:|
| Nyarugenge campus Q3 | 45.70348900 | 13.72081800 | 57.70 m |
| Remera campus Q3 | 45.64337000 | 13.75378700 | 14.10 m |

Distance from current Radio Mobile runs: 7.159 km.

## Saved Pilot Scenarios

| Scenario | Frequency (MHz) | Height (m) | Gain (dBi) | Received signal (dBm) | Fade margin (dB) |
|---|---:|---:|---:|---:|---:|
| Q3 baseline WiFi 5825 MHz 15m 19dBi | 5825 | 15 | 19 | -77.06 | 35.96 |
| Q3 lower height WiFi 5825 MHz 10m 19dBi | 5825 | 10 | 19 | -69.48 | 43.54 |
| Q3 lower gain WiFi 5825 MHz 15m 16dBi | 5825 | 15 | 16 | -83.06 | 29.96 |
| Q3 stronger height WiFi 5825 MHz 20m 19dBi | 5825 | 20 | 19 | -94.79 | 18.23 |

## Minimum Expanded Matrix

Use one frequency first:

- Frequency: 5825 MHz.
- Antenna heights: 5 m, 10 m, 15 m, 20 m, 25 m, 30 m.
- Antenna gains: 10 dBi, 12 dBi, 16 dBi, 19 dBi, 24 dBi.
- Transmit power: keep constant at 0.1 W for the first matrix.
- Symmetric antennas: same height and gain at both ends for first validation.

This gives:

\[
6 \times 5 = 30
\]

successful 5.8 GHz runs if all are accepted by the account.

## Optional Frequency Extension

After the 5825 MHz matrix is completed, test additional account-permitted bands if available. The exact permitted values should be recorded from Radio Mobile before running:

- another permitted 5 GHz channel if available;
- a 2.4 GHz WiFi-style band if available;
- a sub-GHz proxy only if the account permits it.

The 600 MHz TVWS trial must be reported as rejected by the current account unless a permitted TVWS-like band is available. Do not fabricate lower-frequency results.

## Receiver and Link Assumptions

Initial values inferred from the assignment runs:

- Transmit power: 0.1 W, equivalent to 20 dBm.
- Receiver sensitivity: approximately -113.02 dBm inferred from \(P_{rx}\) and fade margin.
- Required fade margin for journal experiments: test at 20 dB and 30 dB.
- Line losses: record the values shown in Radio Mobile for each run. If not explicitly shown, state the default setting used in the account.
- Reliability/statistical setting: record the Radio Mobile reliability/statistical settings before data collection.

## Data to Collect for Each Run

Store raw rows in `research_paper/data/radio_mobile_expanded_results.csv` with these columns:

```csv
run_id,site_a,site_b,frequency_mhz,height_tx_m,height_rx_m,gain_tx_dbi,gain_rx_dbi,tx_power_w,tx_power_dbm,line_loss_tx_db,line_loss_rx_db,distance_km,free_space_loss_db,obstruction_loss_db,statistical_loss_db,clutter_loss_db,total_path_loss_db,received_signal_dbm,receiver_sensitivity_dbm,fade_margin_db,required_fade_margin_db,feasible,radio_mobile_link_name,notes
```

## Naming Convention in Radio Mobile

Use names that are easy to audit:

```text
RP 5825MHz H05 G10
RP 5825MHz H05 G12
...
RP 5825MHz H30 G24
```

If additional frequency bands are used:

```text
RP <freq>MHz H<height> G<gain>
```

## Validation Workflow

1. Generate the 30-run 5825 MHz matrix in Radio Mobile.
2. Save every run under `My Links`.
3. Export or manually record the full output variables.
4. Compute FSPL analytically.
5. Compare model-predicted received signal with Radio Mobile received signal.
6. Fit the terrain/statistical correction model.
7. Recompute MAE, RMSE, fade-margin deviation, and feasibility agreement.
8. Select the minimum-cost feasible configuration.

## Plots to Produce

Save plots in `research_paper/figures/`:

- received signal vs. antenna height for each gain;
- fade margin vs. antenna height for each gain;
- total path loss vs. antenna height;
- obstruction loss heatmap over height and gain;
- model error plot;
- Pareto frontier of deployment cost vs. fade margin.

