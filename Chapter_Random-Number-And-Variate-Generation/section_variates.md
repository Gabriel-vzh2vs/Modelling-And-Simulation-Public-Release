
(sec:random_variates)=
# Generating Random Variates

In {ref}`sec:random_number_generation` we covered generating random
number from the standard uniform distribution $U(0,1)$. In this
section, we will see that once you are armed with an awesome, high
quality $U(0,1)$ RNG, you can generate variates from many other
distributions as well. We cover four main techniques:

- The Inverse Transform Method
- Composition
- Convolution
- Rejection sampling

:::{important} Why should you care about techniques for generating random variates?

Stochastic simulation methods, including discrete event simulation and
system dynamics depend on the generation of variates to sample from
the distributions of the random variables involved. Examples of
include the time to failure for the mechanical component, and the arrival
times of customers at a service location. A good understanding of
probability distributions and the associated techniques for generating
variates is essential for modeling, implementation of simulations
models, analytics, as well as validation and verification.
:::

(sec:inverse_transform_method)=
# The Inverse Transform Method

The setting is the following: we are given a univariate statistical
distribution with cumulative distribution function $F$. For now, we
assume that $F$ is strictly increasing across $0 < F(x) < 1$. Later,
we will see how this can be relaxed. Our goal is to generate variates
from this statistical distribution.

__Algorithm:__ (Inverse transform method - ITM)

  1. Generate $u$ from $U(0,1)$
  2. Return $x=F^{-1}(u)$

How do we know this is correct, and what do we have to demonstrate? We
need to show that the algorithm, viewed as a random variable $X =
F^{-1}(U)$ has CDF given by $F$.

\begin{align*}
 \Pr(X \le x) &= \Pr\bigl(F^{-1}(U) \le x \bigr)\\
	  &= \Pr\bigl(U \le F(x)\bigr) \\
	  &= F(x)\;.
\end{align*}

:::{important} Questions for thought:

1. What does it mean that $F$ is strictly increasing across the
   interval $0 < F(x) < 1$? Can you find an example of a CDF for which
   this is not the case? What does its PDF look like in this case?

2. Where was the assumption of "strictly increasing" used in the proof?

:::


:::{prf:example} Exponential distribution

The exponential distribution is the mandatory example that every
textbook on ITM will include. Recall that the exponential distribution
with rate $\lambda$ has PDF

\begin{equation*}
f(x) =
\begin{cases}
 \lambda e^{-\lambda x},& x \ge 0\\
 0, & \text{otherwise}\;,
\end{cases}
\end{equation*}

and CDF

\begin{equation*}
f(x) =
\begin{cases}
 1 - e^{-\lambda x},& x \ge 0\\
 0, & \text{otherwise}\;.
\end{cases}
\end{equation*}

In this case, solving $F(x) = u$ for $u$ gives $1-u = e^{-\lambda x}$
which after taking (natural) logarithms and sorting out terms leads to
$x = -\frac{1}{\lambda}\ln(1-u)$. The ITM applied to the exponential
distribution therefore becomes:

1. Sample $u$ from $U(0,1)$
2. Return $-\frac{1}{\lambda}\ln(1-u)$
:::


:::{exercise}

If you look in textbooks or online, you will find the following
alternative to the ITM for the exponential distributions:

1. Sample $u$ from $U(0,1)$
2. Return $-\frac{1}{\lambda}\ln(u)$

How can this also be correct?
:::


### Visualizing the inverse transform method

What is the intuition behind the method? Consider the PDF $f$ in the
figure below.

:::{figure} figs/itm-visual-pdf.svg
:width: 600
:::

We expect that the ITM should produce more samples where $f$ is
large. And that is exactly what happens. For the ITM, we "shoot" from
the $y$-axis using the value $u$ we sampled from $U(0,1)$ as shown in
the the following figure:

:::{figure} figs/itm-visual-cdf-ai.svg
:width: 600
:::

The CDF is vertically more stretched out where $f$ is large, which is
precisely what increases the chance of generating samples where
$f$ is large.

:::{prf:example} Triangular distribution

The triangular distribution with parameters $(0, 1, 2)$ has PDF

\begin{equation*}
f(x) =
\begin{cases}
    x,       & \text{if } 0 \leq x < 1 \\
    2-x,     & \text{if } 1 \leq x \leq 2 \;,
\end{cases}
\end{equation*}

and CDF

