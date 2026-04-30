# Research Walkthrough and Defense Guide

This README explains the complete workflow used to build the research paper, from the assignment idea to the analytical equations, Radio Mobile simulations, validation plots, and final deployment recommendation. It is written for presentation and panel defense, especially for questions from a strict reviewer.

## 1. One-Minute Summary

The work studies a point-to-point campus wireless backhaul link between two fixed sites:

- Nyarugenge campus Q3: latitude `45.70348900`, longitude `13.72081800`, elevation `57.70 m`.
- Remera campus Q3: latitude `45.64337000`, longitude `13.75378700`, elevation `14.10 m`.

The link distance reported by Radio Mobile is `7.159 km`. The study asks:

> Which antenna height and antenna gain give a feasible 5.8 GHz backhaul link with enough fade margin, while keeping deployment burden low?

We used two connected methods:

1. Analytical link-budget modeling.
2. Radio Mobile terrain-aware simulation.

The analytical model gives the equations and feasibility rules. Radio Mobile gives terrain-sensitive path-loss results. The final recommendation comes from comparing the model and simulation across 30 scenarios.

## 2. What Was Actually Done

The research started from the assignment's Question 3, but the assignment had only a few comparison cases. For a stronger research workflow, the experiment was expanded to a matrix:

- Frequency: `5825 MHz`.
- Heights: `5, 10, 15, 20, 25, 30 m`.
- Gains: `10, 12, 16, 19, 24 dBi`.
- Total scenarios: `6 x 5 = 30`.

Each scenario was run in Radio Mobile using the same fixed sites, same frequency, same transmit power, same line losses, same receiver threshold, and same reliability setting. Only antenna height and gain changed.

The resulting dataset is:

- `data/radio_mobile_expanded_results.csv`

The model-augmented dataset is:

- `data/radio_mobile_expanded_with_model.csv`

The final manuscript is:

- `draft_paper.tex`
- `draft_paper.pdf`

## 3. Why This Is a Research Problem

Basic link-budget calculations are common, and Radio Mobile planning is also common. The research contribution is not "we used Radio Mobile." The contribution is the decision workflow:

1. Build a transparent analytical model.
2. Use Radio Mobile to introduce terrain-aware path-loss behavior.
3. Compare analytical predictions with simulated results.
4. Classify feasible and infeasible designs.
5. Select the lowest-burden feasible design.

A strict reviewer may ask why this is novel. The answer is:

> The novelty is the structured equipment-selection and validation workflow for a campus backhaul link, not the individual equations or the use of Radio Mobile alone.

## 4. Step-by-Step Workflow

### Step 1: Define the Link

The two endpoints were fixed in Radio Mobile:

| Site | Latitude | Longitude | Elevation |
|---|---:|---:|---:|
| Nyarugenge campus Q3 | 45.70348900 | 13.72081800 | 57.70 m |
| Remera campus Q3 | 45.64337000 | 13.75378700 | 14.10 m |

Radio Mobile computed the path distance as:

```text
Distance = 7.159 km
```

This distance is used in the analytical free-space path-loss equation.

### Step 2: Fix the Radio Assumptions

The fixed settings were:

| Parameter | Value |
|---|---:|
| Frequency | 5825 MHz |
| Transmit power | 0.1 W = 20 dBm |
| Transmitter line loss | 1 dB |
| Receiver line loss | 1 dB |
| Receiver threshold | 0.5 microvolt = about -113.02 dBm |
| Required reliability | 70% |
| Land cover | enabled |
| Two-ray option | enabled |

Only height and gain changed across the 30 scenarios. This matters because it makes the experiment controlled.

### Step 3: Build the 30-Scenario Matrix

Heights:

```text
5, 10, 15, 20, 25, 30 m
```

Gains:

```text
10, 12, 16, 19, 24 dBi
```

The matrix is:

```text
6 heights x 5 gains = 30 simulations
```

Each link was named with this pattern:

```text
RP 5825MHz H05 G10
RP 5825MHz H05 G12
...
RP 5825MHz H30 G24
```

This naming helps an examiner audit the Radio Mobile account and match a saved link to a CSV row.

## 5. How the Equations Were Derived

