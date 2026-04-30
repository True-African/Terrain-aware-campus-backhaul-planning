# Novelty Matrix

| Paper | Year | DOI | Method | Simulation or measurement tool | Mathematical model | Similarity to our idea | Gap left open | How our paper can differ |
|---|---:|---|---|---|---|---|---|---|
| Vasudevan and Yuksel, "Machine Learning for Radio Propagation Modeling: A Comprehensive Survey" | 2024 | 10.1109/OJCOMS.2024.3446457 | Survey of ML-based path-loss and RSS modeling | Literature survey across measured and simulated datasets | ML-based PL/RSS models, feature-based prediction | Confirms path loss and RSS prediction are central to planning | Does not give a practical campus backhaul equipment-selection model | Use a transparent analytical model with Radio Mobile validation rather than a broad ML predictor |
| Yapar et al., "Overview of the First Pathloss Radio Map Prediction Challenge" | 2024 | 10.1109/OJSP.2024.3419563 | Challenge benchmark for radio-map prediction | Simulated radio-map datasets, ray-tracing style data | Radio-map prediction and evaluation metrics | Similar environment-aware path-loss prediction motivation | Focuses on map prediction algorithms, not antenna height/gain/frequency decisions | Frame our work as point-to-point planning and feasibility optimization |
| Soo et al., "Radio Propagation Modeling and Measurement of Uneven Terrain Model" | 2025 | 10.1038/s41598-025-00958-8 | Modeling plus measurement of uneven terrain effects | Measurement and model comparison | Terrain-sensitive propagation model | Supports terrain-aware correction beyond flat-earth assumptions | Not a backhaul planning optimization study | Use terrain obstruction/statistical losses from Radio Mobile as calibration targets |
| Fernandez et al., "Dual-Slope Path Loss Model for Integrating Vehicular Sensing Applications in Urban and Suburban Environments" | 2024 | 10.3390/s24134334 | Empirical dual-slope path-loss modeling | Vehicular/urban-suburban measurement context | Dual-slope path-loss model | Shows that FSPL alone is insufficient in realistic environments | Not focused on campus backhaul, antenna equipment, or Radio Mobile | Include FSPL plus calibrated terrain/statistical/clutter terms for equipment selection |
| Calles-Esteban et al., "Optimizing Antenna Positioning for Enhanced Wireless Coverage: A Genetic Algorithm Approach" | 2024 | 10.3390/s24072165 | Genetic algorithm for antenna positioning | Coverage simulation/optimization environment | Optimization of antenna placement | Similar use of optimization for antenna deployment | Coverage placement problem rather than point-to-point backhaul link-budget validation | Optimize height/gain/frequency for a specific backhaul link and validate with Radio Mobile |
| Hernandez and Knightly, "A Spectral Gap-Based Topology Control Algorithm for Wireless Backhaul Networks" | 2024 | 10.3390/fi16020043 | Simulated annealing for wireless backhaul topology control | Network-topology simulation | Graph spectral gap, robustness, energy cost | Confirms backhaul optimization is established | Network topology, not terrain-aware RF equipment selection | Work at the physical link-planning layer with terrain and fade-margin constraints |
| Cunha et al., "Impact of Regulation on TV White Space Implementation in Brazil" | 2025 | 10.3390/s25082469 | Laboratory and field analysis of TVWS under regulation | 5G-RANGE system field/lab tests | Regulatory and system-performance analysis | Relevant to lower-frequency backhaul alternatives | Not a 5.8 GHz campus backhaul model and not Radio Mobile validation | Treat TVWS as a constrained alternative and document unavailable 600 MHz simulation |
| Mach, Ronoh, and Langat, "Improved Spectrum Allocation Scheme for TV White Space Networks..." | 2023 | 10.1016/j.heliyon.2023.e13752 | Hybrid firefly/genetic/ant-colony optimization | MATLAB simulation | Spectrum-allocation optimization | Similar multi-objective optimization spirit | Focused on spectrum allocation, not link budget, terrain, antenna height/gain | Use constrained equipment selection rather than channel allocation |
| Kaschel, Cordero, and Costoya, "Analysis and Evaluation of Radio Mobile Program on Line of Sight Paths..." | 2019 | 10.1109/CHILECON47746.2019.8988013 | Evaluation of Radio Mobile outputs across terrain datasets | Radio Mobile with SRTM and ASTER DTED | LOS terrain-path simulation comparison | Directly relevant to Radio Mobile reliability and terrain data | Older, evaluates tool behavior rather than building a planning model | Use Radio Mobile as validation data for an explicit optimization model |
| Khaturia, Appaiah, and Karandikar, "On Efficient Wireless Backhaul Planning for the Frugal 5G Network" | 2019 | 10.1109/WCNCW.2019.8902530 | Wireless backhaul planning for affordable rural networks | Optimization/simulation study | Backhaul planning model | Similar concern with low-cost backhaul | Multi-hop rural planning, not campus terrain-aware link validation | Focus on a single institutional backhaul link and equipment minimization |

## Novelty Questions

### 1. What has already been done?

Path-loss modeling, link budgets, terrain-aware simulation, Radio Mobile-based planning, TVWS connectivity studies, antenna placement optimization, and backhaul topology optimization have all been studied. A paper should not claim that these components are new individually.

### 2. What is missing in the literature?

The visible gap is a compact, reproducible framework for selecting antenna height, antenna gain, and permitted frequency band for a campus-scale point-to-point backhaul link, using an analytical link budget and validating terrain/statistical corrections through Radio Mobile outputs.

### 3. Is a paper based on this project likely to be novel?

Yes, but only with a narrowed contribution and an expanded experiment matrix. The four current rows are enough for motivation and pilot evidence, not for journal validation.

### 4. What precise contribution would make it publishable?

The strongest contribution is a terrain-aware multi-objective equipment-selection model that minimizes deployment burden while satisfying received-power and fade-margin constraints, calibrated and validated using a reproducible Radio Mobile simulation matrix.

### 5. What should we avoid claiming?

Avoid claiming novelty for basic link-budget equations, FSPL, Okumura-Hata-style modeling, using Radio Mobile, comparing antenna heights, or observing that lower frequencies propagate better. These are established ideas.