\begin{equation*}
F(x) =
\begin{cases}
    x^2/2,     &  \text{if } 0 \leq x < 1 \\
    1 - (x-2)^2/2, &  \text{if } 1 \leq x \leq 2 \;.
\end{cases}
\end{equation*}

For the ITM, we see that the range $0 \le u < 1/2$ corresponds to $0
\le x < 1$ and the range $1/2 \le u <= 1$ corresponds to $1 \le x \le 2$.

To construct $F^{-1}$ we have to invert the two parts of $F$. For $u <
\frac{1}{2}$ we solve $\frac{x^2}{2} = u$ to obtain $X = \sqrt{2u}$;
for $u \ge \frac{1}{2}$ we get the equation $1-\frac{(x-2)^2}{2} = u$
which has solution $x = 2 \sqrt{2(1-u)}$. Here we had to choose the
sign so that the solution falls in $[1, 2]$.

The ITM algorithm for the triangular distribution is:
  1. Generate $u$ from $U(0,10)$
  1. If $0\le u < 1/2$ return $\sqrt{2u}$; if $1/2 \le u \le 1$ return $2 \sqrt{2(1-u)}$
:::



### What if the CDF $F$ is not stricly increaing?

For the ITM we requried that $F$ be strictly increasing for $0 < F(x)
< 1$. What does $F$ look like if this is not the case? What does its
PDF $f$ look like? It happens if the interval defined by $0 < F(x) <
1$ contains intervals $I = [x_1,x_2]$ such that $f(x) = 0$ whenever
$x\in I$. We have illustrated one such case below:

:::{figure}
:width: 400
Figure to be added.
:::

In this case if $u=1/2$ we obtain $F^{-1}(u) = [1,2]$. How do we solve
this? Rather than using $F^{-1}$ as before, we take
\begin{equation*}
F^{-1}(u) = \inf \{x \in \mathbb{R} \mid F(x) \ge u\}\;.
\end{equation*}

