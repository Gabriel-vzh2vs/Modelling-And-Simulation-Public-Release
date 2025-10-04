:::{admonition} Lab 2
:class: tip dropdown

(lab-2)=
# Lab 2: Retirement Calculations with Monte Carlo Methods (XLRisk or Python)

## Lab 2 Prerequisites

### Pre-labs for Lab 2

- {ref}`prelab-2`

### Mandatory Chapters for Lab 2

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`

### Recommended Chapters for Lab 2

- {ref}`sec:building_simulation_models`
- {ref}`sec:random_number_generation`

## Retirement Lab, Purpose and Patterns

### Retirement Lab, Statement of Model Purpose

This model's purpose is to demonstrate an application of Monte Carlo Methods for calculating projected returns and compare these
results to a commonly-used deterministic model, the simple interest rate formula, $I = Prt$. Moreover, for the third pattern, the model leverages
the concepts of _skewness_ and _kurtosis_ are used to determine the likelihood and magnitude of extreme events that might affect the returns of the model.

### Retirement Lab Patterns

#### Pattern 1. Base Deterministic Model

This pattern describes the function $p_{t+1} = p \cdot (1+r) + s \ \forall t$, which can be expressed as
$I = p \cdot (1+r)+s$ for a singular instance,
this formula of simple interest is often seen in secondary education and financial institutions. However, this model assumes
that there are no extreme events nor variances in interest, making its utility
limited for modern retirement funding schemes. In this case, the model assumes that
$p_0 = 25,000$, $r = 10 \% $, $t = 40$, and $s = 10,000$ as the default values in US dollars.
Additionally, $p_{n+1}$ replaces $p$ for any sequence after the first iteration.

#### Pattern 2. Single-Experiment Crude Monte Carlo with Stochastic Return

This pattern takes Pattern 1, the base deterministic model and adds an element of stochaticity in the rate of return, as in this pattern, the rate of return is defined
once per time segment through a $r = N(\bar{r}, \sigma)$ distribution with $\bar{r} = 10$ and $\sigma = 12$. This is considered a single experiment Monte Carlo.

#### Pattern 3. Crude Monte Carlo with Series of Experiments and Stochaticity in Rate of Return and Principal

This pattern builds upon pattern 2, through adding an additional source of stochaticity with the addition of a triangular distribution upon the principal
with the principal being defined once at the beginning of the simulation as $p = triangular(15000, 25000, 35000)$. Additionally, a requirement for this pattern
is the analysis of skewness and kurtosis for the output state variable, $p_{40}$ over a series of experiments, $n$.

## Entities, State Variables, and Scales (Lab 2)

### State Variables and Scales (Lab 2)

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

## Process Overview and Scheduling (Lab 2)

### Process Overview (Lab 2)

The model is developed to demonstrate an application of the Monte Carlo Method to calculate
returns for an retirement account while showing the impact of extreme events on model behaviors
and metrics.

It is structured within six subprocesses which activate depending on which pattern the model is exhibiting,
with two subprocesses being related to stochaticity which produces random variates via inverse transform
for the normal and triangular distributions in the first (normal_variable) and second (triangular_variable) subprocesses,
respectively, with their random variates being stored into a matrix.
The next subprocess (user_input) is the subprocess that handles input data
from the user and stores it within a matrix or
list. This subprocess, user_input, provides information for the next subprocess, interest_calculation,
representing the expression $p_{t+1} = p \cdot (1+r) + s \ \forall t$ which calculates the expression's
iterations recursively with replacement of the r and p_0 values depending on the pattern. Additionally, the
experiment subprocess, repeat the previous processes excluding user_input for $n$ times and store the results for each experiment into
a matrix. Finally, the subprocess skew_kurtosis calculates skew and kurtosis for each experiment's $p_{40}$,
the value of the total return at step 40.

### Scheduling (Lab 2)

The simulation starts when the sheet or program is initialized by the user through the user_input subprocess.
Once the system initializes, the two subprocesses for random variates generate a sequence of outputs corresponding to their ranges
and random numbers, storing the results into a matrix. From this matrix, the next subprocess, interest_calculation
iterates through the matrix in patterns 2 and 3 in-line with the requirements set in patterns. Moreover, if it is pattern 3,
the simulation subprocess reruns all of the previous subprocesses for $n$ times, then calls the final subprocess,
skew_kurtosis.

```{raw} latex
\begin{enumerate}
        \item \textbf{User Input Collection:}
        \begin{enumerate}
            \item The \textbf{user\_input} subprocess gathers necessary data from the user.
            \item This input data is stored in a matrix or list.
            \item This data includes initial parameters such as the initial principal ($p_0$), regular contribution amounts ($s$), and baseline interest rates ($r$)
            along with the parameters for the random variates defined in the next step.
        \end{enumerate}

        \item \textbf{Generate Random Variates:}
        \begin{enumerate}
            \item \textbf{normal\_variable:} Generates random numbers following a normal distribution using the inverse transform method. 
            \item \textbf{triangular\_variable:} Generates random numbers following a triangular distribution using the inverse transform method. 
        \end{enumerate}

    \item \textbf{Retirement Account Projection:}
    \begin{enumerate}
        \item The \textbf{interest\_calculation} subprocess calculates the account balance over time.
        \item It iteratively applies the formula: $p_{t+1} = p_t \cdot (1+r) + s$.
        \begin{enumerate}
            \item $p_t$ is the principal at time $t$.
            \item $r$ is the interest rate for the period, which can be a stochastic variable drawn from `normal_variate` or `triangular_variate` depending on the active model pattern (e.g., regular market conditions vs. extreme event).
            \item $s$ is the contribution for the period.
            \item The initial principal ($p_0$) and the rate ($r$) are replaced/updated based on the prevailing model pattern (e.g., an extreme event might temporarily change the expected return or lead to a withdrawal/lump sum change).
        \end{enumerate}
        \item This recursive calculation is performed up to a defined time horizon (e.g., 40 steps, leading to $p_{40}$).
    \end{enumerate}

    \item \textbf{Monte Carlo Experiment Execution:}
    \begin{enumerate}
        \item The \textbf{experiment} subprocess manages multiple runs of the simulation.
        \item It repeats the stochastic variable generation (Step 2.b) and interest calculation (Step 3) processes for a user-defined number of experiments ($n$).
        \item The `user_input` process (Step 1) is excluded from these repetitions, as initial conditions are set once per set of experiments.
        \item The results from each of the $n$ experiments (specifically the series of $p_t$ values, or at least the final $p_{40}$) are stored in a data storage structure.
    \end{enumerate}

    \item \textbf{Calculation of Kurtosis and Skewness of Results:}
    \begin{enumerate}
        \item The \textbf{skew\_kurtosis} subprocess analyzes the distribution of outcomes.
        \item It calculates the skewness for the set of final account values ($p_{40}$) obtained from all $n$ experiments.
        \item It calculates the kurtosis for the set of final account values ($p_{40}$) obtained from all $n$ experiments.
        \item These metrics help quantify the impact of extreme events on the distribution of potential retirement outcomes.
    \end{enumerate}
