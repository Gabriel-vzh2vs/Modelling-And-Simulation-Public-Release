(prelab-12)=
# Pre-Lab 12: Advanced Modelling and Analysis Techniques (Do)

:::{note} Notice of this being an Outlne
I am slowly working on this prelab, but because
the course material isn't done yet, this will
be on the back burner.
:::

In previous labs, we focused on building individual models and analyzing their equilibrium behavior. However, real-world decision-making often requires us to look beyond a single "best guess" and consider the full range of possible futures. This pre-lab introduces advanced techniques for quantifying uncertainty and robustness in simulation models
as an extension and formalization of the concepts in {ref}`prelab-2`.

## Ensemble Modelling (Forecasting with Simulation)

Ensemble modeling involves running a set of simulations, rather than a single instance, to predict the future state of a system. What is the relevance of this to operations research? It allows us to account for imperfect initial conditions and model uncertainty. Instead of trusting one trajectory T, we generate an ensemble E={T1​,T2​,…,Tk​}.

Common applications include weather forecasting and financial stress testing. In this section, we will:

- Define the ensemble members by perturbing initial conditions S0​.
- Aggregate the results to form a probability distribution of outcomes at time $t$.
- Discuss metrics for evaluating the "spread" or divergence of the ensemble over time.

### Ensemble Metrics

### Ensemble Sampling

## Time-Series Forecasting with Monte Carlo

While standard time-series methods (like ARIMA) provide point forecasts, integrating them with Monte Carlo simulation allows us to generate "cones of uncertainty." Assume a process is governed by $Y_t​=f(Y_{t−1​})+ \varepsilon t$​, where $\varepsilon_{t}$​ is a stochastic noise term.

To forecast $h$ time steps ahead:

- We do not compute the expected value E[Yt+h​].
- Instead, we sample multiple paths by generating random variates for the sequence of error terms $\varepsilon_{t+1}​,…,\varepsilon_{t+h}​$.
- This results in a fan chart representing confidence intervals (e.g., 50%, 90%) for the future trajectory.

This section covers the implementation of these "fan charts" and the selection of appropriate noise distributions.

### Fan Charts

## Probabilistic Sensitivity Analysis

How much does a specific input parameter affect the variance of the output? Probabilistic Sensitivity Analysis (PSA) goes beyond simple "One-At-a-Time" (OAT) testing. We treat input parameters θ=[θ1​,θ2​,…,θm​] as random variables drawn from specific distributions, rather than fixed values.

We will explore:

    Global Sensitivity Analysis: Varying all parameters simultaneously to capture interaction effects.

    Tornado Diagrams: Visualizing which parameters drive the most uncertainty in the key performance indicators (KPIs).

    Monte Carlo Filtering: Identifying which regions of the parameter space lead to "failed" system states versus "successful" ones, see {cite}saltelli:08.

### Global Sensitivity Analysis

### Tornado Diagrams

### Monte Carlo Filtering