In this example $\{x\in\mathbb{R} \mid F(x) \ge 1/2\} = [1,\infty)$
and thus $F^{-1}(u) = \inf [1,\infty) = 1$. Here $\inf$ denotes the
infimum, see [https://en.wikipedia.org/wiki/Infimum_and_supremum].


### The discrete distribution

Here we show how the ITM can be used with the discrete distribution
$X$ with sample space

\begin{equation*}
  \Omega = \{x_1, x_2, \ldots, x_n\}\;,
\end{equation*}

where $x_1 < x_2 < \cdots < x_n$, and the probability mass function
(PMF) is given by $p_i = \Pr(X = x_i)$ for $1 \le i \le n$. To be a valid
PMF, we require that $p_1 + p_2 + \cdots + p_n = 1$.

The CDF of the PMF is given by

\begin{equation*}
F(x) = \Pr(X \le x) = \sum_{i \atop \text{s.t. } x_i \le u } p_i
\end{equation*}

Looking at the generalized inverse from earlier

\begin{equation*}
F^{-1}(u) = \inf \{x \in \mathbb{R} \mid F(x) \ge u\}\;,
\end{equation*}

we see that $u$ is mapped to the $x_i$ where $i$ is the smalles index
such that $p_1 + p_2 + \cdots p_i$ exceedes $u$.


There is a very intuitive way to see how this works. Consider the
following diagram, where we have stacked the $p_i$ intervals
left-to-right.

:::{figure} figs/discrete-distribution.svg
:width: 600
:::

The ITM in this case generates $u$ from $U(0,1)$. We now determine
which interval the $u$ falls into and pick the corresponding value of
$x$. If $u$ falls precisely on the boundary between $x_i$ and
$x_{i+1}$ we pick the larger value $x_i$ to match $F^{-1}(u)$.



:::{prf:example} Sampling from a custom distribution

We have the following PDF f:

\begin{equation*}
f(x) =
\begin{cases}
x^2,& 0 \le x < 1\;,\\
\frac{2}{3},& 1\le x \le 2\;,\\
0,& \text{otherwise.}
\end{cases}
\end{equation*}

How can such a distribution arise? As we will see in the chapter on
distribution modeling, it may be the result of mapping a sample
(observations of a random variable) into a PDF that does not any of
the standard distribution. It may be the result of domain expertise,
system insights, and distribution modeling handywork.


(This example will be completed in class on 17 Feb 2026)

:::





__Python__: in Python you can use [scipy.stats.rv_discrete](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.html) for this.



### Challenges for the inverse transform method

The ITM relies on being able to invert the CDF $F$. In many cases,
analytically deriving $F^{-1}$ may be challenging, and one may have to
resort to numerical methods. If the numerical method is complex, one
may incur a time penalty, and one should perhaps consider
alternatives. As we will see, generating variates from the triangular
distribution can also be done using the convolution method, which we
cover later.


(sec:composition_method)=
# The Composition Method

The composition method is a technique used to generate random variates from a target distribution $F(x)$ that can be
expressed as a mixture (or "composition") of several simpler (and ideally convex) component distributions.

And our target distribution must be able to be written in the form:

$$F(x) = \sum_i p_i \cdot F_i(x)$$

Where each $F_i(x)$ is a Cumulative Distribution Function (CDF) and $p_i$ represents the weights that
ensure $\sum_i P_i = 1$.

__Algorithm:__

  1. Generate a positive, random integer $I$ such that $P(I = i) = p_i$
  2. Return $X$ with CDF $F_i$ (given $I = i$, $X$ is independent of $I$).

The following proof demonstrates that the variate $X$ generated by the algorithm above
does converge into $F(x)$ when (2) is met when using the law of total probability and the
definition of a CDF.

:::{prf:proof} Composition Proof
:class: dropdown
For any fixed $x$,

```{math}
:label: Composition

P(X \le x) = \sum_{i} P(X \le x | I = i) \cdot P(I = i) \\

= P(X < x | I = i) \cdot  p_i\\

= \sum_{i} F_i(x) \cdot p_i \\

= F(x) \\
```

:::

__Question:__ The proof of the composition method above relies on the Law of Total Probability,
$F(x) = \sum_{i} F_i(x) p_i$. What property of the $p_i$ weights is necessary for $F(x)$ to be a valid Cumulative Distribution Function (CDF)?

:::{prf:example} Laplace Distribution
A classic example of the composition method is the Laplace distribution,
which is the composition between two exponential distributions reflected off
of the $y$-axis.

Let's define the exponential distribution using it's PDF and CDF:

$$ f(x) \equiv \begin{cases} \frac{1}{2}e^x, & x < 0 \\ \frac{1}{2}e^{-x}, & x > 0 \end{cases} \quad \text{and} \quad F(x) \equiv \begin{cases} \frac{1}{2}e^x, & x < 0 \\ 1-\frac{1}{2}e^{-x}, & x > 0 \end{cases}$$

Then decompose $X$ into negative and positive exponential distributions:
$$ F_1(x) \equiv \begin{cases} e^x & \text{if } x < 0 \\ 1 & \text{if } x > 0 \end{cases} \quad \text{and} \quad F_2(x) \equiv \begin{cases} 0 & \text{if } x < 0 \\ 1-e^{-x} & \text{if } x > 0 \end{cases} $$

Next, we need to sum them together (composition) with a 50-50 chance of sampling from either distribution.

$$F(x) = \frac{1}{2} F_1(x) + \frac{1}{2} F_2(x)$$

Equation 10 gives us two processes that we need to do to use $F(x)$:

1) Generate a choice variable: Generate $U_1 \sim \text{Uniform}(0, 1)$.
2) Generate an inversion variable: Generate $U_2 \sim \text{Uniform}(0, 1)$.

We then apply the inverse transform method:
If $U_1 < 0.5$, We sample from $F_1$.

We solve $F_1(X) = U_2$:$$e^X = U_2 \implies X = \ln(U_2)$$

If $U_1 \ge 0.5$ (50\% chance): We sample from $F_2$. We solve $F_2(X) = U_2$:

$$1 - e^{-X} = U_2 \implies e^{-X} = 1 - U_2 \implies X = -\ln(1 - U_2)$$

Notice that if $U_2$ is a $\text{Uniform}(0, 1)$ variable, the term $1 - U_2$ is also distributed as a $\text{Uniform}(0, 1)$ variable. This means we can replace the $\ln(1 - U_2)$ term with $\ln(U_2)$ without changing the result.

This simplifies our algorithm to: If $U_1 < 0.5$: $X = \ln(U_2)$; otherwise, $U_1 \ge 0.5$: $X = -\ln(U_2)$.

$$X \leftarrow \begin{cases} \ln(U) & p = 1/2 \\ -\ln(U) & p = 1/2 \end{cases}$$
:::

(sec:convolution_method)=
# The Convolution Method

