# Overview of Variance Reduction

Variance Reduction refers to methods that
reduce the variance of the Monte Carlo method, which then leads to
a reduced number of samples being required for convergence
in ideal circumstances. These techniques often focus on replacing
the integrand with one that is hopefully easier to evaluate and
has a lower variance at the same time. However,
not every technique has a guarantee that they
will reduce variance; some may increase it depending on the properties of the estimator. The reason
why Variance Reduction is important is that it reduces the computational and
mathematical effort needed to calculate a parameter, $\theta$
with an estimator $\hat{\theta}$, assuming that variance reduction is 
done correctly. More information
on how this is calculated is in {ref}`sec:CrudeMC`, the
section that formally discusses Monte Carlo.

There are generally three families of variance reduction that focus
on reducing variance: Variates (Control, Antithetic), Alternative Sampling Methods (Quasi, MCMC, Importance, Stratified, and
Correlated), and Random Number Modification.
This section covers the first two families of variance reduction as
they have two major benefits over CRN and other random number generation modifications:

1) Sampling and Variates can be seen as modifications upon the integrand of the Monte Carlo Method unlike the methods seen in Random Number Modification from {cite}`Banks:14` and {cite}`Law:13`;

2) Any statistical testing with CRN, as seen in output analysis is
inherently invalid, because it causes a positive correlation between samples violating independence assumptions for ANOVA, t-tests, and Confidence Interval Calculations which requires the use of statistical test specifically for paired data.

## Variate Modification Methods

This section focuses on generating variates that reduce variance by introducing variance that either in the opposite direction (antithetic) or have similar variance (control).

### Control Variates

The fundamental idea is that you replace a part of the integrand with
a known integral to reduce the variance of the crude Monte Carlo method.

:::{prf:definition} Control Variates
c
:::

How does it work? Control variates work through

:::{prf:example} Control Variates 
c
:::

:::{prf:example} Control Variates
c
:::

### Antithetic Variates

Basically, you sum negated variates to reduce the variance of the crude Monte Carlo integrand.

:::{prf:definition} Antithetic Variates
placeholder
:::

:::{prf:example} Antithetic Variates
placeholder
:::

:::{prf:example} Antithetic Variates  (Queuing Example: $M/M/1$)
placeholder
:::

## Sampling Methods

### Correlated Sampling

:::{prf:definition} Correlated Sampling
placeholder
:::

:::{prf:example} Correlated Sampling
placeholder
:::

:::{prf:example} Correlated Sampling
placeholder
:::

### Stratified Sampling

Stratification is dividing the domain of a function into stata 
(regions) that tend to have lower variance, and then are recombined 
into the 

This is also the principal behind {ref}`(sec:QuasiMC)` which has its
own chapter and applications.

:::{prf:definition} Stratified Sampling
placeholder
:::

:::{prf:example} Stratified Sampling
placeholder
:::

:::{prf:example} Stratified Sampling
placeholder
:::


### Importance Sampling

The point of Importance Sampling (IS) is to use another transform the domain with another simpler integrand, and reject the ones that exceed
the original Monte Carlo Integrand. This is similar to {ref}`sec:rejection_sampling`.

# Problems Left to the Reader

:::{seealso} Problem 1 (Monte Carlo: Antithetic Variables)
   It is desired to estimate the value of an integral:

    \begin{equation*}
        \hat{y} = \int_0^1 x^2 \, dx
    \end{equation*}

    by Monte Carlo Integration using f(x) = $\mathbb{I}_{[0,1]}(x)$. This should be familiar territory from Homework 2 before transitioning into something new. 
        1) Define the Monte Carlo Estimator, $\hat{y}$.
        2) Explain how antithetic variables can be used here, and justify briefly why their use here is guaranteed to improve efficiency.
        3) For $Z \sim U[0,1]$, use the results:
        $\mathbb{E}[Z^2] = \frac{1}{3}, \, \mathbb{E}[U^4] = \frac{1}{5}, \mathbb{E}U^2 (1-U)^2 = \frac{1}{30}$ to find the correlation between $U^2 \text{ and } (1-U^2)$. Confirm that antithetic variables reduce the variance of the estimator to an eighth of the original value. 
