(sec:distribution_modeling)=
# Distribution modeling


(sec:distribution_modeling:overview)=
## Overview

In simulation-based modeling and analysis we frequently need to
characterize or capture stochastic aspects of a system. What does that
mean in practice?  For the purpose of a computer simulation, we need
to be able to generate variates for the corresponding random variables
in a representative and accurate manner. Stated differently: we need
to ensure we have a __valid__, stochastic model.  Preferably, we would
also like this done in a computationally efficient manner, but that is
not the focus here. _How do we do generate representative variates that
matches the system characteristics?_

Distribution modeling is about capturing a statistical distribution of
a random variable $X$ based on information about $X$. Information can
come in the form a sample of $X$ or a set of known properties of $X$
and/or the system or model to which $X$ apply. Information can be that
the random variable $X$ is bounded (e.g., can only assume non-negative
values as in the case of bearing lifetimes), or that the system is a
physical process and that underlying physical principles dictate that
$X$ is related to a Poisson process. Information may also come from
the literature: it may have become an established fact that certain
phenomena are accurately modeled using a specific family of
statistical distributions. If that is the case, one should certainly
factor in such insights. As stated in {cite}`Krzysztofowicz:25`,
distribution modeling is parts science and parts art. Here we will
give an introduction to this topic suited for discrete event
simulation.


- Background and introductory examples (see {cite}`Law:13` Section 6.1)

- The notion of location, scale, and shape parameters of continuous,
  parametric distributions.

- \S 6.2.2: Law's catalog of continuous parametrized distributions. Scan on
  your own to see what is available. You will see an entry ``MLE'' in
  most cases. These are the maximum likelihood estimators for the
  parameters of the distribution.

- \S 6.2.3 This is the corresponding catalog of discrete
  distributions. Scan through on your own to get a sense of what is
  available.

- \S 6.2.4 Empirical distributions: This is concerned with
  deriving a distribution directly (e.g., not through fitting to one
  of the standard, parametrized distributions). \textbf{Beware:}
  there is more than one way to define an empirical distribution, and
  they all have their uses. However: for the Kolmogorov-Smirnov
  goodness-of-fit test, there is a particular one of these we have to
  use. This sometimes causes confusion.

- \S 6.3 Assessment of sample independence: we will only cover
  this briefly. You will recognize the \emph{correlational plot} and
  the scatter diagrams as techniques we already visited when testing
  properties of RNGs in Law \S 7.4.

- \S 6.4--6.5 Distribution modeling

- \S 6.11 Selecting distributions when there is no data



Note that there are Before continuing, we note that other terms used for "distribution
modeling", perhaps the most common being "input analysis", a term that
is somewhat ambigeous and could conceivably incorporate other elements
than distribution modeling. Another term is "simulation input
modeling" which is quite similar to "input analysis". Here we will
stick with the concise term of distribution modeling.

<!--Banks: \url{https://ferltz.github.io/inv_oper_2/documents/books/Discrete-Event%20System%20Simulation-Pearson%20Banks%20Carson%20(2013).pdf}-->

There are many excellent texts on this topic such as
{cite}`Law:13,Krzysztofowicz:25,Smith:25,Biller:10`. Details on
specific topic are often described very well in the Wikipedia.
