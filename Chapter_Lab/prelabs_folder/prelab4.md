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

This represents a visualization of the output of the Predator-Prey Model
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

- The Clock which defines the timing of events;
- The System State which changes per event an example of this would be a
queuing system going from 5 people in queue to 4 people with a departure;
- Events List which defines what events can occur within the simulation;
- Terminating and Starting Conditions which are self-explaining;
- Random Number Generators which inform either the intensity of an event or
how often does an event occur in the context of a set distribution;
- Statistics such as confidence intervals for performance metrics.

## Examples of DES

1. [Queuing Model Example](https://stackblitz.com/edit/typescript-efht9t?file=index.ts), this model is written in Javascript,
but it is a simple M/M/1 queuing model similar to what the reader could find in SimPy or Salabim;
2. [Lemonade Stand](https://sim4edu.com/sims/17/Lemonade-Stand-1), this form of the model is very transparent about the events
occurring, and it describes the operation of a lemonade stand as a series of events while following the Processing Network model[^3] that
software like SIMIO, Anylogic, and Flexsim use but tend to hide from the user;
3. [SIR](https://sim4edu.com/sims/25/SIR-Contagious-Disease-Model-1), this is a SIR model that uses DES to model its behaviors using an event to change the state of the system to match the ordinary differential equations that generally mediate a SIR model.

## Toy Model for DES

```{figure} ../../Figs/Chapter_Lab/SIR_SimPy.png

This represents the output from the DES simulation that is made to simulate
a SIR model using a DES framework - with each event being a recovery or infection.
```


```{admonition} Code for the Graphic Above
:class: dropdown
```{code} python
import simpy
import random
import matplotlib.pyplot as plt

# --- Simulation Parameters ---
# These parameters can be adjusted to see how they affect the simulation outcome.

TOTAL_POPULATION = 1000   # Total number of individuals in the population
INITIAL_INFECTED = 5       # Number of individuals who are initially infected
SIMULATION_DAYS = 150      # How many days the simulation should run

# Disease Parameters
INFECTION_RATE = 0.2       # Probability of transmission upon contact with an infected person
CONTACTS_PER_DAY = 8       # Average number of people an individual comes into contact with per day
RECOVERY_TIME = 14.0       # Average time in days it takes to recover from the infection

# --- Data Collection ---
# Lists to store the count of individuals in each state for each day of the simulation.
susceptible_history = []
infected_history = []
recovered_history = []
timestamps = []

class Person:
    """
    Represents an individual in the population. Each person is a SimPy process.
    """
    def __init__(self, env, name, population):
        self.env = env
        self.name = name
        self.population = population
        self.state = 'S'  # Initial state is Susceptible
        self.action = env.process(self.run())

    def run(self):
        """
        The main process for a person, defining their behavior based on their state.
        """
        # The person remains susceptible until they are infected.
        # We wait for an external 'infect' event to be triggered.
        try:
            yield self.env.timeout(SIMULATION_DAYS + 1)
        except simpy.Interrupt:
            # The interrupt signifies that this person has been infected.
            self.state = 'I'
            
            # Now, the person is infected. We wait for the recovery period to pass.
            recovery_duration = random.expovariate(1.0 / RECOVERY_TIME)
            yield self.env.timeout(recovery_duration)
            self.state = 'R'

def infection_spreader(env, population):
    """
    A process that models the spread of the infection through the population
    at discrete daily intervals. 
    """
    while True:
        # At the start of each day, identify who is susceptible and who is infected.
        susceptible_people = [p for p in population if p.state == 'S']
        infected_count = sum(1 for p in population if p.state == 'I')

        # If there's no one to infect or no one to spread the disease, we can skip.
        if not susceptible_people or infected_count == 0:
            yield env.timeout(1)
            continue

        # Each infected person makes a number of contacts.
        # We model this as a pool of total daily contacts.
        for _ in range(infected_count * CONTACTS_PER_DAY):
            if not susceptible_people:
                break
            target = random.choice(susceptible_people)
            # Check if transmission occurs based on the infection rate.
            if random.random() < INFECTION_RATE:
                # If transmission occurs, interrupt the target to infect them.
                target.action.interrupt()
                # IMPORTANT: Remove the person from the list of susceptible people for the
                # remainder of this time step to prevent another infection attempt.
                susceptible_people.remove(target)
        # Wait for the next day to spread infections again.
        yield env.timeout(1)

def monitor(env, population):
    """
    A process that periodically records the number of people in each state (S, I, R).
    """
    while True:
        # Count the current number of people in each state
        s_count = sum(1 for p in population if p.state == 'S')
        i_count = sum(1 for p in population if p.state == 'I')
        r_count = sum(1 for p in population if p.state == 'R')

        # Store the counts and the current simulation time
        susceptible_history.append(s_count)
        infected_history.append(i_count)
        recovered_history.append(r_count)
        timestamps.append(env.now)
        if i_count == 0 and env.now > 1:
            print(f"\nEpidemic ended at day {int(env.now)}.")
            return
        # Record data once per day 
        yield env.timeout(1)

def plot_results():
    """
    Uses Matplotlib to create a plot of the SIR data over time.
    """
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.plot(timestamps, susceptible_history, label='Susceptible', color='blue', linewidth=2)
    ax.plot(timestamps, infected_history, label='Infected', color='red', linewidth=2)
    ax.plot(timestamps, recovered_history, label='Recovered', color='green', linewidth=2)
    
    ax.set_title('SIR Model', fontsize=18)
    ax.set_xlabel('Time (Days)', fontsize=14)
    ax.set_ylabel('Number of People', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Set limits for the axes
    ax.set_xlim(0, SIMULATION_DAYS)
    ax.set_ylim(0, TOTAL_POPULATION * 1.05)
    
    plt.tight_layout()
    plt.show()

# --- Main Simulation Setup ---
if __name__ == '__main__':
    print("Starting simulation...") # this is just for the user to not be confused.

    # Create a SimPy environment
    env = simpy.Environment()

    # Create the population of individuals
    population = [Person(env, i, None) for i in range(TOTAL_POPULATION)]
    for person in population:
        person.population = population
        
    # Infect the initial set of individuals
    initial_infected_people = random.sample(population, INITIAL_INFECTED)
    for person in initial_infected_people:
        person.action.interrupt()

    # Start the simulation processes
    env.process(infection_spreader(env, population))
    env.process(monitor(env, population))
    env.run(until=SIMULATION_DAYS)
    plot_results()
```
```
```

:::

:::{tab-item} Agent-Based Modelling

## What is ABM?

Agent-Based Modelling is a modelling technique that focuses on how agents
interact with other agents in a system. For example, in a swarm of bees,
a simulation based on ABM will represent them as agents with a limited
set of possible interactions with the environment and other agents
such as move, collide, and avoid. This approach allows for an agent
to influence the environment around them and allows for the modelling of
individual decisions. Moreover, the advantages that this modelling
approach brings has made it one of the most popular frameworks in medicine
and biocomplexity for modelling.

## Examples of ABM

These examples below are from an application called "Netlogo" which is the
traditional choice for ABM simulation in academia. And these simulations
represent some common uses of ABM along with the code associated with them.

1. [Bugs](https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Curricular%20Models/ModelSim/Population%20Biology/Bug%20Hunt%20Disruptions.nlogo),
a model about a form of predator-pray model based on the Lotka-Volterra equations.
2. [Virus](https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Sample%20Models/Biology/Virus.nlogo), this is a model about
how viruses spread from person to person in a SIR model;
3. [Virus on a Network](https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Sample%20Models/Networks/Virus%20on%20a%20Network.nlogo)
this is a model about the spread of a virus from entity to entity, which could be used to simulate the spread of information or of a real virus in a community,
also a SIR model, but in this case it is spatially-aware;

## Toy Model for ABM

This toy model is based on {cite}`drossel1992self` which describes the spread of
fire throughout a forest using cellular automatons, and this work will approximate
using Mesa's agent-based simulation functionality. To enable this task, this work uses
the same rules that Drossel did in 1992 which consists of the following rules:

1. A burning cell turns into an burnt cell (burning to ashes)
2. A tree will burn if at least one neighbor is burning (fire spread)
3. A tree ignites with probability f even if no neighbor is burning (fire starting via lighting)
4. An burnt cell fills with a tree with probability p (regrowth).

```{figure} ../../Figs/Chapter_Lab/fire_abm.mp4

Additional context: 
This represents the forest fire Agent-Based Model, and there
are two interactions that a fire tile can do, one is that can
spread if there is a non-burnt tile next to it, and two it can
burn out and transform into a burnt tile. 
```

```{admonition} Code for the Graphic Above
:class: dropdown
```{code} python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Mesa 3.0+ imports
from mesa import Agent, Model
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

class Tree(Agent):
    """
    A tree agent for the forest fire model.
    """
    def __init__(self, pos, model):
        super().__init__(model)
        self.pos = pos
        self.state = 0  # Default state is Empty

    def step(self):
        """
        If a tree is burning, it spreads the fire to its neighbors.
        After spreading, the tree becomes burnt out.
        """
        if self.state == 2:  # If the tree is Burning
            for neighbor in self.model.grid.iter_neighbors(self.pos, moore=True):
                if neighbor.state == 1:  # If neighbor is Green
                    neighbor.state = 2   # It catches fire
            self.state = 3  # The original tree is now Burnt


class ForestFire(Model):
    """
    A forest fire model using the Mesa 3.0+ AgentSet API.
    """
    def __init__(self, width=100, height=100, density=0.7):
        super().__init__()
        self.width = width
        self.height = height
        self.density = density

        self.grid = SingleGrid(width, height, torus=False)

        # Place agents
        for _, pos in self.grid.coord_iter():
            tree = Tree(pos, self)
            if self.random.random() < self.density:
                if pos[0] == 0:
                    tree.state = 2
                else:
                    tree.state = 1
            self.grid.place_agent(tree, pos)
            # The agent is automatically added to the model's AgentSet when created

        self.datacollector = DataCollector(
            model_reporters={"Grid": get_grid}
        )
        self.datacollector.collect(self)

    def step(self):
        """
        Advance the model by one step using the AgentSet API.
        """
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)


def get_grid(model):
    """
    Helper function to get the grid state for visualization.
    """
    grid = np.zeros((model.grid.width, model.grid.height))
    for agent in model.agents:
        if agent.state > 0:
             grid[agent.pos[0]][agent.pos[1]] = agent.state
    return grid


if __name__ == '__main__':
    # --- Model Execution ---
    model = ForestFire(100, 100, density=0.7)
    for i in range(30):
        model.step()

    # --- Data Collection --- #
    all_grids = model.datacollector.get_model_vars_dataframe()

    # --- Animation Setup --- #
    fig, ax = plt.subplots(figsize=(7, 7))
    cmap = plt.matplotlib.colors.ListedColormap(['#FFFFFF', '#009900', '#FF4500', '#222222'])
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    norm = plt.matplotlib.colors.BoundaryNorm(bounds, cmap.N)

    def update(frame):
        ax.clear()
        grid_data = all_grids["Grid"][frame]
        ax.imshow(grid_data.T, cmap=cmap, norm=norm)
        ax.set_title(f"Forest Fire (Mesa 3.0+) - Step {frame}")
        ax.set_xticks([])
        ax.set_yticks([])

    # --- Create and Save Animation --- #
    ani = animation.FuncAnimation(fig, update, frames=len(all_grids), repeat=False)

    ani.save("forest_fire_mesa.mp4", writer="ffmpeg", fps=5, dpi=150)
    print("\nAnimation successfully saved to forest_fire_mesa.mp4")

    plt.show()
```
```
```
:::

::::

[^1]: A control system is a system that controls other devices or systems via control loops.

[^2]: To the point where many industry tools only support Discrete Event Simulation such as
SimPy, Autodesk Factory Design, Ciw, Arena, Flexsim - however, others have it as the default
such as SIMIO and Simul8.

[^3]: Specifically, a Processing Network (PN) model refers a model that uses the concept of
processing objects that enter a system through a source, and go through a series of processing
activities performed at corresponding nodes using resources, and then they finally exit the system
through a sink. This description was based on {cite}`wagner2022object`.
