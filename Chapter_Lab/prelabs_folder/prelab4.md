(prelab-4)=
# Pre-Lab 4: Short Overview of Modelling (Do)
::::{tab-set}

This pre-lab focuses on exposing the reader to different modelling schemas
that will be explored later in future pre-labs, chapters, projects, and
labs once their prerequisites are met. Essentially, this is a transition
pre-lab away from Monte Carlo to help understand the foundations of modelling.

More detailed information can be found {ref}`sec:system_modeling`, but this pre-lab
gives a sampler of different modelling methodologies.

:::{tab-item} System Dynamics

## What is System Dynamics and Why?

System dynamics refers to a method of _continuous_ modelling of real-world or
hypothetical behavior ofl dynamical, nonlinear systems as a series of five components:

1. States, which is anything that acts within a system,
(e.g: a machine chopping wood which feeds into another machine for finishing)
2. Stocks, which represent objects that move throughout the from state to state
(e.g: water moving through a purification system);
3. Flows, that define the paths between one state to another and
often represent a task that transforms stocks from one state to another
(e.g: a conveyor belt moving products through a factory);
4. Feedback Loops, which represent an external flow influencing
the behavior of a state (e.g: a machine stops once it has reached
its processing limit for the day)
5. Time Delays, which represent how long it takes to complete
a task (represented as a flow).

Using these components, system dynamics allows for the modelling of human behavior
using mathematical models (such as ODEs), which makes it useful for simulating human or
natural behaviors in measurable, repeatable, and stochastic ways. Additionally, one
can also model a system that is reactive to changes to its outputs, allowing for the
simulation and modelling of control systems[^1] such as thermostats, reactors, voltage
controllers and more systems of that nature.

## Examples of System Dynamics

This section mostly discusses and links to three publicly-available high-quality examples
of System Dynamics that also show their modelling structure and functionality.

1. [COVID-19 Vaccinations Simulation by ISEE](https://exchange.iseesystems.com/public/isee/covid-19-vaccinations-in-the-usa/index.html#page1), a simple model showing a negative correlation between COVID-19 vaccinations and infections;
2. [A SIR Model](https://exchange.iseesystems.com/public/jondarkow/sir-covid-19-coronavirus-simulation/index.html#page1), a system dynamics form of a model that is commonly used to
predict the spread of disease;
3. [Transportation Model](https://exchange.iseesystems.com/models/player/mindsproject/public-transport-usage-in-bergen), a system dynamics model showing the effects of a policy-change (adding more lanes to cause induced demand) on the number of people taking public transit;

## Toy Model for System Dynamics

In this work, the first model described in {ref}`sec:system_modeling`
"Predator prey models - Ver. 1" is converted into a System Dynamics model.

```{figure} ../../Figs/Chapter_Lab/PredatorPray.png

This represents a visualization of the output of the Predator-Pray Model
from the Systems Modelling Chapter using the BPTK_Py package.
```

```{admonition} Code for the Graphic Above
:class: dropdown
```{code} python
import BPTK_Py
from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

# 1. Initialize BPTK
bptk = BPTK_Py.bptk()

# 2. Define the System Dynamics Model (stocks, flows)
model = Model(starttime=0.0, stoptime=100.0, dt=0.1, name='Lotka-Volterra Model')

prey = model.stock("Prey")
predators = model.stock("Predators")
prey_increase_rate = model.flow("Prey_Increase_Rate")
prey_decrease_rate = model.flow("Prey_Decrease_Rate")
predator_increase_rate = model.flow("Predator_Increase_Rate")
predator_decrease_rate = model.flow("Predator_Decrease_Rate")

# 5. Define the Auxiliary Variables and Constants
prey_fractional_growth_rate_alpha = model.constant("Prey_Fractional_Growth_Rate_alpha")
fractional_predation_rate = model.constant("Fractional_Predation_Rate")
predator_fractional_decrease_rate_gamma = model.constant("Predator_Fractional_Decrease_Rate_gamma")

# 6. Set the Equations for the Stocks and Flows
prey.equation = prey_increase_rate - prey_decrease_rate
predators.equation = predator_increase_rate - predator_decrease_rate

prey_increase_rate.equation = prey * prey_fractional_growth_rate_alpha
prey_decrease_rate.equation = prey * predators * fractional_predation_rate
predator_increase_rate.equation = predators * prey * fractional_predation_rate
predator_decrease_rate.equation = predators * predator_fractional_decrease_rate_gamma

# 7. Set the Initial Conditions for a specific instance to make it replicable
prey.initial_value = 40.0
predators.initial_value = 9.0
prey_fractional_growth_rate_alpha.equation = 0.4
fractional_predation_rate.equation = 0.04
predator_fractional_decrease_rate_gamma.equation = 0.9

bptk.register_model(model)
scenario_manager = {
    "lotka_volterra": {
        "model": model
    }
}
bptk.register_scenario_manager(scenario_manager)
bptk.register_scenarios(
    scenarios={
        "base": {}
    },
    scenario_manager="lotka_volterra"
)

bptk.plot_scenarios(
    scenario_managers=["lotka_volterra"],
    scenarios=["base"],
    equations=["Prey", "Predators"]
)
```
```
```

:::

:::{tab-item} Discrete Event Simulation

## Why Use Discrete Event Simulation?

Unlike the _continuous_ modelling method of System Dynamics, discrete event
simulation involves treating a system as a series of events dispersed across
time. And an event changes the system's state, and no part of the system can
change outside of an event by definition.

This mechanism has several advantages such as the ability to calculate
statistics based on replications, the existence of performance indicators,

all of which has led to Discrete-Event
Simulation being the dominant form of simulation in industry[^2],

Discrete Event Simulations are generally made up of several components:

- The Clock
- The System State
- Events List
- Terminating and Starting Conditions
- Random Number Generators
- Statistics

## Examples of DES

1. [link](),
2. [link](),
3. [link](),

## Toy Model for DES

:::

:::{tab-item} Agent-Based Modelling

## What is ABM?

Agent-Based Modelling is a modelling technique that focuses on how agents
interact with other agents in a system. For example, in a swarm of bees,
a simulation based on ABM

## Examples of ABM

1. [link](),
2. [link](),
3. [link](),

## Toy Model for ABM

:::

::::

[^1]: A control system is a system that controls other devices or systems via control loops.

[^2]: To the point where many industry tools only support Discrete Event Simulation such as
SimPy, Autodesk Factory Design, Ciw, Arena, Flexsim - however, others have it as the default
such as SIMIO and Simul8.