Convolutions are used when a random variable can be expressed as the sum
of two or more random variables, $Y_i$, and then this sum needs to be sampled as a random variate, $X$.
This is similar to the composition method, but expresses
the random variable as a sum of other random variables instead of the CDF as a weighted sum of other CDFs.

__Algorithm:__

  1. Generate $Y_1, Y_2, ... Y_m$ independently using their distribution
  2. Return $X = Y_1 + Y_2 + ... Y_m$

How do we use convolution?

:::{prf:example} Binomial as a Convolution of Bernoullis

A common use of convolution is hidden in one of the most common
distributions, the binomial distribution. Fundamentally, all
binomial random variates are just a sum of i.i.d
Bernoulli random variates.

__Definition__: Let $W = \sum_{i=1}^n X_i$, where $X_i \sim Bernoulli(p)$. Then $W \sim \text{Binomial}(n, p)$.

We want to find the probability $P(W=k)$ for $k \in \{0, 1, ..., n\}$. $W=k$ means that exactly $k$ of the $X_i$ variables are equal to 1 and $n-k$ are equal to 0.

Consider one specific sequence of $k$ successes and $n-k$ failures (e.g., $k$ successes first, then $n-k$ failures).
Because all $X_i$ are independent, the probability of this single sequence is:

$$P(X_1=1, ..., X_k=1, X_{k+1}=0, ..., X_n=0) = p^k (1-p)^{n-k}$$

