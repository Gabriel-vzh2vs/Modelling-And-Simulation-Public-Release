
(sec:random_variates)=
# Generating random variates

In {ref}`sec:random_number_generation` we covered generating random
number from from the standard uniform distribution $U(0,1)$. In this
section we will see that once you are armed with this, you can
generate variates from a range of distributions. Here we will go
through four techniques for this:

- The Inverse Transform Method
- Composition
- Convolution
- Rejection sampling

[A brief section on why one should learn this]

[Continuous and discrete]

(sec:inverse_transform_method)=
# The Inverse Transform Method

The setting is the following: we are given a univariate statistical
distribution with cumulative distribution function $F(x)$. The goal is
to generate variates (or sample) from this statistical
distribution. In the basic version we require that $F(x)$ is strictly
increasing for $0 < F(x) < 1$. We will later see how this can be
relaxed.

__Algorithm:__

  1. Generate $u$ from $U(0,1)$
  2. Return  $x=F^{-1}(u)$

How do we know this is correct? What do we have to demonstrate? We
need to demonstrate that the random variable $X$ given by $F^{-1}(U)$
has CDF given by $F$.

\begin{align*}
 \Pr(X \le x) &= \Pr\bigl(F^{-1}(U) \le x \bigr)\\
	  &= \Pr\bigl(U \le F(x)\bigr) \\
	  &= F(x)\;.
\end{align*}

__Question:__ where was the monotonicity of $F$ used?


Is there any intuition behind the method?


(sec:composition_method)=
# The Composition Method

Composition is usually used when the target distribution's CDF, $F(x)$ is complex and can be decomposed
into a easier to calculate and convex combination of density functions, $p_i(x)$.

__Algorithm:__

  1. Generate a positive, random integer $I$ such that $P(I = i) = p_i$
  2. Return $X$ with CDF $F_i$ (given $I = i$, $X$ is independent of $I$).


[Insert Example here]
Example 1: Symmetric Triangular Distribution with vertical symmetry on $[-1, 1]$.

(sec:convolution_method)=
# The Convolution Method

Convolutions are used when a random variable can be expressed as the sum of two or more random variables, $Y_i$, and then this sum needs to be sampled as a random variate, $X$.

__Algorithm:__

  1. Generate $Y_1, Y_2, ... Y_m$ independently using their distribution
  2. Return $X = Y_1 + Y_2 + ... Y_m$

[Example Here]
Example 1: Geometric to Negative Binominal Random Variate

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

Now, how does this work?

:::{prf:theorem} Rejection Sampling
This proof is based on the Rejection Sampling method from {cite:t}`liu2001monte` :

We get a $X$ conditional on acceptance from step 3, therefore, by the definition of conditional probabilities:

$$P(X \le x) = \frac{P(acceptance, Y \le x)}{P(acceptance)}$$

And for any $y$:
$$P(acceptance| Y = y) = P(U \le \frac{f(y)}{t(y)}) = \frac{f(y)}{t(y)}$$

Because in step 2, we defined $U \sim U(0,1)$, and $Y$ is independent of $U$, and t(y) majorizes f(y), therefore:

```{math}
P(acceptance, Y \le x)= \int^{\infty}_{-\infty} P(acceptance, Y \le x| Y = y) \cdot r(y) dy
```

When then spilt this into the sum of two integration regions, the acceptance range and the rejection range
(aka what is below X and what is above X, respectively).

```{math}
\int^{X}_{-\infty} P(acceptance, Y \le x | Y = y) \cdot r(y) dy + \int^{\infty}_{X}P(acceptance, Y \le x | Y = y) \cdot r(y) dy
```

Which then simplifies into

$$\int^{X}_{-\infty} P(acceptance, Y \le x | Y = y) \cdot r(y) dy$$

And once we substitute in our definition of r(y)

$$\frac{1}{c} \int^{x}_{-\infty} t(y) dy$$

Which simplifies to

$$\frac{F(x)}{C}$$

However, we need to show how to reobtain $F(x)$, our original function from this simplification.
In this case, we can obtain $\frac{1}{c}$ from our probability of acceptance after substituting our
$r(y)$ and performing simplification.

$$P(acceptance) = \int^{\infty}_{-\infty} P(acceptance| Y = y) \cdot r(y) dy $$

Which becomes

$$\frac{1}{c} \int^{\infty}_{-\infty} \frac{f(y)}{t(y)} t(y) dy$$

Then we apply the multiplication of reciprocals (which always become 1), and simplify $\int^{\infty}_{-\infty} F(x)$
as one because it is a density, and therefore also equal to one, to get $\frac{1}{c}$.

Finally, we substitute our $P(acceptance, Y \le x)$ and $P(acceptance)$ into the our definition of the
conditional probability, $\frac{P(acceptance, Y \le x)}{P(acceptance)}$, giving us $F(x)$ through
algebraic manipulation.

$$\frac{F(x)/c}{1/c} \rightarrow F(x)$$
:::

Why is this important?

[Example Here]
Example 1 from Ross, Generate a standard half-normal RV with PDF:
$$$$