(prelab-9)=
# Pre-Lab 9: Overview of Experimental Design and Sensitivity Analysis (Read)

The overall goal of simulation projects is to determine the
impact of inputs on a system, $S$, and to interpret the outputs
of said system. Most simulations taking a naive view
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
fractional. But this also has the benefit of requiring half of the runs of a
full-factorial, making it possible to understand a part of a complex event
space in a finite amount of time.

### Response Surface (Central-composite)

A Central Composite Design is composed on top of a two-level ($2^k$)
full or fractional factorial design, with center points (median of values
from the factorial design) and axial points (runs the same as the center
points with one factor change to be below and above the median of the factorial
levels).

This creates a matrix called the \textit{design matrix},
representing the specific coordinates for each simulation run.
Below is an example for a 2-factor experiment (e.g., Temperature and Pressure):

```{raw} latex
\begin{table}[h!]
    \centering
    \caption{Design Matrix for a Central Composite Design ($k=2$, $\alpha=\sqrt{2}$)}
    \begin{tabular}{|c|l|c|c|}
        \hline
        \textbf{Run} & \textbf{Point Type} & \textbf{$x_1$ (Temp)} & \textbf{$x_2$ (Pressure)} \\
        \hline
        \multicolumn{4}{|c|}{\textit{Factorial Points (Corners)}} \\
        \hline
        1 & Factorial & $-1$ & $-1$ \\
        2 & Factorial & $+1$ & $-1$ \\
        3 & Factorial & $-1$ & $+1$ \\
        4 & Factorial & $+1$ & $+1$ \\
        \hline
        \multicolumn{4}{|c|}{\textit{Axial Points (Star Points)}} \\
        \hline
        5 & Axial & $-\sqrt{2}$ & $0$ \\
        6 & Axial & $+\sqrt{2}$ & $0$ \\
        7 & Axial & $0$ & $-\sqrt{2}$ \\
        8 & Axial & $0$ & $+\sqrt{2}$ \\
        \hline
        \multicolumn{4}{|c|}{\textit{Center Points}} \\
        \hline
        9 & Center & $0$ & $0$ \\
        10 & Center & $0$ & $0$ \\
        11 & Center & $0$ & $0$ \\
        \hline
    \end{tabular}
    \label{tab:ccd_design_matrix}
\end{table}

In this matrix:
\begin{itemize}
    \item \textbf{$\pm 1$} represents the low/high levels of the standard factorial design.
    \item \textbf{$0$} represents the median (center) value.
    \item \textbf{$\pm \sqrt{2}$} (approx $\pm 1.414$) represents the axial distance $\alpha$, which allows 
    curvature estimation.
\end{itemize}
```

Often a Regression (linear) is used to obtain results from
the central composite design see: {ref}`sec:Types_Sensitivity_Analysis` for
more details on obtaining information from this design.

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

For example, consider an ER simulation where the output of
interest is Average Patient Wait Time. You have three input factors:

1. Number of Doctors
2. Number of Nurses
3. Patient Arrival Rate

To perform an OAT analysis, you would establish a baseline scenario
(e.g., 3 Doctors, 6 Nurses, 10 Patients/hr).
You then vary the Number of Doctors from 1 to 5
while holding the Nurses and Arrival Rate strictly constant at
their baseline values. Once that is complete,
you reset the Doctors to 3 and vary the Number of Nurses
while holding the other two constant.

Because you move only one at a time, you never observe a scenario where
both the Number of Doctors is low, and the Patient Arrival Rate is high simultaneously.

However, this approach has some issues and limitations because of the independence
of factors, and because it requires _at least_ one simulation per factor change:

1) It cannot account for interactions between factors by definition;
2) It is inefficient for a large number for factors, particularly if the design
is fully factorial instead of partial factorial.

This is usually used for either small simulations, screening possible variables
of interest, and debugging (and unit testing). However, it does not and cannot
establish causality by itself nor can it be used to support causality outside a single-factor model.

:::

:::{tab-item} Regression

The reader is likely familiar with the concept of regression, most likely as
a transformation of variables (represented as a vector) into another state space
while losing some information (error in the regression estimator).

In this case, regression typically means to fit a
generalized linear model to the data using the coefficient of determination ($r^2$)
as the measure of quality of the predictive power of the
regression against the original data.

