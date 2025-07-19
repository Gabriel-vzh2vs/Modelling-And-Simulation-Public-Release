(prelab-3)=
# Pre-Lab 3: Improving the Robustness of Simulation (Read)

Now that this text has covered a substantial amount of theory,
it is important for the reader to consider malignant patterns and robustness
in simulation, some of these malignant patterns can be discovered
and removed with the methods discussed in this section and by using the more technological-focused solutions in {ref}`prelab-5`.

This pre-lab builds on the knowledge and theory presented in these
two papers: {cite:p}`barth2012typical`
{cite:p}`christie2005error`.

## On Prediction of Complex Phenomena

A common historical discussion in simulation literature is
the question: "how should complex phenomena be presented and analyzed
in simulation?" One of the papers that attempted to build a consensus
around this topic is {cite:p}`christie2005error`. The following subsection
will discuss methods of making simulation more robust to errors in structure
through a variety of approaches that do not rely on software alone.

### Constraining the Model

A core element of modelling and simulation for complex systems with 'big data'
as discussed in {ref}`sec:preface` is having available data. Any simulation practitioner
should also know because of the inherent incompleteness of models, it is critical
to focus on the process and structure of the simulation in the context of the data to
ensure the model can be validated with real-world data. There are many methods for
doing this task, some of which are encapsulated in Christie and et al's "Decomposition of
Errors" three step process:

1. Compare Simulated and Experimental Results, meaning to verify that the
simulated system is operating correctly based on the available information about
the system and that the data from the real world system is valid.
2. Analyze the solution error, which generally means to use classical Bayesian
approaches or bootstrapping to define a confidence interval and determine if simulation experiments'
results are explainable by the aleatoric uncertainty expected from the observed system.
3. Determine the impact of errors on predictability, in this case the core point is to
determine the validity of a model through ensuring that it matches the available data,
if that is not accomplished with the simulated model, it means the errors are too great
for the simulation to be useful.

Note that none of these methods are meant to improve the accuracy (as that is limited
through modelling, data quality, and more concepts covered in {ref}`sec:output_analysis`)
of a model, but to make sure that the model is representative of the known data and its
expected system performance metrics from known parameter estimates.

### Statistical Inference and Prediction

Looking back on {ref}`prelab-2`, this work discussed a method for using for constructing
correlated variates (copula), and this is a common
method of improving statistical inferences and prediction using a Bayesian
approach as a method of improving observations through contextualization.
These methods are then combined with concepts from {ref}`sec:prob_stats` to
create predictions of system performance (outputs) from the model, which is
what Christie argues is the point of modelling and simulating complex (or not) phenomena.

In Christie and et al's, the following quote is important for understanding uncertainty:
"Numerical and observation errors are the leading terms in the determination of the Bayesian likelihood",
as uncertainty is a function of the variance of the observations in the vast majority of cases
using statistical inference. Moreover, there are a variety of methods both Bayesian and 
Non-Bayesian to inform and structure inferences and predictions of which only a limited set are seen throughout this work
(e.g: Monte Carlo, Confidence Intervals, and Simulation for Predictions) and below (Interval Analysis, Fuzzy Logic, and DS theory).

:::{admonition} Advisory on the Content below
:class: warning dropdown

In general, the content discussed below is a limited overview of more
complex topics that lead into number theory with applications in simulation. The purpose of exposing the
reader to these topics is not mastery nor familiarity with these topics, but to allow for further exploration.
It is not expected that the reader will be able to use everything in the following three subsections.

:::

#### Interval Analysis (Abstract Interpretation)

The basic concept of interval analysis (arithmetic) is taking a point estimate
such as a number, and converting it into to a range of possible values. This method has
several benefits as a computational technique that allows for the
creation of enclosures that are certain to contain at least one
solution for a specific equation or optimization problem.

A common use case is the interval extension of a general function
which gives an interval of values because giving a precise result
such as a point is functionally (and likely mathematically) unfeasible,
which is then applied to applications that do not have an exact numerical value
such as fuzzy intervals, tolerance analysis (this is a classical part of input-output analysis),
constraint programming, propagation of error analysis, and solutions to PDEs of specific
families (such as an ODE).

A reader might be wondering how does this apply to simulation? There are three major ways that
Interval Analysis is sometimes used in simulation: parameter estimation ({cite}`jaulin1993guaranteed`),
hybrid simulation ({cite}`gao2011hybrid`), and Robust Simulation and Optimization along with its
associated reliability analysis ({cite}`zou2010nonlinearity`, and {cite}`ma2013interval`). These
are important tools for making models more useful even in varying conditions, and can be used to
inform modelling choices that enhance the precision of the conclusions from simulations.

An Python package that is used for interval analysis [^1] (arithmetic) is portion which provides
a data structure with associated operations for intervals (note: it uses a namedtruple which is why
the footnote is there).

#### Fuzzy sets, logic, and numbers

