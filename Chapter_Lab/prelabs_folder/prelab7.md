(prelab-7)=
# Pre-Lab 7: Automated Distribution Fitters (Short Do)

## On Automated Distribution Fitters (i.e: Phitter, Fitter)

Through simulation literature and real-world applications, it is relatively rare to see
methods as seen with {cite}`Krzysztofowicz:25` for one reason, the vast majority of the
literature is not building novel distributions or meta-Gaussians, but instead often use one of
these three tests to pick from an existing distributions. Keep in mind that in general these
tests are comparing an empirical (observed data) distribution to a parametric (defined by a
closed-form formula) distribution.

- The $\chi^2$ Goodness Of Fit Test (this test can be deceptive, read {ref}`sec:distribution_modeling`) for more information about this, and that you should consider not using this for continuous distributions.
- Kolmogorov–Smirnov test (the test for comparing data to continuous distributions, which has the limitation of sensitivity to differences near the median between an empirical and parametric distribution)
- Anderson–Darling Test (similar to the K-S test, but is more sensitive to differences between the tails of the empirical and parametric distributions)

## Exercises

::::{tab-set}

:::{tab-item} Exercise 1 with Given Hypothesis
A small call center has automatically recorded the wait times (in minutes) for a sample of 20 consecutive incoming calls.

```{code} python
1.619349216, 1.570739596, 2.38882075, 1.660162223, 1.594000051, 1.939417783, 1.840022611,
2.485874562, 1.693257222, 2.091845183, 1.526335951, 1.866234179, 1.541921394, 1.520759608,
1.629551915, 1.556652485, 1.914162185, 1.594754923, 2.027844882, 1.694913864, 2.4335776
```

Based on the nature of wait times, an exponential
distribution is often considered. First, calculate the sample mean of this data. Using this
sample mean as an estimate for the mean ($\frac{1}{\lambda}$) of an exponential distribution, determine the
rate parameter $\lambda$. Then, using this estimated $\lambda$, write down the probability density function (PDF)
of the fitted exponential distribution. Finally, use a software package (Phitter, Fitter) to fit an exponential distribution to
this data and compare its estimated parameters to your by-hand calculations.
:::

:::{tab-item} Exercise 2 without Given Hypothesis
A factory machine produces items in batches. Over 25 consecutive production runs, the number of defective
items found in each run are represented the data below

```{code} python
14, 15, 11, 10, 12, 5, 10, 7, 10, 17, 7, 11, 
13, 6, 8, 9, 13, 12, 7, 9, 9, 12, 11, 12, 9
```

Estimate the sample mean and the standard deviation of the number of defective items. Then use the observed
properties of the distribution (e.g: making a histogram, assessing its natural bounds), to determine the
possible hypothesis for the posterior distribution. Then test these hypothesis using a software package like
Fitter/Phitter or a statistical package.
::::