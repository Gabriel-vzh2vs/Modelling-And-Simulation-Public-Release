# Sample Size Estimation

A common question when doing simulation or anything that involves statistics
is "how many events do you need to get a significant result". First, a significant
result is often defined in the context of a hypothesis, where a result that
is unlikely to occur by stochaticity of the observed process is significant. And
the methods for estimating sample sizes depend on why you are estimating the
sample size.

## Estimation for Parameters

When estimating a parameter, a larger sample size usually leads to increase precision
as the Law of Large Numbers that with a sufficient number of samples, the estimator will
converge to the true value of the parameter[^1].

## As a Prerequisite for Statistical Tests

### On Power

#### Calculating Power

#### Simulating Power

[^1]: If and only if the estimator is asymptotically consistent (testable with Chebyshev's or Markov's inequality)
and the random variable of the parameter has an expected value that exists, is non-infinite, and all samples are
i.i.d, otherwise it will not function or converge with an error (weak law of large numbers).
