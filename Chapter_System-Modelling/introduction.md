(sec:system_modeling)=
#  Introduction to Modelling #

You have likely done some form of modeling. As we indicated in the
introduction under {ref}`sec:intro_sim`, models range in complexity
from basic to highly involved. The goal of this chapter is to
establish a basic foundation for mathematical modeling. Followup
literatre and more advanced references on this topic include
{cite}`abc` and {cite}`efg`.


## Model classes ##

At a high level, models are often classified as __continuous__ or
__discrete__. As we will see, things are usually more nuanced than
this. We will illustrate this and also include brief descriptions of
other model classes and paradigms, some of which have their own
chapters.


### Continuous versus discrete ###

Broadly speaking, continuous refers to the nature of the variables of
the model as well as how they may evolve. This is perhaps best
illustrated through examples.

````{prf:example} Predator prey models - Ver. 1
:label: ex:predator_prey

The [Lotka-Volterra
equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)
are a famous example of a set of __non-linear ordinary differential
equations__ (ODEs). They govern the time-evolution of a pair of
interacting species where one is the predator and one is the prey. The
ODEs ({ref}`more-on-odes-here`)are given by:

```{math}
:label: eq:lotka_volterra_ode
\begin{align*}
x'(t) = \frac{dx}{dt} &= \alpha x - \beta xy\\
y'(t) = \frac{dy}{dt} &= -\gamma y + \delta xy
\end{align*}
```

Here $t \in \mathbb{R}$ denotes time, and the real-valued variable (or
states) $x,y \ge 0$ capture the population densities of prey and
predators, respectively. In addition, we have positive parameters
$\alpha, \beta, \gamma, \delta \in \mathbb{R}$. The parameter $\beta$,
for example, governs the rate of decline of the prey-population
resulting from predators interacting (aka eating) with prey, the
latter captured through the cross-term $xy$. Similarly, $\delta$ is a
parameter that governs the rate at which the predator population grows
by interactig with prey, again represented by the cross-term $xy$. The
remaining parameters $\alpha$ and $\gamma$ govern how prey
(resp. predators) evolve on their own without interacting with the
other species. One may regard the Lotka-Volterra equations as the most
basic non-linear model capturing this kind of two-species dynamic.

Depending on your goal with this model, you may also need an __initial
condition__, that is, a starting point $(x(t=0), y(t=0))$.

The model given by {ref}`eq:lotka_volterra_ode` is an example of a
fully continuous model: all states and all parameters are
continuous. In addition, the time-evolution is continuous. It is also
a __deterministic__ model.

__Assumptions:__ Many assumptions were made to arrive at
{ref}`eq:lotka_volterra_ode`. Below are some examples.

- In the real system, the populations would be spread out spatially.

- The numbers of animals within both species have to be sufficiently
  large to warrant a model approximation using ODEs.

- The interaction is capture through terms like $\beta xy$ and $\delta
  xy$. In general, one would expect a more general form, perhaps
  captured by functions $f_{\text{prey}}(x,y)$ and
  $g_{\text{predator}}(x,y)$.

- In practice, there may be limited resources for the prey which would
  make the single term $\alpha x$ unrealistic. If there are no
  predators, this model would give exponential growth. A more
  realistic model would contain terms preventing unbound growth.

Can you give give additional examples of assumptions? Clearly one can
make other choices when modeling a predator-prey system.

````

````{prf:example} Predator prey models - Ver. 2
:label: ex:predator_prey_discrete


In
{cite}`Din:13` the __discrete Lotka-Volterra model__ is studied. It
takes the form

```{math}
:label: eq:lotka_volterra_discrete
\begin{align*}
x_{t+1} &= \frac{ \alpha x_t -  \beta x_t y_t}{1+\epsilon x_n}\\
y_{t+1} &= \frac{ \gamma y_t - \gamma x_t y_t}{1+\epsilon x_n}
\end{align*}
```

where $x_{t}, y_{t} \in \mathbb{R}$ are non-negative and $t \in
\mathbb{N}$, and $\alpha,\beta,\gamma,\delta,\epsilon \in \mathbb{R}$
are non-negative parameters. In contrast to
{ref}`eq:lotka_volterra_ode`, the time-evolution of
{ref}`eq:lotka_volterra_discrete` is discrete: the system (as captured
by the model) progresses in discrete steps, $t=0$, $t=1$, $t=2$, and
so on. We refer to {ref}`eq:lotka_volterra_discrete} as a system of
__difference equations__. As before, depending on your goals, you may
also need an __initial condition__, that is, a starting point $(x_0,
y_0)$.

Here you see that the states $x_t$ and $y_t$ are continuous but that
time $t$ is discrete. In classical dynamical system theory, a system
such as {ref}`eq:lotka_volterra_discrete` is called a discrete
dynamical system. In a broader modeling setting, a more appropriate
term might be a __hybrid model__.
````

````{prf:example} Predator prey models - Ver. 3
:label: ex:predator_prey_fully_discrete

{cite}`Rodrigues:12` gives yet another version of the predator prey
model. In this case, they represent two-dimentions space  using a
lattice where the cells of the lattice are indexed by pairs $(i,j)$ as shown
in {ref}`fig:lv_lattice`.

```{figure}
:label: fig:lv_lattice

(Figure to be included here)

An illustration of the lattice of {ref}`ex:predator_prey_fully_discrete`.
```

As in {ref}`ex:predator_prey_discrete` time is discrete
$t\in\mathbb{N}$.  To each cell $(i,j)$ of the lattice one associates
the two integer states $N_{i,j,t}$ and $P_{i,j,t}$ denoting the number of prey
and predators at cell $(i,j)$ at time $t$.

The dynamics that maps this system from time $t$ to $t+1$ is specified
by a 2-step process. The first step is referred to as dispersal and
captures how members of $N$ and $P$ population migrate between
cells. It is modeled as

```{math}
\begin{align*}
N'_{i,j,t}
    &=(1-\mu_N) N_{i,j,t} + \sum_{(i',j')\in V_{i,j}} \mu_N N_{i',j',t}/4\;, \\
