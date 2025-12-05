(prelab-10)=
# Pre-Lab 10: A Review of Optimization (Read)

The main purpose of simulation optimization is the
idea that there is an "ideal" state for the system
to reach, meaning that the outputs are maximized,
minimized, or at a target value based on a set of
factors. These factors are often discovered
through sensitivity analysis as discussed in
{ref}`prelab-9`.This works because Sensitivity
analysis creates a response surface that is then
constrained based on assumptions and limits so
that optimal configurations become feasible[^1].

## What does it mean to Optimize?

### How can you Optimize a Simulation?

A method for making a model easier to optimize is to
use a metamodel/surrogate model (discussed further in
{ref}`sec:surrogate_modeling`), as it simplifies
a model into a regression problem instead of a
series of inputs and outputs.

## Common Software for Simulation Optimization

### OpenModelica

### Optquest

[^1]: If the reader wants to know more about how constraints work in
non-linear optimization (common in simulations), they should look into
the Karush-Kuhn-Tucker (KKT) Conditions. And for linear optimization, they should
look into the duality and slackness conditions. These are common conditions
for optimality.
