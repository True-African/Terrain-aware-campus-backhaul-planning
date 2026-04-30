# Analytical Link-Budget and Optimization Model

## Decision Variables

For each candidate link design \(i\):

- \(h_{t,i}\): transmitter antenna height above ground level in m.
- \(h_{r,i}\): receiver antenna height above ground level in m.
- \(G_{t,i}\): transmitter antenna gain in dBi.
- \(G_{r,i}\): receiver antenna gain in dBi.
- \(P_{t,i}\): transmitter power in dBm.
- \(f_i\): carrier frequency in MHz.
- \(b_i\): selected permitted frequency band.

For a symmetric campus backhaul design, the first experiment can set:

\[
h_{t,i}=h_{r,i}=h_i,\qquad G_{t,i}=G_{r,i}=G_i.
\]

## Link Budget

The received signal level is:

\[
P_{rx,i}=P_{t,i}+G_{t,i}+G_{r,i}-L_{t,i}-L_{r,i}-PL_{total,i},
\]

where \(L_t\) and \(L_r\) are feeder, connector, and implementation losses.

## Maximum Allowable Path Loss

For receiver sensitivity \(P_{sens}\) and required fade margin \(FM_{req}\), the maximum allowable path loss is:

\[
PL_{max,i}=P_{t,i}+G_{t,i}+G_{r,i}-L_{t,i}-L_{r,i}-P_{sens}-FM_{req}.
\]

A candidate design is feasible if:

\[
PL_{total,i}\le PL_{max,i}.
\]

## Path-Loss Structure

Free-space path loss is:

\[
PL_{FS,i}=32.44+20\log_{10}(d_i)+20\log_{10}(f_i),
\]

where \(d_i\) is distance in km and \(f_i\) is frequency in MHz.

The total modeled path loss is:

\[
PL_{total,i}=PL_{FS,i}+L_{terrain}(h_{t,i},h_{r,i},d_i)+L_{stat,i}+L_{clutter,i}+L_{impl,i}.
\]

Radio Mobile outputs can be used to estimate:

\[
L_{terrain,i}+L_{stat,i}=PL_{RM,i}-PL_{FS,i},
\]

where \(PL_{RM,i}\) is the total path loss reported by Radio Mobile.

If Radio Mobile separately reports obstruction loss and statistical loss, the calibration can use:

\[
L_{terrain,i}=L_{obstruction,i},\qquad L_{stat,i}=L_{statistical,i}.
\]

## Fade Margin

Fade margin is:

\[
FM_i=P_{rx,i}-P_{sens}.
\]

The feasibility constraint is:

\[
FM_i\ge FM_{req}.
\]

The current assignment results imply \(P_{sens}=-113.02\) dBm because the baseline has \(P_{rx}=-77.06\) dBm and \(FM=35.96\) dB.

## Optimization Objective

The planning objective minimizes deployment burden:

\[
\min C_i=\alpha_h(h_{t,i}+h_{r,i})+\alpha_g(G_{t,i}+G_{r,i})+\alpha_pP_{t,i}+\alpha_fC_f(b_i)+\alpha_l(L_{t,i}+L_{r,i}).
\]

Subject to:

\[
FM_i\ge FM_{req},
\]

\[
P_{rx,i}\ge P_{sens}+FM_{req},
\]

\[
h_{min}\le h_{t,i},h_{r,i}\le h_{max},
\]

\[
G_{min}\le G_{t,i},G_{r,i}\le G_{max},
\]

\[
P_{t,i}\le P_{reg}(b_i),
\]

\[
f_i\in B_{allowed}.
\]

The cost weights \(\alpha_h,\alpha_g,\alpha_p,\alpha_f,\alpha_l\) should be selected before the final experiment. A practical first setting is to normalize each term by its maximum value:

\[
C_i=w_h\frac{h_{t,i}+h_{r,i}}{2h_{max}}+w_g\frac{G_{t,i}+G_{r,i}}{2G_{max}}+w_p\frac{P_{t,i}}{P_{max}}+w_fC_f(b_i).
\]

## Validation Metrics

For \(N\) Radio Mobile runs:

\[
e_i=P_{rx,i}^{model}-P_{rx,i}^{RM}.
\]

Mean absolute error:

\[
MAE=\frac{1}{N}\sum_{i=1}^{N}|e_i|.
\]

Root mean square error:

\[
RMSE=\sqrt{\frac{1}{N}\sum_{i=1}^{N}e_i^2}.
\]

Fade-margin deviation:

\[
\Delta FM_i=FM_i^{model}-FM_i^{RM}.
\]

Feasibility classification agreement:

\[
Acc=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\{Feasible_i^{model}=Feasible_i^{RM}\}.
\]

## Model Calibration Plan

1. Use the expanded Radio Mobile matrix to estimate terrain/statistical correction terms.
2. Fit a simple correction model such as:

\[
L_{terrain}(h_t,h_r)=\beta_0+\beta_1\log_{10}(h_t)+\beta_2\log_{10}(h_r)+\beta_3\frac{1}{h_t+h_r}.
\]

3. Compare three analytical variants:
   - FSPL only.
   - FSPL plus average correction.
   - FSPL plus height-dependent terrain correction.

4. Select the simplest model that reduces error without overfitting.

