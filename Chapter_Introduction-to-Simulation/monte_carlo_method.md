(sec:monte_carlo_method)=
# The Monte Carlo Method #


What is the Monte Carlo method? As you can read under [Monte Carlo
method](https://en.wikipedia.org/wiki/Monte_Carlo_method#Simple_Monte_Carlo)
on the Wikipedia, it is a class of algorithms that rely on sampling to
derive results. You will find that there is a basic form,
sometimes called "simple Monte Carlo". Let's just agree to make this
simple by dropping "simple" and simply say Monte Carlo in this
case. We can add adjectives and names for the advanced extensions.

A common application of Monte Carlo methods is to study stochastic
systems. In this case, a common pattern is to describe a system by a
model which is implemented as code, giving us a __simulation
model__. Sampling is then done by running the simulation model a
number of times, as we did in
{ref}`sec:buffons_needle`, typically followed by estimation of system
variables, something we cover in {ref}`sec:output_analysis`.

To illustrate another version of the Monte Carlo method, let show how
it can be used to estimate definite integrals such as

\begin{equation}
\label{eq:mc_integral}
I = \int_0^1 g(x)\, dx\;,
\end{equation}

where $g(x)$ is some function. The key observation or "trick" is the
following: we try match $I$ with the expectation of a cleverly chosen
random variable. With some practice, you will note that
{ref}`eq:mc_integral` is precisely what you get if you (a) pick the
uniform random variable $X\sim U(0,1)$ which has probability density
function $f(x) = 1$, and (b) introduce the random variable $Y =
g(X)$. The expectation of $Y$ equals

$$
\mathbb{E}[Y] = \mathbb{E}[g(X)] = \int_0^1 g(x) \cdot f(x)\, dx = I\;.
$$

As we will see in {ref}`sec:output_analysis`, this allows us to
estimate $I$ by sampling: construct $N$ samples from $U(0,1)$,
evaluate $g$ on each sample point $x_i$, and then estimate $I$ in
{ref}`eq:mc_integral` as:

$$
\frac{1}{N} \sum_{i=1}^N g(x_i)
$$

Neat! We will return to this example later.


## Monte Carlo method - version 0

So what exactly is the Monte Carlo method? It is a little hard to nail
down. You likely will not find a single clear-cut definition, but you
may want to look at {cite}`Owen:13`, an excellent reference. The key
elements of MC methods are present in both the examples above:

1. You have a computer program, a function, or a procedure that allows
   you to determine some measure of interest. An example is the number
   of customer in line at the Ivy Post Office at noon on a Wednesday,
   modeled as a random variable associated to some _arrival process_.
   However, as illustrated in the second example with the integral
   $I$, the function we evaluate does not have to be a random
   variable: here we just have a function $g$. You may also apply the
   MC method to a "real" procedure, that is, not something done _in
   silico_. Example: a coin flip experiment with actual coins, or a
   needle tossing experiment as in  {ref}`sec:buffons_needle`. Other "real"
   examples include real life bearing lives in measured in a test lab,
   or the number of times an actual machine fails during a 10 year
   period.

2. Every time you run your procedure in (1), you specify its input
   configuration (perhaps in the form of a random seed used to
   initialize a random number generator or RNG), and the
   initialization protocol. In each case, your procedure records and
   outputs the measure(s) of interest.

3. Next, you run the procedure $N$ times to create a sample $Z$ of size $N$.

4. Estimate the measure of interest as the average across $Z$.

The overall scheme is clear, but we have been a little cavalier on
details. As you will see, we have to cover a fair bit of material to
make these steps precise and to justify why this works as well as
when. We start with theory (the strong law of large numbers) in
{ref}`sec:output_analysis`, and continue with RNGs and the generation
of variates in {ref}`chap:random_number_generation`.  Theory and
computation both need to be done right for the MC method to work.

As we noted earlier, the MC method is not limited to computer
simulation models (the _in silico_ setting). You can also apply it to
"physical" or "real" systems such as a coin toss experiment with
actual coins. When applied to such a "real" experiment, some prefer to
say the Monte Carlo _method_. When applied to a computer simulation
model (i.e., _in silico_), they like to call it Monte Carlo
_simulation_. We simply use _method_, leaving these nuances to people
with more time on their hands than us. Throughout this book and its
exercises, you will get plenty of experience with the technique.
