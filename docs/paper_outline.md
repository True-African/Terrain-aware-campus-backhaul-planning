# Paper Outline

## Title

Terrain-Aware Multi-Objective Optimization of Campus Wireless Backhaul Links Using Link-Budget Modeling and Radio Mobile Validation

## Abstract

State the problem, method, Radio Mobile validation, main quantitative results, and deployment recommendation after the expanded experiments are complete.

## Keywords

wireless backhaul; link budget; terrain-aware propagation; Radio Mobile; antenna height optimization; fade margin; campus network planning

## 1. Introduction

- Campus and institutional networks often need low-cost point-to-point backhaul.
- Link-budget equations are transparent but incomplete under terrain obstruction.
- Terrain-aware tools add practical realism but do not directly give a cost-aware equipment choice.
- State the study link and the decision variables.

## 2. Related Work

- Path-loss and RSS modeling.
- Terrain-aware and radio-map prediction methods.
- Wireless backhaul optimization.
- TVWS and lower-frequency alternatives.
- Radio Mobile and terrain-tool-based planning.

## 3. Problem Statement and Contributions

- Define the equipment-selection problem.
- State contribution as optimization plus simulation validation.
- Make clear that the work does not claim a new propagation law.

## 4. Analytical Link-Budget and Optimization Model

- Link-budget equation.
- FSPL and terrain/statistical correction model.
- Fade-margin and received-signal constraints.
- Deployment-cost objective.
- Feasibility definition.

## 5. Radio Mobile Simulation Methodology

- Corrected sites and coordinates.
- Frequency and account constraints.
- Antenna heights, gains, power, and receiver assumptions.
- Data collection protocol.
- Saved links under `My Links`.

## 6. Results and Discussion

- Start with the four pilot scenarios.
- Add expanded 30-run matrix results.
- Discuss terrain obstruction behavior.
- Identify feasible designs by margin threshold.
- Compare minimum-cost and maximum-margin designs.

## 7. Model Validation

- Compare FSPL-only, average-correction, and height-dependent correction models.
- Report MAE, RMSE, fade-margin deviation, and feasibility classification agreement.
- Discuss cases where the model fails or where Radio Mobile results are counterintuitive.

## 8. Practical Deployment Recommendations

- Recommended antenna height/gain combination.
- Minimum fade margin recommendation.
- When to increase gain versus height.
- How to treat lower-frequency alternatives under account/regulatory limits.

## 9. Limitations

- Simulation validation is not field measurement.
- One terrain path limits generalization.
- Account frequency restrictions limit direct TVWS evaluation.
- Radio Mobile settings and terrain data affect the outputs.

## 10. Conclusion

- Summarize the optimized design and validation result.
- State next work: field measurements, additional paths, and permitted lower-frequency simulations.

## References

Use DOI-backed references where available.

## Candidate Venues

- IEEE Access, if the expanded dataset and validation are strong enough.
- IEEE Open Journal of the Communications Society, if the modeling contribution is strengthened.
- Sensors, if the paper emphasizes open reproducible planning, simulation, and practical deployment.
- Future Internet, if the paper emphasizes backhaul planning and optimization.

