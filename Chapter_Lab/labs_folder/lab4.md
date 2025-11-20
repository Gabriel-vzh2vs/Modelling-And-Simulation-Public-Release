(lab-4)=
# Lab 4: Simulating Stochastic Processes with Monte Carlo Methods (Python + Excel)

:::{admonition} Lab 4: Stochastic Process Simulation
:class: danger

## Note

So, from this lab onwards, we skip the ODD formalism as the reader
has been exposed to it sufficiently enough to understand its purpose.

## Lab 4 Prerequisites

### Required Pre-labs

- {ref}`prelab-2`
- {ref}`prelab-3`
- {ref}`prelab-4`

### Optional Pre-Labs

- {ref}`prelab-8`
- {ref}`prelab-5`

### Mandatory Chapters for Lab 4

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`distribution_modeling`

### Optional Chapters for Lab 4

- {ref}`sec:CrudeMC`
- {ref}`sec:VarReduction`
- {ref}`sec:QuasiMC`

## Background Information

In Computational Finance, Monte Carlo is often used to model the behaviors of
equities (such as stocks) and their derivatives (i.e: stock options), which
are defined through stochastic processes and random variates. This situation
gives us a good case study for using Monte Carlo in "real world" context similar
to {ref}`lab-3` and {ref}`lab-2`.

Now, let's begin the case study.

Stocks represent ownership in a corporation, which is defined as a fraction of market cap
(the total value of the company) over the number of outstanding shares.
And the goal of holding a stock price $S_t$, is to "buy low and sell high",
as in a rational actor wants $S_t$ to be higher than $S_0$ when they bought the stock.

Stock Options refer to a contract that says that you will either buy (call) or sell (put) a stock by a certain
date (maturity date). In European and American options, you pay a premium to obtain a option representing
100 shares at a strike price (the price you agree to sell or buy at). For example, you might pay 20 dollars
for a call option at strike price of 15 dollars on the maturity date of January 16th, 2026. If the stock
is at 20 dollars at maturity, then you make a profit of $5 \cdot 100 - 20  = 480$ dollars if you exercise the option.
This is basically buying stock at a discount; however, this is not a free lunch, if the option is out of the money,
meaning $S_t$ is below the strike price for a call or above for a put, you will lose all of your premium.

## Tasks

We now get into lab tasks, we should have a model for *how* we expect the stock
market to behave like. In this case, we are using a variant of the SDE described in Prelab 8, Example 2:
the Geometric Brownian Motion model.

$$dS_t = \mu S_t dt + \sigma S_t d W_t$$

Where $\mu$ is the expected rate of return, $\sigma$ represents the standard deviation of
the return, over $n$ time steps, which is similar to Lab 3. However, there are two parts of this
equation, the linear ODE for exponential growth, $\mu \cdot S_t dt$, and the second term representing
volatility proportional to price of the stock.

However, we also need to include the risk-free rate as an rational agent on the market has the option
of choosing a treasury bond, which has no realistic risk in the financial system. This will discount
our returns by $e^{rT}$, representing the returns on a risk-free investment. Which changes the pricing
of the premium for something like a Asian Call
into $e^{rT} \cdot E^Q [max(0, \bar{S} - K)]$, with $E_Q$ being the expectation of the
risk-free measure. But that does not change that much for our GBM:

$$dS_t = rS_t dt + \sigma S_t d W_t$$

Which replaces $\mu$ with the risk-free return rate $r$, but only for the linear ODE, because the
value of the security still determines the relative volatility of the system.

### Construct and Verify the Stochastic Process

Construct a method for simulating the GBM model given the initial value, $S_0$, and the
additional parameters $\mu$, $\sigma$ over the interval $

### Estimate Premiums

Using the first GBM, estimate a premium for an Asian Call Option on SPY, a index fund tracking the S&P 500,
where the initial price is $S_0 = 500$, the strike price is $K = 510$ over $T = 1$ year.
We know the annualized rate and volatility of the S&P 500 is about $\mu = 0.08$ and $\sigma = 0.15$. Assume that
there are 250 trading days for the year with no halts. Obtain the premium $C$ and the estimation of the standard deviation. Compare this with the second GBM with a risk-free rate of 3.83 percent and all other parameters being
the same. Which model do you trust more, and would you trust either one with your investment plans?
:::