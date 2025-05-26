(sec:pre-labs)=
# Pre-Labs

Pre-labs are made to aid the reader with the concepts presented in the
Laboratory Section of this book. These pre-labs consist of structured
activities linked with the lab with the same number (e.g: Pre-Lab 1 connects to Lab 1).

There are two categories of Pre-Lab: Read and Do. Pre-Labs marked with "Read" are
functionally equivalent to a typical section of the book as in the reader sees examples
and learns similarly to the rest of the sections of the book. In contrast,
Pre-Labs marked with "Do" ask the reader to complete an exercise step-by-step that
helps the reader comprehend the tasks they need to do for the associated lab.

Grading for the Pre-Labs is at the instructor's discretion; additionally, we recommend
completing a pre-lab for each lab at a 1 to 1 ratio (meaning, if you do 7 labs,
you should do 7 pre-labs). However, if you are self-studying, you can choose which
pre-labs you do based on your knowledge level.

(prelab-1)=
# Pre-Lab 1: Fundamental Excel Skills and Data Management (Read)

::::{tab-set}

:::{tab-item} Fundamental Excel Skills

## The Cell

a

## Formulas

b

## Ranges

c

## References

d

:::

:::{tab-item} Data Management

## Data Structures

## Data Cleaning

## Topic 3

## Topic 4
:::

::::

(prelab-2)=
# Pre-Lab 2: Tutorial for Monte Carlo Methods (Do)

This pre-lab uses XLrisk as the main implementation method; however,
these all of these tasks can be done within python as well
through monaco or pyMC (either one combined with the Copulas package).


## Functions

## Correlations

## Trials

## Results

## Skew and Kurtosis

## Walk-Through

(prelab-3)=
# Pre-Lab 3: Advanced Excel Functions or Fundamentals of Debugging (Do)

## Live Formulas

## Debugging

## Examples

## Walk-Through

(prelab-4)=
# Pre-Lab 4: Python Review (Read)
::::{tab-set}

:::{tab-item} Jupyter Notebook
:::

:::{tab-item} Conda

:::

:::{tab-item} Examples

:::

::::
(prelab-5)=
# Pre-Lab 5: Introduction to Simulation Software (Do)

::::{tab-set}

:::{tab-item} SIMIO
:::

:::{tab-item} Anylogic

:::

:::{tab-item} Python

:::

::::

(prelab-6)=
# Pre-Lab 6: A Quick Review of Queuing Theory (Reading)

## Exponential Distribution

In probability courses and textbooks you may have heard about the exponential
distribution, one of the most prototypical queuing systems ($M/M/1$) relies on the
exponential distribution for its service times and inter-arrival rates.

Now, what are the properties that make exponential distributions useful for

## Birth-Death Processes and Queues

A Birth-Death Process is the fundamental idea underpinning queuing theory
as every $M/M/1$, which was one of the first queues observed, is a birth-death
process. The first informal written description of a $M/M/1$ was in France, 

## Kendall's Notation for Queues

How are queues formally represented? For example, what does $M/M/1$ mean?

In general, every queue can be represented in the format A/B/c/K/N/D
with the last three often excluded in most literature.

:::{table}
:label: Kendall-Notation

| Position | Description                      | Common Symbols                                                                                                |
| :------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **A** | **Arrival Process** | M (Markovian/Poisson), D (Deterministic/Constant), E$_k$ (Erlang), G or GI (General/General Independent)                      |
| **B** | **Service Time Distribution** | M (Markovian/Exponential), D (Deterministic/Constant), E$_k$ (Erlang), G (General)                                  |
| **c** | **Number of Servers** | Integer value (1, 2, 3, ..., $\infty$)                                                                                      |
| **K** | **System Capacity** (Optional)      | Integer value (maximum number of customers in the system, including those being served), $\infty$ if omitted     |
| **N** | **Calling Population** (Optional)   | Integer value (size of the population from which customers arrive), $\infty$ (if omitted)                        |
| **D** | **Queue Discipline** (Optional)     | FIFO/FCFS (First-In, First-Out/First-Come, First-Served), LIFO/LCFS (Last-In, First-Out/Last-Come, First-Served), SIRO (Service In Random Order), PRI (Priority) |

:::

Using the {ref}`Kendall-Notation` above, we can determine that a $M/M/1$ queue is a
queue with a Markovian Arrival Process, a Service time that is Markovian,
and one server. Moreover, using this information, we know that the inter-arrival
times are exponential, and the time it takes to serve someone the queue is
also exponential, and that means we can calculate queue behaviors through
closed-form formulas, as seen below in {ref}`MM1Performance-Metrics`.

:::{table}
:label: MM1Performance-Metrics

