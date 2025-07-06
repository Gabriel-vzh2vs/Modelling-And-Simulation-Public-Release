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

A core element of modelling and simulation for complex systems with 'big data' as discussed in {ref} `sec:preface` is having available data; note, that the data does not
and cannot be fully representative of the whole system. Any simulation practitioner should also know because of the inherent incompleteness of models, it is critical to focus on process and structure of the simulation in the context of the data to ensure the model can be validated with real-world data. There are several methods for doing this, which are encapsulated in Christie and et al's 'Decomposition of Errors:

### Inference and Prediction

Looking back on {ref}`prelab-2`, this work discussed a method for using for binding correlated variates together (copula), and this is a common
method of improving statistical inferences and prediction using a Bayesian approach.

In Christie and et al's, the following quote is important for understanding uncertainty: "Numerical and observation errors are the leading terms in the determination of the Bayesian likelihood", as uncertainty is a function of the variance of the observations in the vast majority of cases using statistical inference.

#### Interval Analysis

The basic concept of interval analysis (arithmetic) is taking a point estimate such as a number, and converting it into to a range of possibilities. This method has several benefits as a computational technique

#### Fuzzy sets, logic, and numbers

The concept of a mathematical construction being fuzzy was first described in 1923 by Russell in his short paper named "Vagueness" in which he described a logic where a preposition can evaluate as true and false which was extended to sets[^2] with their elements being able to exist within a range within a set as opposed to crisp sets[^3] which are binary in nature. Fuzzy numbers are an extension on fuzzy sets and a generalization of a real number.

Fuzzy Logic is sometimes used in Agent-Based Modelling, Control Systems[^4], specialized Monte Carlo Method Implementations ({ref}`FuzzyMonteCarlo2013`), linear programming ({ref}`Sakawa13`) and more recently, as a formal method for simulating human behavior and perception when interacting with machines ({ref}`bolton2022fuzzy`).

#### Theory of Belief Functions

This subsection builds on some other topics in Statistical Inference and Prediction that applies to modelling, for more information a reader might be interested in {cite}`GlennEvidence76` and {cite}`Xu2025QuestionableTitle`.

From a formal perspective, Theory of Belief Functions are a method of generalizing probability theory with a framework that models epistemic
uncertainty - in plain English, it is the mathematical formalization of evidence. It is often used to combine information and therefore conclusions from multiple sources into a coherent, provable statement.

This formalization starts from a event space that is bounded through support and plausibility, then it assigns masses (probabilities) to this sets[^5], 

Of a Bayesian Approximation
<table>

### Statistical Error

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

[^1]:

[^2]: An example of a fuzzy set might be natural numbers that are close to three with a
degree of relatedness defined through a membership function associated with each element that can be described as 'partially true'. I.e: [1 (0.25), 2 (0.5), 3 (1.0), 4 (0.5), 5 (0.25)].

[^3]: If the reader sees the term _crisp set_ it refers to sets that have a defined if-then statement defining them; for example, this set goes from all natural numbers smaller than 6 to only even natural numbers smaller than six to only natural numbers that are a multiple of 2 [1, 2, 3, 4, 5, 6] -> [2, 4, 6] -> [4, 6].

[^4]: Such as energy-efficient motors, auto-focusing cameras, handwriting recognition, and most modern control systems that operate on a series of rules that are phrased similar to the following: "IF first qualitative condition AND second qualitative condition, then do qualitative action".

[^5]: These sets are often referred to as Focal Sets.
