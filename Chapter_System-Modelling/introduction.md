(sec:system_modeling)=
#  Introduction #

You have likely done some form of modeling. As we indicated in the
introduction under {ref}`sec:intro_sim`, models range in complexity
from basic to highly highly involved. While we do emphasize modeling
in this book, it is still beneficial to establish a basic foundation
and reference frame.


## Model classes ##

At a high level, models are often classified as __continuous__ or
__discrete__. Broadly speaking, continuous refers to the nature of the
variables of the model as well as how they may evolve. The
distinctions are perhaps best illustrated through examples.

````{prf:example} Predator prey models - Ver. 1
:label: ex:predator_prey

The [Lotka-Volterra
equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)
are a famous example of a set of __non-linear ordinary differential
equations__ (ODEs). They govern the time-evolution of a pair of
interacting species where one is the predator and one is the prey. The
ODEs are given by:

```{math}
:label: eq:lotka_volterra_ode
\begin{align*}
x'(t) = \frac{dx}{dt} &= \alpha x - \beta xy\\
y'(t) = \frac{dy}{dt} &= -\gamma y + \delta xy
\end{align*}
```

Here $t \in \mathbb{R}$ denotes time, and the real-valued variable (or
states) $x,y \ge 0$ capture the population densities of prey and
predator, respectively. In addition, we have positive parameters
$\alpha, \beta, \gamma, \delta \in \mathbb{R}$. The parameter $\beta$,
for example, governs the rate of decline of the prey-population
resulting from predators interacting (aka eating) prey which is
captured through the cross-term $xy$. Similarly, $\delta$ is a
parameter that governs the rate at which the predator population grows
by interactig with prey, again represented by the cross-term $xy$. The
remaining parameters $\alpha$ and $\gamma$ govern how prey
(resp. predator) evolve on their own without interacting with the
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

- In the real system, the populations would be spread out spatially

- The numbers of animals within both species have to be sufficiently
  large to warrant an ODE approximation

- The interaction is capture through terms like $\beta xy$ and $\delta
  xy$. One would expect a more general form, perhaps given by
  functions $f_{\text{prey}}(x,y)$ and  $g_{\text{predator}}(x,y)$.

- In practice, there may be limited resources for the prey which would
  make the single term $\alpha x$ unrealistic. It should possibly be
  changed to a limited growth model.

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

{cite}`Rodrigues:12` gives another version of the predator prey
model. In this case, the two-dimensional space is represented using a
lattice where the cells of the lattice are indexed as $(i,j)$ as shown
in {ref}`fig:lv_lattice`.

```{figure}
:label: fig:lv_lattice

(Figure to be included here)

An illustration of the lattice of {ref}`ex:predator_prey_fully_discrete`.
```

As in {ref}`ex:predator_prey_discrete` time is discrete
$t\in\mathbb{N}$.  To each cell $(i,j)$ of the lattice one associates
two integer states $N_{i,j,t}$ and $P_{i,j,t}$ denoting the number of prey
and predators at cell $(i,j)$ at time $t$.

The dynamics mapping this system from time $t$ to $t+1$ is specified
by a 2-step process. The first step is referred to as dispersal and
captures how members of $N$ and $P$ population migrate between cells
and is modeled as

```{math}
\begin{align*}
N'_{i,j,t}
    &=(1-\mu_N) N_{i,j,t} + \sum_{(i',j')\in V_{i,j}} \mu_N N_{i',j',t}/4\;, \\
P'_{i,j,t}
     &= (1-\mu_P) P_{i,j,t} + \sum_{(i',j')\in V_{i,j}} \mu_P P_{i', j',t}/4\;,
\end{align*}
```

where $V_{i,j} = {(i−1, j), (i+1, j), (i, j−1), (i, j+1)}$.

N_{x,y,t+1} =f\left(N_{x,y,t}^{^{\prime}},P_{x,y,t}^{^{\prime }}\right),

N_{x,y,t+1} =f\left(N_{x,y,t}^{^{\prime}},P_{x,y,t}^{^{\prime }}\right),

````





What governs the choice of model classes.

Let's be blunt:

Analysis techniques. Numerical analysis



Continuous

Discrete

Hybrid

Agent-based modeling

Finite state machines

Stochastic models


## Modeling and scale ##

Multi-scale and big-data. Nobody wants single-scaled models fueled by medium-sized data.


## Modeling in the real world ##

A key aspect of modeling is validation. As we saw in
{ref}`sec:intro_validation`, this is about ensuring that the model $M$
is sufficiently detailed and precise so that we can adequately address
the questions that we intend to answer about the system
$S$. Verification, on the other hand, seeks to ensure that the model
$M$ is accurately committed to code. One may regard verification and
validation as conceptually separate processes. This point of view is
perfectly fine for basic models. However, as one seeks to analyze
complex system, one will often find that the modeling paradigms that
one chooses to apply will be
