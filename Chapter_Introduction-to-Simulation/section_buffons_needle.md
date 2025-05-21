
(sec:buffons_needle_summary)=
# Buffon's Needle - Summary and Key Points #


In {ref}`sec:buffons_needle` we went through the motions of modeling,
implementing, and simulating followed by estimating $p$, the
probability that the needle falls across two strips. This example
includes most of the key elements of simulation based science. It is
time to reflect:

## Validation ##
First, is the model we introduced a __valid__ model? It seems quite
reasonable, although things could go wrong if the person (or device)
tossing the needle onto the table does this in some kind of biased
way. How would you test something like this? We will return to this in
the chapter {ref}`sec:distribution_modeling`. Here one might collect a
sample of size $k$ of pairs $(x, \theta)$ and formally test if the
observed values of $x$ and $\theta$ are consistent with the specified
statistical distributions. Perhaps one will use a __$\chi^2$-test__ or
a __Kolmogorov-Smirnov__ (K-S) test for this.

Our model is __stochastic__, and our estimate of $p$ (or $\pi$) is a
point estimate. What can we say about the variance of our estimate?
How well have we estimated $\pi$? From
{ref}`fig:buffon_needle_pi` we see a fair bit of fluctation as we vary
the sample size $n$. We would like to provide some guarantee on the
estimate in the form of error bounds. This is the topic of
{ref}`sec:output_analysis` where we cover the construction of
__confidence intervals__ and theory that goes with that.

:::{figure} #fig:bNeedlePi
:label: fig:buffon_needle_pi

Estimating $\pi$ using the needle experiment by Buffon. The $x$-axis
show the sample size.

:::

A question related to output analysis is the following: How large does
$n$ have to be to ensure a prescribed accuracy? We will return to this
later, and also in exercises.


## Verification ##

Is the model in {ref}`howthehelltoreferencecodelisting` correctly
implemented? It is a fairly straightforward code. There is one
possible error: when estimating $\pi$, we may end up dividing by
zero. (Question: how can this happen?) Even though this is quite
unlikely, and maybe of little consequence here, for a more complex
simulation model, failing to include such tests can lead to a great
deal of grievance. In {ref}`sec:sw_practice` we look more closely at
good practices and patterns for simulation model development


### Random number generation ###

There are other assumptions that have been made. One comes through the
use of the python $\texttt{random}$ library. Is
$\texttt{random.random}$ a high quality random number generator (RNG)?
Can we trust it? Yes. But as we will see in
{ref}`sec:random_number_generation`, this was not always so
straightforward. There are many examples of RNGs that rose to fame
only to later be thrown on the landfill. Nowadays (which is 2025),
most established tools have quite solid RNGs. But not all tools, some
of which are in widespread use.  This concern is also present if you have to
develop a new tool like Simio, Arena, AnyLogic, or Matlab, or perhaps
a new programming language. In this case, you will still have to think
hard about properly generating random numbers and variates.  We will
have more to say about this topic in
{ref}`sec:random_number_generation` where we also cover generation of
random variates from distributions other than $U(0,1)$.

## Probability and statistics ##

The example with Buffon's needle illustrates standard applications of
probability and statistics. While we have included the chapter
{ref}`sec:prob_stats` this is by no means a substitute for a course or
a textbook.
