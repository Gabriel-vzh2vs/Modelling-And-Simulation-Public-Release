(sec:CrudeMC)=
# Crude Monte Carlo
Through most of this book, we stated that the Monte Carlo Method
is the foundation of many different simulation techniques and methods as seen in {ref}`sec:monte_carlo_method`.
This section will be a more technical view into the
Monte Carlo Method to give context for variance reduction techniques.

In general, you most likely read about this algorithm for Monte
Carlo, and this algorithm is a common sight in simulation. Moreover, this form of this algorithm is
often in the context of {ref}`sec:random_variates`
which are usually sampled using Monte Carlo from a variate, $X$, with
sample size, $N$. And generally, it is considered a problem of evaluating a multidimensional
integral with different parameters of interest, $\theta$ through an indicator function, $\mathbb{I}$.

__Algorithm:__

  1. Generate Realizations of $X$: $X_1, ..., X_{N}$
  2. Compute $g(X_1), g(X_2), ..., g(X_N)$ 
  3. Estimate $\hat{\theta}_N = \frac{1}{N} \sum_{j=1}^{N} g(X_{j})$

This algorithm is commonly called Monte Carlo, but a more proper name
would be the Crude Monte Carlo Method (CMC). Instances of the CMC have the following characteristics:

1. The estimator _asymptotically_ converges into the expected value of the parameter $\hat{\theta} \rightarrow \theta$ if and only
if there is a sufficient number of samples (Law of Large Numbers).

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
Efficiency refers to the number of samples required for asymptotical convergence. This metric
typically calculated through a sample size calculation for the degree of accuracy required.

For example, Let us assume that we are trying to estimate the parameter: $\theta = E(g(X))$,
then the estimate shall be in the form:

$$\hat{\theta}_N = \frac{1}{N} \sum^{N}_{J_1} g(X_{j})$$

And it has standard error $s_{\hat{\theta}} = \frac{s}{\sqrt{N}}$ One way to measure the
quality of the estimator $\hat{\theta}$ is through the half-width for the confidence
interval for $\theta$, and when set to a specific $\alpha$ which defines the possibility that
the interval will fail to capture the true value within the probability confidence interval.

$$\text{Half Width } = z_{\frac{\alpha}{2}} \sqrt{\frac{\text{Var}(g(X))}{N}}$$

Then the minimum sample size requirement for Monte Carlo is defined through
this expression:

$$N \le \frac{z_{\frac{a}{2}}}{\text{Half Width}} \cdot \text{Var}(g(X))$$
:::

And generally the smaller the required sample size: the more efficient the estimation will be. This is where variance reduction techniques come in, as they specifically target the variance as it determines the half-width and is a factor in determining sample size.
