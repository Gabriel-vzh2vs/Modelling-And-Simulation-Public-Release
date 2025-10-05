
(sec:random_number_generation)=
# Random Number Generation

(sec:rng_overview)=
## Overview

These lecture notes cover the following material on random number
generation. It is recommended that you read Law \S 7.1 before starting
as a general introduction to the topic.

- Arithmetic modulo $n$
- Linear congruential generators (LCGs)
- Tests for when an LCG has full period
- More general classes of random number generators
- Empirical- and formal test for selected properties of random
  number generators

A large part of these notes deal with linear (congruential) generators
of the form
\begin{equation*}
z_{i} = a z_{i-1} + c {\pmod m} \;.
\end{equation*}
Here, the ${\mod m}$ means that we operate modulo $m$ which
translates to only considering the (non-negative) remainder of $z_i$
when divided by $m$.

__What better way to start this than some modulo $m$ gymnastics?!__


%% ----------------------------------------------------------------------

(sec:rng_modn)=
## Arithmetic Modulo $n$


:::{prf:definition}
Let $n>0$ be an integer. Integers $a,b$ are congruent modulo $n$, written
\begin{equation}
  a \equiv b {\pmod n}\;,
\end{equation}
if $a-b = km$ for some integer $k$.
:::

We will prove some of the following statements; for others we will
content ourselves with simply stating some of the facts. You should be
able to fill in the details.

(i) We have $a \equiv b {\pmod n}$ if and only if $a$ and $b$ leave
the same remainder when divided by $m$.

Note that this statement is of the ``if and only if'' kind. This means
that we need to demonstrate both implications. We do this for practice.

Assume that $a \equiv b {\pmod n}$ which means that $a - b = kn$ for
some integer $k$. Let $b = q_b n + r_b$ where
$r_b$ is the  remainder of $b$ when
divided by $n$. Inserting this into the first equality leads to

\begin{equation*}
  a = b + kn = q_b n + r_b + kn = (q_b + k)n + r_b
\end{equation*}

demonstrating that $a$ has the same remainder as $b$ when divided by $n$.

Assume next that $a$ and $b$ have the same remainder $r$ when divided
by $n$. We can then write $a = q_a n + r$ and $b = q_b n + r$ which
leads to

\begin{equation*}
a - b = q_a n + r - (q_b n + r) = (q_a + q_b) n \;,
\end{equation*}

which shows that $a \equiv b {\pmod n}$.


The next three results are stated without proof. The statements are
for general $a,b,c\in \mathbb{Z}$ and $n>0$. Using the definition, you
will have no problem providing a proof, should someone corner you in
an alley.

(ii) $a \equiv a {\pmod n}$

(iii)  $a \equiv b {\pmod n}$ implies  $b \equiv a {\pmod n}$

(iv)  $a \equiv b {\pmod n}$ and  $b \equiv c {\pmod n}$ imply $a \equiv c {\pmod n}$

__(*) Additional details:__ We note that $\equiv$ is a
\textbf{relation} on the integers $\mathbb{Z}$. (In general, a
relation on $\mathbb{Z}$ is a subset of~$\mathbb{Z}\times
\mathbb{Z}$.) Part (ii) states that $\equiv$ is \textbf{reflexive},
part (iii) states that $\equiv$ is symmetric, and (iv) states that
$\equiv$ is transitive. A relation that has these three properties is
called an \textbf{equivalence relation}. There are other types of
relations, a common one being that of a partial order (whose
properties are reflexivity, anti-symmetry and transitivity.)

We define the set $[a] = \{b \mid a
\equiv b {\pmod n}\}$ and call this the residue class of $a$. (For a
general equivalence relation, the set $[a]$ is called the equivalence
class of $a$.) From the earlier discussion, it is clear that $[a]$
equals precisely one of $[0]$, $[1]$, $[2], \ldots, [n-1]$. Which one?
If~$a = q_a n + r$ then $[a] = [r]$. Moreover, it is also clear that
$\mathbb{Z} = [0] \cup [1] \cup [2] \cup \cdots \cup [n-1]$ and also
that $[a] \cap [b] = \varnothing$ whenever $[a] \ne [b]$. This means
that the set of residue classes of~$\equiv$ form a \textbf{partition}
of $\mathbb{Z}$, a fact that is true for any equivalence relation.

