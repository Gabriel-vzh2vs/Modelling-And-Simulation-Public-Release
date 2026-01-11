:::{admonition} Lab 7
:class: attention
(lab-7)=
# Lab 7: Expanding Modelling Methods: Compartmental Models Lab

## Lab 7 Prerequisites

### Required Pre-labs

- {ref}`prelab-8`
- {ref}`prelab-3`

### Required Chapters

- {ref}``
- {ref}``
- {ref}``
- {ref}``


## Background Information

This lab covers a topic of compartmental models, which is a modelling technique
that analyzes and recreates the movement of population through different states
which are often defined through ODEs with some being formulated on random variables.
Compartmental models are often used in pharmacokinetics, epidemiology, population
ecology, and operations research.

One of the these models is the SIR model, discovered by Kermack and McKendrick in 1927,
{cite}`SIR1927`, which separates its states into three different
"compartments":

- Susceptible (S)
- Infected (I)
- Recovered (R)

Which are represented by the following ODEs when using the traditional SIR model:

``` {raw} latex
\begin{aligned}
    \frac{dS}{dt} &= -\frac{\beta}{N}IS, \\
    \frac{dI}{dt} &= \frac{\beta}{N}IS - \gamma I, \\
    \frac{dR}{dt} &= \gamma I,
\end{aligned}

\noindent \textbf{Variables:}
\begin{itemize}
    \item $S(t)$: The number of \textbf{susceptible} individuals at time $t$.
    \item $I(t)$: The number of \textbf{infectious} individuals at time $t$.
    \item $R(t)$: The number of \textbf{recovered} (or removed) individuals at time $t$.
\end{itemize}

\noindent \textbf{Parameters:}
\begin{itemize}
    \item $N$: The total population size, where $N = S + I + R$.
    \item $\beta$: The \textbf{transmission rate}, representing the probability of transmitting the disease between a susceptible and an infectious individual.
    \item $\gamma$: The \textbf{recovery rate}, which is the inverse of the average duration of infection ($1/\gamma$).
\end{itemize}
```

This modelling technique is often used to model extremely infectious diseases without
the chance of reinfection such as mumps, a specific strain of flu, and tuberculosis (when
curable).

Many models expand upon the SIR model either through adding additional states (as seen in
some of the models here), adding bayesian details (like in {ref}`prelab-8`), or abstracted
into a Multi-Compartmental Model (system dynamics as seen in {ref}`prelab-3`).

## Tasks

### 

:::
