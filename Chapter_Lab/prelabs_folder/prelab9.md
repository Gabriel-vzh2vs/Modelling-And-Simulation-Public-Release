(prelab-9)=
# Pre-Lab 9: Overview of Experimental Design and Sensitivity Analysis (Read)

The overall goal of simulation projects is to determine the
impact of inputs on a system, $S$, and to interpret the outputs
of said system. Most simulations taking an naive view
of experimental and simulation design, meaning that the
goal of the simulation is to observe the influence of
a factor through either changing one factor at a time
or using random numbers to generate an average.
However, there are methods that can improve
interpretation quality and allow for the removal
of non-informative factors.

## What is a Factor?

Factors[^1] represent different inputs into the simulation
model, and as such there are different types of factors:

- Quantitative
- Qualitative

With two subcategories describing the behaviors of the factor:

- Deterministic (Fully Observable, Controllable and Predictable)
- Stochastic (Not Fully Controllable nor Predictable)

And factors influence model outputs, and these outputs
are called responses. And in simulation and modelling,
technically all factors are controllable but fully controlling
them is likely to require a tradeoff in some way (such as decreasing
model fidelity or making an assumption).

Normally, in a simulation, depending on its complexity, there
can be many factors and responses belonging to $S$, and some
examples are below:

```{raw} latex
\begin{tabular}{|p{2.2cm}|l|c|c|c|c|l|}
\hline
\multicolumn{1}{|c|}{System, $S$} & \multicolumn{1}{c}{Possible Factors} & \multicolumn{1}{c}{Quantitative} & \multicolumn{1}{c}{Qualitative} & \multicolumn{1}{c}{Controllable} & \multicolumn{1}{c}{Uncontrollable} & \multicolumn{1}{|c|}{Possible Responses} \\
\hline

% SYSTEM 1: Emergency Department
\multirow{6}{=}{Emergency Department (ED)} 
 & Patient arrival rate & $\checkmark$ & & & $\checkmark$ & Waiting times \\
 & Triage protocol & & $\checkmark$ & $\checkmark$ & & Length of stay (LOS) \\
 & Number of doctors & $\checkmark$ & & $\checkmark$ & $\checkmark$? & LWBS (Left w/o being seen) \\
 & Bed capacity & $\checkmark$ & & $\checkmark$ & & Staff utilization \\
 & Treatment times & $\checkmark$ & & & $\checkmark$ & Diversion frequency \\
 & Shift schedule policy & & $\checkmark$ & $\checkmark$ & & \\
\hline

% SYSTEM 2: Cloud Computing Cluster
\multirow{6}{=}{Cloud Computing Server} 
 & Job arrival rate & $\checkmark$ & & & $\checkmark$ & Response time / Latency \\
 & Job size distribution & $\checkmark$ & & & $\checkmark$ & Throughput \\
 & Max Number of Users & & $\checkmark$ & $\checkmark$ & & Server utilization \\
 & Number of servers & $\checkmark$ & & $\checkmark$ & $\checkmark$? & Power consumption \\
 & Failure/Repair rates & $\checkmark$ & & & $\checkmark$ & Dropped requests \\
 & Priority queuing rules & & $\checkmark$ & $\checkmark$ & & System reliability \\
\hline

% SYSTEM 3: Traffic Intersection
\multirow{5}{=}{Traffic Intersection} 
 & Signal cycle length & $\checkmark$ & & $\checkmark$ & & Average vehicle delay \\
 & Vehicle arrival rate & $\checkmark$ & & & $\checkmark$ & Queue length \\
 & Turn-lane capacity & $\checkmark$ & & $\checkmark$? & $\checkmark$? & Fuel consumption \\
 & Weather conditions & & $\checkmark$ & & $\checkmark?$ & Accident probability \\
 & Right-on-red policy & & $\checkmark$ & $\checkmark$ & & Throughput \\
\hline

\end{tabular}
```

## Non-Extensive Description of Experimental Designs

In this case, a designed experiment is a test or series of tests where
purposive changes are made to the input variables of a process so that we may
observe and identify corresponding changes in the output response. The point of
experimental design in simulation is to establish some level of causality, where one factor
has mathematical and technical support for causing specific changes in responses.

Moreover, there are almost an infinite amount of methods to do so, but this section
will cover some of the most commonly used ones in simulation.

