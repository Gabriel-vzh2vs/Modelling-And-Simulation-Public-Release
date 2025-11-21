:::{admonition} Lab 5
:class: attention dropdown
(lab-5)=
# Lab 5: Foundations of Modelling (SIMIO, Anylogic, or Python): House Heating Example

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

## Background Information

It is often required in modelling to accommodate different modelling techniques,
a classic example of a hybrid system is dynamic house heating. This might seem
extremely simple at first, but it really requires the combination of events,
continuous sampling (represented as an ODE), and processes to correctly simulate
and model.

In this room heating, we have continuous processes (like Lab 4) and discrete events:

- Heating has two states: On or Off
- A room cools $\dot{Q_c} [\frac{J}{h}]$ at a certain rate proportional
to the difference between room temperature $T_{r}$ and environmental
temperature, $T_e[K]$.
- A room heats $\dot{Q_h} [\frac{J}{h}]$ at a rate proportional to the
temperature difference between the heating fluid $T_h [K]$ and the room
temperature, $T_r [K]$.
- The room temperature, $T_r$ changes proportional to the difference between
heating and cooling: $\dot{Q_c}$ and $\dot{Q_h}$ respectively.

This information can be represented as these series of continuous processes:

$$\dot{Q}_c = \frac{(T_r - T_e)}{\eta R} \quad \left[\frac{J}{h}\right], \text{ where R = thermal resistance } \left[\frac{Kh}{J}\right], \eta = \text{efficiency factor} \le 1.0 \\
\dot{Q}_h = \alpha (T_h - T_r) \quad \left[\frac{J}{h}\right], \text{ where } \alpha = \text{proportionality factor } \left[\frac{J}{Kh}\right] \\
\dot{T}_h = \beta \left(\dot{Q}_h - \dot{Q}_c\right) \quad \left[\frac{K}{h}\right], \text{ where } \beta = \text{proportionality factor } \left[\frac{K}{J}\right] \\
\dot{T}_c = - \beta \dot{Q}_c \quad \left[\frac{K}{h}\right], \text{ when heating is switched off.}$$

In this lab, we assume the following are true and help to parameterize the model:
- the thermostat is set to switch heating on if $T_r$ falls under 20 degrees C and to switch heating off if $T_r$ rises above 23 degrees C,
- time units are hours,
- the temperature $T_h$ of the heating fluid is 40 degrees C on average,
- the temperature $T_e$ of the environment follows a stochastic process based on a sine function between 8 and 20 degrees C with $T_e$, min at 4am and $T_{e,max}$ at 4pm,
- the constants have values R=1×10−6 [KhJ],α=2×106 [JKh],β=3×10−7[KJ],
people entering the room may reduce insulation efficiency by a factor $\eta \ge 1.0$ to R, the room temperature is initially $T_{r,0} = 20$ degrees C
- and the heater is initially off.

## Tasks

Construct the physical model that represents the heating system inside of the environment over a period
of 24 hours from midnight to midnight that updates the parameters and environment every virtual minute,
ensure that your model is only modelling the stochastic processes and responses.




:::