:::

:::{seealso} Problem 2 (Monte Carlo: Sampling for Variance Reduction)
    It is desired to estimate the value of an integral

    \begin{equation*}
        \hat{y} = \int_0^1 x^2 \, dx
    \end{equation*}

    by Monte Carlo Integration using f(x) = $\mathbb{I}_{[0,1]}(x)$. This should be familiar territory from Homework 2 before transitioning into something new. 
        1) Define the Monte Carlo Estimator, $\hat{y}$.
        2) Explain how antithetic variables can be used here, and justify briefly why their use here is guaranteed to improve efficiency.
        3) For $Z \sim U[0,1]$, use the results:
        $\mathbb{E}[Z^2] = \frac{1}{3}, \, \mathbb{E}[U^4] = \frac{1}{5}, \mathbb{E}U^2 (1-U)^2 = \frac{1}{30}$ to find the correlation between $U^2 \text{ and } (1-U^2)$. Confirm that antithetic variables reduce the variance of the estimator to an eighth of the original value. 
:::

:::{seealso} Problem 3 (Monte Carlo: Importance Sampling)
    It is desired to estimate the value of an integral

    \begin{equation*}
        \hat{y} = \int_0^1 x^2 \, dx
    \end{equation*}

    by Monte Carlo Integration using f(x) = $\mathbb{I}_{[0,1]}(x)$. This should be familiar territory from Homework 2 before transitioning into something new. 
        1) Define the Monte Carlo Estimator, $\hat{y}$.
        2) Explain how antithetic variables can be used here, and justify briefly why their use here is guaranteed to improve efficiency.
        3) For $Z \sim U[0,1]$, use the results:
        $\mathbb{E}[Z^2] = \frac{1}{3}, \, \mathbb{E}[U^4] = \frac{1}{5}, \mathbb{E}U^2 (1-U)^2 = \frac{1}{30}$ to find the correlation between $U^2 \text{ and } (1-U^2)$. Confirm that antithetic variables reduce the variance of the estimator to an eighth of the original value. 
:::

:::{seealso} Problem 4 (Monte Carlo: Importance Sampling)
    It is desired to estimate the value of an integral

    \begin{equation*}
        \hat{y} = \int_0^1 x^2 \, dx
    \end{equation*}

    by Monte Carlo Integration using f(x) = $\mathbb{I}_{[0,1]}(x)$. This should be familiar territory from Homework 2 before transitioning into something new. 
        1) Define the Monte Carlo Estimator, $\hat{y}$.
        2) Explain how antithetic variables can be used here, and justify briefly why their use here is guaranteed to improve efficiency.
        3) For $Z \sim U[0,1]$, use the results:
        $\mathbb{E}[Z^2] = \frac{1}{3}, \, \mathbb{E}[U^4] = \frac{1}{5}, \mathbb{E}U^2 (1-U)^2 = \frac{1}{30}$ to find the correlation between $U^2 \text{ and } (1-U^2)$. Confirm that antithetic variables reduce the variance of the estimator to an eighth of the original value. 
:::

:::{seealso} Problem 5 (Monte Carlo: Importance Sampling)
    It is desired to estimate the value of an integral

    \begin{equation*}
        \hat{y} = \int_0^1 x^2 \, dx
    \end{equation*}

    by Monte Carlo Integration using f(x) = $\mathbb{I}_{[0,1]}(x)$. This should be familiar territory from Homework 2 before transitioning into something new. 
        1) Define the Monte Carlo Estimator, $\hat{y}$.
        2) Explain how antithetic variables can be used here, and justify briefly why their use here is guaranteed to improve efficiency.
        3) For $Z \sim U[0,1]$, use the results:
        $\mathbb{E}[Z^2] = \frac{1}{3}, \, \mathbb{E}[U^4] = \frac{1}{5}, \mathbb{E}U^2 (1-U)^2 = \frac{1}{30}$ to find the correlation between $U^2 \text{ and } (1-U^2)$. Confirm that antithetic variables reduce the variance of the estimator to an eighth of the original value. 
:::