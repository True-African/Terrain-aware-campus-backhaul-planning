# Literature Review

## Local technical foundation

The assignment and lecture notes point to a radio-link planning problem built around link budget, free-space path loss, antenna gain, antenna height, fade margin, terrain obstruction, and Radio Mobile simulation. The strongest research path is therefore not a general wireless networking paper. It is a focused point-to-point backhaul planning study where analytical equations are compared with terrain-aware simulation outputs.

The current local experiment uses a 7.159 km campus-to-campus link at 5825 MHz. Four saved Radio Mobile scenarios vary antenna height and antenna gain. The results show that the simulated obstruction term is strongly height-dependent and not monotonic in the four initial runs, which is exactly why a terrain-aware validation step is needed before recommending height or gain.

## Recent propagation and terrain-aware modeling work

Recent work confirms that path-loss prediction remains a central problem in wireless planning. Vasudevan and Yuksel (2024) survey machine-learning-based propagation modeling and note the importance of path loss and received-signal prediction for coverage mapping and network optimization. Their review also shows that modern models increasingly use environmental features, terrain-like descriptors, coordinates, antenna height, and sparse measurements. This supports our use of terrain-aware simulation as a calibration/validation layer, while also showing that a paper cannot claim novelty merely for predicting received power.

Yapar et al. (2024) summarize the first pathloss radio-map prediction challenge. The paper emphasizes environment-aware path-loss maps, ray tracing, building information, and evaluation methodology. This is close to the broader field of radio-map prediction, but it targets map prediction algorithms rather than a practical decision model for selecting antenna height and gain for a specific backhaul link.

Soo et al. (2025) model and measure propagation over uneven terrain. Their contribution is valuable because it explicitly challenges flat-surface assumptions and shows that uneven terrain can affect radio propagation. This supports the need for a terrain correction term in our model. Their setting is not a campus backhaul optimization framework, leaving room for a link-planning decision model validated through Radio Mobile.

Fernandez et al. (2024) develop a dual-slope path-loss model for urban and suburban vehicular sensing. This reinforces a broader trend: simple FSPL is insufficient when distance, environment, and blockage regimes change. The study is not about antenna equipment selection or Radio Mobile validation, but it supports the idea of including empirical or correction terms beyond FSPL.

## Wireless backhaul planning and optimization

Backhaul planning research already includes optimization. Khaturia, Appaiah, and Karandikar (2019) study efficient wireless backhaul planning for a frugal 5G setting, focusing on low-cost rural/middle-mile networks and multi-hop design. Hernandez and Knightly (2024) propose a topology-control algorithm for wireless backhaul networks using the Laplacian spectral gap and simulated annealing. These papers show that backhaul optimization is an established topic.

The gap for this project is narrower: these works do not primarily build a terrain-aware single-link equipment-selection model that chooses antenna height, antenna gain, and frequency under fade-margin constraints, then validates each candidate setting against a Radio Mobile terrain simulation.

## Radio Mobile and terrain-tool-based validation

Radio Mobile has been used in applied wireless planning studies. For example, rainfall-monitoring network work has used Radio Mobile to compare Zigbee and LoRa links and uses link margin as a practical feasibility indicator. Kaschel, Cordero, and Costoya (2019) evaluated Radio Mobile outputs for line-of-sight paths using different terrain datasets. These examples mean that "using Radio Mobile" is not novel. The manuscript should instead use Radio Mobile as a validation instrument for a mathematical planning model.

Longley-Rice/ITM and related terrain-aware tools remain a reference point for point-to-point propagation over irregular terrain. Radio Mobile is commonly associated with terrain-profile-based prediction, Fresnel-zone inspection, and link-budget style outputs. The research should be careful to describe the tool outputs used and avoid claiming direct field-measurement validation unless measurements are actually collected.

## TV White Space and lower-frequency alternatives

TV White Space research remains active because lower UHF frequencies propagate farther and penetrate obstructions better than 2.4 GHz or 5 GHz WiFi bands. Cunha et al. (2025) report laboratory and field analyses of TVWS implementation in Brazil and emphasize the role of regulation. Mach, Ronoh, and Langat (2023) optimize TVWS spectrum allocation using hybrid metaheuristics.

For this project, a direct 600 MHz trial was rejected by the Radio Mobile account because the account is restricted to predefined bands. That limitation can still be useful scientifically: the paper can discuss TVWS as a candidate lower-frequency class and document the account/regulatory limitation, but it should not present unavailable 600 MHz Radio Mobile outputs as simulated evidence.

## Literature-based conclusion

A paper based only on the current assignment would not be novel enough for a journal. A defensible paper is possible if the work is reframed as a reproducible terrain-aware decision model:

- It should optimize antenna height, antenna gain, and permitted frequency band.
- It should minimize a deployment burden or cost proxy.
- It should impose received-signal and fade-margin constraints.
- It should validate analytical predictions against an expanded Radio Mobile simulation matrix.
- It should report error metrics and feasibility-classification agreement.

The contribution is strongest if the dataset is expanded from 4 successful scenarios to at least 30 scenarios for one frequency, and preferably more if additional permitted bands are available.

