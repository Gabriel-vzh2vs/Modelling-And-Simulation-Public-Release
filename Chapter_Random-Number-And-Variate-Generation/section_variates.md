
(sec:random_variates)=
# Generating random variates

In {ref}`sec:random_number_generation` we covered generating random
number from from the standard uniform distribution $U(0,1)$. In this
section we will see that once you are armed with this, you can
generate variates from a range of distributions. Here we will go
through four techniques for this:

- The Inverse Transform Method:
- Composition:
- Convolution:
- Rejection sampling:

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

The convolution method is usually used when the target distribution's CDF, $F(x)$,


(sec:convolution_method)=
# The Convolution Method




(sec:rejection_sampling)=
# Rejection Sampling

Acceptance-rejection sampling is usually used when there is not a tractable, closed-form
expression for the target distribution's CDF $F(x)$. The goal is to generate variates $X$ from the density function $f(x)$ of the target distribution. A requirement is that we must select a function $t(x)$ that _majorizes_ $f(x)$ for all of $x$.

__Algorithm:__
  1. Generate $Y$ having density d
  2. Generate $U$ from $U(0,1)$
  3. If $U \le \frac{f(Y)}{t(Y)}$, return $X = Y$ and stop (accept), else return to step 1 (reject)

Now, how does this work?
