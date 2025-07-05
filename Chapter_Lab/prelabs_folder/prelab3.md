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

#### Fuzzy sets

#### Theory of Belief Functions

This subsection builds on some other topics in Statistical Inference and Prediction that applies to modelling, for more information a reader might be interested in {cite}`GlennEvidence76` and {cite}`Xu2025QuestionableTitle`.

From a formal perspective, Theory of Belief Functions are a method of generalizing probability theory with a framework that models epistemic
uncertainty - in plain English, it is the mathematical formalization of evidence. It is often used to combine information and therefore conclusions from multiple sources into a coherent, provable statement.

This formalization starts from a event space that is bounded through support and plausibility, then it assigns masses (probabilities) to this sets[^1], 

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

[^1]: These sets are often referred to as Focal Sets 
