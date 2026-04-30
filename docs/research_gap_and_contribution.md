# Research Gap and Contribution

## Novelty Decision

The proposed journal paper has a defensible contribution if it is framed as a terrain-aware optimization and validation framework. It is not defensible as a publication if it remains a short assignment-style case study with four Radio Mobile results.

## Recommended Title

Terrain-Aware Multi-Objective Optimization of Campus Wireless Backhaul Links Using Link-Budget Modeling and Radio Mobile Validation

## Problem Gap

Campus and institutional backhaul planning often requires practical choices about antenna height, antenna gain, transmit power, frequency band, and acceptable fade margin. Analytical link-budget calculations are transparent but miss terrain effects. Terrain-aware simulation tools include obstruction and statistical losses but do not automatically produce a cost-aware design recommendation.

The gap is therefore the decision layer between calculation and simulation: a method that searches feasible equipment choices, minimizes deployment burden, and validates the selected design against terrain-aware simulation outputs.

## Proposed Contribution

This paper will contribute:

1. A link-budget-based optimization model for point-to-point campus backhaul planning.
2. A terrain-aware correction structure that separates FSPL, obstruction/terrain loss, statistical loss, and clutter or implementation loss.
3. A multi-objective deployment-cost function covering antenna height, antenna gain, transmit power, and frequency-band burden.
4. A Radio Mobile validation workflow that compares analytical predictions with simulated received signal and fade margin.
5. A reproducible experiment matrix for the Nyarugenge--Remera campus link using saved Radio Mobile scenarios and additional planned runs.

## Research Questions

RQ1. How accurately can a link-budget model with calibrated terrain/statistical correction predict Radio Mobile received signal for a 5.8 GHz campus backhaul link?

RQ2. Which antenna height and antenna gain combinations satisfy a required fade margin with minimum deployment burden?

RQ3. How sensitive is feasibility classification to antenna height, antenna gain, and terrain obstruction loss?

RQ4. How should lower-frequency alternatives such as TVWS be treated when the simulation account or regulation does not permit direct 600 MHz modeling?

## Working Hypotheses

H1. FSPL alone will systematically underestimate the variation in received power across height scenarios because terrain obstruction and statistical losses change with antenna height.

H2. Increasing antenna height will not always improve the simulated link if terrain-profile and Fresnel-zone interactions change nonlinearly.

H3. A low-cost feasible design can be found by optimizing height and gain jointly rather than maximizing both.

## Claims to Make Carefully

- The model supports planning decisions for the studied link and similar point-to-point campus links.
- Radio Mobile validation tests the model against terrain-aware simulation, not against field measurements.
- TVWS is discussed as a lower-frequency alternative, but the current account did not permit a 600 MHz Radio Mobile run.

## Claims to Avoid

- Do not claim a new path-loss law.
- Do not claim field validation unless measured RSS data are collected.
- Do not claim Radio Mobile use as a novel method.
- Do not claim global optimality unless the full search space and constraints are defined.