We may also factor $\mathbb{Z}$ through the equivalence relation
$\equiv$ to form the quotient set
\begin{equation*}
  (\mathbb{Z}/\!\!\equiv)\, = \{[0], [1], [2], \ldots,[n-1]\}
\end{equation*}
and show that that operations of addition and multiplication on
$\mathbb{Z}$ behaves as they should on $\mathbb{Z}/\!\!\equiv$ by
picking representatives. Forming such quotients is fairly standard
construction in mathematics. You might find it in a course on discrete
mathematics or abstract algebra. \textbf{(End of starred material)}

Continuing, we have the following two results:

(v) $a \equiv b {\pmod n}$ then (1) $a+c \equiv b + c {\pmod n}$ and
(2) $ac \equiv bc {\pmod n}$.

(vi) $a \equiv b {\pmod n}$ implies $a^k \equiv b^k {\pmod n}$ for any $k>0$.

:::{prf:example}
:label:ex:division

We claim that $2^{20} - 1$ is divisible by $41$. A typical approach
for this is to make use of (vi), which is exactly what we will do. We
first notice that $2^5 \equiv -9 \pmod{41}$. This is directly from the
definition since $2^5 \equiv 2^5 - 41 \equiv -9 \pmod{41}$. We next
use~(vi):
\begin{equation*}
2^{20} = (2^5)^4 \equiv (-9)^4 = 81^2 \pmod{41}
\end{equation*}
Explicitly: since $2^5 \equiv -9 \pmod {41}$ we have
$(2^5)^4 \equiv (-9)^4 \pmod{41}$. We next consider $81$ for which we
have $81 \equiv 81 - 41 \equiv 40 \pmod{41}$. We can then consider
$40^2$ instead of $81^2$, but this is not much easier. We are
therefore led to $81 \equiv 81 - 2\cdot 41 \equiv -1 \pmod{41}$. We
have almost arrived. Adding all the details we then have:
\begin{equation*}
  2^{20}-1 \equiv
  (2^{5})^4 - 1 \equiv
  (-9)^4 - 1 \equiv
  81^2 - 1 \equiv
  (-1)^2 - 1 \equiv
  0 \pmod{41}
\end{equation*}
With a little bit of practice, these steps and simplifications become
quite quick.
:::

