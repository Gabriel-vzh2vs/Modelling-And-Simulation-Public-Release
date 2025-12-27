(sec:VarReduction)=
# Variance Reduction

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
with an estimator $\hat{\theta}$, assuming that variance reduction is  done correctly. More information
on how this is calculated is in {ref}`sec:CrudeMC`, the
section that formally discusses Monte Carlo.

There are generally three families of variance reduction that focus
on reducing variance: Variates (Control, Antithetic), Alternative Sampling Methods (Quasi, MCMC, Importance, Stratified, and
Correlated), and Random Number Modification.
This section covers the first two families of variance reduction as
they have two major benefits over CRN and other random number generation modifications:

1) Sampling and Variates can be seen as modifications upon the integrand of the Monte Carlo Method unlike the methods seen in Random Number Modification from {cite}`Banks:14` and {cite}`Law:13`;

2) Any statistical testing with CRN, as seen in output analysis is inherently invalid. As CRN causes a positive correlation between samples violating independence assumptions for ANOVA, t-tests, and Confidence Interval Calculations which requires the use of statistical test specifically for paired data.

## Variate Modification Methods

Simulation is inherently noisy. When we estimate a parameter using Monte Carlo simulation, our result is a random variable with its own variance. To improve the precision of our estimates without simply running the simulation for millions of extra iterations, we can employ variate modification.

This section focuses on methods that modify the underlying random variates to reduce the standard error of our estimators. The core principle often involves introducing correlation—either negative (to cancel out errors) or positive (to exploit known relationships) to reduce variance.

### Control Variates

The method of Control Variates exploits information we already possess about a similar system to improve our estimate of an unknown system.

The fundamental idea is to replace the crude estimator with one that balances itself based on a known quantity. Suppose we want to estimate the mean $\mu=E[X]$ of a random output X from our simulation.

We introduce a Control Variate $Y$, which is another random variable correlated with $X$ (ideally positively correlated), for which we know the exact expected value $E[Y]= \mu \cdot y$​.

We construct a new estimator X_{CV}​:

```{math}
X_{CV} = X - c(Y - \mu_y)
```

where c is a constant.

- If $Y$ and $X$ are positively correlated, then when X is above its mean, $Y$ is likely also above $\mu y$​. The term ($Y − \mu y​$) becomes positive, and subtracting it pulls X back down towards the mean parameter.
- The variance is minimized when $c=\text{Var}(Y)\text{Cov}(X,Y)$​.

:::{prf:example} Control Variates
:label: ex:control_variates