### Factorials

Most literature in experimental design uses a method based on factorial design.
Factorial design means that it is tests a set of combinations of factors as
different _treatments_ across the possible event space.

#### Full Factorial

Full-Factorials are particularly useful in small, less-complex models
as they cover the entire event space ensuring that _every_ possibility
is covered.

This example is based on {cite}`olver2010nist`, a commonly-cited source for
engineers using statistical concepts:

Suppose there is a polishing operation with three factors:
Speed ($X_a$), Feed, ($X_b$) and Depth ($X_c$),
and one response variable: Yield, $Y$. Speed, Feed, and Depth, the three factors
each have three levels (Low, Medium, and High). In this case, we want to determine
the impact of each factor on yield.

We can defined the table of factor levels through a factor level table:

``` {raw} latex
\begin{tabular}{|l||c|c|c||c|}
    \hline
    % Header Row
        & \textbf{\makecell{Low\\(-1)}} & \textbf{\makecell{Standard\\(0)}} & \textbf{\makecell{High\\(+1)}} & \textbf{Units} \\
    \hline\hline
    % Data Rows
    \textbf{Speed} & 12 & 16 & 20 & rpm \\
    \hline
    \textbf{Feed} & 0.002 & 0.004 & 0.006 & \makecell{cm/\\sec} \\
    \hline
    \textbf{Depth} & 0.005 & 0.01 & 0.015 & \makecell{cm/\\sec} \\
    \hline
\end{tabular}
```

In this case, it is desired to try various combinations of these setting
to find the ideal way for running the polisher. In this case, there are
2^3, as there are three factors ($k = 3$), and 2 settings (+1/-1), meaning
that this design has 8 combinations via the factorial expression $2^k$.

Here is a visualization of this full factorial design:

```{figure} 23factorial.png
:label: fig:23factorial

Here is a visualization of this full factorial design.
```

If the full model of all possible combinations is ran, then the all of the
main effects, second-order interactions, and third-order interactions can
be expressed as a full model in this form with all coefficients being estimable:

\begin{align*}
    Y \quad = \quad & \beta_0 + \beta_a X_a + \beta_b X_b + \beta_c X_c + \\
    & \beta_{ab} X_a X_b + \beta_{ac} X_a X_c + \beta_{bc} X_b X_c + \\
    & \beta_{abc} X_a X_b X_c + \epsilon
\end{align*}

And this can be expressed through a tabular form called "standard order"
which lists every vertex on the factorial design in order once it has been
recoded with low settings being -1, and high settings being +1:

```{raw} latex
\begin{tabular}{|c||c|c|c|}
        \hline
         & $\mathbf{X_a}$ & $\mathbf{X_b}$ & $\mathbf{X_c}$ \\
        \hline\hline
        (1) & -1 & -1 & -1 \\
        \hline
        a & +1 & -1 & -1 \\
        \hline
        b & -1 & +1 & -1 \\
        \hline
        ab & +1 & +1 & -1 \\
        \hline
        c & -1 & -1 & +1 \\
        \hline
        ac & +1 & -1 & +1 \\
        \hline
        bc & -1 & +1 & +1 \\
        \hline
        abc & +1 & +1 & +1 \\
        \hline
    \end{tabular}
```

#### Fractional Factorial

Fractional factorials are particularly useful when the event space is so
large that it would be impossible to fully compute every possible combination
in the event space or when a series of factors are considered unfeasible to
co-occur.

Like the previous example, this example is
based on {cite}`olver2010nist`, a commonly-cited source for
engineers using statistical concepts:

First, a fractional factorial is generally based on a smaller full-factorial
design, for example, if an experiment has a $2^3$ design, and we decided
to make a half-factorial design, we should start with a 2^2 design with
a high and a low setting. This gives use the following standard order table:

```{raw} latex
\begin{tabular}{|c|c||c|}
        \hline
         & $\mathbf{X_a}$ & $\mathbf{X_b}$ \\
        \hline\hline
         1 & $\mathbf{-1}$ & $\mathbf{-1}$ \\
         \hline
         2 & $\mathbf{+1}$ & $\mathbf{-1}$ \\
         \hline
         3 & $\mathbf{-1}$ & $\mathbf{+1}$ \\
         \hline
         4 & $\mathbf{+1}$ & $\mathbf{+1}$ \\
         \hline
\end{tabular}
```

