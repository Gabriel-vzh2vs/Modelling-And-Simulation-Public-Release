(lab-8)=
# Lab 8: Comparing Two Modelling Methodologies (ABM vs MC): Simulating an Election

:::{admonition} Lab 8
:class: attention

## Lab 8 Prerequisites

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

As discussed in {ref}`prelab-3`, Agent-Based Modelling is a modelling technique that focuses on how agents
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

To implement an Agent-Based Modelling (ABM) model for elections, we first need to find appropriate data,
luckily enough, we have data that we can work with from {cite}`kononovicius2017empirical`. In this lab,
we will try to reproduce the 2012 election using an abridged and programmatic method based on the paper.
This section is basically a walk-through of how to roughly do this for the 1992 election, but it should
be a relatively simple swap.

Then, we have to consider the distribution that fits the behavior of the data. A reasonable hypothesis
using Phitter is the beta distribution, although other distributions match the data sufficiently well.

For example, if we fit the data for the 1992 elections for the top five parties using phitter,
we get a set of parameters pretty similar to the original paper.

```{raw} latex
\begin{tabular}{rrlllrl}
\toprule
year & org\_id & party & alpha & beta & n & mean\_share \\
\midrule
1992 & 15 & LDDP & 5.035 & 5.508 & 2060 & 0.4793 \\
1992 & 1 & Reform Movement (Sąjūdis) & 3.117 & 13.36 & 2056 & 0.1901 \\
1992 & 14 & LKDP & 2.255 & 15.47 & 2042 & 0.1273 \\
1992 & 7 & LLRA-KSS (EAPL-CFA) & 0.2647 & 2.481 & 809 & 0.07854 \\
1992 & 4 & LSDP & 2.55 & 46.94 & 2020 & 0.05156 \\
\bottomrule
\end{tabular}
```

Now, a common ABM model for the beta distribution is the 
Kirman Two State Model, which is expressed as a Markov
Chain with specific state transitions probabilities:

```{raw} latex
Let $X$ be the number of agents in State 1. The transition probabilities in time step $\Delta t$ are:
\begin{align*}
    P(X \to X+1) &= (N-X)(\sigma_1 + hX)\Delta t \quad \\
    P(X \to X-1) &= X[\sigma_2 + h(N-X)]\Delta t \quad 
\end{align*}


\begin{itemize}
    \item $\sigma_1, \sigma_2$: Idiosyncratic attractiveness of the states.
    \item $h$: Recruitment efficiency parameter.
\end{itemize}
```

And if the system is at an infinite number of agents, the
entire system can be expressed using the Fokker-Planck Equation (FP).
Moreover, if the FP equation has the following form with
drift $A(x)$ and diffusion $B(x)$, then when it has a sufficiently
large number of samples converges into the Beta Distribution as
shown below.

```{raw} latex
For large $N$, the fraction $x = X/N$ is described by a Fokker-Planck equation 
\begin{align*}
    A(x) &= \epsilon_1(1-x) - \epsilon_2 x \quad \text{where } \epsilon_i = \sigma_i/h \\
    B(x) &= 2x(1-x) 
\end{align*}

The long-term behavior follows a Beta distribution, $Be(\epsilon_1, \epsilon_2)$:
\begin{equation*}
    \omega_{st}(x) = \frac{1}{B(\epsilon_1, \epsilon_2)} x^{\epsilon_1-1}(1-x)^{\epsilon_2-1}
\end{equation*}
```

Doing this programmatically is easier than what the notation indicates!

```{admonition} Code for the Kirman Two State Model
:class: dropdown tip

```{code} python
class KirmanTwoStateModel:
    def __init__(self, n_agents, epsilon_1, epsilon_2, h):
        self.N = n_agents
        self.state = np.random.randint(0, self.N) 
        self.e1 = epsilon_1
        self.e2 = epsilon_2
        self.h = h

    def step(self):
        n1 = self.state
        n2 = self.N - n1

        # The Transition Probabilities 
        p_1_to_2 = (n1 / self.N) * (self.e2 + self.h * n2) / (self.e1 + self.e2 + self.h * self.N)
        p_2_to_1 = (n2 / self.N) * (self.e1 + self.h * n1) / (self.e1 + self.e2 + self.h * self.N)

        r = np.random.rand()
        if r < p_1_to_2: self.state -= 1
        elif r < p_1_to_2 + p_2_to_1: self.state += 1

    def run(self, steps, record_every=100):
        history = np.zeros(steps // record_every)
        for i in range(len(history)):
            for _ in range(record_every):
                self.step()
            history[i] = self.state / self.N
        return history
```
```
```

Which might seem complex, but we can break it down a bit more.

1. The Setup: `__init__`

- self.N (Population): The total number of agents (e.g., traders, ants).
- self.state (Current Situation): Instead of tracking every single agent individually (which is slow),
we only need to track how many agents are in State 1.

The Parameters (ϵ and h):

- ϵ (Noise/Idiosyncratic): The tendency to switch states randomly/independently (e.g., "I just felt like changing my mind").
- h (Herding): The tendency to copy others (e.g., "Everyone else is voting this way, so I will too").

2. The Mechanics: `step`

With every tick of the clock, we need to count the number of people who are in the first group (stay)
and the second group (switch), which are what `n1` and `n2` represent.

Then we need to define the Markov Transitions in our code based on opportunity and pressure:

- Opportunity: (`n1 / self.N`) is the chance of randomly picking an agent who is currently in State 1.
- Pressure: (`self.e2 + self.h * n2`) is the pressure to move to State 2 that represents agent preference and
peer pressure.

And these factors allow for us to create an approximation of the Markovian Transition Rates.

After implementing this, we can now visualize our results for each party, in this example,
we used the Reform party and compare it against the beta distribution fit.

### Example of ABM-Model Output

![](figs/ReformPartyLit.png)
This model had the following parameters: 2,000,000 steps, h = 1, agents = 500.

### Implementing an Monte Carlo-Based Simulation Model

In this lab, we will be using election and demographic data from the 2008 Bangladeshi Election[^1]
to do three things:

1) Construct the random variables defining the estimator (vote)
2) 


:::

[^1]: This was chosen to make sure that this lab is broadly applicable, as the parties and
government structure that surrounds it no longer exist, and there is reliable data for the
election and demographics in question.
