# Overview of Variance Reduction

## Variate Modification Methods

### Control Variates

### Antithetic Variates

## Sampling Methods

### Correlated Sampling

### Stratified Sampling

Stratification is dividing the domain of a function into stata 
(regions) that tend to have lower variance, and then are recombined 
into the 

### Importance Sampling

The point of Importance Sampling (IS) is to use Monte Carlo to 

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

:::{seealso} Problem 2 (Monte Carlo: Importance Sampling)
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