P'_{i,j,t}
     &= (1-\mu_P) P_{i,j,t} + \sum_{(i',j')\in V_{i,j}} \mu_P P_{i', j',t}/4\;,
\end{align*}
```

where $V_{i,j} = {(i−1, j), (i+1, j), (i, j−1), (i, j+1)}$ denotes the
set of neighbor cells of cell $(i,j)$. The interaction between
predator and prey is then captured as follows by

```{math}
\begin{align*}
N_{i,j,t+1} &=f\bigl( N'_{i,j,t}, P'_{i,j,t}\bigr) \;,\\
P_{i,j,t+1} &=g\bigl( N'_{i,j,t}, P'_{i,j,t}\bigr)\;.
\end{align*}
```

In this example, both time and states are discrete.

````

__Summary:__

The three examples above illustrate aspects of what may be meant by
"discrete" and "continuous" models. As you can see, using these terms
in a "wholesale" manner is simplistic. We would rather say that
specific aspects of a model are discrete or continuous. A model
containing both types will be called a __hybrid model__.


### Stochastic versus deterministic models ###

The model we saw in the previous section are all deterministic. A
model that incorporates one or more random variables (see
{ref}`def:random_variable`) will be called __stochastic__. Stochastic
models are central to this book, and some of the theory needed to
analyze and simulate such models are provided in {ref}`here`.


### Network-based models ###

In practice, the structure of many systems will not lend themselves to
modeling using differential equations. One such class is networked
systems which consists of entities coupled by edges in graph. An
example of this is a supply chain network. The edges encode
dependencies among the vertices. This class of models can directly
encode complex, non-heterogenous dependencies among system
constitutent. Analyzing this class of systems requires its own set of
tools, something we address in {ref}`gds-page-comes-here`.


### Agent-based models (ABMs) ###

We have devoted a whole section to agent-based models, see
{ref}`sec:ABM`. Broadly speaking, such models have __agents__ that are
embedded in an __environment__ where agents can interact with the
environment and and possibly other agents via __actions__. Agents can
modulate their __behavior__ based on feedback from the environment
where the feedback is presented as __rewards__ based on the agent's
actions. (Reference BDI {cite}`bdi`) We note that an ABM may be
networked.  An agent-based model where all agents perform a fixed
action is called a __micro-simulation__.


### Finite state machines ###

A mini introduction


### Modeling and scale ###

No doubt, you have heard about terms such as __multi-scale__ models,
and models relying on __big data__.  After all, who wants
single-scale models fueled by moderately sized data? 🙃



## Techniques for analysing models ##

Models based on ordinary- and partial differential equations have a
long history dating back to Newton and Leibniz. They represent a
cornerstone in modeling of continuous systems and come with a rich
literature and set of techniques rooted in, e.g., topology, analysis,
operator theory, and differential geometry.

The structure of networked models and ABMs, on the other hand,
typically have many discrete elements. As such, classical dynamical
system theory does not readily apply and rely instead on, e.g., graph
theory, combinatorics, and algebra. Work on such models may be
regarded as more computational in nature than their "continuous
cousins", since they apparently rely more on simulation.

In practice, whether models are "continuous", "discrete", "networked"
or "agent-based", __the analysis of virtually any complex model will
be analyzed through computational experiments__. The gap from articles
and textbooks to the needs of actual systems is generally large.
Models rooted in ODEs or PDEs, for example, rely on a multitude of
techniques from numerical analysis, and are solved (numerically)
through computations (aka simulation). A stochastic queueing model,
which one would likely regard as a "discrete" model, would similarly
be analyzed computationally through approaches such as discrete event
simulation, see {ref}`sec:queueing_systems`.



## Modeling in the real world ##

Faced with a set of questions about a system $S$, what governs the
model selection process? Should the model be continuous or discrete?
Should it be multi-scale? Model selection should be guided by a range
of criteria, but first and foremost the questions about $S$ that one
is tasked to answer, including the __precision__, __accuracy__,
__resolution__ and __fidelity__ that is needed.  The characteristics
of $S$ will further dictate what one pulls out from the modeling
toolset.

While one may be drawn to the lure of closed-form solutions that
sometimes happen for ODEs under textbook conditions, such biases can
easily cause one to gravitate towards elegant solutions, albeit to
oversimplified or an altogether different system. (And if we had to be
blunt, we would argue that the classical training in mathematics and
physics is a root cause of this preference.)

Modeling for complex systems is an inherently, well ... complex,
undertaking. It requires a breadth of knowledge about modeling
paradigms, analysis techniques, model compatibility, and model
shortcomings. Earlier, we mentioned that a key aspect of modeling is
validation. As we saw in {ref}`sec:intro_validation`, this is about
ensuring that the model $M$ is sufficiently detailed and precise so
that we can adequately address the questions that we intend to answer
about the system $S$. Verification, on the other hand, seeks to ensure
that the model $M$ is accurately committed to code. One may regard
verification and validation as conceptually separate processes. This
point of view is perfectly fine for basic models. However, as one
seeks to analyze complex system, one will often find that the modeling
paradigms that one chooses to apply will have to be done with a keen
eye on what the simulation models will look like as well as the
hardware on which they will run.

## Summary ##

In this book we will only consider basic mathematical
modeling. Nonetheless, the perspective above is useful to keep in
mind.