The concept of a mathematical construction being fuzzy was first described in 1923 by Russell
in his short paper named "Vagueness" in which he described a logic where a preposition can evaluate
as true and false which was extended to sets[^2] with their elements being able to exist within a
range within a set as opposed to crisp sets[^3] which are binary in nature. Fuzzy numbers are an
extension on fuzzy sets and a generalization of a real number.

Fuzzy Logic is sometimes used in Agent-Based Modelling, Machine Learning, Control Systems[^4],
specialized Monte Carlo Method Implementations ({cite}`FuzzyMonteCarlo2013`),
increasing the complexity of linear programming ({cite}`Sakawa13`),
and more recently, as a formal method for simulating human behavior and perception when
interacting with machines ({cite}`bolton2022fuzzy`).

What follows this passage is a toy example of using Fuzzy Logic for a simulated control system,
which is a canonical example of a control system, a Heating, Ventilation and Air Conditioning (HVAC)
system controlled by a thermostat. This example uses scikit-fuzzy as an implementation for fuzzy logic (a reader could also implement this using the fuzzylogic package.)

:::{admonition} Code
:class: dropdown

```{code} python3
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
hvac = ctrl.Consequent(np.arange(-100, 101, 1), 'hvac')

# Define the membership functions for temperature, humidity, and outputs
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['comfortable'] = fuzz.trimf(temperature.universe, [15, 20, 25])
temperature['hot'] = fuzz.trimf(temperature.universe, [20, 40, 40])
humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['comfortable'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['humid'] = fuzz.trimf(humidity.universe, [50, 100, 100])
hvac['heating'] = fuzz.trimf(hvac.universe, [-100, -100, 0])
hvac['off'] = fuzz.trimf(hvac.universe, [-25, 0, 25])
hvac['cooling'] = fuzz.trimf(hvac.universe, [0, 100, 100])

# Fuzzy Rules

rule1 = ctrl.Rule(temperature['cold'], hvac['heating'])
rule2 = ctrl.Rule(temperature['hot'] & humidity['humid'], hvac['cooling'])
rule3 = ctrl.Rule(temperature['comfortable'] & humidity['comfortable'], hvac['off'])

# Control System Creation and Simulation
hvac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
hvac_simulation = ctrl.ControlSystemSimulation(hvac_ctrl)

# Simulate a warm and somewhat humid day
hvac_simulation.input['temperature'] = 28
hvac_simulation.input['humidity'] = 65
hvac_simulation.compute()
print(f"HVAC Output: {hvac_simulation.output['hvac']:.2f}")
humidity.view()
hvac.view()
hvac.view(sim=hvac_simulation)
```

:::

#### Theory of Belief Functions (Dempster–Shafer theory)

This subsection builds on some other topics in Statistical Inference and Prediction that
applies to modelling, for more information a reader might be interested in {cite}`GlennEvidence76`
and {cite}`Xu2025QuestionableTitle`. And if a reader is interested in a more rigorous and formal treatment of the theory of belief functions there is {cite}`chen2004evidential` which is about a specific implementation of the theory in warfare or {cite}`sentz2002combination` for a more traditional analysis.

From a formal perspective, Theory of Belief Functions are a method of
generalizing probability theory with a framework that models _epistemic_
uncertainty - in plain English, it is the mathematical formalization of evidence.
It is often used to combine information and therefore conclusions from
multiple sources into a coherent, provable statement. And the end result of this
framework is an rigorous enclosure of the true value of a calculated or
simulated number.[^5]
This formalization starts from a event space that is bounded through
support and plausibility, then it assigns masses (probabilities) to
the sets[^6] that when added together must sum to a total probability of one. Then, belief functions add context to the true but unknown probabilities in
accordance with Dempster's rule (a rule that allows for the combination of opinions/information of disparate probability distributions.)
All of these factors combine into a non-bayesian method for supporting evidence that provides an alternative view of probability judgement.

Some applications of the Theory of Belief Functions in Simulation (or at least in fields related to it) include the simulation of decision-making processes like stock trading systems {cite}`sevastianov2009synthesis`,
predictions of future events in context of Markov Chain Monte Carlo [^7] {cite}`he2011prognostics`, and most commonly in Machine Learning {cite}`belmahdi2023application` and{cite}`nachappa2020flood`.

## Errors in Interpretation and Communication

In {cite:p}`barth2012typical`, they describe the existence of five
distinct pitfalls: acceptance, distraction, complexity, implementation,
and interpretation. It does so in the context of a six stage cycle which consists of formulating the question, identifying relevant elements of the target system, choosing a model structure, implementation, model analysis, and communicating results.

### Acceptance, Understanding, & Interpretation