However, for our purposes we use regression not
merely for prediction, but for inference. We treat the simulation model
as a black box function $f(x)$ and approximate it using
 a linear metamodel (or response surface). By analyzing
 the coefficients of this linear approximation,
 we can determine which input factors carry the most weight
 in influencing the output.

```{raw} latex
The goal is to approximate the simulation output $Y$ using a linear combination of the inputs $x_1, x_2, \dots, x_k$:

\begin{equation}
    Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_k x_k + \epsilon
\end{equation}

\noindent Where:
\begin{itemize}
    \item $Y$ is the simulation output variable.
    \item $x_i$ are the input parameters (factors).
    \item $\beta_i$ are the regression coefficients.
    \item $\epsilon$ is the error term (residuals), representing the non-linear behavior 
    or stochastic noise not captured by the linear model.
\end{itemize}

A raw regression model is often misleading for sensitivity analysis because the
input variables likely have different units and scales (e.g., comparing Pressure
in Pascals vs. Temperature in Celsius). A large coefficient $\beta$ might simply mean
the unit of $x$ is small, not that the system is sensitive to it.

To resolve this, we use Standardized Regression Coefficients (SRCs).
This involves standardizing the input data (often to a mean of 0 and variance of 1,
or coding them between -1 and +1) before fitting the model. This is similar to the
methods used when constructing a factorial design.

When the model is standardized, the magnitude of the coefficient $|\beta_i|$ becomes a direct measure of sensitivity:
\begin{itemize}
    \item \textbf{High $|\beta_i|$}: The output $Y$ is highly sensitive to input $x_i$.
    \item \textbf{Positive/Negative Sign}: Indicates the direction of the relationship (e.g., $+ \beta$ means $Y$ increases as $x$ increases).
\end{itemize}


As noted in the introduction, the quality of this analysis relies on the
correlation. In multiple regression, we utilize the Coefficient of Determination ($R^2$):

\begin{equation}
    R^2 = \frac{\text{Variance explained by the model}}{\text{Total Variance of } Y}
\end{equation}

\noindent The $R^2$ value can have specific implications for your sensitivity analysis:
\begin{itemize}
    \item \textbf{If $R^2 \approx 1$}: The simulation is predominantly linear. The SRCs are highly reliable indicators of sensitivity.
    \item \textbf{If $R^2$ is low (e.g., $< 0.5$)}: The simulation is driven by strong non-linearities or interactions that the linear model cannot capture. In this case, linear regression sensitivity analysis is \textbf{invalid}, and you must move to non-linear methods (like variance-based sensitivity analysis).
\end{itemize}
```

:::

:::{tab-item} Sobol (Variance-Based) Method
The Sobol method decomposes the variance of the model into fractions that belong
to different factors or set of factors. By this method, the Sobol method provides
information about quantification of the size
of the factor and the interaction between factors in the system.

It is defined as the following mathematical formulation:

\begin{gather*}
Y = f_0 + \sum_{i=1}^{d} f_i(X_i) + \sum_{i<j} f_{ij}(X_i, X_j) + \dots + f_{1,2\dots d}(X_1, X_2, \dots X_d) \\
\text{Var}(Y) = \sum_{i=1}^{d} V_i + \sum_{i<j} V_{ij} + \dots + V_{1,2\dots,d}
\end{gather*}

The Sobol Method is often used within the context of Quasi-Monte Carlo (QMC) methods.
Calculating these variances requires computing high-dimensional integrals, which is
computationally expensive using standard Monte Carlo sampling ($O(1/\sqrt{N})$ convergence). Using QMC sequences
(specifically Sobol sequences) improves the convergence rate to approximately $O(1/N)$, making the calculation of
indices feasible for complex models.

To make the variance decomposition of the Sobol sequence interpretable,
we normalize the partial variances by the total variance $V = \text{Var}(Y)$.
This results in two primary metrics for each factor $X_i$:

```{raw} latex
\begin{enumerate}
    \item \textbf{First-Order Index ($S_i$):}
    \begin{equation}
        S_i = \frac{V_i}{\text{Var}(Y)}
    \end{equation}
    This measures the \textbf{main effect} of factor $X_i$ alone, excluding any interactions.
    It represents the reduction in variance you would achieve if you could fix $X_i$ to its true value.

    \item \textbf{Total-Order Index ($S_{Ti}$):}
    \begin{equation}
        S_{Ti} = \frac{E_{\mathbf{X}_{\sim i}}[\text{Var}_{X_i}(Y|\mathbf{X}_{\sim i})]}{\text{Var}(Y)} = 1 - \frac{\text{Var}_{\mathbf{X}_{\sim i}}(E_{X_i}[Y|\mathbf{X}_{\sim i}])}{\text{Var}(Y)}
    \end{equation}
    This measures the contribution of factor $X_i$ \textbf{including all its interactions} with other parameters. 
    Mathematically, it is the sum of all sensitivity indices where index $i$ appears (e.g., $S_i + S_{ij} + S_{ijk} + \dots$).
\end{enumerate}

By comparing $S_i$ and $S_{Ti}$, we can derive deep insights into the model structure:
\begin{itemize}
    \item \textbf{If $S_{Ti} \approx S_i$}: The factor $X_i$ acts independently. There are no significant interactions with other parameters.
    \item \textbf{If $S_{Ti} \gg S_i$}: The factor $X_i$ is heavily involved in interactions. Changing $X_i$ alone might have a small effect, but changing it in combination with other specific factors has a large effect.
    \item \textbf{If $S_{Ti} \approx 0$}: The factor is non-influential (unimportant) and can be fixed to a constant value to simplify the model (Dimensionality Reduction).
\end{itemize}
```

:::

:::{tab-item} Fractional Factorial Method
The Fractional Factorial method builds a design matrix and then uses this design
matrix to run simulations of the original model. This design matrix
then is evaluated through the dot products of the linear combination
of the parameters.

While a Full Factorial design ($2^k$) provides information on all possible main
effects and interactions, it becomes computationally prohibitive as the number
of factors $k$ increases. The Fractional Factorial design ($2^{k-p}$) solves this by
selecting a specific subset of the runs (a fraction $\frac{1}{2^p}$ of the total) to
estimate the most important effects efficiently.

The evaluation mentioned typically refers to the calculation of Contrasts or Effects.
Since the columns of the design matrix are orthogonal, the effect of any specific factor $j$ can be
calculated as the normalized dot product of the response vector $\mathbf{Y}$ and the column vector of
signs for that factor $\mathbf{x}_j$:

\begin{equation}
    \text{Effect}_j = \frac{2}{N} (\mathbf{x}_j \cdot \mathbf{Y}) = \frac{2}{N} \sum_{i=1}^{N} x_{ij} y_i
\end{equation}

\noindent Where:
\begin{itemize}
    \item $N$ is the total number of runs in the fractional design.
    \item $x_{ij} \in \{-1, +1\}$ is the level of factor $j$ in run $i$.
    \item $y_i$ is the simulation output for run $i$.
\end{itemize}

The trade-off for running fewer simulations is \textbf{Aliasing}.
Because we do not run all combinations, certain effects become
mathematically indistinguishable from one another. For example, the
main effect of Factor A might be aliased with the interaction of
Factors B and C ($A = BC$).

We categorize these designs by their \textbf{Resolution}, which tells us how bad"the aliasing is:
\begin{itemize}
    \item \textbf{Resolution III:} Main effects are aliased with 2-factor interactions. (Good for screening many variables for their impact,
    bad for detailed information on how the input interacts wit the rest of the system).
    \item \textbf{Resolution IV:} Main effects are clear, but 2-factor interactions are aliased with other 2-factor interactions.
    \item \textbf{Resolution V:} Main effects and 2-factor interactions are clear; 2-factor interactions are aliased
    with 3-factor interactions (which are usually negligible).
\end{itemize}

Fractional designs rely on the \textit{Sparsity of Effects Principle}, which states that the system
is likely driven by main effects and low-order interactions. High-order interactions (e.g., 3-way, 4-way)
are usually rare and negligible, allowing us to sacrifice them to save computational time.

:::

::::

[^1]: Some sources will describe factors as Independent Variables (IV) or features, but
a factor is the specification of a IV (levels) on some type of scale, while IVs are more
conceptual and difficult to directly or completely measure.