### 5.1 Received Signal Equation

The received signal is based on a standard link budget:

```text
Received power = transmitted power + gains - losses
```

In symbols:

```text
P_rx = P_tx + G_tx + G_rx - L_tx - L_rx - PL_total
```

Where:

- `P_rx` is received signal in dBm.
- `P_tx` is transmit power in dBm.
- `G_tx` is transmit antenna gain in dBi.
- `G_rx` is receive antenna gain in dBi.
- `L_tx` is transmitter line loss in dB.
- `L_rx` is receiver line loss in dB.
- `PL_total` is total path loss in dB.

Why addition and subtraction?

- Power and gains are positive contributors.
- Cable/line losses and propagation losses reduce received signal.
- Everything is in dB/dBm, so multiplication in linear units becomes addition/subtraction in decibel units.

Example using `RP_5825_H05_G10`:

```text
P_tx       = 20.00 dBm
G_tx       = 10.00 dBi
G_rx       = 10.00 dBi
L_tx       = 1.00 dB
L_rx       = 1.00 dB
PL_total   = 129.16 dB
```

So:

```text
P_rx = 20 + 10 + 10 - 1 - 1 - 129.16
P_rx = -91.16 dBm
```

Radio Mobile reports:

```text
Received signal = -91.16 dBm
```

This confirms that the analytical link-budget equation maps directly to the Radio Mobile output.

### 5.2 Free-Space Path Loss

Free-space path loss estimates spreading loss when the signal travels through ideal unobstructed space:

```text
PL_FS = 32.44 + 20log10(d) + 20log10(f)
```

Where:

- `d` is distance in km.
- `f` is frequency in MHz.
- `32.44` is the unit-conversion constant for km and MHz.

For this study:

```text
d = 7.159 km
f = 5825 MHz
```

So:

```text
PL_FS = 32.44 + 20log10(7.159) + 20log10(5825)
PL_FS ≈ 124.80 dB
```

Radio Mobile reports the same free-space loss:

```text
Free space loss = 124.80 dB
```

This is important because it proves that our analytical FSPL part is aligned with Radio Mobile.

### 5.3 Why Total Path Loss Is Bigger Than FSPL

Radio Mobile does not stop at FSPL. It adds terrain and statistical effects. In the paper, this is written as:

```text
PL_total = PL_FS + L_terrain + L_stat + L_clutter + L_impl
```

In Radio Mobile fields, these appear as:

- free-space loss;
- obstruction loss;
- forest loss;
- urban loss;
- statistical loss;
- total path loss.

For `RP_5825_H05_G10`, Radio Mobile reports:

```text
Free-space loss    = 124.80 dB
Obstruction loss   = -3.18 dB
Forest loss        = 0.00 dB
Urban loss         = 1.00 dB
Statistical loss   = 6.54 dB
Total path loss    = 129.16 dB
```

Check:

```text
124.80 - 3.18 + 0.00 + 1.00 + 6.54 = 129.16 dB
```

That is why the model uses a correction term:

```text
L_corr = PL_RM - PL_FS
```

For the same case:

```text
L_corr = 129.16 - 124.80 = 4.36 dB
```

The correction is the part that FSPL alone misses.

### 5.4 Fade Margin

Fade margin measures how far the received signal is above the receiver sensitivity:

```text
FM = P_rx - P_sens
```

For `RP_5825_H05_G10`:

```text
P_rx   = -91.16 dBm
P_sens = -113.02 dBm
FM     = -91.16 - (-113.02)
FM     = 21.86 dB
```

Radio Mobile reports:

```text
Fade margin = 21.86 dB
```

So the fade-margin equation is also directly verified against Radio Mobile.

### 5.5 Feasibility Constraint

A link is feasible if:

```text
FM >= FM_required
```

We tested two thresholds:

```text
20 dB: moderate planning threshold
30 dB: more conservative planning threshold
```

Results:

```text
23 of 30 scenarios satisfy 20 dB
13 of 30 scenarios satisfy 30 dB
```

### 5.6 Maximum Allowable Path Loss

The maximum allowable path loss answers:

> How much path loss can the link tolerate before it fails the required fade margin?

Start from:

```text
P_rx = P_tx + G_tx + G_rx - L_tx - L_rx - PL_total
```

For feasibility:

```text
P_rx >= P_sens + FM_required
```

Substitute:

```text
P_tx + G_tx + G_rx - L_tx - L_rx - PL_total >= P_sens + FM_required
```

Rearrange for `PL_total`:

```text
PL_total <= P_tx + G_tx + G_rx - L_tx - L_rx - P_sens - FM_required
```

So:

```text
PL_max = P_tx + G_tx + G_rx - L_tx - L_rx - P_sens - FM_required
```

This equation is useful because it converts a design target into a path-loss limit.

## 6. How the Equations Map to Radio Mobile

| Model Quantity | Radio Mobile Field |
|---|---|
| `P_tx` | TX power |
| `G_tx` | TX antenna gain |
| `G_rx` | RX antenna gain |
| `L_tx` | TX line loss |
| `L_rx` | RX line loss |
| `P_sens` | RX sensitivity |
| `PL_FS` | Free space loss |
| `L_terrain` | Obstruction loss |
| `L_clutter` | Forest loss + urban loss |
| `L_stat` | Statistical loss |
| `PL_total` | Total path loss |
| `P_rx` | Received Signal in dBm |
| `FM` | Fade Margin |

This table is one of the most important defense tools. It shows that the equations are not disconnected from the simulation. The equations explain the same variables that Radio Mobile reports.

## 7. How the Radio Mobile Simulation Was Run

The workflow was:

1. Log in to Radio Mobile.
2. Confirm the corrected sites exist under `My Sites`.
3. Open `New Link`.
4. Select:
   - From: `Nyarugenge campus Q3`.
   - To: `Remera campus Q3`.
5. Set antenna height for both ends.
6. Set frequency to `5825 MHz`.
7. Set transmit power to `0.1 W`.
8. Set TX line loss to `1 dB`.
9. Set RX line loss to `1 dB`.
10. Set TX/RX antenna gain according to the scenario.
11. Set receiver threshold to `0.5 microvolt`.
12. Set required reliability to `70%`.
13. Enable land cover.
14. Enable two-ray option.
15. Submit the link.
16. Record the Radio Mobile output.
17. Save the link under `My Links`.
18. Repeat for the next height/gain combination.

The process was automated after verifying that the baseline case reproduced the assignment result exactly:

```text
Baseline 15 m / 19 dBi:
Received signal = -77.06 dBm
Fade margin     = 35.96 dB
```

This verification step matters. It confirms that the automation used the same settings as the manually saved assignment result.

## 8. How the Plots Were Created

Radio Mobile produced the raw link-budget outputs. The plots were generated from the CSV results using:

- `analyze_radio_mobile_results.py`

The script reads:

- `data/radio_mobile_expanded_results.csv`

Then it computes:

- FSPL model received signal;
- average-correction model received signal;
- height-calibrated model received signal;
- prediction errors;
- feasibility classifications;
- deployment burden.

The generated plots are saved in:

- `figures/received_signal_vs_height.png`
- `figures/fade_margin_vs_height.png`
- `figures/fade_margin_heatmap.png`
- `figures/model_error_by_height.png`
- `figures/cost_vs_fade_margin.png`

### 8.1 Received Signal vs Height

This plot shows received signal in dBm for each height and gain.

Main message:

> Increasing antenna gain improves received signal, but increasing height does not always improve the link.

Reason:

> Height changes the terrain obstruction term. At 20 m, Radio Mobile reports a high obstruction loss, so received signal becomes worse.

### 8.2 Fade Margin vs Height

This plot shows whether each scenario clears the 20 dB or 30 dB fade-margin target.

Main message:

> Some low-height cases are feasible, while some higher-height cases are not.

This supports the paper's recommendation not to use a simple "higher antenna is always better" rule.

### 8.3 Fade Margin Heatmap

This plot shows height on one axis, gain on the other axis, and fade margin as color.

Main message:

> It gives a quick feasibility map for design selection.

It helps answer:

- Which configurations meet 20 dB?
- Which configurations meet 30 dB?
- Which configurations fail?

### 8.4 Model Error by Height

