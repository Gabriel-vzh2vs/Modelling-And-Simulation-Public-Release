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
# Pre-Lab 2: Tutorial for XLRisk (Do)

## Functions

## Correlations

## 

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

## Kendall's Notation

How are queues represented? For example, what does $m/m/1$ mean?


## Exponential Distribution

In probability courses and textbooks you may have heard about the exponential
distribution, one of the most prototypical queuing systems (m/m/1) relies on the
exponential distribution for its service times and inter-arrival rates.

Now, what are the properties that make exponential distributions useful for

## Birth and Death Processes

(prelab-7)=
# Pre-Lab 7: Review of Distributions (Reading)

## When and How to Pick a Distribution

There are hundreds of methods for selecting a distribution with some being more
rigorous than others ranging from the most rigorous {cite}`Krzysztofowicz:25`
(parts of Krzysztofowicz's work is shown in {ref}`sec:distribution_modeling`
mixed with Maximum Likelihood Estimation, a subset of Maximum A Posteriori
for estimating parameters).

## On Automated Distribution Fitters (i.e: Phitter, Fitter)

Through simulation literature and real-world applications, it is relatively rare to see
methods as seen with {cite}`Krzysztofowicz:25` for one reason, the vast majority of the
literature is not building novel distributions or meta-Gaussians, but instead often use one of
the three tests to pick from an existing distributions

- The Chi-Square Goodness Of Fit Test (this test can be deceptive, read {ref}`sec:distribution_modeling`)
for more information about this.
- 
- 

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

Additionally, there are several types of DEs, some of which you are likely
familiar with 

## ODEs for Modelling

These examples of using ODEs for modelling come a variety of places
with this segment being mainly inspired by {cite}`harte1988consider`, which
might sound a bit silly as a title, but it is a landmark work in
modelling and problem-solving in Environmental Science.

Example 1:

Example 2:

Example 3:

Example 4:

## Solving DEs with Python

## Application to Simulation

DEs can be used to approximate behaviors for different outcomes

## Basic Simulation and Modelling Exercises with Solutions

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
