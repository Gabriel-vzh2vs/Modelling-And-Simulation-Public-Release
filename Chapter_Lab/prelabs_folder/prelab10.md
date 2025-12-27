(prelab-10)=
# Pre-Lab 10: A Review of Optimization (Read)

:::{note} Notice of this being an Outlne
I am slowly working on this prelab, but because
the course material isn't done yet, this will
be on the back burner.
:::

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

Optimization is the mathematical process of finding the
optimal solution from a set of feasible alternatives.
In a deterministic context, this often involves maximizing
or minimizing an objective function $f(x)$ subject to
constraints $g(x) \le 0$ and $h(x)=0$.

However, in the context of simulation, the objective function is usually
not a closed-form algebraic equation. Instead, it is the output of a
stochastic model, meaning the value of f(x) is only an estimate
$f^*(x)$ with associated variance. Therefore, simulation optimization
seeks to solve:

$x \in \theta \text{ min }(​E[L(x,\eta)])$

Where:

- x represents the decision variables (inputs).
- $\theta$ is the feasible region defined by constraints.
- $\eta$ represents the random elements in the system.
- L is the loss function of the model.

### How can you Optimize a Simulation?

Key approaches include:

- Gradient-Based Methods (with Estimation): Attempting to estimate the gradient $\triangledown f(x)$ using
finite differences, though this is computationally expensive and sensitive to noise.
- Direct Search Methods: Techniques like Pattern Search or Nelder-Mead that do not
require derivatives, instead stepping through the search space based on function
evaluations.
- Metaheuristics: Algorithms such as Genetic Algorithms (GA), Simulated Annealing, or
Tabu Search, which are robust against local optima and noisy data.

A method for making a model easier to optimize is to use a
metamodel/surrogate model (discussed further in {ref}sec:surrogate_modeling),
as it simplifies a model into a regression problem instead of a series of inputs and outputs.
By fitting a smooth curve (like a polynomial or Kriging model) to the noisy simulation data,
we can apply standard deterministic optimization techniques to the surrogate.

### Multi-objective Optimization

### Meta-Heuristics

## Common Software for Simulation Optimization

### ParMOO

ParMOO (Python library for parallel multiobjective simulation optimization) is an open-source framework designed to exploit high-performance computing. It focuses on:

- Multiobjective Optimization: Solving problems with conflicting goals (e.g., minimizing cost while maximizing throughput) to find a set of Pareto optimal solutions.
- Surrogate Modeling: It heavily utilizes response surface methodology to minimize the number of expensive simulation runs required.

#### Example of its use

### Optquest

OptQuest is a proprietary optimization engine widely integrated into commercial simulation packages (such as Arena, Simio, and AnyLogic). It is known for:

- Black-Box Optimization: It requires no knowledge of the internal model structure.
- Scatter Search: It primarily uses a metaheuristic known as Scatter Search, combined with Tabu Search
and Neural Networks, to intelligently explore the solution space and escape local optima.

[^1]: If the reader wants to know more about how constraints work in
non-linear optimization (common in simulations), they should look into
the Karush-Kuhn-Tucker (KKT) Conditions. And for linear optimization, they should
look into the duality and slackness conditions. These are common conditions
for optimality.