One of the errors that could occur during the communication stage of
simulation is that a practitioner assumes that the model is valid
and verified because its output is consistent with expectations. In Barth,
the describe this as the acceptance pitfall,
although in the social sciences this is known as confirmation bias. It is 
important to understand that just because a model is consistent
with expectations does not mean that is representative of the model or that it is useful.
An example of this is [an article](https://www.ft.com/content/5ff6469a-6dd8-11ea-89df-41bea055720b)
from the Financial Times that claims that by March 24th, 2020, half of the population of the
United Kingdom of Great Britain and Northern Ireland was infected
by the Novel Coronavirus, SARS-COV-2, based on a SIR model
(which this text discusses later) with an $\rho$ that was not constrained
nor supported by the data of the time nor in retrospect. This is an
example of confidently misunderstanding the results of a simulation the results along with the
data because it appears to match with the expectations of the practitioner.
An another problem with how this result is presented and
structured is that it is presented without the possibility of error.

A practitioner must consider the assumptions, the uncertainty, the implications
and the context that their model exists in or may generate. It is natural
to assume increased confidence because of a model, but even a model that appears to
be perfect should be backed through proper communication of results and assumptions and a
replicable, reproducible methodology for its construction[^8].

### Distraction

Distraction is often defined as something that prevents a person from giving their full attention
to the subject at hand.

In simulation, it refers to the idea that a practitioner is not accomplishing enough in the model,
constantly adding more details and increasing the scope to what they assume that.
This often occurs in the context of external or internal pressures by stakeholders to
answer every question with a single model.

It often goes "why not use this model to answer this", the reason why is the same
reason why a map cannot have every detail of the terrain, at that point the map is useless -
it is just reality.

The fundamental pair of errors in the context of distraction is scope creep and
overconfidence, these two factors make it impossible to finish the model or at best,
make the model so complex that it is impossible to understand.

How does a practitioner avoid distraction? They must have both
conceptual clarity in the fundamentals in their model and have
clarity in their research question which clients often lack.
This is difficult in many different
environments as there is often a desire to meet all of the demands
from every stakeholder and answer every question, but that is impossible
without losing the original question. Moreover, it might be needed
to switch the question if it is too vague or broad.

### Complexity and Implementation

Complexity refers to the rules that control and interact with the model, this is often a source of aleatoric uncertainty. One of the
main tasks of an engineer is to manage this uncertainty with simplicity
without destroying the usefulness of the model.

It is often hard to figure out what to exclude from the model, but
a practitioner must use their experience, conceptual clarity, willpower, and data to figure out what is useful. Moreover, this concept might require the practitioner to understand that modelling is a two-way process of addition and subtraction - it is not just building and combing concepts it is also taking away concepts that do not aid in discovery or conclusion making to find a useful, relative truth.

Implementation relies on a reasonable amount of complexity and a infrastructure that can be understood and verified by the practitioners as a useful tool and not reality itself. It is often stated in Simulation textbooks such as {ref}`Law:13` that face validity is a critical part of making models that are suitable for obtaining founded
conclusions. This is a double-edged sword, as face validity is required but not in any way sufficient for building useful models. It also needs to be rigorously analyzed and validated while maintaining a detached view of the model itself which is more and more difficult with time.

[^1]: Often Julia with its impressive set of [interval analysis tools](https://juliaintervals.github.io/dev/) is more useful for most tasks involving intervals along with Fortran (XSC), C++ (Boost Collection), or anything with the Basic Linear Algebra Subprograms will have more robust support for these operations than Python.

[^2]: An example of a fuzzy set might be natural numbers that are close to three with a
degree of relatedness defined through a membership function associated with each element that can be described as 'partially true'. I.e: [1 (0.25), 2 (0.5), 3 (1.0), 4 (0.5), 5 (0.25)].

[^3]: If the reader sees the term _crisp set_ it refers to sets that have a defined if-then statement defining them; for example, this set goes from all natural numbers smaller than 6 to only even natural numbers smaller than six to only natural numbers that are a multiple of 2 [1, 2, 3, 4, 5, 6] -> [2, 4, 6] -> [4, 6].

[^4]: Such as energy-efficient motors, auto-focusing cameras, handwriting recognition, and most modern control systems that operate on a series of rules that are phrased similar to the following: "IF first qualitative condition AND second qualitative condition, then do qualitative action".

[^5]: A reader might be wondering, then "why do confidence intervals exist?" The answer is that a rigorous enclosure for a statistic (which could be sufficient, complete, or ancillary) defines the _bounds_ of which an statistic (like expected value) may exist in, a confidence interval allows for smaller intervals where the statistic is _likely_ to exist instead of the entire range where it _does_ exist.

[^6]: These sets are often referred to as Focal Sets.

[^7]: In the paper, they refer to MCMC (Markov Chain Monte Carlo) as Bayesian Monte Carlo which is quite peculiar, since modern Bayesian inference is built on MCMC and not the other way around [a lecture on why MCMC is important to Bayesian inference](https://www.stats.ox.ac.uk/~reinert/mcmc/mcmc.pdf).

[^8]: This is one of the reasons why this work exists - to help early simulation practitioners understand what to consider when doing simulation.
