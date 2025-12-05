(prelab-9)=
# Pre-Lab 9: Introduction to Experimental Design and Sensitivity Analysis (Read)

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

<example>

#### Fractional Factorial

Fractional factorials are particularly useful when the event space is so
large that it would be impossible to fully compute every possible combination
of event spaces as they cover the entire event space ensuring 
that _every_ possibility is covered.

<example>

### Response Surface (Central-composite)

A Central Composite Design is composed on top of a two-level ($2^k$)
full or fractional factorial design, with center points (median of values
from the factorial design)

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

It is defined as the following mathematical construction


The Sobol Method is often used within the context of Quasi-Monte Carlo

:::

:::{tab-item} Fractional Factorial Method


:::

::::

[^1]: Some sources will describe factors as Independent Variables (IV) or features, but
a factor is the specification of a IV (levels) on some type of scale, while IVs are more
conceptual and difficult to directly or completely measure.