How does [](#ex:division) relate to linear congruential
generators? We will see this in the next section where we need check
if a prime $p$ divides integers of the form $2^m - 1$ when we assess
properties of random number generators.

We close this section with one more result, which is a well known
divisibility criterion.

:::{prf:proposition}
:label: prop:divisibility

Let $p(x) = \sum_{k=1}^m c_k x^k$ be a polynomial with integer
coefficients. If $a \equiv b \pmod n$ then $p(a) \equiv p(b) \pmod n$.
:::

You can prove this by making use of (v) and (vi) from earlier: first
establish that $a \equiv b \pmod n$ implies $a^k \equiv b^k \pmod n$
and then that $c_k a^k \equiv c_k b^k \pmod n$, and then add the terms to
form $p(a) \equiv p(b) \pmod n$.


__Divisibility criterion:__ Let $N = c_m 10^m + c_{m-1} 10^{m-1} + \cdots + c_1 10^1 + c_0 10^0$ and let $S = c_m + c_{m-1} + \cdots + c_1 + c_0$. We can now state: 9 divides $N$ if and only if $9$ divides
$S$.

We remark that $N$ is the decimal expansion of the integer usually
written $(c_m c_{m-1} \cdots c_2 c_1 c_0)$. For example, we have $9301
= 9 \cdot 10^3 + 3 \cdot 10^2 + 0\cdot 10^1 + 1 \cdot 10^0$.

How do we prove this criterion? We have $10 \equiv 1 \pmod 9$. Using
{ref}`prop:divisibility` we conclude that $N = p(10) \equiv
p(1) = S \pmod 9$. From this we see that $N$ and $S$ are in the same
residue class modulo~$9$, which is the compact way of stating the criterion.



%% ----------------------------------------------------------------------
(sec:lcgs)=
## Linear Congruential Generators


Let $a$, $c$, $m$ and $z_0$ be positive integers with $a,c,z_0 <
m$. We define the sequence of integers~$z_1$, $z_2$, $z_3,\ldots$ by

\begin{equation}
\label{eq:lcg}
 z_i = a z_{i-1} + c \pmod m \;,
\end{equation}

where $z_0$ is called the __seed__, $a$ the __multiplier__,
$c$ the __increment__, and $m$ the __modulus__. The sequence
$(z_i)_{i} = (z_0, z_1, z_2, \ldots)$ form the starting point for
generating variates from $U(0,1)$. To transform the $z_i$'s to
$U(0,1)$ variates we set

\begin{equation}
\label{eq:u_sequence}
  u_i = z_i / m \;.
\end{equation}

From {ref}`sec:rng_modn` it is clear that $0 \le z_i < m$ for all
$i$. We can visualize the "dynamics" of the $z_i$'s as in
{ref}`fig:lcg`. (We can also view {ref}`eq:lcg` as 1-dimensional
discrete dynamical system.)  Here arcs indicate how $z_i$ is mapped to
$z_{i+1}$. As we iteratively compute the $u_i$'s, we get the orbit
that starts at the seed $u_0 = z_0/m$.

:::{figure} figs/lcg-dynamics
:label: fig:lcg
:width: 600pt

The "dynamics" of the LCG in {ref}`eq:lcg`. An arc starts at
$z_i$ and ends at $z_{i+1}$. The ``mixing'' and ``distribution'' of
the $z_i$'s across $[0,1]$ is governed by the number-theoretic
relations among $a$, $c$ and $m$, see {ref}`thm:lcg`.

:::

__Question:__ what would we look for in a "good" random number
generator (RNG) like the LCG? Some properties we would likely want
include (a) the sequence of the $u_i$'s is distributed uniformly
across~$[0,1]$. We likely would want the arcs/dynamics that appear to
not be "predictable" or have discernible patterns. In
Section~\ref{sec:testing} we will make these properties precise and
also give examples of tests one can conduct to assess if such
properties holds for one's candidate RNG.

For the sequence of $u_i'$ from {ref}`eq:u_sequence`, it is clear
that there will be "gaps": by design, the sequence can only visit

\begin{equation*}
 0/m,\, 1/m,\,2/m,\,3/m,\, \ldots , (m-1)/m\;,
\end{equation*}

leaving gaps of width $1/m$ between consecutive values. For this
reason, one would typically like the modulus $m$ to be large. How
large is large? For reasons that we will see later in this section, it
is often desirable to have $m = 2^q$ or $m=2^q - 1$ where $2^q - 1$ is
prime. The latter class of primes are called Mersenne primes. You can
see a list of known such primes
[here](https://www.mersenne.org/primes/), the largest one at the
time of writing given by $q = 136279840$ with $\log_{10} (2^q-1) > 41
\cdot 10^6$.

One can also show the LCG in {ref}`eq:lcg` has closed form:

\begin{equation}
z_n = a^n z_0 + \frac{c(a^n-1)}{a-1} \pmod m
\end{equation}

This can be established by mathematical induction: the induction basis
($n=1$) becomes {ref}`eq:lcg`. With induction hypothesis that the
formula holds for $n=k$ we seek to demonstrate that it implies it will hold
for $n=k+1$:

\begin{align*}
  z_{k+1}
  &= a z_k + c \pmod m \\
  &= a\Bigl(a^k z_0 + \frac{c(a^k-1)}{a-1}\Bigr) + c \pmod m\\
  &= a^{k+1} z_0 + \frac{ac(a^k-1) + ac - c}{a-1} \pmod m\\
  &= a^{k+1} z_0 + \frac{c(a^{k+1}-1)}{a-1} \pmod m
\end{align*}


One of the properties we would like to have is that the $u_i$'s are
"evenly spread out" or uniformly distributed across $[0,1]$. If the
sequence given by the $z_i$'s visit all the numbers $0$ through $m-1$,
then the $u_i$ will be spread out as much as possible (although not
necessarily uniformly). We say that an LCG with this property has
\textbf{full period}. This naturally leads to the question "what
properties of {ref}`eq:lcg` ensure a full period"? The answer is
given by:

:::{prf:theorem}
:label: thm:lcg

The LCG defined by {ref}`eq:lcg` has full period _if and only
  if_:

(a) The greatest common divisor of $m$ and $c$ is $1$ (which we write
$\gcd(m,c) = 1$);


(b) If $q$ is a prime with $q|m$ ($q$ divides $m$ with remainder $0$),
then $q|(a-1)$;

(c) If $4|m$ then $4|(a-1)$.

:::

:::{prf:example}
For the LCG given by $z_i = 5 z_{i-1} + 3 \pmod{16}$ we have $a=5$,
$c=3$, and~$m=16 = 2^4$. We see that $\gcd(m,c) = \gcd(2^4,3) = 1$
showing that (a) holds. The prime $q=2$ divides $m$, and is also the
only prime for which $q|m$. We see that $q | (a-1) = 4$, and therefore
that $(b)$ holds. Finally, we note $4 | m$, but since $4|(a-1) = 5$ we
find that $(c)$ holds. By the above theorem, we can conclude that this
LCG has full period.
:::

:::{prf:example}
Does the LCG given by $z_i = 5 z_{i-1} + 1 \pmod 8$ have full period?
While we could use the theorem, we can also do some modulo~$m$
gymnastics starting with seed $z_0 = 0$:
\begin{equation*}
0 \to 1 \to 6 \to 7 \to 4 \to 5 \to 2 \to 3 \to 0
\end{equation*}
By brute force (or at least a slight application of moderate force), we have
demonstrated that the LCG has full period.
:::



## More advanced RNGs

In {cite}`Law:13` $\S$ 7.3 you will find other classes of RNGs. A generalization of the
LCGs from $\S$ 7.2 is based on a function

\begin{equation*}
 g(z_{i-1}, z_{i-2}, \ldots, z_{i-p}) \pmod m
\end{equation*}

where one then constructs

\begin{equation*}
 z_i = g(z_{i-1}, z_{i-2}, \ldots, z_{i-p}) \quad\text{with}\quad u_i = z_i/m \;.
\end{equation*}

A particular example of this is when $g$ is a linear function:

\begin{equation}
\label{eq:mrg}
g(z_{i-1}, z_{i-2}, \ldots, z_{i-p})
  = a_1 z_{i-1} + a_2 z_{i-2} + \cdots + a_p z_{i-p}
\end{equation}

The corresponding random number generator is called a multiple
recursive generator (MRG). An MRG like {ref}`eq:mrg` requires $p$
seeds, $z_0$, $z_1,\ldots,z_{p-1}$.

A particular version of {ref}`eq:mrg` is

\begin{equation}
 z_i = z_{i-1} + z_{i-2} \pmod m \;,
\end{equation}

known as the Fibonacci generator. As you will see in Homework 3, the
Fibonacci generator has a serious flaw. You will be challenged to
propose a fix for this.

A more involved type of RNG is given in $\S$ 7.3.2 with the
__composite, multiple, recursive generators__ which we abbreviate CMRGs.
L'Ecuyer developed one such CMRG for 32-bit processors
(see {cite}`Law:13` p. 404 and {cite}`LEcuyer:99`). This CMRG requires
6 seeds: $z_{1,0}$, $z_{1,1}$, $z_{1,2}$, $z_{2,0}$, $z_{2,1}$,
$z_{2,2}$, and is defined through the set of equations

\begin{align*}
  z_{i,j} &= 1,403,580 z_{1,i-2} - 810,728 z_{1,i-3} \pmod{2^{32} - 209}\;,\\
  z_{2,i} &= 527,612 z_{2,i-1} - 1,370,589 z_{2,i-3} \pmod{2^{32} - 22,853}\;,\\
  y_i    &= z_{1,i} - z_{2,i} \pmod{2^{32} - 209}\;,\\
  u_i    &= y_i / (2^{32} - 209)\;.
\end{align*}

Preston White reported that ARENA replaced the Lewis-Learmonth LCG
with this CMRG developed by L'Ecuyer in its 5th version. How good is
this RNG and what period does it have? This is from Preston White who
received got this from Barry Nelson (no numbers verified))

- CMRG's in general appear to have excellent statistical
  properties and very long periods.

- The L'Ecuyer CMRG has a period of $2^{191}$ which is approximately
  $3.1 \cdot 10^{57}$.

- How long is this? If your simulation could generate $2 \cdot
  10^9$ random numbers per second, it would take it approximately $4.6
  \cdot 10^{40}$ years to exhaust the period of this generator.

- For reference: the age of the universe is only about $2 \cdot
  10^{10}$ years!

You would likely be all right for some time, but who really knows?



(sec:testing)=
## Testing Random Number Generators


So far, we have seen examples of RNGs that were

- Fair (e.g., some of the LCGs)

- Rather horrible (e.g., $z_i = z_{i-1} + 1 \pmod m$)

- Good (the L'Ecuyer CMRG)

But how do we systematically assess whether a RNG is good? Tests of RNGs fall into two categories:

- __Empirical tests__
- __Formal tests__ (aka theoretical tests (Law), or theory-based tests)


(sec:empirical)=
### Empirical tests

Empirical tests operate on the sequences

\begin{equation}
\label{eq:sample}
  S = (u_1, u_2, \ldots, u_n)
\end{equation}

produced by the RNG, and the various kinds of tests, some of which we
will go through here, examine aspects and properties of what good RNGs
out to have.


(sec:uniform)=
#### Uniform distribution across $[0,1]$

Even distribution of $S$ covering the entire interval $[0,1]$ is
clearly necessary. We can use tests such as the $\chi^2$-test and the
Kolmogorov Smirnov (KS) test for this. Here we show the~$\chi^2$-test
and return to the KS-test when we cover distribution modeling (aka
input analysis).

The $\chi^2$ test for $U(0,1)$:

- Split $[0,1]$ into $k$  sub-intervals of equal width.
- Determine $f_j$, the number of samples from $S$ that fall into
  the $j$th bin $[\frac{j-1}{k}, \frac{j}{k})$ where~$1\le j \le k$.
- Under the assumption that the sample $S$ comes from $U(0,1)$,
  the null hypothesis, the expected number of samples in each of the
  $k$ bins is $n/k$.
- The test statistic is
  \begin{equation}
    \label{eq:chi2}
    \chi^2 = \sum_{i=1}^k (f_j - n/k)^2\Bigl/(n/k)
  \end{equation}
  which has approximately a $\chi^2$ distribution with $k-1$ degrees
  of freedom.
- Determine $\chi^2$ from~\eqref{eq:chi2} and compare with the
  $\chi^2_{k-1,1-\alpha}$ percentile. Reject if $\chi^2 > \chi^2_{k-1,1-\alpha}$.


```{exercise}
:label: ex:chi2
({cite}`Banks:14`) Use the CSV file in Data/chi-square-test-banks-et-al-ex-7.csv in
Canvas, take $k=10$, and determine the value of the test statistic
$\chi^2$. What is your conclusion based on the provided sample?
```

__Questions:__ what are concerns regarding the $\chi^2$-based
approach? The $\chi$-square test is developed for categorical
data. Having to introduce bins and deciding on the value of $k$ will
always leave questions. \textbf{Question:} what questions? Law has an
example of a sample where the null hypothesis is not rejected for
$k=10$ and $k=40$, but is rejected for $k=20$ (\cite[Example 6.17,
  p. 351]{Law:13}). One also needs $n$ to be sufficiently large, which
is generally not an issue in this context, and one would also like to
have $\ge 5$ sample points in each bin.


```{exercise}
:label: ex:chi2
({cite}`Banks:14` - Example~6, p.~286) You can return to this exercise
once we have covered the KS-test. Here five sample points $u_i$ were
generated:

\begin{equation*}
  0.44, 0.81, 0.14, 0.05, 0.93
\end{equation*}

Determine the KS-statistic and state your conclusion regarding this
data being distributed~$U(0,1)$.
```

```{exercise}
For the data in {ref}`ex:chi2`, run a KS-test. Does the
conclusion stay the same as for the $\chi^2$-test?
```



#### Serial test

We are again considering a sample as in {ref}`eq:sample` but now form
non-overlapping $d$-tuples

\begin{align*}
\bm{u}_1 &= (u_1, u_2, \ldots, u_d),\\
\bm{u}_2 &= (u_2, u_3, \ldots, u_{d+1}),\\
&\vdots\\
\bm{u}_r &= (u_r, u_{r+1}, \ldots, u_{r+d}) \;
\end{align*}

which, if $S$ comes from $U(0,1)$ should be IID random vectors in
$[0,1]^d$. __Question:__ how does this look for $d=2$? What would
one observe if the hypothesis was false?

One may use a $\chi^2$-test as in the previous section. Here one would
split each of the $d$ intervals~$[0,1]$ into $k$ equal-sized
sub-intervals to form $k^d$ sub-cubes ($d$-dimensional). The expected
number of sample points in each sub-cube, assuming $U(0,1)$, is
$n/k^d$. The book-keeping is more involved than before, but, well,
that is just book-keeping.

We also note that any deviation from a $d$-dimensional uniform
distribution is indicating \textbf{dependence} among the $u_i$'s.


(sec:runs)=
#### Runs tests

A runs-up test records lengths of maximal unbroken, increasing sub-sequences and their lengths. Consider the following example where $S$ has sample points $u_1$ through $u_{10}$:

\begin{equation*}
  \underbrace{0.86}_1\quad \underbrace{0.11\quad0.23}_2\quad\underbrace{0.03\quad0.12}_2\quad
  \underbrace{0.06\quad0.55\quad0.64\quad0.87}_4\quad\underbrace{0.10}_1
\end{equation*}

The recorded statistics is the number $r_1$ through $r_6$ of such runs
of length $1$, $2$, $3$, $4$, $5$, and~$\ge 6$. For the example, we
have $r_1 = 2$, $r_2 = 2$, $r_3=0$, $r_4=1$, and $r_5 = r_6 = 0$. A
somewhat specialized test statistic is used in this case,
see {cite}`Law:13` p. 411.

We could, of course, have considered decreasing maximal
sequences. While we will not cover this test in much detail, a
takeaway from this is the property that the test targets: one should
expect certain frequencies of runs-up and runs-down. If this is not
present, one may question if there is dependence.  You will see a
variant of this in Homework 3 for the Fibonacci generator.




(sec:autocorr)=
#### Auto-correlation tests

Consider the following sample of size 30 from~\cite{Banks:14} where the order of the
variates are left-right then top-bottom (e.g., $u_1 = 0.12$, $u_2 =
0.01$, and $u_{30} = 0.87$).

\begin{verbatim}
          0.12 0.01 0.23 0.28 0.89 0.31 0.64 0.28 0.83 0.93
          0.99 0.15 0.33 0.35 0.91 0.41 0.60 0.27 0.75 0.88
          0.68 0.49 0.05 0.43 0.95 0.58 0.19 0.36 0.69 0.87
\end{verbatim}

__Question:__ does the sample appear "random", or are there
discernible and potentially worrisome patterns?

Through ocular inspection, you will notice that starting from $u_5$,
every $\ell = 5$ sample point is quite large, that is, $\ge 0.87$. Does this
seem all right if samples come from $U(0,1)$? Perhaps, but it raises
at least one eyebrow.

More generally, we want to examine sub-sequences

\begin{equation*}
 u_{i}, u_{i+\ell}, u_{i+2\ell}, \ldots, u_{i+(1+M)\ell} \;
\end{equation*}

of length $M+2$, where $M$ is the largest integer for which
$i+(1+M)\ell \le n$, and study the auto-correlation estimator

\begin{equation}
\hat{\rho}_{i\ell} = \frac{1}{M+1}\Bigl[ \sum_{k=0}^M u_{i+k\ell}
  u_{i+(k+1)\ell} \Bigr] - (\frac{1}{2})^2 \;.
\end{equation}

The test statistic is

\begin{equation}
A_{i\ell} = \hat{\rho}_{i\ell}/\sigma_{\hat{\rho}_{i\ell}}
\end{equation}

where

\begin{equation*}
\sigma_{\hat{\rho}_{i\ell}} = \frac{\sqrt{13M + 7}}{12(M+1)}\;.
\end{equation*}

Here $Z_{i\ell}$ approaches a standard normal distribution as $M$
becomes large under the assumption of independence.

Note that the term $(1/2)^2$ is the expectation of $U(0,1)$ squared,
and that $12$ equals the reciprocal of the variance of $U(0,1)$.


Formally, we are in the setting of \S 4.3 of~\cite{Law:13} with
stochastic processes where want to determine covariance and
correlation. Here the quantity $\rho_{i\ell}$ corresponds to Law's
$C_{i,\ell}$.
The test is

\begin{equation}
 H_0 : \rho_{i\ell} = 0 \quad\text{and}\quad  H_1 : \rho_{i\ell} \ne 0
\end{equation}

where $\rho_{i\ell}$ is the corresponding correlation coefficient. We
do not reject if

\begin{equation*}
 -z_{1-\alpha/2} \le A_{i\ell} \le z_{1-\alpha/2}\;;
\end{equation*}

otherwise, we reject. If $\rho_{i\ell} > 0$ the sub-sequence exhibits
positive auto-correlation; if $\rho_{i\ell} < 0$ the sub-sequence
exhibits negative auto-correlation.

```{prf:example}
We consider the data at the beginning of the section. First, let us
examine the sub-sequence starting at position 3, and consider a lag of
$\ell = 5$. We use $\alpha = 0.05$. The sub-sequence in question is

\begin{verbatim}
  0.23 0.28 0.33 0.27 0.05 0.36,
\end{verbatim}

and we have $M=4$. In this case

\begin{equation*}
\hat{\rho}_{3,5}
= \frac{1}{4+1}\bigl[
    0.23\cdot 0.28
    + 0.28\cdot 0.33
    + 0.33\cdot 0.27
    + 0.27\cdot 0.05
    + 0.05\cdot 0.36
    \bigr]
- 0.25 = -0.19452\,
\end{equation*}

and $\sigma_{\hat{\rho}_{3,5}} = \frac{\sqrt{12\cdot 4 + 7}}{12(4+1)} =
0.1280$ with $A_{3,5} = -0.1945/0.1280 = -1.515$. Since
$z_{1-0.05/2} = 1.96$ we do not reject $H_0$.

How about the sub-sequence starting at position 5? This is the one
that raised an eyebrow earlier.

\begin{verbatim}
     0.89 0.93 0.91 0.88 0.95 0.87
\end{verbatim}

Here

\begin{equation*}
\hat{\rho}_{5,5}
= \frac{1}{4+1}\bigl[
    0.89\cdot 0.93
    + 0.93\cdot 0.91
    + 0.91\cdot 0.88
    + 0.88\cdot 0.95
    + 0.95\cdot 0.87
    \bigr]
- 0.25 = 0.57746\,
\end{equation*}

and $\sigma_{\hat{\rho}_{3,5}} = 0.1280$ as before, and $A_{5,5} =
0.57746/0.1280 > 4.511$ which exceeds $z_{1-0.05/2} = 1.96$ leading to
rejection of $H_0$.

```


(sec:formal)=
### Formal tests

This category of tests establishes (or debunks) properties of RNGs
through formal arguments. One basic example of this is to formally
determine the average of an LCG with full period across its orbit. You
will get to do this in Homework~3.

One of the more famous examples of such tests was done by Marsaglia
in {cite}`Marsaglia:68`. As before, we denote the random numbers
generated by $u_1$, $u_2$, and so on. We next fix $d>0$ and form the
overlapping tuples

\begin{align*}
  \bm{u_1} &= (u_1, u_2, \ldots, u_d)\\
  \bm{u_2} &= (u_2, u_3, \ldots, u_{d+1})\\
  \bm{u_3} &= (u_3, u_4, \ldots, u_{d+2})\\
  &\vdots
\end{align*}

__Question:__ Can you think of reason(s) why anyone would form
such sequences?

The main result from~\cite{Marsaglia:68} is that for multiplicative LCGs,

\begin{equation*}
 z_i = a z_{i-1} \pmod m\;,
\end{equation*}

the collection of sequences $(\bm{u}_i)_i$ will lie on a relatively
small set of $(d-1)$-dimensional hyperplanes in $[0,1]^d$.

```{prf:example}
Let $d=2$. In Law you will see this illustrated for the two LCGs $z_i
= 18 z_{i-1} \pmod{101}$ and $z_i = 2 z_{i-1} \pmod{101}$. The second
example, visualized in~\cite[Fig.~7.3]{Law:13} is striking.

In the case of the infamous LCG RANDU, which is given by

\begin{equation*}
z_i = 65539 z_{i-1} \pmod{2^{31}} \;,
\end{equation*}

one can show that for $d=3$ the collection of sequences $(\bm{u}_i)_i$
is confined to a collection of 15 planes in $[0,1]^3$,
see~\cite[Fig.~7.4]{Law:13}.

```