Imagine you are trying to use simulation to price a complex Asian Option ($X$) where no closed-form formula exists. However, a standard European Option ($Y$) behaves very similarly and *does* have a known closed-form price through the [Black-Scholes formula](https://www.columbia.edu/~mh2078/FoundationsFE/BlackScholes.pdf).

Instead of just simulating the Asian Option, you simulate both using the same random numbers (CRN).

- If the simulated European Option comes out \$5 higher than its known Black-Scholes price, it's likely your random numbers were positively biased.
- Therefore, your Asian Option estimate is most likely overestimating the value of the option.
- You subtract a portion of that \$5 error from your Asian Option estimate to correct it.
:::

### Antithetic Variates

Antithetic Variates (AV) is a technique that reduces variance by inducing negative correlation between two replication runs.

In a crude Monte Carlo simulation, we generate independent samples $X_1​,X_2$​. The variance of the mean is $\text{Var}(2X1​+X2​​)=4\text{Var}(X)+\text{Var}(X)​=2\text{Var}(X)​.$

However, if $X_1$​ and $X_2$​ are negatively correlated, the variance becomes:

```{math}
Var\left(\frac{X_1+X_2}{2}\right) = \frac{Var(X_1) + Var(X_2) + 2Cov(X_1, X_2)}{4}
```

If $\text{Cov}(X_1​,X_2​)$ is negative, the total variance falls below $2 \cdot \text{Var}(X)$​.

We achieve this by using Complementary Random Numbers. If $U$ is a uniform random number in [0,1], then $1−U$ is also a uniform random number.

- Run the simulation using inputs $U_1​,U_2​,…$ to get output $X_a$​.
- Run the simulation again using inputs $1−U_1​,1−U_2​,…$ to get output $X_b$​.
- Average $X_a$​ and $X_b​$.

If a "high" U causes a high output, then a "low" 1−U should cause a low output, canceling out the extreme variations.

:::{prf:example} Antithetic Variates
:label: ex:antithetic_queue

Consider a simulation of an M/M/1 queue to find the average waiting time.

- **Run 1 (Crude):** We generate inter-arrival times using $U$. If $U$ is small (e.g., 0.05), inter-arrival times are short, customers arrive fast, and the queue builds up (High Waiting Time).
- **Run 2 (Antithetic):** We use $1-U$. If $U=0.05$, then $1-U=0.95$. This generates long inter-arrival times. Customers arrive slowly, and the queue stays empty (Low Waiting Time).

By averaging Run 1 (High Wait) and Run 2 (Low Wait), we get a more stable estimate of the true average waiting time than two independent runs would provide.
:::

## Sampling Methods

### Correlated Sampling

Correlated Sampling (often called Common Random Numbers or CRN) is the opposite of Antithetic Variates. It is used when comparing two different system designs (e.g., System A vs. System B).

If we want to know if System A is better than System B, we care about the difference $D=X_A​−X_B$​.

To minimize the variance of the difference, we want positive correlation (maximize $Cov(X_A​,X_B​)$).

- Use the exact same seeds for both System A and System B.

- If you want to compare the aerodynamics of two cars, you drive them both on the same day with the same wind conditions (correlated environment). You don't drive Car A on a calm day and Car B during a hurricane.

:::{prf:definition} Correlated Sampling
placeholder
:::

:::{prf:example} Correlated Sampling
placeholder
:::

### Stratified Sampling

Stratification involves dividing the input domain into distinct regions (strata) and sampling from each region explicitly to ensure the full range of inputs is covered.

Instead of hoping the random generator samples the tails of a distribution, we force it to.
- Divide the probability distribution into k strata (e.g., 0-25%, 25-50%, 50-75%, 75-100%).
- Draw $n_i$​ samples from each stratum.
- Combine the results using a weighted average.

This ensures that rare but important events are represented in the sample exactly as often as they should be, eliminating some variance in sampling distributions. This is the foundational principle behind Quasi-Monte Carlo (QMC) methods (see {ref}`sec:QuasiMC`), which use deterministic sequences to cover the domain evenly.

:::{prf:definition} Stratified Sampling

:::

:::{prf:example} Stratified Sampling
placeholder
:::

### Importance Sampling

The point of Importance Sampling (IS) is to use another transform the domain with another simpler integrand, and reject the ones that exceed
the original Monte Carlo Integrand. This is similar to {ref}`sec:rejection_sampling`.

For example, of we want to estimate the probability of a rare system crash (e.g., $10^{−6}$), standard Monte Carlo might require millions of runs to see a single crash. IS transforms the probability measure to make the rare event common.

- Change of Measure: We sample from a biased distribution $g(x)$ that encourages the rare event (e.g., forcing service times to be artificially long), rather than the true distribution $f(x)$.
- Likelihood Ratio: Because we biased the simulation, the results are wrong. We correct them by multiplying by the likelihood ratio (weight) $W=\frac{f(x)}{g(x)}$.

:::{prf:definition} Algorithm of Importance Sampling
In [Qing Zhou's notes](http://www.stat.ucla.edu/~zhou/courses/Stats102C-IS.pdf), he defines importance sampling as the following:

```{raw} latex
\begin{enumerate}
    \item Draw $x^{(1)}, \dots, x^{(n)}$ from $g$ independently, and calculate importance weight:
    \begin{equation}
        w(x^{(i)}) = \frac{f(x^{(i)})}{g(x^{(i)})} \quad \text{for } i = 1, 2, \cdots, n;
    \end{equation}

    \item Estimate $\mathbb{E}_f(h)$ by
    \[
        \widehat{\mu}_h = \frac{1}{n} \sum_{i=1}^n w(x^{(i)})h(x^{(i)}).
    \]
\end{enumerate}

Then $\widehat{\mu}_h \xrightarrow{a.s.} \mathbb{E}_f[h(X)]$ as $n \to \infty$.
```

:::

:::{prf:example} Importance Sampling
:label: ex:importance_sampling

Suppose you are simulating a bridge failure.
* **Standard MC:** You simulate standard wind speeds. The bridge almost never fails. Variance is high because you have mostly 0s and one rare 1.
* **Importance Sampling:** You simulate from a distribution where "hurricane" wind speeds are common. The bridge fails often (the event is no longer rare).
* **Correction:** When the bridge fails under hurricane conditions, you weight that observation by a very small number (because hurricanes are actually rare).

This drastically reduces the variance for estimating very small probabilities.
:::


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