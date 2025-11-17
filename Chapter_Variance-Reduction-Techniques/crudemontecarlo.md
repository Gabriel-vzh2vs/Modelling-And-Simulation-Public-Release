(sec:CrudeMC)=
# On Crude Monte Carlo
Through most of this book, we stated that the Monte Carlo Method
is the foundation of many different simulation techniques and methods as seen in {ref}`sec:monte_carlo_method`. This section will be a
more technical view into the
Monte Carlo Method to give context for variance reduction techniques.

In general, you most likely read about this algorithm for Monte
Carlo, and this algorithm is a common sight in simulation. Moreover, this form of the algorithm is
often in the context of {ref}`sec:random_variates`
which are often sampled using Monte Carlo from the variate, $X$, with
sample size, $N$. And generally, it is considered a problem of evaluating a multidimensional integral with different parameters of interest, $\theta$ through an indicator function, $\mathbb{I}$.

__Algorithm:__

  1. Generate Realizations of $X$: $X_1, ..., X_{N}$
  2. Compute $g(X_1), g(X_2), ..., g(X_N)$ 
  3. Estimate $\hat{\theta}_N = \frac{1}{N} \sum_{j=1}^{N} g(X_{j})$

This algorithm is commonly called Monte Carlo, but a more proper name
would be the Crude Monte Carlo Method (CMC). Instances of the CMC have the following characteristics:

1. The estimator _asymptotically_ converges into the expected value of the parameter $\hat{\theta} \rightarrow \theta$ if and only if there is a sufficient number of samples (Law of Large Numbers).

2) If the $\text{var}(g(X)) = \sigma^2$, the estimate of the standard deviation is:
$$s^2 = \frac{(\sum_{j=1}^{N}g(X_j)-\hat{\theta})^2}{N-1}$$

3) This means that the Standard Error must be $\frac{s}{\sqrt{N}}$ and
for sufficiently large $N$, the Central Limit Theorem allows for the
construction of approximate confidence bounds for $\theta$.
$$\hat{\theta}_{N} - z_{\frac{a}{2}} \cdot \frac{s^2}{\sqrt{N}} + z_{\frac{a}{2}} \cdot \frac{s^2}{\sqrt{N}}$$

4) The error (precision) of $\hat{\theta} \propto \frac{1}{N}$ and is dependent on the value of the variance, $s^2$.

Characteristics 1 and 2 also create a problem, because this means that it might take
a VERY large $N$ for convergence, and if the function has irregularities like heavy tails,
it may never converge.

This problem of the required number of samples is often thought about in terms of "efficiency".

:::{prf:definition} Efficiency in Monte Carlo
a
:::

:::{prf:example} Example
a
:::

:::{seealso} Problem 1 (Monte Carlo: Application)

:::

:::{seealso} Problem 2 (Monte Carlo: Application)

:::
