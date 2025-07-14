(prelab-3)=
# Pre-Lab 3: When Simulation Breaks Down (Read)

Now that this text has covered a substantial amount of theory,
it is important for the reader to consider malignant patterns
in simulation, some of these malignant patterns can be discovered
and removed with the methods discussed in {ref}`prelab-5`.

This pre-lab builds on the knowledge and theory presented in these
three papers: {cite:p}`barth2012typical` {cite:p}`robinson1999three`
{cite:p}`christie2005error`.

## On Prediction of Complex Phenomena

A common historical discussion in simulation literature is
the question: "how should complex phenomena be presented and analyzed
in simulation?" One of the papers that attempted to build a consensus
around this topic is {cite:p}`christie2005error`.

### Constraining the Model

A core element of modelling and simulation for complex systems with 'big data'
as discussed in {ref}`sec:preface` is having available data; note, that the data does not
and cannot be fully representative of the whole system. Any simulation practitioner
should also know because of the inherent incompleteness of models, it is critical
to focus on process and structure of the simulation in the context of the data to
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

In Christie and et al's, the following quote is important for understanding uncertainty: "Numerical and observation errors
are the leading terms in the determination of the Bayesian likelihood", as uncertainty is a function of the variance of the
observations in the vast majority of cases using statistical inference.

#### Interval Analysis (Abstract Interpretation)

The basic concept of interval analysis (arithmetic) is taking a point estimate such as a number,
and converting it into to a range of possibilities. This method has
several benefits as a computational technique that allows for the
creation of enclosures that are certain to contain at least one
solution for a specific equation or optimization problem.

A common use case is the interval extension of a general function
which gives an interval of values because giving a precise result
such as a point is functionally (and likely mathematically) unfeasible, which is then applied to applications that do not have an exact numerical value such as fuzzy intervals, tolerance analysis (this is a classical part of input-output analysis), constraint programming, propagation of error analysis, and solutions to PDEs of specific families (such as ODE).

A reader might be wondering how does this apply to simulation? There are three major ways that
Interval Analysis is sometimes used in simulation: parameter estimation ({cite}`jaulin1993guaranteed`), hybrid simulation ({cite}`gao2011hybrid`), and Robust Simulation and Optimization along with its associated reliability analysis ({cite}`zou2010nonlinearity`, and {cite}`ma2013interval`). These are important tools for making models more useful even in varying conditions, and can be used to inform modelling choices that enhance the precision of the conclusions from simulations.

An Python package that is used for interval analysis [^1] (arithmetic) is Inveralpy.


#### Fuzzy sets, logic, and numbers

The concept of a mathematical construction being fuzzy was first described in 1923 by Russell
in his short paper named "Vagueness" in which he described a logic where a preposition can evaluate
as true and false which was extended to sets[^2] with their elements being able to exist within a
range within a set as opposed to crisp sets[^3] which are binary in nature. Fuzzy numbers are an
extension on fuzzy sets and a generalization of a real number.

Fuzzy Logic is sometimes used in Agent-Based Modelling, Control Systems[^4],
specialized Monte Carlo Method Implementations ({cite}`FuzzyMonteCarlo2013`),
increasing the complexity of linear programming ({cite}`Sakawa13`),
and more recently, as a formal method for simulating human behavior and perception when
interacting with machines ({cite}`bolton2022fuzzy`).

#### Theory of Belief Functions

This subsection builds on some other topics in Statistical Inference and Prediction that
applies to modelling, for more information a reader might be interested in {cite}`GlennEvidence76`
and {cite}`Xu2025QuestionableTitle`.

From a formal perspective, Theory of Belief Functions are a method of
generalizing probability theory with a framework that models epistemic
uncertainty - in plain English, it is the mathematical formalization of evidence.
It is often used to combine information and therefore conclusions from
multiple sources into a coherent, provable statement. And the end result of this
framework is an rigorous enclosure of the true value of a calculated or
simulated number.[^5]

This formalization starts from a event space that is bounded through
support and plausibility, then it assigns masses (probabilities) to
the sets[^6],

Of a Bayesian Approximation
<table>

## Systematic Errors in Development

### Modelling

### Data

### Experimentation

## Errors in Interpretation and Communication

In {cite:p}`barth2012typical`, they describe the existence of five
distinct pitfalls: acceptance, distraction, complexity, implementation,
and interpretation.

### Acceptance

### Distraction

### Complexity

### Implementation

### Interpretation

a

[^1]: Often Julia with its impressive set of (interval analysis tools)[https://juliaintervals.github.io/dev/] is useful for this task along with Fortran (XSC), C++ (Boost Collection), or anything with the Basic Linear Algebra Subprograms will have more robust support for these operations than Python.

[^2]: An example of a fuzzy set might be natural numbers that are close to three with a
degree of relatedness defined through a membership function associated with each element that can be described as 'partially true'. I.e: [1 (0.25), 2 (0.5), 3 (1.0), 4 (0.5), 5 (0.25)].

[^3]: If the reader sees the term _crisp set_ it refers to sets that have a defined if-then statement defining them; for example, this set goes from all natural numbers smaller than 6 to only even natural numbers smaller than six to only natural numbers that are a multiple of 2 [1, 2, 3, 4, 5, 6] -> [2, 4, 6] -> [4, 6].

[^4]: Such as energy-efficient motors, auto-focusing cameras, handwriting recognition, and most modern control systems that operate on a series of rules that are phrased similar to the following: "IF first qualitative condition AND second qualitative condition, then do qualitative action".

[^5]: A reader might be wondering, then "why do confidence intervals exist?" The answer is that a rigorous enclosure defines the _bounds_ of which an sufficient statistic (like expected value) may exist in, a confidence interval allows for smaller intervals where the statistic is _likely_ to exist instead of the entire range where it _does_ exist.

[^6]: These sets are often referred to as Focal Sets.
