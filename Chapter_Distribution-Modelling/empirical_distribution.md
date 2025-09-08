
(sec:empirical_distribution)=
# Empirical Distributions

Here we consider the case where we have a sample
\begin{equation}
  S = \{x_1, x_2, \ldots, x_n\} \quad\text{with}\quad x_i \in
  \mathbb{R}
\end{equation}
of a continuous random variable $X$, and where we assume that the
sample points are arranged in increasing order:
\begin{equation*}
 x_1 \le x_2 \le \cdots \le x_n
\end{equation*}

If your sample is unsorted, you will have to rearrange it. Sometimes,
the sample points are a time stamp providing the order in which they
were collected. In this case, we would consider $S$ not as a set, but
instead as a __time series__, and we would not sort it. We will not be
concerned with this case in this chapter.

We define the __empirical distribution function__ for the sample
$S = \{x_1, x_2, \ldots, x_n\}$ by
\begin{equation}
\label{eq:empirical}
\tilde{F}(x) = \bigl|\{x' \in S \mid x' \le x\}\bigr| \Bigl/ n \;,
\end{equation}
where the domain of $\tilde{F}$ is the real numbers $\mathbb{R}$.

What does this function look like? Going from left to right on the
real line, the function $\tilde{F}$ starts out at $0$, then jumps a
vertical distance of $1/n$ as each point $x_i$ is encountered. An
example of such a function is given in {ref}`fig:empirical_distribution`.



:::{figure} ../Figs/empirical-distribution.svg
:align: center
:width: 600
:label: fig:empirical_distribution
The empirical distribution function for a sample $S =
  \{x_1, x_2, x_3, x_4, x_5\}$.
:::

The definition of the empirical distribution function $\tilde{F}$

The function defined in {ref}`eq:empirical` is piecewise constant
non-decreasing function. It is precisely the definition of an
empirical distribution function that is used for the
Kolmogorov-Smirnov (KS) test, which we will return to in
{ref}`sec:distribution_modeling`. The definition {ref}`eq:empirical`
matches Equation~(6.5) in {cite}`Law:13` who gives an alternative
version of an empirical distribution on p. 313; you will find yet
other ones in {cite}`Krzysztofowicz:25`, all with their specific
purposes. In this book, we will only use the version {ref}`eq:empirical`.


::::{tip} Python - Empirical distribution function
:class:dropdown
```{code} python
import matplotlib.pyplot as plt
from scipy import stats

sample = [1.0, 2.3, 1.53, 0.5, 0.2]
emp_dist = stats.ecdf(sample)

# You should inspect the object:
print(emp_dist)

# Use matplotlib to visualize:
ax = plt.subplot()
emp_dist.cdf.plot(ax)

# r-strings permit LaTeX formatting. This is optional, but looks professional.
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'Empirical CDF $\tilde{F}$')
plt.show()
```

:::{figure} ../Figs/empirical_distribution_example.svg
:align: center
:width: 600
:label: fig:empirical_distribution_examples
The empirical distribution function for the Python example.
:::

Python documentation
- [scipy.ecdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ecdf.html)

::::