The total number of such arrangements is given by $\binom{n}{k}$.
Since each of these $\binom{n}{k}$ sequences is disjoint (a different outcome)
and has the same probability $p^k (1-p)^{n-k}$, the total probability $P(W=k)$ is the sum of their probabilities. Thus
$$P(W=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

This is the exact Probability Mass Function (PMF) of a Binomial($n, p$) random variable. Thus, $W$ is binomially distributed.

And if you don't believe this result, we can also show a comparable result
using the Crude Monte Carlo method (CMC) to simulate a series of Bernoulli
Random Variates into a Binomial Random Variate, $W \sim Binomial (6, 0.4)$.

![image](../Figs/Figure_1.png)

:::{admonition} Simulation Code
:class: dropdown

```{code} python
import numpy as np
import pandas as pd
from scipy.stats import binom
from plotnine import (ggplot, aes, geom_histogram, geom_point, theme_minimal, labs)

np.random.seed(2025)
n_samples = 1_000_000
x = np.random.binomial(5, 0.4, n_samples)
y = np.random.binomial(1, 0.4, n_samples)
w = x + y

print(f"Mean of x: {x.mean():.4f}") # 2.003
print(f"Mean of y: {y.mean():.4f}") # 0.3997
print(f"Mean of w: {w.mean():.4f}") # x + y = 2.4

df_w = pd.DataFrame({'w': w})
k = np.arange(7)
pdf = binom.pmf(k, 6, 0.4)
df_pdf = pd.DataFrame({'k': k, 'pdf': pdf})
hist_breaks = np.arange(-0.5, 7.5, 1)

p = (ggplot(df_w, aes(x='w'))
    + geom_histogram(
        aes(y='..density..'),
        breaks=hist_breaks,
        fill="gray",
        color="black"
    )
    + geom_point(
        data=df_pdf,
        mapping=aes(x='k', y='pdf'),
        color="black",
        size=3
    )
    + labs(
        title="BINOM(6, 0.4)",
        y="Density",
        x="w"
    )
    + theme_minimal()
)
p.show()
```

:::

:::

:::

(sec:rejection_sampling)=
# Rejection Sampling

Acceptance-rejection sampling is usually used when there is not a tractable, closed-form
expression for the target distribution's CDF $F(x)$. The goal is to generate variates $X$ from the density function $f
(x)$ of the target distribution. A requirement is that we must select a function $t(x)$ that _majorizes_ $f(x)$ for all
of $x$. However, t(x) is not a density, therefore, we need to set $c$ which is defined as $\int^{\infty}_{-\infty} t(x) dx \ge 1$,
and then define $d$ as a density that applies for all of $x$ as $d(x) = \frac{t(x)}{c}$.

__Algorithm:__

  1. Generate $Y$ having density d
  2. Generate $U$ from $U(0,1)$, independent of $Y$
  3. If $U \le \frac{f(Y)}{t(Y)}$, return $X = Y$ and stop (accept), else return to step 1 (reject)

The proof below shows how the algorithm, given enough samples, will converge into $f(x)$ using the
definition of conditional probabilities, law of total probability, calculus, and basic algebra.

:::{prf:proof} Long Proof: Rejection Sampling
:class: dropdown
This proof is based on the Rejection Sampling method from {cite:t}`liu2001monte`.

We get a $X$ conditional on acceptance from step 3; therefore, by the definition of conditional probabilities:

$$P(X \le x) = \frac{P(\text{acceptance}, Y \le x)}{P(\text{acceptance})}$$

And for any $y$:
$$P(\text{acceptance}| Y = y) = P(U \le \frac{f(y)}{t(y)}) = \frac{f(y)}{t(y)}$$

Because in step 2, we defined $U \sim U(0,1)$, and $Y$ is independent of $U$, and t(y) majorizes f(y), therefore:

```{math}
P(\text{acceptance, } Y \le x)= \int^{\infty}_{-\infty} P(\text{acceptance, } Y \le x| Y = y) \cdot r(y) dy
```

When this is spilt this into the sum of two integration regions, the acceptance range and the rejection range
(aka what is below X and what is above X, respectively).

```{math}
\int^{X}_{-\infty} P(\text{acceptance, } Y \le x | Y = y) \cdot r(y) dy + \int^{\infty}_{X}P(\text{acceptance}, Y \le x | Y = y) \cdot r(y) dy
```

Which then simplifies into

$$\int^{X}_{-\infty} P(\text{acceptance}, Y \le x | Y = y) \cdot r(y) dy$$

And once we substitute in our definition of r(y)

$$\frac{1}{c} \int^{x}_{-\infty} t(y) dy$$

Which simplifies to

$$\frac{F(x)}{C}$$

However, we need to show how to reobtain $F(x)$, our original function, from this simplification.
In this case, we can obtain $\frac{1}{c}$ from our probability of acceptance after substituting our
$r(y)$ and performing simplification.

$$P(\text{acceptance}) = \int^{\infty}_{-\infty} P(\text{acceptance}| Y = y) \cdot r(y) dy $$

Which becomes

$$\frac{1}{c} \int^{\infty}_{-\infty} \frac{f(y)}{t(y)} t(y) dy$$

Then we apply the multiplication of reciprocals (which always becomes 1), and simplify $\int^{\infty}_{-\infty} F(x)$
as one because it is a density, and therefore also equal to one, to get $\frac{1}{c}$.

Finally, we substitute our $P(\text{acceptance, } Y \le x)$ and $P(\text{acceptance})$ into the our definition of the
conditional probability, $\frac{P(\text{acceptance, } Y \le x)}{P(\text{acceptance})}$, giving us $F(x)$ through
algebraic manipulation.

$$\frac{F(x)/c}{1/c} \rightarrow F(x)$$
:::

__Question__: The method requires an "envelope" $c \cdot g(x)$ such that $f(x) \le c \cdot g(x)$. What property of the constant $c$ is essential for the acceptance probability $P(\text{acceptance})$ to be valid, and where in the proof is this used?

Now, how can we use rejection sampling?

:::{prf:example} Half-Normal Random Variable

This example is based on {cite}`ross2022simulation`. In this example, we
wish to generate a standard half-normal RV with PDF using rejection sampling:

$$f(x) = \frac{2}{\sqrt{2\pi}}e^{-x^2/2}, \quad x \geq 0.$$

Then we use the majorizing function:
$$t(x) = \sqrt{\frac{2e}{\pi}} e^{-x} \text{ } \forall x \text{ } \ge 0$$

When we calculate $c$, we take the integral of $t(x)$ upon x:
$$c = \sqrt{\frac{2e}{\pi}} \int_{0}^{\infty} e^{-x} dx \rightarrow  \sqrt{\frac{2e}{\pi}}  = 1.3155$$

Then we get the proposed density function $h(y)$ through dividing $t(y)$ over $c$:

$$h(y) \equiv \frac{t(y)}{c} = e^{-y}$$

And then we need $g(y)$, the ratio of $f(y)$ and $t(y)$, which represents the rejection ratio.
$$g(y) = \frac{f(y)}{t(y)} = e^{-\frac{(y-1)^2}{2}}$$

Once we have our functions, we can then apply the algorithm which allows us to have a random variate representing the half-normal r.v:

1) Generate $Y$ from the "proposed density" $h(y) = e^{-y}$.
2) Generate $U \sim \text{Uniform}(0, 1)$.
3) Accept/Reject: Check if $U \le g(Y)$, where $g(Y)$ is the ratio from Equation (32):

