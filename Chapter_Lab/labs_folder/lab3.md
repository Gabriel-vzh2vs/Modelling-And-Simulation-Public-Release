:::{admonition} Lab 3
<!-- :class: tip dropdown -->
(lab-3)=
# Lab 3: Building a Portfolio with Monte Carlo Methods (XLRisk or Python)

Note: This is the last lab in the ODD framework, as this book aims
to make its readers/users adaptable across different presentations
of problems and labs.

## Lab 3 Prerequisites

### Pre-labs for Lab 3

- {ref}`prelab-2`
- {ref}`prelab-3`

### Mandatory Chapters for Lab 3

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`sec:building_simulation_models`

### Recommended Chapters for Lab 3

- {ref}`sec:random_number_generation`
- {ref}`sec:distribution_modeling`

## Purpose and Patterns (Lab 3)

### Statement of Model Purpose (Lab 3)

This model's purpose is three-fold, to demonstrate an application of Monte Carlo Methods for
calculating projected returns based on specific stocks while determining possible risks for selecting a strategy,
to select parameters based on real-world data while verifying the parameter's validity, and to show
how to process and analyze real-world data.

### Patterns (Lab 3)

#### Pattern 1. Monte Carlo Method in the Context of Stock Data

This pattern reflects the idea that the stock market can be modelled through a stochastic process that can be replicated
through Monte Carlo through the generation of an average that reflects the value of a security at a specific point in time.
With higher average returns, the value of the security should increase, and the opposite will occur with the converse assuming no variance.
However, with a higher variance of the security, the security's value exhibits more values away from the data's mean dependent on the underlying random variable's skew and kurtosis, with the converse, the value of the Monte Carlo calculated average tends to readily converge with the data's mean.

## Entities, State Variables, and Scales (Lab 3)

In this model, the following entities are included: the securities symbol, a random variable representing the mean value and variance of the securities, initial value of the portfolio (assuming fractional securities), the time horizon of contributions before retirement, and the expected mean contributions into the portfolio during the contribution time horizon. These factors represent a "bucket" of securities which compose 401k retirement accounts as opposed to a defined-pension as discussed in Lab 2.

### State Variables and Scales (Lab 3)

```{raw} latex
\begin{tabular}{llll}
\hline
\textbf{Variable} & \textbf{Scale} & \textbf{Type} & \textbf{Description} \\
\hline
$p_{0}$ & $[0 - \infty]$ & Double & The initial value of the principal. \\
$s_{name}$ & $[0 - \infty]$ & String & The name of the security. \\
$a_{t}$ & $[0 - \infty]$ & Double & The value of the contributions at step t, if any (this can also be expressed as a random variable.)\\
$r$ & $[-\infty - \infty]$ & Double & The underlying random variable of the security.\\
$t$ & $[-\infty - \infty]$ & Double & The length of the time horizon for investment defined through days.\\
$\bar{r}$ & $[0 - \infty]$ & Double & The expected percentage of increase in the value of the security, annualized. \\
$\sigma_{r}$ & $[0 - \infty]$ & Double & The standard deviation of the random variable. \\
$r_s$ & $[0 - 1]$ & Floating Point, Double & The weight (allocation of money) of the security in the portfolio.\\
$p_{t}$ & $[-\infty - \infty]$ & Double & The value of the return at step t. \\
$n$ & $[1 - \infty]$ & Integer & The number of experiments performed. \\
$s$ & 5 x 365 & Series & the series of security values over a period of a year, sampled daily. \\
\hline
\end{tabular}
```

The model runs on a daily time step, ignoring after hours movements of the security, as that data is not publicly available due to being held through decentralized exchanges (a form of dark pools held by stock brokers-dealers or market-makers). The model's spital extent consists of the smallest unit for a security being a single American cent, and it is bounded to zero cents for a valueless or less than valueless security[^1]. There are 365 total steps representing a year for the portfolio.

## Process Overview and Scheduling

Processes: This model is built to cover the basic movements of a security in the context of other securities in a portfolio as a risk (defined as variance in financial contexts) hedging or profit improving method. It is structured within five processes: one related to the gathering of security data, three related to the generation and contextualization of random variables (random variable selection, weight assignment to random variables, and output variate collection), and one process related to the performance of the portfolio (the average value of the portfolio based on the weighting and constituent random variables.)

Schedule:The simulation starts at a time zero, and continues until the simulation reaches the user-set parameter $t$.
Upon initialization, the parameters $r$, $s_{name}$, $p_{0}$ and $r_s$ are set through user-intervention.
With the first process, the variables, $s$ is obtained through a web-based process such as the STOCKHISTORY
function in excel or Stockdex in Python. The second process, then takes this information and fits the random
variable to the data (likely through a python package like phitter or through direct testing such as the K-S test).
Upon the completion of this process, the weight assignment with the user-provided information from the parameter
$r_s$ is then applied to $r$ constituting the third process. At this point, the random variables are now defined
and then the variates from the variable(s) are now initiated as instances of a variable which are added up time
period by time period to form the overall value of the portfolio per period, which is the fourth process.
The final and fifth process takes the information from the fourth process and calculate statistical data from the portfolio.

## Design Concepts

### Basic Principles

This model depicts the usage of Monte Carlo Methods for building estimations of a
portfolio while also showing a method for reducing aleatoric variance (known as financial risk)
through diversification in securities if the securities in question are independent of each other.
This idea builds on the general concept of correlation, where if the variables have negative correlations
or no correlations with each other - variance shall decrease, this principal is widely taught in financial
courses along with being the foundation of a variance reduction technique named antithetic variates
in the application of Monte Carlo Methods.

## Input Data

The user inputs the following data points:

- Initial Value, Weight, Standard Deviation as Gaussian Variable & Symbol of Security
- Contributions over a Time Horizon
- Time Horizon
- Initial Principal
- Number of Experiments

## Questions left to the reader to answer

1. Are the sample variance and deviation similar enough to the population variance and deviation to state that we have a sufficient $N$ for normality?
2. What are your 25% percentile, median, and 75% percentile values, and what do they say about the extreme values?
3. Moreover, would you say that this portfolio would pay off (have a positive value if we subtract the $E[X] = 10,000$ from the FV), in a week, which is our length of simulation.
4. Given the Kurtosis of the Model from XLrisk, what would you say about extreme events with this portfolio?
5. If you change the mixture of the stocks from all equal to only one stock, for example, MSTR, what happens to the variance, and why? And how does connect to portfolio strategies in the real world?
<!-- ::: -->

[^1]: There are securities that have a negative value, we call these "short" positions (short selling or selling a put/call option) - which can be represented in this model, but it is not expected that a student would have those in their portfolio.
