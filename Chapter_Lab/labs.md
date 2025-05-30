(sec:labs)=
# Labs

The labs serve a dual purpose in this text, they enable the reader to apply lessons from this book to real-world examples,
and they allow for assessment of the reader's knowledge of the material either through comparing models with reference models
through self-assessment or by formal assessment by an external grader. It is recommended to do eight to eleven labs within a
course of self-study or in the context of a formal course in simulation. In this case it is recommended that the number of labs
that a reader does correlates with their educational goals, for example: eight to nine labs for am advanced undergraduate-level
understanding of Simulation and Modelling, and ten to eleven labs being suitable for a graduate-level understanding.  

Moreover, these labs are written to be technology-agnostic - meaning that you could theoretically use any toolkit to
complete these tasks; however, we have included recommendations for specific technological implementations as a guide for
readers as the authors used them in the creation of the labs.

In accordance with technological agnosticism and to show how literature presents their case studies, lab descriptions are written
with a modified ODD (Overview, Design concepts and Details) protocol that is shortened based on the model's
requirements (e.g: sections that do not apply to the model, or sections that are left to the reader to complete).

:::{note} A Note on Difficulty Levels
:class: dropdown

In this section, difficulty is expressed by a symbol and a color, which are dual indicators
meaning that they will always go together (i.e: you will never see a color with a different symbols)

- Green and Pen: Labs that we consider approachable and should take the average prepared student less than 1 hour to complete;
- Orange and Megaphone: Labs that we consider will take a bit of thought, we recommend taking 1 to 2 hours to complete this task;
- Red and Circle: Labs that are made to prepare the student for the project, we recommend taking 5+ hours to complete this lab.

Additionally, if you do not complete the pre-lab, you can move each difficulty level up by one (e.g: Green and Pen goes to Orange and Megaphone).
:::

:::{admonition} Lab 1
:class: tip dropdown

(lab-1)=
# Lab 1: Computing $\pi$ with Monte Carlo Methods (Excel or Python)

## Lab 1 Prerequisites

### Pre-labs

- {ref}`prelab-1`

### Required Chapters

- {ref}`sec:preface`
- {ref}`sec:prob_stats`
- {ref}`sec:buffons_needle_summary`

## Purpose and Patterns

### Statement of Model Purpose

This model's purpose is to demonstrate the concept of Monte Carlo Integration through calculating $\pi$
through random sampling from a uniform random variable.

### Patterns

#### Pattern 1. Unit Circle of Radius 1 and Square with Side Length 2

This pattern describes how $\pi$ is calculated with well-defined shapes without respect to units.
In this pattern, we obtain $\pi$ from our calculations in Excel when we consider
indicator variable to be equal to one when an experiment is within the union of the unit circle
and square with side-length 2. **This is the pattern that you should try to replicate.**

#### Pattern 2. Unit Circle of Radius 2 and Square with Side Length 1

This pattern describes a different region for Monte Carlo Integration,
as it fails to calculate $\pi$ as the circle surpasses the area of the square, and now it
calculates the area of the square instead as the area of integration is defined
through the greater of the two regions. **This is a malignant pattern.**

## Entities, State Variables, and Scales

### State Variables and Scale

In this context, the state variables relate to trials, in this instance,
a trial is represented as a point in a 2-dimensional plane.
Once you have enough trials, the indicator variable converges into
$\pi$ by the fact that a sufficient number of points reside in the union of
interest.

```{raw} latex
\begin{tabular}{llll}
\hline
\textbf{Variable} & \textbf{Scale} & \textbf{Type} & \textbf{Description} \\
\hline
$x$ & [-1 - 1] & Double & A sample of U[0,1] that determines the x-position of the trial \\
$y$ & [-1 - 1] & Double &  A sample of U[0,1] that determines the y-position of the trial \\
$z = x^2 + y^2 $ & [0 - 1] & Double & This refers to the variable that represents a circle's standard form.  \\
$|z| <= 1 $ & 0 or 1 & Binary & This is the binary that states is the point in the circle. \\
$x_{in}$ & [0 - 1] & Product of Double and Binary & The product of z and x that is used to show a point that exists within the circle. \\
$y_{in}$ & [0 - 1] & Product of Double and Binary & The product of z and y that is used to show a point that exists within the circle. \\
Darts in Circle, $D_{in}$ & [0 - $\infty$] & Double & This variable represents the summation over z. \\
Darts out of Circle, $D_{out}$ & [0 - $\infty$] & Double & The total number of points minus Darts in Circle. \\
Pi Approximation, $\hat{\pi}$ & [0 - $\infty$] & Double & The ratio of Darts in Circle over Darts out of Circle.\\
Percent Error & [0 - $\infty$] & Double & The percent difference ($\frac{|\hat{\pi}-\pi|}{\pi}$) between the approximation and $\pi$. \\
\hline
\end{tabular}
```