In this case, the $2^2$ factorial design has the sufficient number of runs,
but there is a insufficient number of variables, as we want three when only
two exist in the current table. However, we can address this through creating
a new variable defined as the interaction term of $x_a$ and $x_b$: $x_c$.

```{raw} latex
\begin{tabular}{|c|c||c|c|}
        \hline
         & $\mathbf{X_a}$ & $\mathbf{X_b}$ & $\mathbf{x_c}$ \\
        \hline\hline
         1 & $\mathbf{-1}$ & $\mathbf{-1}$ & $\mathbf{+1}$\\
         \hline
         2 & $\mathbf{+1}$ & $\mathbf{-1}$ & $\mathbf{-1}$\\
         \hline
         3 & $\mathbf{-1}$ & $\mathbf{+1}$ & $\mathbf{-1}$\\
         \hline
         4 & $\mathbf{+1}$ & $\mathbf{+1}$ & $\mathbf{+1}$\\
         \hline
\end{tabular}
```

The limitation of this approach this that it is going cover less
of the event space than a full-factorial. This leads to averages of the
main effect only being based on four runs instead of the eight of the full
fractional. But this also has the benefit of requiring half of the runs.
of a full-factorial, making it possible to understand a part of an
extremely complex or large event space in a reasonable amount of time.

### Response Surface (Central-composite)

A Central Composite Design is composed on top of a two-level ($2^k$)
full or fractional factorial design, with center points (median of values
from the factorial design) and axial points (runs the same as the center
points with one factor change to be below and above the median of the factorial
levels.)

This creates a matrix called the _design matrix_

<example>

Often a Regression (linear) is used to obtain results from
the central composite design see: {ref}`sec:Types_Sensitivity_Analysis` for
more details on obtaining information from this design.

### Randomized Design (Latin-Hypercube)

<example>


(sec:Types_Sensitivity_Analysis)=
## Types of Sensitivity Analysis

There are many forms of sensitivity analysis with their applications,
limitations, and mathematical foundations. Some might be used because
of either assumptions about the event space, limitations on possible
configurations (often because of resource limits), or as a method
for filtering out variables of interest.

::::{tab-set}

:::{tab-item} Morris's One at A Time/One-Way Design (OAT)

OAT is the typical method when most people think about sensitivity analysis,
it is changing a variable across a range over a series of simulations for
each variable, *independent* of all other variables.

--Example --

However, this approach has some issues and limitations because of the independence
of factors, and because it requires _at least_ one simulation per factor change:

1) It cannot account for interactions between factors by definition;
2) It is inefficient for a large number for factors, particularly if the design
is fully factorial instead of partial factorial.

This is usually used for either small simulations, screening possible variables
of interest, and debugging (and unit testing). However, it does not and cannot
establish causality by itself nor can it be used to support causality outside
of a single-factor model.

:::

:::{tab-item} Regression

The reader is likely familiar with the concept of regression, most likely as
a transformation of variables (represented as a vector) into another state space
while losing some information (error in the regression estimator).

In this case, regression typically means to fit a linear model to the data using
pearson correlation ($r$), 

:::

:::{tab-item} Sobol (Variance-Based) Method
The Sobol method decomposes the variance of the model into fractions that belong
to different factors or set of factors, which allows for quantification of the size
of the factor and the interaction between factors in the system.

It is defined as the following mathematical formulation:

\begin{gather*}
Y = f_0 + \sum_{i=1}^{d} f_i(X_i) + \sum_{i<j} f_{ij}(X_i, X_j) + \dots + f_{1,2\dots d}(X_1, X_2, \dots X_d) \\
\text{Var}(Y) = \sum_{i=1}^{d} V_i + \sum_{i<j} V_{ij} + \dots + V_{1,2\dots,d}
\end{gather*}

The Sobol Method is often used within the context of Quasi-Monte Carlo

:::

:::{tab-item} Fractional Factorial Method
The Fractional Factorial method builds a design matrix and then uses this design
matrix to run simulations of the original model. This design matrix
then is evaluated through the  dot products of the linear combination
of the parameters

:::

::::

[^1]: Some sources will describe factors as Independent Variables (IV) or features, but
a factor is the specification of a IV (levels) on some type of scale, while IVs are more
conceptual and difficult to directly or completely measure.
