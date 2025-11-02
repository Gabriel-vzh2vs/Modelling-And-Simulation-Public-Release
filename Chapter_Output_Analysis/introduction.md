
(sec:output_analysis)=
# Output Analysis #

You have modeled ... You have implemented ... You have run the simulations ... Now what?

In this chapter we give an introduction analyzing output data from
generated from running simution models. Of course, samples are
samples, so you can of course use what you learn here for data this is
not generated from simulations. We will talk about the Monte Carlo
(MC) method. As you can read on the
[Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method), you may
not find a clear-cut defention of what the MC method is, but you will
definitely get a very clear flavor of what is involved here.

Of course, we would not be doing this unless the systems that we are
modeling and simulating are __stochastic__. For a deterministic model
that is implemented carefully, you will always get the same outcome.

We will cover the following:

- Viewing models of stochastic systems as random variables or
  stochastic processes.

- Estimating the mean & the Strong Law of Large Numbers

- Constructing confidence intervals for the means & the Central Limit
  Theorem

- A basic classification of simulation models. Here we will cover (i)
  terminating simulations and (ii) non-terminating simulations (steady
  states and cycle parameters). Time plots of variables (9.8) ??

- Handling multiple measures of performance (9.7)

- Estimating correlation (Law 4)