This plot compares analytical predictions with Radio Mobile.

Models compared:

1. FSPL only.
2. FSPL plus average terrain/statistical correction.
3. FSPL plus height-calibrated correction.

Main message:

> FSPL alone misses terrain-sensitive behavior. Height-calibrated correction tracks Radio Mobile closely because it uses the height-specific Radio Mobile loss behavior.

Defense wording:

> We are not claiming field measurement accuracy. We are showing how much terrain-aware simulation deviates from FSPL and how calibration reduces that simulation mismatch.

### 8.5 Deployment Burden vs Fade Margin

This plot ranks configurations by a cost-like objective:

```text
C = 0.55(height / max height) + 0.45(gain / max gain)
```

Why this objective?

- Taller masts increase installation burden.
- Higher-gain antennas may increase cost and alignment sensitivity.
- Height was weighted slightly more because mast height often drives civil-work and permission difficulty.

Main result:

```text
20 dB target: 5 m / 10 dBi
30 dB target: 5 m / 16 dBi
```

## 9. Important Results to Memorize

### 9.1 Best Designs

| Fade-margin target | Best design | Fade margin |
|---|---|---:|
| 20 dB | 5 m, 10 dBi | 21.86 dB |
| 30 dB | 5 m, 16 dBi | 33.86 dB |

### 9.2 Feasibility Counts

```text
20 dB threshold: 23 / 30 feasible
30 dB threshold: 13 / 30 feasible
```

### 9.3 Model Validation

| Model | MAE Rx | RMSE Rx |
|---|---:|---:|
| FSPL only | 8.337 dB | 12.030 dB |
| FSPL + average correction | 6.574 dB | 8.673 dB |
| FSPL + height correction | 0.043 dB | 0.043 dB |

### 9.4 Height-Specific Terrain Behavior

| Height | Obstruction loss | Total path loss |
|---:|---:|---:|
| 5 m | -3.18 dB | 129.16 dB |
| 10 m | -5.87 dB | 125.48 dB |
| 15 m | 1.71 dB | 133.06 dB |
| 20 m | 19.43 dB | 150.79 dB |
| 25 m | 3.89 dB | 135.25 dB |
| 30 m | -6.02 dB | 125.34 dB |

Key interpretation:

> Height does not behave monotonically because changing height changes the terrain profile, Fresnel clearance, and obstruction contribution calculated by Radio Mobile.

## 10. Case-by-Case Explanation of the Results

### Case 1: 5 m Height

At 5 m, Radio Mobile gives total path loss of `129.16 dB`. The lowest gain case, `10 dBi`, still gives:

```text
Received signal = -91.16 dBm
Fade margin     = 21.86 dB
```

This passes the 20 dB threshold but not the 30 dB threshold. Increasing gain to 16 dBi gives:

```text
Fade margin = 33.86 dB
```

That becomes the minimum-burden design for the conservative 30 dB target.

### Case 2: 10 m Height

At 10 m, total path loss is `125.48 dB`, the second-lowest path loss in the matrix. This height performs strongly. For 19 dBi gain:

```text
Received signal = -69.48 dBm
Fade margin     = 43.54 dB
```

This matches the earlier assignment comparison.

### Case 3: 15 m Height

At 15 m, total path loss increases to `133.06 dB`. The 15 m / 19 dBi baseline gives:

```text
Received signal = -77.06 dBm
Fade margin     = 35.96 dB
```

This is feasible, but it is not the minimum-burden solution.

### Case 4: 20 m Height

At 20 m, Radio Mobile reports:

```text
Obstruction loss = 19.43 dB
Total path loss  = 150.79 dB
```

This is the weakest height in the matrix. Even at 19 dBi:

```text
Fade margin = 18.23 dB
```

That fails the 20 dB threshold. This is the strongest evidence that antenna height should be optimized rather than simply increased.

### Case 5: 25 m Height

At 25 m, total path loss drops to `135.25 dB`, better than 20 m but worse than 5, 10, and 30 m. It can be feasible at moderate or high gains, but it is not the best burden-margin tradeoff.

### Case 6: 30 m Height

