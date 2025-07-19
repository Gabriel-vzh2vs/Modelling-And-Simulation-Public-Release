(sec:software)=
# Software Resources and Information

This is a chapter reference that can be used throughout the labs and the exercises
in this book. It is located in the lab section, as most of the materials
in this section relate to the pre-labs, labs, and projects.

## Excel

Excel is a spreadsheet program is a part of MS Office 365
which is used for many, many things, even when it was not made for those
applications!

However, Excel is used in workplaces for simulation, modelling, and
data storage all of which are of interest in this text. In this course,
it is an option for visualizing concepts in simulation as a visualization of a
matrix with transformations and embedded functions.

### Common Excel Functions

This is a non-exhaustive table of Excel functions, but for this text, it is sufficient enough to
perform any task needed with base Excel functions as other features are provided through Excel plugins.

:::{table}

| Excel Function | Description                                                                 | Parameters / Use Case                                                                                                                                                                                             |
| :------------- | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VAR.P()** | Calculates variance based on the entire **population**.                       | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing the entire population). <br> **Use Case:** Measuring the dispersion of a complete dataset, like the scores of all students in a specific class. |
| **VAR.S()** | Calculates variance based on a **sample** of the population.                  | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing a sample of the population). <br> **Use Case:** Estimating the population variance based on a smaller subset of data, like survey responses from a sample of a city's residents. |
| **KURT()** | Calculates the **kurtosis** of a data set (measure of "tailedness").        | **Parameters:** `number1`, `[number2]`, ... (The numbers or range for which you want to calculate kurtosis). <br> **Use Case:** Determining if a dataset has heavy tails (many outliers) or light tails (few outliers) compared to a normal distribution, often used in financial risk analysis. |
| **STDEV.P()** | Calculates standard deviation based on the entire **population**.             | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing the entire population). <br> **Use Case:** Quantifying the amount of variation or dispersion of a set of values for an entire population, such as the heights of all players on a professional sports team. |
| **STDEV.S()** | Calculates standard deviation based on a **sample** of the population.        | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing a sample of the population). <br> **Use Case:** Estimating the population standard deviation from a sample, like the variability in the lifespan of a sample of light bulbs from a production batch. |
| **SKEW()** | Calculates the **skewness** of a distribution (measure of asymmetry).       | **Parameters:** `number1`, `[number2]`, ... (The numbers or range for which you want to calculate skewness). <br> **Use Case:** Assessing the asymmetry of a dataset around its mean. For example, determining if income distribution in a region is skewed towards higher or lower incomes. |
| **T.INV()** | Returns the left-tailed inverse of the Student's **t-distribution**.          | **Parameters:** `probability`, `deg_freedom`. <br> (`probability` is the probability associated with the t-distribution; `deg_freedom` is the number of degrees of freedom). <br> **Use Case:** Finding the t-value for a given probability and degrees of freedom, often used in constructing confidence intervals or in hypothesis testing. |
| **IF()** | Performs a **logical test** and returns one value for a TRUE result and another for a FALSE result. | **Parameters:** `logical_test`, `value_if_true`, `value_if_false`. <br> (`logical_test` is any value or expression that can be evaluated to TRUE or FALSE). <br> **Use Case:** Assigning grades based on scores (e.g., IF(Score>90, "A", "B")), categorizing data, or controlling calculations based on certain conditions. |
| **XLOOKUP()** | **Searches a range or an array** for a match and returns the corresponding item from a second range or array. Default is an exact match. | **Parameters:** `lookup_value`, `lookup_array`, `return_array`, `[if_not_found]`, `[match_mode]`, `[search_mode]`. <br> **Use Case:** Finding specific information in a table, like looking up an employee's department based on their ID, or finding a product price given its name.  |

:::

### Excel Resources and Examples

In this subsection, we would like to point out some resources that may assist
the reader in understanding how to use Excel and some of the plugins that were
used when making this book.

#### Excel Video Series

#### Excel Textbooks

### XLRisk

XLRisk is a Free and Open Source VBA-based plugin that is made to compete with
atRisk, a widely-used commercial program that does Monte Carlo Method calculations.

#### XLRisk Variates and Functions