| Performance Measure                      | Symbol        | Formula                                         |
| :--------------------------------------- | :------------ | :---------------------------------------------- |
| Arrival Rate                             | $\lambda$     | Given                                           |
| Service Rate                             | $\mu$         | Given or $\frac{1}{\text{service time}}$         |
| Server Utilization (Traffic Intensity)   | $\rho$        | $\frac{\lambda}{\mu}$                           |
| Probability of an Empty System           | $P_0$   | $1 - \rho$                                            |
| Probability of $n$ customers in the system | $P_n$       | $P_0 \rho^n = (1-\rho)\rho^n$                   |
| Average Number of Customers in the System | $L$ or $L_s$ | $\frac{\lambda}{\mu - \lambda} = \frac{\rho}{1-\rho}$ |
| Average Number of Customers in the Queue  | $L_q$        | $\frac{\lambda^2}{\mu(\mu - \lambda)} = \frac{\rho^2}{1-\rho}$ |
| Average Time a Customer Spends in the System | $W$ or $W_s$ | $\frac{1}{\mu - \lambda} = \frac{L}{\lambda}$     |
| Average Time a Customer Spends in the Queue  | $W_q$     | $\frac{\lambda}{\mu(\mu - \lambda)} = \frac{L_q}{\lambda}$ |
| Probability that the number of customers in the system is greater than or equal to *n* | $P(\text{N} \ge n)$ | $\rho^n$ |
| Probability that the waiting time in the queue is greater than *t* (for $t \ge 0$) | $P(T_q > t)$ | $\rho e^{-(\mu-\lambda)t}$|
| Probability that the system time is greater than *t* (for $t \ge 0$) | $P(T_s > t)$ | $e^{-(\mu-\lambda)t}$|

:::

Let's look at an example of a $M/M/1$ queue to show the power of these facts. 

```{admonition} M/M/1 Example:
:type: tip
  An example of an admonition with a _title_.
```

(prelab-7)=
# Pre-Lab 7: Automated Distribution Fitters (Do)

## On Automated Distribution Fitters (i.e: Phitter, Fitter)

Through simulation literature and real-world applications, it is relatively rare to see
methods as seen with {cite}`Krzysztofowicz:25` for one reason, the vast majority of the
literature is not building novel distributions or meta-Gaussians, but instead often use one of
these four tests to pick from an existing distributions.

- The $\chi^2$ Goodness Of Fit Test (this test can be deceptive, read {ref}`sec:distribution_modeling`)
for more information about this, and that you should consider not using this for continuous distributions.
- Kolmogorov–Smirnov test (the test for comparing data to continuous distributions, which has the limitation
of sensitivity to differences near the median between an empirical and parametric distribution)
- Anderson–Darling Test 
- Cramér–von Mises Criterion



## The Exercises


(prelab-8)=
# Pre-Lab 8: Review of Ordinary Differential Equations (Do)

Previously in this text, we discussed and worked with queuing networks, the
Monte Carlo Method, System Dynamics, Distribution Modelling,
Random Variates, Random Number Generation, and Output Analysis
which are ubiquitous throughout simulation; however, these are
required but not sufficient for understanding the field of simulation,
because you will often see ODEs, SDEs, and PDEs being used to model behavior,
and a simulation practitioner (or any engineer) should be familiar
with them. This pre-lab focuses on giving a basic review of
ODEs and their application in simulation and modelling.

## What even are DEs, ODEs, PDEs, and SDEs?

In general, a differential equation (DE) is an equation that relates
a function to its derivatives, an example is

```{math}
1 + 1 = 2
```

Additionally, there are several types of DEs, the first two
of which you are likely familiar with

- ODE (Ordinary Differential Equations)
- PDE (Partial Differential Equations)
- SDE (Stochastic Differential Equations)

In this work, we define ODEs as 

## ODEs for Modelling

These examples of using ODEs, PDEs, and SDEs for modelling are inspired by
{cite}`harte1988consider`, which might sound a bit silly if you read the title,
but it is a landmark work in modelling and problem-solving in
Environmental Science.

::::{tab-set}

:::{tab-item} Example 1: Depleting Resources

:::

:::{tab-item} Example 2: A Warming Sphere

:::

::::

## PDEs for Modelling

::::{tab-set}

:::{tab-item} Example 1: Heat flow in a uniform rod

:::

:::{tab-item} Example 2: Brownian motion

:::

::::

## SDEs for Modelling

These examples of using SDEs for modelling come a variety of places
with this segment being mainly inspired by {cite}`harte1988consider`, which
might sound a bit silly as a title, but it is a landmark work in
modelling and problem-solving in Environmental Science.

::::{tab-set}

:::{tab-item} Example 1: Poisson (point) process

:::

:::{tab-item} Example 2

:::

::::



## Solving DEs with Python

## Application to Simulation

DEs can be used to approximate behaviors for different outcomes

## DE-based Simulation and Modelling Exercises with Solutions

::::{tab-set}

:::{tab-item} Exercise 1

:::

:::{tab-item} Exercise 2

:::

:::{tab-item} Exercise 3

:::

:::{tab-item} Solution 1

:::

:::{tab-item} Solution 2

:::

:::{tab-item} Solution 3

:::

::::

(prelab-9)=
# Pre-Lab 9: Becoming Proficient at Simulation Software (Do)

## Building Queues ###

## Constructing Queuing Systems ##

## Beyond Queuing

## Walk-Through ##

(prelab-10)=
# Pre-Lab 10: A Short Introduction to Agent-Based Modelling (Do)

## What is an Agent? ##

## Walk-Through ##


(prelab-11)=
# Pre-Lab 11: A Review of Optimization (Read)

## What does it mean to Optimize?

## 
