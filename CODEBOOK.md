# Codebook

This codebook describes the main data files used by the analysis workflow.

## `data/radio_mobile_expanded_results.csv`

Processed Radio Mobile results for the 30 simulated scenarios.

Key fields:

- `run_id`: unique scenario identifier.
- `radio_mobile_link_name`: link name used in Radio Mobile.
- `site_a`, `site_b`: link endpoints.
- `frequency_mhz`: operating frequency in MHz.
- `height_tx_m`, `height_rx_m`: transmit and receive antenna heights in meters.
- `gain_tx_dbi`, `gain_rx_dbi`: transmit and receive antenna gains in dBi.
- `tx_power_w`, `tx_power_dbm`: transmit power in watts and dBm.
- `line_loss_tx_db`, `line_loss_rx_db`: cable/line losses in dB.
- `distance_km`: Radio Mobile link distance in kilometers.
- `free_space_loss_db`: free-space path loss reported by Radio Mobile.
- `obstruction_loss_db`: obstruction loss reported by Radio Mobile.
- `forest_loss_db`, `urban_loss_db`, `clutter_loss_db`: environmental loss components.
- `statistical_loss_db`: statistical propagation loss.
- `total_path_loss_db`: total Radio Mobile path loss.
- `received_signal_dbm`: received signal reported by Radio Mobile.
- `receiver_sensitivity_dbm`: receiver threshold used for fade-margin calculation.
- `fade_margin_db`: Radio Mobile fade margin.
- `required_reliability_percent`: reliability setting used in Radio Mobile.
- `feasible_fm20`: whether the scenario satisfies a 20 dB fade-margin target.
- `feasible_fm30`: whether the scenario satisfies a 30 dB fade-margin target.
- `notes`: scenario notes.

## `data/radio_mobile_expanded_with_model.csv`

The same scenario data with analytical-model columns added.

Additional fields:

- `height`, `gain`, `freq`, `distance`: normalized copies used by the analysis script.
- `tx_loss`, `rx_loss`: line-loss fields used by the model.
- `rx_signal_rm`, `rx_sens`, `fade_rm`: Radio Mobile received signal, receiver sensitivity, and fade margin.
- `fspl_rm`, `total_loss_rm`: Radio Mobile free-space and total path loss.
- `terrain_stat_loss`: difference between total path loss and free-space loss.
- `fspl_model`: analytical free-space path-loss estimate.
- `rx_fspl_only`: received-signal prediction using FSPL only.
- `rx_avg_corr`: received-signal prediction using average terrain/statistical correction.
- `rx_height_corr`: received-signal prediction using height-calibrated correction.
- `fade_fspl_only`: fade-margin prediction using FSPL only.
- `fade_avg_corr`: fade-margin prediction using average correction.
- `fade_height_corr`: fade-margin prediction using height-calibrated correction.

## `data/validation_metrics.csv`

Model-validation metrics reported in the paper.

Fields:

- `model`: analytical model variant.
- `required_fade_margin_db`: tested fade-margin threshold.
- `mae_received_signal_db`: mean absolute error of received-signal prediction.
- `rmse_received_signal_db`: root mean square error of received-signal prediction.
- `mae_fade_margin_db`: mean absolute error of fade-margin prediction.
- `feasibility_agreement`: fraction of scenarios where analytical feasibility agrees with Radio Mobile feasibility.

## `data/raw_radio_mobile_html/`

Raw Radio Mobile HTML outputs for each simulated scenario. Files ending in `_add.html` are additional Radio Mobile output pages associated with the same scenario.