At 30 m, total path loss is `125.34 dB`, slightly better than 10 m. It gives strong margins, especially at 19 and 24 dBi. However, the deployment-burden objective penalizes height, so 30 m is not selected as the minimum-burden solution.

## 11. How Equations and Radio Mobile Support Each Other

The equations explain the physics and accounting:

- FSPL explains distance and frequency spreading loss.
- Link budget explains how power, gain, losses, and path loss combine.
- Fade margin explains feasibility.
- Optimization explains design selection.

Radio Mobile supplies the terrain-aware correction:

- obstruction loss;
- forest/urban loss;
- statistical loss;
- total path loss.

Together:

```text
Equations give structure.
Radio Mobile gives terrain-aware numerical values.
Validation checks whether the equation-based predictions match the simulation outputs.
Optimization chooses the preferred feasible design.
```

## 12. What a Harsh Reviewer May Ask

### Q1. Is this really novel?

Answer:

> The equations and Radio Mobile tool are not new. The contribution is the structured workflow that combines link-budget modeling, terrain-aware simulation, validation metrics, and deployment-burden optimization for a campus backhaul link.

Do not say:

> We invented a new propagation model.

Say:

> We created and tested a decision model for selecting feasible low-burden antenna settings using Radio Mobile as terrain-aware validation.

### Q2. Why is Radio Mobile validation enough?

Answer:

> It is enough for simulation validation, not field validation. The paper states this limitation clearly. Field RSS measurements would be the next stage.

This is important because a reviewer may object that simulation is not reality. Agree with that boundary.

### Q3. Why did you not use field measurements?

Answer:

> The current work focuses on planning-stage validation against a terrain-aware simulation tool. Field measurements require installed equipment and site access. The paper treats field validation as future work.

### Q4. Why use 5825 MHz only?

Answer:

> The Radio Mobile account accepted 5825 MHz. A 600 MHz TVWS trial was rejected because the account was restricted to predefined bands. We did not fabricate lower-frequency results.

This is a strength, not a weakness, because it shows integrity.

### Q5. Why does 20 m perform worse than 10 m and 30 m?

Answer:

> Radio Mobile reported a much larger obstruction loss at 20 m: 19.43 dB. The terrain/Fresnel interaction changes with antenna height, so height is not monotonic in this path.

### Q6. Is negative obstruction loss physically meaningful?

Answer:

> In the Radio Mobile output, obstruction loss is a model component relative to the free-space baseline and terrain profile. A negative value means the terrain-profile correction reduced the total loss relative to the free-space-plus-statistical/clutter accounting. We report it as Radio Mobile provides it and validate using total path loss.

If pressed:

> The design decision is based on total path loss, received signal, and fade margin, not on obstruction loss alone.

### Q7. Why are gain changes so linear?

Answer:

> At fixed height, distance, frequency, and terrain losses are unchanged. In a dB link budget, increasing gain by 1 dB at each end increases received signal by 2 dB. That is why gain changes are linear across a fixed height.

Example:

At 5 m:

- 10 dBi gain gives `-91.16 dBm`.
- 12 dBi gain gives `-87.16 dBm`.

The gain increased by 2 dB at both ends, so total antenna gain increased by 4 dB, and received signal improved by 4 dB.

### Q8. Why does the height-calibrated correction have such low error?

Answer:

> Because Radio Mobile's terrain/statistical loss is constant across gain at each fixed height. Once the height-specific correction is calibrated, the remaining link-budget calculation is almost exact. This is simulation calibration, not independent field prediction.

This answer is crucial. Do not oversell the `0.043 dB` error.

### Q9. Did you overfit?

Answer:

> The height-calibrated model is fitted to the same Radio Mobile matrix, so it should be described as calibrated simulation matching. The paper compares it against simpler FSPL and average-correction baselines to show the value of height-specific terrain correction. A stronger future paper would validate the fitted correction on additional paths or held-out heights.

### Q10. Why choose 20 dB and 30 dB fade margins?

Answer:

> They are planning thresholds used to compare moderate and conservative designs. The paper does not claim they are universal. The method can use any fade-margin requirement chosen by the network operator.

### Q11. Why use a deployment-burden objective?

Answer:

> The engineering goal is not simply maximum received signal. Very tall masts and high-gain antennas may cost more, require stronger mounting, and increase alignment burden. The objective formalizes the tradeoff between feasibility and deployment burden.

### Q12. Why is height weighted 0.55 and gain 0.45?

Answer:

> This is a first planning assumption. Height was weighted slightly more because mast height often drives installation complexity, permissions, safety, and cost. Sensitivity analysis can be added by varying the weights.

If a reviewer challenges it:

> The selected weights are transparent, and the dataset allows recalculation with other weights.

### Q13. Why not include transmit power in the objective?

Answer:

> Transmit power was held constant at 0.1 W for experimental control. The general model includes transmit power, but this first matrix isolates height and gain effects.

### Q14. Why use symmetric antenna height and gain?

Answer:

> Symmetry reduces the search space and makes the first validation interpretable. Asymmetric height/gain planning can be added in future work.

### Q15. What is the role of two-ray propagation?

Answer:

> The two-ray option was enabled in Radio Mobile. The analytical model does not separately derive a two-ray term; instead, Radio Mobile's total path loss is treated as the terrain-aware simulation reference. The correction term absorbs the difference between FSPL and Radio Mobile total path loss.

### Q16. Why not use Okumura-Hata?

Answer:

> Okumura-Hata-type models are useful for empirical area coverage, especially cellular-style environments. This work is a fixed point-to-point terrain path at 5.8 GHz, so FSPL plus Radio Mobile terrain correction is more directly tied to the simulated link.

### Q17. Why is the receiver threshold in microvolts converted to dBm?

Answer:

Radio Mobile entered threshold as `0.5 microvolt` and reported sensitivity as `-113.02 dBm`. The equation uses dBm because the link budget is in dB/dBm. We used Radio Mobile's reported sensitivity directly.

### Q18. Why does the best 20 dB design have only 10 dBi antennas?

Answer:

> Because the 5 m / 10 dBi scenario still gives 21.86 dB fade margin. Since it satisfies the 20 dB requirement, higher gain would add margin but also increase deployment burden under the objective.

### Q19. Would you deploy the 20 dB design in real life?

Answer:

> It depends on the reliability requirement, interference environment, hardware quality, and weather fading. For a conservative deployment, the 30 dB design is safer. The paper reports both.

### Q20. What is the practical recommendation?

Answer:

> For moderate margin, use 5 m / 10 dBi. For a more conservative margin, use 5 m / 16 dBi. Avoid assuming that 20 m is better; Radio Mobile shows high obstruction loss at 20 m on this path.

## 13. Likely Q1 Reviewer Concerns and Clean Responses

### Concern: The manuscript is too site-specific.

Response:

> The paper is a site-specific case study with a reproducible method. The contribution is the workflow and validation structure. Generalization requires additional links, which are listed as future work.

### Concern: The dataset is small.

Response:

> The dataset contains 30 controlled simulations for one link. It is sufficient for a planning case study and method demonstration, but not for universal propagation-model claims.

### Concern: No independent validation set.

Response:

> Correct. The current validation compares analytical predictions against Radio Mobile outputs. A future extension should use held-out paths or field RSS measurements.

### Concern: The height-calibrated model is too close to Radio Mobile.

Response:

> That is expected because it is calibrated from Radio Mobile height-specific loss. The important result is the contrast with FSPL-only and average-correction models, not a claim of universal predictive accuracy.

### Concern: The novelty is not enough for a high-impact journal.

Response:

> For a high-impact journal, the work should be expanded to multiple links, additional permitted bands, independent validation, and sensitivity analysis. In its current form, it is strongest as a focused applied planning paper or conference/journal case study.

## 14. Likely Q2 Reviewer Concerns and Clean Responses

### Concern: The paper should define all variables.

Response:

> The model section defines transmit power, gains, line losses, path loss, receiver sensitivity, fade margin, height, frequency, and deployment burden. Any missing variable can be added to a notation table.

### Concern: The figures need stronger explanation.

Response:

> Each figure should be interpreted as part of the design workflow: received signal shows raw link quality, fade margin shows feasibility, heatmap shows design space, model error shows validation, and cost-margin plot shows final selection.

