:::{admonition} Lab 7
:class: attention
(lab-7)=
# Lab 7: Expanding Modelling Methods: Compartmental Models Lab

## Lab 7 Prerequisites

### Required Pre-labs

- {ref}`prelab-8`
- {ref}`prelab-3`

### Required Chapters

- {ref}`sec:differential_equations`
- {ref}`sec:system_modeling`

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
    \item $\beta$: The \textbf{transmission rate}, representing the probability of 
    transmitting the disease between a susceptible and an infectious individual.
    \item $\gamma$: The \textbf{recovery rate}, which is the inverse of the average 
    duration of infection ($1/\gamma$).
\end{itemize}
```

This modelling technique is often used to model extremely infectious diseases without
the chance of reinfection such as mumps, a specific strain of flu, and tuberculosis (when
curable).

Many models expand upon the SIR model either through adding additional states (as seen in
some of the models here), adding Bayesian details (like in {ref}`prelab-8`), or abstracted
into a Multi-Compartmental Model (system dynamics as seen in {ref}`prelab-3`).

## Tasks

In the context of simulation, Pharmacokinetics (PK)
provides a deterministic framework for modeling the time-course of drug absorption,
distribution, metabolism, and excretion (ADME). Unlike the stochastic nature
often found in epidemic models (like discrete SIR simulations), PK models are typically
continuous system dynamics models defined by coupled Ordinary Differential Equations (ODEs).

In this lab, you will model the body as a system of kinetically
homogeneous compartments or volumes. This lab is based on {cite}`mould2013basic` and
{cite}`levy1969multicompartment`.

### Task 1: The One-Compartment Model (IV Bolus)

The simplest PK model is the One-Compartment Model.
This model assumes the body acts as a single, kinetically homogeneous unit
where the drug mixes instantaneously upon administration (IV Bolus). This model is often sufficient
for highly hydrophilic drugs (e.g., aminoglycosides) that are confined to
body water and do not distribute extensively into tissues.

In this model, when a drug is administered via Intravenous (IV) Bolus, the input
is modeled as an instantaneous impulse at $t=0$, establishing an
initial condition $C_0$ (initial concentration). The rate of change is driven solely by elimination.

The differential equation governing the amount of drug in the body ($X$) is:
\begin{equation}
    \frac{dX}{dt} = - k_{el} X
\end{equation}
where $k_{el}$ is the first-order elimination rate constant ($time^{-1}$).

For simulation purposes, we often track Concentration ($C_p$) rather than mass, related by the Apparent Volume of Distribution ($V_d$):
\begin{equation}
    X = V_d C_p \implies \frac{dC_p}{dt} = -k_{el} C_p
\end{equation}

The analytical solution to this ODE is a mono-exponential decay function:
\begin{equation}
    C_p(t) = C_0 e^{-k_{el} t}
\end{equation}

Or in logarithmic form (linearized):
\begin{equation}
    \ln C_p = \ln C_0 - k_{el} t
\end{equation}

#### Simulation Requirements

1. Develop the Model: Implement the differential equation $\frac{dC}{dt} = -k_{el}C$ in your simulation environment (e.g., Python/SimPy).
2. Run the Simulation: Simulate the concentration profile over 10 hours using the following parameters from the literature:

```{raw} latex
    \begin{itemize}
        \item Initial Concentration ($C_0$): $100 \mu g/ml$
        \item Elimination Rate ($k_{el}$): $0.347 hr^{-1}$
    \end{itemize}
```

3. Verification: Plot your numerical simulation results against the analytical solution ($C_p(t) = 100 e^{-0.347 t}$) to verify your integrator's accuracy.
4. Parameter Extraction: From your simulated data, plot $\ln(C_p)$ vs. time. ]Verify that the slope of this line corresponds to $-k_{el}$.

### Task 2: Two-Compartment Model (Bi-Exponential Decay)

High-fidelity modeling often requires acknowledging that the body is heterogeneous. The \textbf{Two-Compartment Model} separates the system into:

```{raw} latex
\begin{itemize}
    \item \textbf{Central Compartment (1):} Blood and highly perfused organs (liver, kidneys) where elimination occurs.
    \item \textbf{Peripheral Compartment (2):} Poorly perfused tissues (muscle, fat) that equilibrate slowly.
\end{itemize}
```

This system represents a delayed distribution model.
The dynamics are defined by the reversible transfer rates between compartments ($k_{12}, k_{21}$)
and the elimination rate ($k_{el}$ or $k_{10}$).

The system of coupled ODEs is:
\begin{align}
    \frac{dC_1}{dt} &= k_{21}C_2 - k_{12}C_1 - k_{el}C_1 \\
    \frac{dC_2}{dt} &= k_{12}C_1 - k_{21}C_2
\end{align}
Note: $C_1$ represents the central compartment concentration and $C_2$ the peripheral.

The analytical solution for the central compartment is the sum of two exponential terms,
representing the distinct Distribution Phase ($\alpha$) and Elimination Phase ($\beta$):

\begin{equation}
    C_1(t) = A e^{-\alpha t} + B e^{-\beta t}
\end{equation}

where $\alpha$ and $\beta$ are hybrid rate constants derived from the micro-constants ($k_{12}, k_{21}, k_{el}$)

#### Simulation Requirements

```{raw} latex
1.  Implementation: Define the system of coupled ODEs in Python.

2.  Phase Analysis: Simulate the system and generate a semi-log plot ($\log C$ vs $t$).

3.  Comparison: Unlike the linear semi-log plot of the One-Compartment model, you should observe a \textbf{bi-phasic} curve:
    \begin{itemize}
        \item An initial rapid decline (Distribution Phase/$\alpha$-phase) where drug moves from Central $\to$ Peripheral
        \item A terminal slower decline (Elimination Phase/$\beta$-phase) where equilibrium is reached and elimination dominates
    \end{itemize}
4.  Method of Residuals: Attempt to decompose your simulated curve into the two linear 
components ($A e^{-\alpha t}$ and $B e^{-\beta t}$) to estimate the intercept constants $A$ and $B$.
```

:::
