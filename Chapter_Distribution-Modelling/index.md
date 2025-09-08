
(chap:distribution_modeling)=
# Introduction


<!-- (sec:distribution_modeling:overview)=
## Overview -->

Distribution modeling is about mapping system information, perhaps a sample
$Z = \{z_1, z_2, \ldots, z_n\}$, to a statistical distribution. What
is the relevance of this to modeling and simulation? To ensure we have
a valid model, we need to characterize or capture its stochastic
components. What does that mean in practice? It requires us to
describe these parts as random variables and identify appropriate
parameter values for the associated distributions. If we implement the
model as a simulation we also need to be able to generate variates
frome these distributions; this is the topic of
{cite}`sec:random_variates`.

Assume we have a system $S$ whose model $M$ contains a random variable
$X$. What does "information" mean in this context when we say "mapping
information"? Information about $X$ may take several forms:

- A sample $Z = \{z_1, z_2, \ldots, z_n\}$

- Known properties of $X$. Example: $X$ is bounded (e.g., $X \ge 0$ as
  in the case of lifetimes for mechanical components, or $a \le X \le
  b$)

- Insights about processes that govern the properties of $S$ such as
  physical laws (e.g., conservation principles)

- Literature: through applied and theory-based research it may have
  become an established fact that certain phenomena are accurately
  modeled using a specific family of statistical distributions. If
  that is the case, one should certainly consider factoring in such
  insights in one's modeling approach.

In this chapter we will give an introduction to this topic. While this
book is geared towards modeling and simulation of stochastic systems,
what we cover here can be read as a standalone chapter. It is
structured as follows:

- We first introduce the notion of {cite}`sec:empirical_distribution`
  which are determined directly from a sample $Z$.  There is more than
  one way to define an empirical distribution; we will be using the
  version that goes with Kolmogorov-Smirnov goodness-of-fit test. We
  will also introduce the tool Phitter [reference] and Python
  libraries that can be used for constructing empirical distributions.

- Following this, we will review some standard statistical
  distributions. Here we cover location, scale and shape parameters of
  distributions, see {cite}`sec:distribution_examples`.

- Sample independence is often an assumption for many methods; see
  {cite}`sec:sample_independence`.

- The process {cite}`distribution_modeling` constitute the major
  portion of this chapter.

- Sometime we have no data about the system, and in this case we are led to {cite}`no_data`.


Before rounding out this introduction, we point out that "input
analysis" is another commonly used term. As you likely guessed, we
prefer distribution modeling and will use this term throughout. There
are many excellent texts on this topic, see, e.g.,
{cite}`Law:13,Krzysztofowicz:25,Smith:25,Biller:10`. Details on
specific topics and distributions are often described very well in the
Wikipedia. Plan to spend some time on this concept: as stated in
{cite}`Krzysztofowicz:25`, distribution modeling is parts science and
parts art.

<!--Banks: \url{https://ferltz.github.io/inv_oper_2/documents/books/Discrete-Event%20System%20Simulation-Pearson%20Banks%20Carson%20(2013).pdf}-->