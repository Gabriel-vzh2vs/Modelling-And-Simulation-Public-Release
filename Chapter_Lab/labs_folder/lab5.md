:::{admonition} Lab 5
:class: attention
(lab-5)=
# Lab 5: Advanced Modelling (Discrete Events + ODEs) with Python

## Lab 5 Prerequisites

### Mandatory Pre-labs

- {ref}`prelab-3`
- {ref}`prelab-5`

### Recommended Pre-Labs

- {ref}`prelab-8`

### Mandatory Chapters for Lab 5

- {ref}`sec:prob_stats`
- {ref}`sec:CrudeMC`
- {ref}`sec:random_number_generation`
- {ref}`sec:distribution_modeling`

```{raw} latex
\section*{Background: Modeling Hybrid Systems}

Real-world systems frequently exhibit hybrid behavior, characterized by the interaction between continuous dynamics and discrete events. While continuous systems are typically modeled using Ordinary Differential Equations (ODEs), hybrid systems require a simulation framework capable of handling both continuous state evolution and discrete state transitions.

A classic pedagogical example of a hybrid system is a thermostatically controlled environment. In this scenario, the simulation must account for:
\begin{itemize}
    \item \textbf{Continuous Dynamics:} The thermodynamic evolution of room temperature over time.
    \item \textbf{Discrete Events:} The state change of the actuator (heater) toggling between \textbf{On} and \textbf{Off}.
\end{itemize}

\subsection*{1. Governing Equations}
The thermal dynamics of the room are governed by the balance of heat loss to the environment and heat gain from the heating unit.

\paragraph{Heat Loss ($\dot{Q}_{\text{loss}}$):}
The room loses thermal energy to the environment at a rate proportional to the temperature gradient between the room ($T_r$) and the environment ($T_e$). This is modeled as:
\begin{equation}
    \dot{Q}_{\text{loss}} = \frac{(T_r - T_e)}{\eta R} \quad \left[\mathrm{\frac{J}{h}}\right]
\end{equation}

\paragraph{Heat Gain ($\dot{Q}_{\text{gain}}$):}
When the heater is active, the room gains thermal energy at a rate proportional to the gradient between the heating fluid ($T_h$) and the room ($T_r$):
\begin{equation}
    \dot{Q}_{\text{gain}} = \alpha (T_h - T_r) \quad \left[\mathrm{\frac{J}{h}}\right]
\end{equation}

\paragraph{Temperature Rate of Change ($\dot{T}_r$):}
The rate of change of the room's temperature depends on the system's current discrete state. $\beta$ represents the thermal mass proportionality factor.

\begin{itemize}
    \item \textbf{State 1: Heating (Active)}
    \begin{equation}
        \frac{dT_r}{dt} = \beta \left(\dot{Q}_{\text{gain}} - \dot{Q}_{\text{loss}}\right) \quad \left[\mathrm{\frac{K}{h}}\right]
    \end{equation}
    
    \item \textbf{State 2: Cooling (Passive)}
    \begin{equation}
        \frac{dT_r}{dt} = - \beta \left(\dot{Q}_{\text{loss}}\right) \quad \left[\mathrm{\frac{K}{h}}\right]
    \end{equation}
\end{itemize}

\subsection*{2. Simulation Parameters \& Boundary Conditions}
For the purpose of this simulation study, the system is parameterized using the constants and initial conditions defined in Table 1.

\begin{table}[h!]
    \centering
    \caption{System Constants and Variables}
    \vspace{0.2cm}
    \begin{tabular}{@{} l c l l @{}} 
        \toprule
        \textbf{Parameter} & \textbf{Symbol} & \textbf{Value / Unit} & \textbf{Description} \\
        \midrule
        Thermal Resistance & $R$ & $1 \times 10^{-6} \; \mathrm{[Kh/J]}$ & Resistance to heat flow. \\
        Heat Gain Factor & $\alpha$ & $2 \times 10^6 \; \mathrm{[J/Kh]}$ & Heat transfer coef. of heater. \\
        Thermal Mass Factor & $\beta$ & $3 \times 10^{-7} \; \mathrm{[K/J]}$ & Energy to temp proportionality. \\
        Insulation Efficiency & $\eta$ & $\ge 1.0$ & Factor for insulation loss. \\
        Heater Fluid Temp & $T_h$ & $40^\circ\mathrm{C}$ & Avg temp of heating element. \\
        \bottomrule
    \end{tabular}
\end{table}

\paragraph{Control Logic (Thermostat):}
The discrete state transitions are triggered by the following threshold logic:
\begin{itemize}
    \item \textbf{Switch ON:} If $T_r < 20^\circ\mathrm{C}$
    \item \textbf{Switch OFF:} If $T_r > 23^\circ\mathrm{C}$
\end{itemize}

\paragraph{Environmental Conditions ($T_e$):}
The environmental temperature $T_e$ is modeled as a stochastic process governed by a sinusoidal function ranging between $8^\circ\mathrm{C}$ and $20^\circ\mathrm{C}$.
\begin{itemize}
    \item $T_{e,\min}$ occurs at 04:00.
    \item $T_{e,\max}$ occurs at 16:00.
\end{itemize}

\paragraph{Initial Conditions ($t=0$):}
Room Temperature $T_{r,0} = 20^\circ\mathrm{C}$; Heater State is \textbf{Off}.
```

```{raw} latex
\section*{Lab Tasks: Simulation and Analysis}

\begin{enumerate}
    \item \textbf{Baseline Model Implementation} \\
    Construct a hybrid simulation model capturing the thermodynamics of the heating system and its interaction with the environment. 
    \begin{itemize}
        \item \textbf{Simulation Horizon:} The simulation must span a complete diurnal cycle of 24 hours, defined as $t \in [0, 24]$.
        \item \textbf{Requirements:} Implement the governing equations (1--4) and the control logic defined in the Background section.
        \item \textbf{Visualization:} Generate a time-series plot displaying the trajectory of the room temperature $T_r(t)$ superimposed against the environmental temperature $T_e(t)$. Clearly annotate the periods where the heating element is active either through a line at the bottom or another indicator.
    \end{itemize}
    
    \item \textbf{Discrete Events (Occupant Behavior)} \\
    For the second task, extend the baseline model to account for occupant behavior.
    \begin{itemize}
        \item \textbf{Scenario:} Introduce discrete events representing the opening of a door or window, which temporarily degrades the system's thermal isolation.
        \item \textbf{Parameterization:} During these events, modify the insulation efficiency factor such that $\eta > 1.0$.
        \item \textbf{Frequency:} Model these events occurring at 1 to 2 distinct instances within the simulation window.
        \item \textbf{Analysis:} Compare the temperature response $T_r(t)$ of this model against the baseline results from Task 1.
    \end{itemize}
\end{enumerate}
```

## Output Examples
```{figure} Lab5HouseHeating.png
:label: fig:Lab5HouseHeating

This graph shows an example of a fully developed model for Occupant Behavior
on top of the Baseline Model. This graphing style is based on Simulate.ji's
documentation.
```

:::