This is a almost exhaustive list of XLRisk Variates and Functions, that come from
[XLRiskDocumentation](https://github.com/pyscripter/XLRisk/wiki/RiskFunctions)
refer to that resources if more XLRisk variates could be helpful.


##### XLRisk Variates

:::{table}

| XLRisk Function    | Description                                                                                                | Parameters                                                                 |
| :----------------- | :--------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **RiskBernoulli** | Generates samples from a Bernoulli distribution.                                                           | `P` (probability of success)                                               |
| **RiskBeta** | Generates samples from a Beta distribution. Optionally provide A and B as the minimum and maximum.           | `alpha`, `beta` (shape parameters), `[A]` (minimum), `[B]` (maximum)         |
| **RiskBinomial** | Generates samples from a Binomial distribution.                                                            | `N` (number of trials), `P` (probability of success)                         |
| **RiskCumul** | Generates samples from a cumulative distribution, specified by min, max, and X,Y coordinates.              | `minvalue`, `maxvalue`, `XValues` (array), `YValues` (array of cumulative probabilities) |
| **RiskDiscrete** | Generates samples from a discrete distribution where specific values have defined probabilities.              | `Values` (array or range in ascending order), `Probabilities` (array or range of respective probabilities) |
| **RiskDUniform** | Generates samples from a discrete uniform distribution where each specified value has an equal chance.      | `Values` (array or range of values)                                        |
| **RiskErlang** | Generates samples from an Erlang distribution.                                                             | `alpha` (integer shape parameter), `beta` (scale parameter)                |
| **RiskExponential**| Generates samples from an Exponential distribution.                                                        | `mean`                                                                     |
| **RiskGamma** | Generates samples from a Gamma distribution.                                                               | `alpha` (shape parameter), `beta` (scale parameter)                        |
| **RiskLogNorm** | Generates samples from a log-normal distribution.                                                          | `mean`, `stdev` (standard deviation)                                     |
| **RiskNormal** | Generates samples from a normal distribution.                                                              | `mean`, `stdev` (standard deviation)                                     |
| **RiskPert** | Generates samples from a PERT distribution (a special case of Beta, smoother version of Triangular).         | `min`, `mostlikely`, `max`                                                 |
| **RiskTriang** | Generates samples from a triangular distribution.                                                          | `min`, `mostlikely`, `max`                                                 |
| **RiskUniform** | Generates samples from a uniform distribution.                                                             | `min`, `max`                                                               |
| **RiskWeibull** | Generates samples from a Weibull distribution.                                                             | `alpha` (shape parameter), `beta` (scale parameter)                        |

:::

##### XLRisk Functions

:::{table}

| XLRisk Function         | Description                                                                                                | Parameters / Use Case                                                                                                                               |
| :---------------------- | :--------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RiskCorrmat** | Creates a link to a correlation matrix when used as an optional last argument in a Risk function.           | **Parameters:** `CorrmatRng` (range of the correlation matrix), `Index` (column/row index in the matrix for the current Risk function). <br> **Use Case:** To model dependencies between different uncertain variables in a Monte Carlo simulation by correlating their input distributions. |
| **RiskCorrectCorrmat** | Fixes a correlation matrix that is not semipositive definite and returns a valid correlation matrix.         | **Parameters:** `CorrmatRng` (range of the correlation matrix to be corrected). <br> **Use Case:** To ensure a user-defined or imported correlation matrix is mathematically valid for use in simulations, preventing errors if it's not positive semidefinite. |
| **RiskIsValidCorrmat** | Checks whether a correlation matrix is valid, including a test for semipositive definiteness. Returns TRUE/FALSE. | **Parameters:** `CorrmatRng` (range of the correlation matrix to be validated). <br> **Use Case:** To programmatically check if a correlation matrix can be used in simulations before running them, or for data validation purposes. |
| **RiskSCorrel** | Returns the Spearman's rank correlation coefficient between two arrays.                                       | **Parameters:** `Array1`, `Array2` (the two datasets/arrays for which to calculate the rank correlation). <br> **Use Case:** To measure the strength and direction of a monotonic relationship between two variables, especially when the relationship is not linear or when outliers are present. |

:::

## AnyLogic

### AnyLogic Resources

Anylogic has resources

### Anylogic's Java

## Python

### Built-In Functions and Statements

#### List of Built-In Types

Insert Table with the following structure: Name of the Type, Description, and Examples (Oh, this is going to hurt)

#### List of Useful Built-In Functions

### Resources to Learn Python

### Functions From External Python Packages

#### monaco

#### pyMC

The following subsection discusses common distributions, options,
sampling methods, and statistical methods that exist within the PyMC package (at least its ecosystem.)

##### Probability Distributions

:::{table}
| Distribution (`pm.*`) | Description | Key Parameters |
| :--- | :--- | :--- |
| **Continuous Distributions** | | |
| `Normal` | A continuous, symmetric, bell-shaped distribution. | `mu` (mean), `sigma` (std. dev.) |
| `HalfNormal` | A normal distribution constrained to be non-negative. | `sigma` (std. dev.) |
| `Uniform` | A continuous distribution where all values in a range are equally likely. | `lower` (lower bound), `upper` (upper bound) |
| `StudentT` | Similar to the Normal distribution but with heavier tails, making it robust to outliers. | `nu` (degrees of freedom), `mu` (mean), `sigma` (scale) |
| `Exponential` | A continuous distribution for modeling the time between events. ⏳ | `lam` (rate parameter, $\lambda$) |
| `Beta` | A continuous distribution defined on the interval [0, 1], often used for modeling probabilities or proportions. | `alpha`, `beta` (shape parameters) |
| `Gamma` | A two-parameter continuous distribution for non-negative random variables. | `alpha` (shape), `beta` (rate) |
| `LogNormal` | A distribution whose logarithm is normally distributed. Used for positive random variables. | `mu` (mean of the log), `sigma` (std. dev. of the log) |
| **Discrete Distributions** | | |
| `Bernoulli` | A distribution for a single trial with two outcomes (0 or 1, success or failure). 🪙 | `p` (probability of success) |
| `Binomial` | Models the number of successes in a fixed number of independent Bernoulli trials. | `n` (number of trials), `p` (probability of success) |
| `Poisson` | Models the number of events occurring in a fixed interval of time or space. 📊 | `mu` (rate, expected number of events) |
| `NegativeBinomial` | Models the number of successes in a sequence of Bernoulli trials before a specified number of failures occurs. | `mu` (mean), `alpha` (dispersion) |

:::

##### pyMC Statistics

Through the Arviz package. 

:::{table}
| Function (`pm.*`) | Description | Key Parameters / Usage |
| :--- | :--- | :--- |
| `summary` | Generates a DataFrame with key summary statistics for the posterior distribution, such as mean, standard deviation, effective sample size (`ess`), and the R-hat diagnostic (`r_hat`). | `trace`, `var_names` |
| `plot_posterior` | Creates a plot of the posterior distribution for specified variables, typically shown as a histogram or a Kernel Density Estimate (KDE). 📊 | `trace`, `var_names`, `hdi_prob` |
| `trace_plot` | Creates a plot showing the MCMC trace (the time series of the samples) on one side and the posterior density on the other. It's essential for diagnosing convergence issues. | `trace`, `var_names` |
| `sample_posterior_predictive` | Generates new data based on the fitted model and posterior samples. This is crucial for posterior predictive checks to see how well the model simulates new data. | `trace`, `model`, `samples` |
| `loo` | Computes the approximate Leave-One-Out cross-validation (LOO) score, a metric for estimating a model's out-of-sample predictive accuracy. Used for model comparison. | `trace`, `model` |
| `waic` | Computes the Watanabe-Akaike Information Criterion (WAIC), another popular metric for estimating out-of-sample predictive accuracy. | `trace`, `model` |
| `model_to_graphviz` | Renders a visual graph of the model's structure, showing the relationships between random variables and data. 🔗 | `model` |

:::

##### pyMC Sampling

:::{table}
| Function / Concept | Description | Key Parameters / Usage |
| :--- | :--- | :--- |
| `pm.sample()` | This is the core function used to run the MCMC sampler and draw samples from your model's posterior distribution. | `draws`, `tune`, `chains`, `cores`, `target_accept` |
| **NUTS Sampler** | The **No-U-Turn Sampler** is PyMC's default, highly efficient MCMC algorithm for sampling from continuous variables. It uses gradient information to explore the posterior. | Automatically assigned by `pm.sample()` to continuous variables. |
| `draws` | The number of samples to generate and save for each chain, *after* the tuning phase. | `draws=2000` |
| `tune` | The number of initial "warm-up" iterations per chain. These are used to adapt the sampler's parameters and are then discarded. | `tune=1000` |
| `chains` | The number of independent MCMC chains to run. Running multiple chains (e.g., 4) is essential for diagnosing whether the sampler has converged properly. | `chains=4` |
| `cores` | The number of CPU cores to use for running chains in parallel. Setting this to the number of chains speeds up sampling significantly. | `cores=4` |
| `target_accept` | The target acceptance rate for the NUTS sampler. The default is usually 0.8. Increasing it can help resolve sampling difficulties (divergences) in complex models. | `target_accept=0.9` |
| **InferenceData** | The object returned by `pm.sample()`. It's an `arviz.InferenceData` object that contains all sampling results (posterior, observed data, etc.). Often called `idata` or `trace`.| This object is the input for all diagnostic and plotting functions, like `pm.summary(idata)`. |
:::

#### Ciw

#### Salabim

#### PySim
