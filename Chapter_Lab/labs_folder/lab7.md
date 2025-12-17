:::{admonition} Lab 7
:class: attention dropdown
(lab-7)=
# Lab 7: Comparing Two Modelling Methodologies (Simple ABM vs MC): Simulating an Election

## Lab 7 Prerequisites

### Pre-labs

- {ref}`prelab-3`

### Chapters
- {ref}`sec:preface`
- Simulation and Modelling
- Buffon's Needle

## Background Information

For many years, statisticians and engineers have used different modelling techniques
for predictions based on the Monte Carlo method, and some of the major subjects of
these modelling techniques are: elections, weather, and engineering systems. This
lab builds on three sources: {cite}`mann1960values`, {cite}`kononovicius2017empirical`,
and {cite}`pasek2015predicting`.

### Agent-Based Modelling (ABM)

As discussed in {ref}`sec:prelab-3`, Agent-Based Modelling is a modelling technique that focuses on how agents
interact with other agents in a system. For example, in a swarm of bees, a simulation based on ABM will represent
them as agents with a limited set of possible interactions with the environment and other agents
such as move, collide, and avoid. This approach allows for an agent to influence the environment around them.

### Monte Carlo (MC) Review

The reader is most likely familiar with Monte Carlo at this point in the book; however, here is a
review of what is Monte Carlo in this context. When using the Monte Carlo method for simulative prediction, the
Monte Carlo Method uses random variables to predict probabilistic events. Through aggregating these
experiments (elections), it becomes possible to determine based on a set of assumptions the likelihood
of an event occurring (a party or candidate winning an election).

## Tasks

### Implementing an Agent-Based Modelling Election Model

To implement a Agent-Based Modelling (ABM) model for elections, we first need to find appropriate data,
luckily enough, we have data that we can work with from {cite}`kononovicius2017empirical`. In this lab,
we will try to reproduce the 1992 election using an abridged and programmatic method from the paper. 

Then,
we have to consider the distribution that fits the behavior of the data. A reasonable hypothesis
using Phitter is the beta distribution, although other distributions match the data sufficiently well.

### Implementing an Monte Carlo-Based Simulation Model

In this lab, we will be using election and demographic data from the 2008 Bangladeshi Election[^1]
to do three things:

1) Construct the random variables defining the estimator (vote)
2) 

## Example of Output

### ABM 

### MC 



:::

[^1]: This was chosen to make sure that this lab is broadly applicable, as the parties and
government structure that surrounds it no longer exist, and there is reliable data for the
election and demographics in question.
