
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

- Known properties of $X$ such that $X$ is bounded (e.g., $X \ge 0$ as
  in the case of lifetimes for mechanical components, or $a \le X \le
  b$)

- Insights about processes that govern the properties of $S$ or
  applicable physical laws (e.g., conservation principles)

- Literature: through applied and theory-based research it may have
  become an established fact that certain phenomena are accurately
  modeled using a specific family of statistical distributions. If
  that is the case, one should certainly consider factoring in such
  insights in one's modeling approach.

In this chapter we will give an introduction to this topic where we
mostly focus on the the first two cases. While this book is geared
towards modeling and simulation of stochastic systems, what we cover
here can be read as a standalone chapter. It is structured as follows:

- We first introduce the notion of __empirical distributions__ which
  are determined directly from a sample $Z$.  There is more than one
  way to define an empirical distribution; we will be using the
  version that goes with Kolmogorov-Smirnov goodness-of-fit test.


An example


 The following sections will also include the use of tools
such as Phitter as well as Python libraries.




- Background and introductory examples (see, e.g., {cite}`Law:13`
  Section 6.1)

- The notion of __location, scale, and shape parameters__ of
  continuous, parametric distributions. Illustrations using __common
  continuous and discrete parametrized distributions__ from, e.g.,
  Sections 6.2.2 and 6.2.3 in {cite}`Law:13` or the Wikipedia. Such
  listings will often include the ``MLEs''. These are the __maximum
  likelihood estimators__ for the parameters of the distribution.


- Assessment of sample independence will be covered briefly. You will
  recognize the \emph{correlational plot} and the scatter diagrams as
  techniques we already visited when testing properties of RNGs
  [REFERENCE].

- Distribution modeling, including the case where there is no data.



Note that there are other terms used for "distribution
modeling", perhaps the most common being "input analysis", a term that
is somewhat ambigeous and could conceivably incorporate other elements
than distribution modeling. Another term is "simulation input
modeling" which is quite similar to "input analysis". Here we will
stick with the concise term of distribution modeling.

<!--Banks: \url{https://ferltz.github.io/inv_oper_2/documents/books/Discrete-Event%20System%20Simulation-Pearson%20Banks%20Carson%20(2013).pdf}-->

There are many excellent texts on this topic such as
{cite}`Law:13,Krzysztofowicz:25,Smith:25,Biller:10`. Details on
specific topic are often described very well in the Wikipedia.


As stated in {cite}`Krzysztofowicz:25`,
distribution modeling is parts science and parts art.
