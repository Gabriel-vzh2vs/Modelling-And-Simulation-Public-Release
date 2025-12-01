# Confidence Intervals

It is highly likely that you have done some form of statistics course
or at least reviewed the first chapter {ref}`sec:prob_stats`. And therefore
have heard the idea of a confidence interval before, most likely with a
definition similar to: "A confidence interval (CI) is a range of values,
calculated from sample data, that is likely to contain an unknown
population parameter (i.e. location or scale parameter)" and that
the confidence portion represents the reliability of the method used to
calculate this estimate in frequentist statistics.

## The Classical Central Limit Theorem

When estimating the mean using $\bar{X}$,
we rely on the Central Limit Theorem (CLT).

Central Limit Theorem: Let $X_1, X_2, ... X_n$
be a sequence of IID random variables with finite mean $\mu$ and a finite, non-negative, standard deviation, and let $Z_n$ be the random variable:

$$Z_n = (\bar{X} - \mu) / \sqrt{\frac{\sigma^2} {n}}.$$

Then asymptotically:

$$\text{Pr}(X_{n} \le z) = F_{n,Z}(z) \rightarrow \psi(z)$$

Where $\psi$ represents the CDF of the standard normal, $N(0,1)$.

However, for practicable purposes, we need to find $\mu$ and a guarantee
of the quality of the estimate. This is where
confidence intervals come into the picture as we need to determine values that bound the estimate of the mean within a prescribed probability.

Now that we have $Z_n$ with an unknown $\sigma^2$, we have to construct a random
variable $t_n$ and estimator $S^2(n)$ in:

$$t_n = (\bar{X}(n) - \mu) / \sqrt{S^2(n) / n}$$

Which by the Classic CLT, asymptotically converges into $\psi$, and allowing for a approximation defined through:

\begin{align*}
 \Pr\Bigl(
 & -z_{1-\alpha/2} \le (\bar{X}(n) - \mu)/\sqrt{S^2(n)/n} \le z_{1-\alpha/2}
  \Bigr)
  \\
&=
\Pr\left(
\bar{X}(n) -z_{1-\alpha/2}\sqrt{S^2(n)/n}
\le - \mu
\le \bar{X}(n) + z_{1-\alpha/2}\sqrt{S^2(n)/n}
\right) \\
&\approx 1 - \alpha
\end{align*}

$\alpha$ is often called the significance level, and $z_{1-\alpha/2}\sqrt{S^2(n)/n}$ is the half length of the convergence interval.

## What is a Confidence Interval, Really?

A confidence interval defines a probabilistic guarantee that a parameter
will reside within an interval, and this probability level is
provided by percentage of intervals that contain $\mu$ also
known as _coverage_. And if the underlying
distribution is IID with finite variance, it will assume the form:

$$\bar{X}(n) \pm Z_{1-a/2} \sqrt{S^2(n)/n}$$

The problem with this asymptotic convergence
is the "$n$ is sufficiently large" problem
because of two facts:

1) The more skewed $X_i$ are, the larger
n has to be, and the rate of convergence could
become infinity.

2) The fact that heavy tails exist, making it
impossible for some distributions to converge
using Classical CLT and the Strong Law of Large Numbers.

### Willink Confidence Intervals

For the first problem, we can consider using
a Willink Confidence interval (WCI) to correct skewness, the third central moment ($\nu = \exp[(X-\mu)^3]/(\sigma^2)^{3/2}$).

In general, WCI is a modified frequentist approach designed to correct positive skewness (i.e: the skewness found in Gamma, log-normal distributions) included coverage error by incorporating the sample skewness into the calculation.

The WCI modifies the critical value used in the interval. Instead of using the symmetric $t$-quantile directly, it transforms the quantile using a function $G(\cdot)$ that accounts for the third central moment (skewness).

The $(1-\alpha)$ in WCI is given by:

$$\left[ \bar{X} - G\left(t_{crit}\right)\sqrt{\frac{S^2}{n}}, \quad \bar{X} + G\left(t_{crit}\right)\sqrt{\frac{S^2}{n}} \right]$$

To construct this interval, several statistics must be computed from the sample data $X_1, X_2, \dots, X_n$:

1) Sample Moments, which involves calculating the sample mean ($\bar{X}$) and variance ($S^2$). The method heavily relies on an unbiased-type estimator for the third central moment, denoted in the text as $\hat{\mu}_3$:$$\hat{\mu}_3 = \frac{n}{(n-1)(n-1)} \sum_{i=1}^{n} (X_i - \bar{X})^3$$

2) The Skewness Parameter ($a$), The parameter $a$ represents a scaled measure of the skewness of the sampling distribution of the mean. It normalizes the third moment against the variance and sample size:
$$a = \frac{\hat{\mu}_3}{6\sqrt{n}(S^2)^{3/2}}$$
If the data is perfectly symmetric, $\hat{\mu}_3 = 0$, which makes $a=0$.

3) The Transformation Function $G(r)$This is the core of the Willink correction. It maps a value $r$ (usually the $t$-critical value) to a new value that adjusts for the estimated skewness $a$.
$$G(r) = \frac{1 + 6a(r - a)^{1/3} - 1}{2a}$$

This function is derived from an inversion of a purely algebraic approximation (often related to the Wilson-Hilferty transformation) intended to normalize a _pivotal quantity_ involving the sample mean.

## What a Confidence Interval Is Not

To Bayesians, there is a second concept that is often confused with
the confidence interval, the Credible interval. This interval defines the
possibility of a parameter residing in set of numbers within a given region
in the context of a posterior distribution. This is the concept
most people popularly associate with a confidence interval.

Credible intervals can be calculating using the simulation-sampling technique
described as Markov Chain Monte Carlo, which is defined further in {ref}`sec:MCMC`.

## Alterative Methods of Confidence Interval Construction

### Bootstrapping Methods

Bootstrapping methods are a family of methods
that can assign a series of measures of accuracy (i.e: Confidence Intervals, Variance, Bias, Power, and Hypothesis Testing) to sample estimates. without relying on CLT.
It will provide better results in cases where the CLT and LLN do not apply (i.e: no
closed-form expression for the distribution). And the naive bootstrap is never worse than CLT in terms of accuracy.

#### How Does Bootstrapping Work?

Naive Bootstrapping is a sampling method that
consists of the following method, which was defined by Efron, 1979:

Suppose you have access to an i.i.d. sample $\{X_i\}_{i=1}^n$ and you want to compute a
statistic $\theta$ using an estimator $\hat{\theta}(X)$. You can approximate the
distribution of $\hat{\theta}$ by

```{raw} latex
\begin{enumerate}
    \item Sample $n$ observations with replacement from your sample $\{\tilde{X}_i\}_{i=1}^n$
    \item Compute the estimator $\hat{\theta}_{bootstrap}(\tilde{X})$
    \item Repeat steps 1 and 2 a large number of times
\end{enumerate}
```

The distribution of $\hat{\theta}_{bootstrap}$ is a good approximation of the distribution of $\hat{\theta}$.

To use this framework to create a confidence
interval at 95% confidence around the true
value of a parameter, $\theta$ for population $p$, we can do the following.

Suppose we draw 6,742 bootstrap samples
of size $n$, each with a new estimate of the
estimator for the parameter.

We then rank these estimates from least to
greatest with the smallest estimate 


#### Why not Bootstrap Everything?

Like other sampling methods, the naive bootstrap is particularly vulnerable to heavy tails. 

There is a way to address this with the Bayesian Bootstrap, introduced by Rubin, 1981

## What does this mean for Simulation?