### Concern: The cost weights are arbitrary.

Response:

> They are transparent planning weights, not universal constants. A sensitivity analysis can be added by testing alternative weight pairs such as 0.5/0.5, 0.7/0.3, and 0.3/0.7.

### Concern: The paper needs stronger related work.

Response:

> The references already cover propagation modeling, radio-map prediction, uneven terrain, antenna optimization, wireless backhaul, Radio Mobile evaluation, and TVWS. The related-work section can be expanded if targeting a stricter journal.

### Concern: The coordinates look unusual for Rwandan campus names.

Response:

> The coordinates were provided by the assignment correction and were used consistently in Radio Mobile. The paper should describe them as the corrected experimental coordinates for the study link rather than making geographic claims beyond the provided setup.

## 15. Presentation Script

Use this order when presenting:

1. Start with the engineering problem: a campus backhaul link must be feasible without overbuilding.
2. Show the two sites and distance.
3. Explain the link-budget equation.
4. Show that FSPL from the equation matches Radio Mobile's FSPL.
5. Explain why Radio Mobile adds obstruction, urban/forest, and statistical losses.
6. Explain fade margin and feasibility.
7. Show the 30-scenario matrix.
8. Present the heatmap first because it summarizes feasibility.
9. Explain the surprising 20 m case.
10. Present validation metrics.
11. Present the deployment-burden objective.
12. Give the recommendation for 20 dB and 30 dB targets.
13. End with limitations and next work.

## 16. Short Defense Version

If the panel asks for a short explanation:

> We modeled the link with a standard dB link budget. The free-space loss is computed from distance and frequency, while Radio Mobile supplies terrain, clutter, and statistical corrections. We ran 30 simulations by varying height and gain. We then compared FSPL-only, average-corrected, and height-corrected analytical predictions against Radio Mobile. The results show that terrain effects make height non-monotonic: the 20 m case performs poorly because Radio Mobile reports high obstruction loss. The minimum-burden feasible design is 5 m / 10 dBi for a 20 dB margin, and 5 m / 16 dBi for a 30 dB margin. The work is simulation-validated, not field-validated, and future work should add measurements and more paths.

## 17. Files to Mention During Defense

| File | Purpose |
|---|---|
| `draft_paper.pdf` | Manuscript output |
| `draft_paper.tex` | LaTeX manuscript source |
| `data/radio_mobile_expanded_results.csv` | Raw 30-scenario Radio Mobile dataset |
| `data/radio_mobile_expanded_with_model.csv` | Dataset with analytical model predictions |
| `data/validation_metrics.csv` | MAE, RMSE, and feasibility agreement |
| `figures/fade_margin_heatmap.png` | Main design-space figure |
| `figures/model_error_by_height.png` | Validation error figure |
| `analyze_radio_mobile_results.py` | Script used to compute metrics and plots |
| `references.bib` | DOI-backed references |

## 18. What Not to Claim

Do not claim:

- that the paper invents link-budget theory;
- that Radio Mobile itself is new;
- that the model is field-validated;
- that 5 m / 10 dBi is universally best;
- that 20 dB or 30 dB is a universal fade-margin rule;
- that 600 MHz TVWS was simulated.

Safe claim:

> For the studied Radio Mobile terrain path and fixed 5825 MHz settings, the optimization workflow selects 5 m / 10 dBi for a 20 dB target and 5 m / 16 dBi for a 30 dB target.

## 19. Future Work to Offer

If the panel asks how to strengthen the paper:

1. Add field RSS measurements with real radios.
2. Add more campus or rural paths.
3. Test asymmetric antenna heights.
4. Add transmit-power optimization.
5. Add sensitivity analysis for deployment-burden weights.
6. Test additional account-permitted frequency bands.
7. Add an independent validation set or cross-validation by holding out some heights.
8. Compare Radio Mobile with another terrain tool such as SPLAT! or Longley-Rice/ITM implementation.

## 20. Final Takeaway

The central message is:

> Link-budget equations explain how the received signal is formed. Radio Mobile adds terrain-aware path-loss behavior. Validation shows that FSPL alone misses important height effects. Optimization then converts the simulation results into a practical antenna recommendation.