$$U \le e^{-\frac{(Y-1)^2}{2}}$$
if it passes, accept, return $X$ = $Y$; otherwise reject. Go back to step 1.
:::

# Problems Left to the Reader

:::{seealso} Problem 1 (Software Implementation of Random Variate)
Supposed that a Random Variable, $B$ has the following p.d.f:

$$f(x) = \begin{cases}
    0 & \text{if } x < 0 \text{ or } x > 2 \\
    x & \text{if } 0 \le x \le 1 \\
    \frac{1}{2} & \text{if } 1 \le x \le 2
\end{cases}$$

a) Use a method for generating realizations $B$ through any of the four methods, some are likely to
be easier than others.

b) Write code that implements the inverse transform method for this p.d.f.

c) How would you computationally verify that your simulation method is correct?

d) Compare the Inverse Transform method and the Rejection Sampling method for this specific p.d.f.
:::

:::{seealso} Problem 2 (Analytic Application: Machine Failure)
A machine is taken out of production either if it fails or after a period of 7 hours. By running
similar machines until failure, it has been found that time to failure, $F$, has the Weibull distribution with
$\alpha = 9, \beta = 0.55, \text{ and } \nu = 0$.

a) Write out a step-by-step procedure for generating the time, $X$, until the machine is out of production. _Hint_: This can be expressed through $X = min(F, 7)$.

b) Calculate the probability is the machine is taken out of production exactly at 7 hours, $P(X=7)$, then the expected time that machine is in production, $E[X]$.

c) Using Crude Monte Carlo, Empirically Estimate $E[X]$ and $P(X=7)$ using $n = 1,000$ samples.

d) Compare your Empirical Estimate to your Analytical Answer from (b).

:::

:::{warning} Problem 3 (Analytic Exam-Style Question)
Domain experts have provided their insights regarding a random
variable that is part of a stochastic model. The insight comes in the
form of the following probability density function

\begin{equation*}
  f(x) =
  \begin{cases}
    c e^{2x},& x \le 0,\\
    c e^{-2x},& x > 0\;
  \end{cases}
\end{equation*}

that captures the associated random variable $X$ of your model.

a) Determine the constant $c$. _Hint_: Use symmetry to
save yourself some work.

b) Construct an algorithm for sampling from $X$ using the
inverse transform method.

c) Explain how you could use the convolution method to
construct an algorithm for sampling.

d) A second random variable $Y$ for the model is given by the
probability density function

\begin{equation*}
 g(x) \propto f(x) \sin^2(x), \qquad x\in\mathbb{R} \;.
\end{equation*}

Here $g(x) \propto f(x) \sin^2(x)$ means that $g(x)$ is given by
$f(x)\sin^2(x)$ up to a multiplicative constant. For rejection
sampling, explain why you do not need to determine this constant.

e) Prepare an algorithm for generating variates from the
distribution of $Y$ in (c) using rejection sampling, basing it
on the sampling method you developed in (b).
:::

:::{warning} Problem 4 (Computational Exam-Style Question: Rejection Sampling)
You need to generate samples from a target distribution $g(x)$ on the interval $x \in [-\pi, \pi]$.

The distribution is proportional to a "cosine bump":
$$g(x) \propto 1 + \cos(x), \quad x \in [-\pi, \pi]$$

You decide to use a uniform majorizing distribution, $f(x)$, which is the PDF for $U(-\pi, \pi)$:

$$f(x) = \frac{1}{2\pi}, \quad x \in [-\pi, \pi]$$

a) Analytically find the smallest constant $M$ such that $g(x) \le M \cdot f(x)$ for all $x$. _Hint_: The non-normalized target is $h(x) = 1 + \cos(x)$. You need to find $M = \sup_x \frac{h(x)}{f(x)}$.

b) Write Code that generates a single accepted sample $Y$ using rejection
sampling.

c) Use your function from part (b) to generate 10,000 accepted samples. Plot a histogram of your samples. On the same plot, overlay the true, normalized PDF $g(x)$.

d) Analyze Efficiency: Keep track of the total number of proposals $N_{total}$ and the number of accepted samples $N_{accepted}$. Calculate the empirical acceptance rate $\frac{N_{accepted}}{N_{total}}$. Compare this to the theoretical acceptance rate, which is $\frac{1}{M}$.
:::