## Process Overview and Scheduling

### Processes

The model is developed to demonstrate the process of Monte Carlo Integration.
It is structured within three subprocesses, one related to the generation of samples
(updated samples from a uniform distribution into two variables, x and y) and their
placement onto a 2-D chart to show the uniformity of the random number generator,
another subprocess concerns the if statement determining whether any specific
point resides in the unit circle,
and the final subprocess referring to the construction of the state
variables $x_in$ and $y_in$, with a zero referring to a point that is out
of the unit circle and then removing the point or coloring it
differently than a point that is marked with its calculated value, along with
summing on z to calculate $D_{in}$, using this state variable along
with the total number of points in the circle to define the new state variables:
$D_{out}$, $\hat{\pi}$ (through the ratio, $\frac{D_{in}}{D_{out}}$), and
percent error with the process defined in state variables and scale.

The state variables are updated once at the beginning of the simulation when
the system is initialized. During this process, the user determines the number
of points, which changes the accuracy of the simulation.

### Scheduling (Lab 1)

The simulation starts when the sheet or program is initialized by the user.
Once it has been initialized, the first subprocess begins by starting the
random number generation for the first two state variables, $x$ and $y$
is the first task, because the subsequent state variables and subprocesses
depend on these initial variables. Afterwards, the subprocess for the placement of
points activates, plotting the points, triggering the third subprocess of determining
through an if statement the validity of the points (are they within the circle). Finally,
the fourth subprocess builds the state variables $x_in$, $y_in$, Darts in Circle,
Darts out of Circle, Pi Approximation, and Percent Error, based on the results of
state variables $z$, $x$, and $y$.

```{raw} latex
\begin{enumerate}
    \item \textbf{System Initialization:}
    \begin{enumerate}
        \item User defines the total number of random points ($N$) to be generated for the simulation.
        \item Initial state variables are set (e.g., $D_{in} = 0$, $D_{out} = 0$).
    \end{enumerate}

    \item \textbf{Random Sample Generation and Placement:}
    \begin{enumerate}
        \item Generate $N$ random $x$-coordinates from a uniform distribution (typically between -1 and 1, or 0 and 1 if considering a quadrant).
        \item Generate $N$ random $y$-coordinates from a uniform distribution (similarly, between -1 and 1, or 0 and 1).
        \item Plot the generated $(x, y)$ points on a 2-D chart.
    \end{enumerate}

    \item \textbf{Point Evaluation (In-Circle Check):}
    \begin{enumerate}
        \item For each generated point $(x, y)$:
        \begin{enumerate}
            \item Calculate $z = x^2 + y^2$.
            \item If $z \le 1$, the point is inside or on the unit circle.
            \item If $z > 1$, the point is outside the unit circle.
        \end{enumerate}
    \end{enumerate}

    \item \textbf{State Variable Construction and Calculation:}
    \begin{enumerate}
        \item For each point:
        \begin{enumerate}
            \item If the point is inside the unit circle (from step 3.1.2):
            \begin{enumerate}
                \item Assign the point's coordinates to $x_{in}$ and $y_{in}$ (or simply mark it as 'in').
                \item Increment the count of points inside the circle ($D_{in}$).
                \item Color or mark the point differently to distinguish it as inside.
            \end{enumerate}
            \item If the point is outside the unit circle (from step 3.1.3):
            \begin{enumerate}
                \item Assign a zero or null value to $x_{in}$ and $y_{in}$ for this point (or simply mark it as 'out').
                \item Remove the point or color it differently to distinguish it as outside.
                \item Increment the count of points outside the circle (or calculate $D_{out} = N - D_{in}$ after all points are processed).
            \end{enumerate}
        \end{enumerate}
        \item Calculate the approximation of Pi: $\hat{\pi} = 4 \times \frac{D_{in}}{N}$ (assuming the square enclosing the circle spans from -1 to 1 in both $x$ and $y$, thus having an area of 4; if using a quadrant, the ratio is multiplied by 4).
        \item Calculate the percent error: $Percent Error = \frac{|\hat{\pi} - \pi_{actual}|}{\pi_{actual}} \times 100\%$.
    \end{enumerate}
\end{enumerate}
```

