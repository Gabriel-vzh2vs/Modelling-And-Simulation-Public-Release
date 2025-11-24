:::{admonition} Lab 6
:class: warning
(lab-6)=
# Lab 6: Queuing and Output Analysis in Simulation: Goldratt's Dice Game

Note: This lab is a bit of an odd one, as it is based on a book called
"The Goal" from Mr. Goldratt which is about the Theory of Constraints,
which is a fancy way of saying Linear Programming, which the reader has
likely taken a course on before if they are Industrial or Systems Engineering.
However, we are going to simulate one of the processes from this book, specifically
from pg. 105 in the third edition.

## Lab 6 Prerequisites

### Mandatory Pre-labs

- {ref}`prelab-2`
- {ref}`prelab-3`
- {ref}`prelab-4`
- {ref}`prelab-6`

### Mandatory Chapters for Lab 6

- {ref}`sec:prob_stats`
- {ref}`sec:distribution_modeling`
- {ref}`sec:random_number_generation`

## Background Information

In Eliyahu Goldratt’s classic business novel The Goal, the protagonist, Alex Rogo, thinks
manufacturing while on a hiking trip with a troop of Boy Scouts. He organizes a game
to demonstrate how a production line works.

The setup is deceptively simple. You have a line of workers (the scouts). The product
must pass from one worker to the next. However, there is a catch,
the speed at which a worker can pass matches is determined by rolling a die.

This means that this system can be represented as a series of five workers in sequence
on an assembly line. Each worker takes a mean 3.5 time units for processing
defined through a uniform distribution because of the die. Additionally, these workers have
infinite capacity (storage) for the items. This is a "balanced plant" model according to
industrial designers.

## Tasks

### Model Construction

First, a worker is defined as a entry buffer (a queue), with a time delay (processing time),
a output buffer, and a blocker which prevents the entrance of new material into the system. Next,
the connections between workers are established through the construction of a queuing network.
Programmatically, this can be implemented in Python using yield and store.get(). Now,
once the model is built, you should generate a graph of the inventory.

However, the base model above has some problems: inaccurate modelling of process time and
excessive inventory. As the first problem can be seen by the use of a uniform distribution
in the base model, and the second problem is visible through the inventory graph.

For solving the first problem, replacing the uniform distribution with a gamma with a
mean of one is supportable based on distribution modelling based on natural boundaries.

For the second problem, a common solution for this comes from Six Sigma: Kanban.
In this case, Kanban means that we want to set a limit on how many inventory items are passing
through the system. This is set through a conditional: a worker cannot pass an item forward
if the next buffer has more than 5 items. This is the next modification that the model needs
for efficiency.

Once those tasks are done, the model should behave in a more efficient way, with a higher level
of throughput, document this number in some form. Along with having lower fluctuations (variance)
than the base model.

### Output Analysis: Experimental Design and Statistical Analysis

It is important to understand what factors in the system connect with
system performance metrics (i.e: throughput rate). In this system, we want to construct
an experimental design to inform our output analysis. More details about experimental
design are available in Prelab 9, but here is a short summary; experimental design refers
to explaining the variance of factors within a series of different conditions.

In this lab, a full factorial design (3,300 runs) with varying line length, buffer sizes,
processing variation, and worker variation is recommended, as it is not computationally
expensive to do so (that's where the other factorial designs come in). Hint: Using itertools.product
makes it easier to get an appropriate set of combinations.

Finally, statistical analysis using a GLM (Linear Regression) to show that buffer
size and processing variation
:::