\end{enumerate}
```

## Design Concepts (Lab 2)

### Basic Principles (Lab 2)

This model depicts the usage of Monte Carlo Methods for building estimations of future
retirement accounts - however, the purpose of this model is to show that simulation
can be used to build predictions based on a limited set of data with epistemic
uncertainty. Similar to Lab 1, this lab leverages the Law of Large Numbers to build
pausable estimations for $P_{40}$, however, unlike lab 1, this model also uses non-uniform
random variables (a function that maps outcomes from a sample space to values)
to generate random variates that enter an function (the interest calculation) that
estimates target state variables ($r$ and $p_0$) with a definite pattern. These ideas
were covered in more detail in {ref}`sec:prob_stats`.

### Stochaticity (Lab 2)

Stochaticity is used when initializing the model to build the state variables of
$p_0$ and $r$ in pattern 3, $r$ in pattern 2, and does not exist in pattern 1.
Moreover, stochaticity is fundamental to any Monte Carlo Method, as they are
fundamentally based on principle of using random sampling to obtain numerical results
and in this case, it is used to simulate a stochastic system. And during the simulation,
every state variable excluding $t$ and $n$ are the results of stochastic processes.

## Input Data (Lab 2)

The user inputs the following data points:

- Initial Interest Rate
- Parameters for Normal and Triangular Distributions
- Time Horizon
- Initial Principal
- Number of Experiments

## Questions or Additional Tasks left to the reader to answer or perform (Lab 2)

1. Why were the normal and triangular distributions chosen for generating random variates? What aspects of return rates or economic conditions are they intended to represent?
2. Beyond skewness and kurtosis of $p_{40}$, what other output metrics or visualizations does the model produce to help understand the distribution of potential retirement outcomes (e.g., probability of ruin, range of terminal wealth values, confidence intervals)? Pick one of these outputs metrics or visualizations to model.
3. How should your client interpret the calculated skew and kurtosis for $p_{40}$ in practical terms for their retirement planning? What does a highly skewed or kurtotic distribution imply about their potential outcomes?
4. How sensitive are the model's conclusions about the impact of extreme events to the specific parameters chosen for the normal and triangular distributions?
:::
