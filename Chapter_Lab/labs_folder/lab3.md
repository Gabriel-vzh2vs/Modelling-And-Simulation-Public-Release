:::{admonition} Lab 3
:class: tip dropdown
(lab-3)=
# Lab 3: Building a Portfolio with Monte Carlo Methods (XLRisk or Python)

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

This pattern 

## Entities, State Variables, and Scales (Lab 3)

### State Variables and Scales (Lab 3)

```{raw} latex
\begin{tabular}{llll}
\hline
\textbf{Variable} & \textbf{Scale} & \textbf{Type} & \textbf{Description} \\
\hline
$p_{0}$ & $[0 - \infty]$ & Double & The initial value of the principal. \\
$r$ & $[-\infty - \infty]$ & Double & The rate of return which is often [0-100] percent, but can be any number. \\
$\bar{r}$ & $[0 - \infty]$ & Double & The average rate of return defined by the user. \\
$\sigma$ & $[0 - \infty]$ & Double & The standard deviation of the rate of return defined by the user. \\
$t$ & $[0 - 1]$ & Integer & The time horizon for the model. \\
$p_{t}$ & $[-\infty - \infty]$ & Double & The value of the return at step t. \\
$n$ & $[1 - \infty]$ & Integer & The number of experiments performed. \\
\hline
\end{tabular}
```

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

This model depicts the usage of Monte Carlo Methods for building estimations of future
retirement accounts - however, the purpose of this model is to show that simulation
can be used to build predictions based on a limited set of data with epistemic
uncertainty. Similar to Lab 1, this lab leverages the Law of Large Numbers to build
pausable estimations for $P_{40}$, however, unlike lab 1, this model also uses non-uniform
random variables (a function that maps outcomes from a sample space to values)
to generate random variates that enter an function (the interest calculation) that
estimates target state variables ($r$ and $p_0$) with a definite pattern. These ideas
were covered in more detail in {ref}`sec:prob_stats`.

## Input Data

The user inputs the following data points:

- Initial Interest Rate
- Parameters for Normal and Triangular Distributions
- Time Horizon
- Initial Principal
- Number of Experiments


## Questions left to the reader to answer

1. Are the sample variance and deviation similar enough to the population variance and deviation to state that we have a sufficient $N$ for normality?
2. What are your 25% percentile, median, and 75% percentile values, and what do they say about the extreme values?
3. Moreover, would you say that this portfolio would pay off (have a positive value if we subtract the $E[X] = 10,000$ from the FV), in a week,
which is our length of simulation.
4. Given the Kurtosis of the Model from XLrisk, what would you say about extreme events with this portfolio?
5. If you change the mixture of the stocks from all equal to only one stock, for example, MSTR, what happens to the variance, and why? And how does connect to portfolio strategies in the real world?
:::