## Design Concepts

### Basic Principles

This model depicts a classic problem of numerical integration using random numbers to
compute a multidimensional definite integral using $N$ uniform samples also known as Monte Carlo Integration through Crude Monte Carlo (CMC).
Moreover, this process leverages the Law of Large Numbers that allows for the average of the indictor variable, $\hat{\pi}$ to
converge to $\pi$ with a sufficient number of trials. In this case, we define the Law of Large Numbers as
Khinchin's Weak Law of Large Numbers: the observation that the average of the results obtained from a large number of
i.i.d random samples converges to the value, if it exists,
which is supported by Proof 1 in the appendix {ref}`sec:proofs`. {cite}`shum2024laws`
Additionally, the foundations of Monte Carlo Integration are further elaborated in one of the prerequisite chapters,
{ref}`sec:buffons_needle_summary`.

### Stochaticity

Stochaticity is used when initializing the model to build the uniform state variables
$x$ and $y$; this process allows for the usage of Monte Carlo Integration within the
defined region (the unit circle embedded within a square with side length of 2).
During the simulation, stochaticity is used to define the sample ($x, y$ points) that
defines the estimate of $\hat{\pi}$ and the visual representations of the points
through the subprocesses defined through the processes section.

## Input Data

There is no input data beyond then number of samples and the regions defined in
the functions that define the subprocesses.

## Questions left to the reader to answer

1. What happens to the estimate of $\pi$ when $N$, the number of points increases or decreases?
2. Why did we use the ODD approach for organizing our model despite its simplicity?  
:::

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

:::{admonition} Lab 4
:class: danger dropdown
(lab-4)=
# Lab 4: Posterior Probability Estimation with Monte Carlo Methods (Python + Excel)

## Lab 4 Prerequisites

### Pre-labs

- {ref}`prelab-4`

### Mandatory Chapters for Lab 4

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`sec:distribution_modeling`

## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables and Scales (Lab 4)

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

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 5
:class: attention dropdown
(lab-5)=
# Lab 5: Foundations of Modelling (SIMIO, Anylogic, or Python)

## Lab 5 Prerequisites

### Pre-labs

- {ref}`prelab-5`

### Mandatory Chapters for Lab 3

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`sec:building_simulation_models`

### Recommended Chapters for Lab 3

- {ref}`sec:random_number_generation`
- {ref}`sec:distribution_modeling`


## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 6
:class: tip dropdown
(lab-6)=
# Lab 6: Applied Queuing Theory in Simulation (Ciw, SIMIO, or Anylogic)

## Lab 6 Prerequisites

### Pre-labs

- {ref}`prelab-6`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle

## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 7
:class: attention dropdown
(lab-7)=
# Lab 7: Introduction to System Dynamics from Queuing (SIMIO, Ciw, or Anylogic)

## Lab 7 Prerequisites

### Pre-labs

- {ref}`prelab-7`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle

## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 8
:class: attention dropdown
(lab-8)=
# Lab 8: Modelling the Spread of Illness via SIR Models (PySim/Salabim, Anylogic, or SIMIO)

## Lab 8 Prerequisites

### Pre-labs

- {ref}`prelab-8`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle


## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 9
:class: danger dropdown
(lab-9)=
# Lab 9: Introduction to Hybrid Modelling (System Dynamics + Discrete Event) (PySim/Salabim, Anylogic, or SIMIO) 

## Lab 9 Prerequisites

### Pre-labs

- {ref}`prelab-8`
- {ref}`prelab-9`

### Chapters
- {ref}`sec:preface`
- {ref}`sec:system_modeling`
- 

## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 10
:class: danger dropdown
(lab-10)=
# Lab 10: Introduction to Agent-Based Modelling (Python via Mesa or Anylogic)

## Lab 10 Prerequisites

### Pre-labs

- {ref}`prelab-10`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle


## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer

## Questions to Think about:
:::

:::{admonition} Lab 11
:class: attention dropdown
(lab-11)=
# Lab 11: Optimization through Simulation (PySim/Salabim, Anylogic, or SIMIO)

## Lab 11 Prerequisites

### Pre-labs

- {ref}`prelab-11`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle

## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::

:::{admonition} Lab 12
:class: attention dropdown
(lab-12)=
# Lab 12: Simulating an Election (Monte Carlo vs ABM) (PySim/Salabim, Anylogic, or SIMIO)

## Lab 12 Prerequisites

### Pre-labs

- {ref}`prelab-12`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle

## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::
