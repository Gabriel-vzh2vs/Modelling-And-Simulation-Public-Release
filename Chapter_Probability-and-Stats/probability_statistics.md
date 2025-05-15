```{math}

\newcommand{\wins}{\text{win-s}}
\def\Pr{\operatorname{Pr}}
\def\extra{(*)\xspace}
\def\th{${}^{\text{th}}$\xspace}
\def\exp{E}
\def\var{\operatorname{Var}}
\def\cov{\operatorname{Cov}}
```

(sec:prob_stats)=
# Probability and Statistics #



This chapter is meant as a brief review of material from the
Probability and Statistics courses that you have had (or are taking),
and that will be used in this course. Some of this material is covered
in the textbook (Law) in Chapter~4. It will be beneficial to review
(or preview) this from these courses. The description may be a little
bit more formal than what you are used to. This is done to help
clarify concepts.

The notes were prepared using {cite}`Chen:25,Taylor:84,Law:13,Ross:24`


## Probability space ##

You have had an introduction to probability in APMA 3100. Here we will
refresh key elements and cover the following concepts which together
form a probability space:
- An __experiment__;
- The __sample space__ of an experiment, a set whose elements
  are the __sample points__;
- The __family of events__ whose elements are __events__;
- The __probability measure__

These concepts will be illustrated with basic examples. Note that some
of these concepts are not always called out in introductory
probability textbooks, but you can rest assured (or hope) that the
author kept good track of these without when writing the book.

:::{prf:definition} Probability space
:label: def:prob_space

A __probability space__ consists of the following:

- A __sample space__ $\Omega$, a set whose elements $\omega$ (called
  __sample points__) correspond to the possible outcomes of an
  experiment.

- A family of __events__, that is, a collection $\mathcal{F}$ of
  subsets of $\Omega$. We say that the event $A$ __occurs__ if the
  outcome $\omega \in \Omega$ of the experiment is an element of $A$.

-  A __probability measure__ $\Pr$. This is a function defined
  on the set $\mathcal{F}$, the family of events, that satisfies
  $\Pr(\varnothing) = 0$, $\Pr(\Omega) = 1$ (where $\varnothing$ is
  the empty set), as well as
  \begin{equation*}
    0 = \Pr(\varnothing) \le \Pr(A) \le \Pr(\Omega) = 1 \quad\text{for $A\in\mathcal{F}$}\;,
  \end{equation*}
  and
  \begin{equation*}
    \Pr( \cup_{n=1}^\infty A_n) = \sum_{n=1}^\infty \Pr(A_i)
  \end{equation*}
  if the events $A_1$, $A_2$, $\ldots$ are disjoint, i.e., $A_i \cap
  A_j = \varnothing$ when $i\ne j$.

The triple $(\Omega, \mathcal{F}, \Pr)$ is called a __probability space__.
:::


Why this level formality? Whereas some introductory courses in
probability choose to omit mentioning, e.g., the family of events
$\mathcal{F}$, and may not mention the phrase _probability space_, we
think that being clear actually helps organize and structure the
concepts, which in turn helps support understanding. For example, the
probability measure is defined on the family of events $\mathcal{F}$,
not on the sample set $\Omega$. When the instructor (and/or a textbook
author) chooses to ``not needlessly complicate matters'', the reader
is left to figure all this out on their own, somehow implicitly an
unknowingly. And while it often works quite well, it never feels
satisfactory to leave this ambiguity. (Puts away soapbox.)


:::{prf:example} Coin-tossing
:label: ex:somelabel

Consider an experiment that
consists of tossing a nickel and a dime and then recording for each
coin the outcome. We write $H$ for "heads" and $T$ for "tails". In
this case, the sample space $\Omega$ of the experiment is:
\begin{equation}
\Omega = \{(H,H), (H,T), (T,H), (T,T)   \} \;.
\end{equation}
Here the sample point $(H,T)$ captures the case where the nickel came
up "heads" and the dime came up "tails".
:::

In practice, we impose additional properties on the collection
of events $\mathcal{F}$. Specifically, we require that:
1.  $\varnothing \in \mathcal{F}$ and $\Omega \in \mathcal{F}$;
2.  $A^c \in \mathcal{F}$ whenever $A\in \mathcal{F}$. (Here $A^c =
  \{\omega \in \Omega | \omega \not\in A\}$, the _complement_ of
  $A$ in $\Omega$.)
3.  $\cup_{i=1}^\infty A_n$ is in $\mathcal{F}$ whenever $A_n$ is in
  $\mathcal{F}$ for $n=1,2,\ldots$.

A collection of subsets $\mathcal{F}$ of $\Omega$ that satisfies
(1)-(3) is called a __$\sigma$-algebra__.
%%

If you think back to calculations you may have done in your
probability courses, many of them made implicit use of the fact that
the conditions (1)-(3) would hold. One such example that
should be familiar is the "fact" that
\begin{equation*}
\Pr(A) = 1 - \Pr(A^c) \;,
\end{equation*}
a rule that only makes sense if $A^c$ is $\mathcal{F}$ whenever $A \in \mathcal{F}$.


:::{prf:example} Coin-tossing (continued)
:label: ex:somelabel

For the coin tossing example we
may let $\mathcal{F}$ to be the set of all subset of $\Omega$ (which
is called the power set of $\Omega$).  In this case, the elements of
$\mathcal{F}$, and their probabilities, are shown in
Table~\ref{tab:coins}.
%%

```{table} The collection $\mathcal{F}$ of events for the coin-tossing example.
:label: tab-coins
:align: center
| $A \in \mathcal{F}$| $\Pr(A)$ | $A \in \mathcal{F}$     | $\Pr(A)$ |
| -------------------| ---------|-------------------------|----------|
| $\varnothing$      | 0        | $\Omega$                | 1        |
| $\{(H,T)\}$        | 1/4      | $\{(H,T),(T,H),(T,T)\}$ | 3/4      |
| $\{(H,H)\}$        | 1/4      | $\{(H,H),(T,H),(T,T)\}$ | 3/4      |
| $\{(T,H)\}$        | 1/4      | $\{(H,H),(H,T),(T,H)\}$ | 3/4      |
| $\{(T,T)\}$        | 1/4      | $\{(H,H),(H,T),(T,H)\}$ | 3/4      |
| $\{(H,H),(H,T)\}$  | 1/2      | $\{(T,T),(T,H)\}$       | 1/2      |
| $\{(H,H),(T,H)\}$  | 1/2      | $\{(T,T),(H,T)\}$       | 1/2      |
| $\{(H,H),(T,T)\}$  | 1/2      | $\{(H,T),(T,H)\}$       | 1/2      |
```

Here are some examples of events:

-  ``At least one heads'': $A_1 = \{(H,H),(H,T),(T,H)\}$ with
  $\Pr(A_1) = 3/4$;
-  ``Exactly 1 heads and 1 tails'': $A_2 = \{(H,T), (T,H) \}$ with
  $\Pr(A_2) = 1/2$.
-  ``The nickel is heads'': $A_3 = \{(H,T), (H,H) \}$ with
  $\Pr(A_3) = 1/2$.

:::

:::{prf:example} Monty Hall
:label: ex:monty_hall

For the Monty Hall ``experiment'', the
sample space $\Omega$ has three elements:

```{math}
\begin{equation}
  \Omega = \{A_1, A_2, A_3\}
\end{equation}
```
Here $A_i$ denotes the experiment outcome (or sample point) where the
prize is behind door $i$. We construct the family~$\mathcal{F}$ in
Table~\ref{tab:montyhall}. (\extra You may notice once more that
$\mathcal{F}$ is the power set of $\Omega$, a common choice when the
sample space is finite.)
%%
```{table} The family $\mathcal{F}$ for the Monty Hall problem.
:label: tab:montyhall
:align: left
|$A \in \mathcal{F}$ | $\Pr(A)$ | $A \in \mathcal{F}$ | $\Pr(A)$ |
|--------------------|----------|---------------------|----------|
|$\varnothing$       | 0        | $\Omega$            | 1        |
|$\{A_1\}$           | 1/3      | $\{A_1, A_2\}$      | 2/3      |
|$\{A_2\}$           | 1/3      | $\{A_2, A_3\}$      | 2/3      |
|$\{A_3\}$           | 1/3      | $\{A_2, A_3\}$      | 2/3      |
```

Assume the contestant picks the first door. The event that corresponds to
\``win-by-switching'' is $\{A_2, A_3\}$ which has probability
$2/3$. Similarly, ``win-by-not-switching'' corresponds to $\{A_1\}$
which has probability $1/3$. $\Box$
:::

(sec:prob_stats_defs)=
## Common terms and definitions

The following terms and facts should be familiar from your introductory
courses on probability. Here $A$ and $B$ denotes events.
%%
-  The event that at least one of events $A$ and $B$ occur is $A
  \cup B$, the union of $A$ and $B$.
-  The event that both events $A$ and $B$ occurs is $A \cap B$, the
  intersection of $A$ and $B$.
-  The event that $A$ does not occur is $A^c$, the complement of $A$.
-  The event $\Omega$ is called the __certain event__.
-  The event $\varnothing$ is called the __impossible event__.
-  Events $A$ and $B$ are __disjoint__ if $A\cap B =
  \varnothing$. (Here $\varnothing$ denotes the empty set.) For
  example, the two events $A= \{(H,H),(T,H)\}$ and $B=\{(H,H),(H,T)\}$
  in the coin-tossing example are __not disjoint__: $A \cap B =
  \{(H,H)\}$.
-  Events $A$ and $B$ are __independent__ if $\Pr(A \cap B) = \Pr(A)
  \times \Pr(B)$;


__The probability of $A \cup B$:__ For all events $A$ and $B$ we
have
```{raw} latex
\begin{equation*}
\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B) \;.
\end{equation*}
```


:::{prf:definition} Conditional probability
:label: def:prob_space

For events $A$ and $B$, the
conditional probability of $A$ given $B$ is defined by
```{math}
:label: eq:conditional
\begin{equation}
\Pr(A|B) = \frac{\Pr(A\cap B}{\Pr(B)}\;, \quad \text{ if $\Pr(B) > 0$}\;,
\end{equation}
```
and is undefined if $\Pr(B) = 0$.
:::

One may rewrite the expression {eq}`eq:conditional` as
\begin{equation*}
\Pr(A\cap B) = \Pr(A|B)\Pr(B) \;.
\end{equation*}


Note that if $A$ and $B$ are independent (see definition above), then
\begin{equation*}
  \Pr(A|B) =
  \frac{\Pr(A\cap B)}{\Pr(B)} = \frac{\Pr(A)\Pr(B)}{\Pr(B)} = \Pr(A) \;.
\end{equation*}
```
In other words, knowing that the event $B$ has occurred does not
impact the probability of the event $A$ from occurring.


__Law of total probability:__ Let $A_1$, $A_2$, $\ldots$, $A_n$
be events (yes, elements of $\mathcal{F}$) such that the following two
conditions are met: (1) $A_i$ and $A_j$ are disjoint when $i\ne j$,
and (2) $\Omega = A_1 \cup A_2 \cup \cdots \cup A_n$. Then for any
event $B$ we have:
```{math}
:label: eq:total_prob
\begin{equation}
  \Pr(B) = \sum_{i=1}^n \Pr(B \cap A_i) = \sum_{i=1}^n \Pr(B | A_i)\Pr(A_i)
\end{equation}
```
Note that the last equality follows from the definition of conditional
probability.


:::{prf:example} {cite}`Taylor:84`
:label: ex:urns

Consider the case with three urns
labeled I, II and III containing silver and gold coins as in {ref}`tab:urns`.

```{table} The example with urns and coins.
:label: tab:urns
:align: center
|Urn | \#(gold coins) | \#(silver coins)|
|---:|---------------:|----------------:|
|I   |              4 |               8 |
|II  |              3 |               9 |
|III |              6 |               6 |
```
Question: a coin is selected by first picking an urn, all urns being
equally likely, and then by picking one coin from the resulting urn at
random. What is the probability of the event $G$ of picking a gold
coin?

This situation is tailored for the use of the law of total
probability, one just needs to carefully choose the sets $A_i$
above. Let $A_1$ be the event that urn I was chosen, $A_2$ for urn II,
and $A_3$ for urn III. We then have (by the law of total probability):

```{raw} latex
\begin{align*}
  \Pr(G)
  &= \Pr(G \cap A_1) + \Pr(G \cap A_2) + \Pr(G \cap A_3) \\
  &= \Pr(G |A_1)\Pr(A_1) + \Pr(G | A_2)\Pr(A_2) + \Pr(G|A_3)\Pr(A_3) \\
  &= \frac{4}{12}\cdot \frac{1}{3} + \frac{3}{12} \cdot\frac{1}{3} + \frac{6}{12}\cdot\frac{1}{3} \\
  &= \frac{13}{36}
\end{align*}
:::

:::{prf:example} Monty Hall continued - for the last time)

To illustrate the law of total probability, let $A_1$ denote (as
before) the event that the prize is behind door~1. Then~$A_1^c =
\{A_2, A_3\}$. The two conditions in the law of total probability are
satisfied since (1) $A_1 \cap A_1^c = \varnothing$, and (2) $\Omega =
A_1 \cup A_1^c$. (These two equalities are always true, of course.)

Having picked door~1, we now want to compute the probability of
winning by switching, denoted by $\Pr(win-s)$, using the law of total
probability. This gives

\begin{align*}
  \Pr(win-s)
  &= \Pr(win-s \cap A_1) + \Pr(win-s\cap A_1^c) \\
  &= \Pr(win-s|A_1)\Pr(A_1) + \Pr(win-s|A_1^c)\Pr(A_1^c)\\
  &= 0 \cdot 1/3 + 1 \cdot 2/3 = 2/3 \;.
\end{align*}


The last equality follows since $\Pr(win-s|A_1)$, the probability of
winning by switching, having chosen door~1, and given that the event
$A_1$ occurred (the prize is behind door~1), is 0.  $\Box$
:::

:::{prf:example} {cite}`Ross:24`

Two cards are selected randomly from a deck of 52 playing cards. (a)
What is the probability that the two cards constitute a pair? (b) What
is the conditional probability that they constitute a pair given that
they are of different suits?

(a) Let $A$ denote the event where the two cards constitute a
pair. When drawing the second card, there are a total of 51
possibilities. Out of these, 3 will match the value of the first
card. The probability of the event $A$ is therefore $\Pr(A) = 3/51 =
1/17$.

(b) Let $B$ denote the event that the two cards are of different
suits. The problem is asking for $\Pr(A | B)$. Using the formula for
conditional probability, we can rewrite this as $\Pr(A | B) = \Pr(A
\cap B)/ \Pr(B)$. What is $A \cap B$? The event $A$, the two cards are
a pair, implies that they must be of different suits. Therefore,
$A \cap B = A$ in this case, and we have $\Pr(A \cap B) = 3/51$ from
part (a). What is the probability that the two cards are of
different suits, that is, $\Pr(B)$? There are 51 possibilities for the
second card, 39 of which of suit that differs from the first
card. Therefore $\Pr(B) = 39/51$, and we conclude that $\Pr(A |B) =
\Pr(A \cap B)/\Pr(B) = (3/51)\Bigl/(39/51) = 3/39 = 1/13$.

__Bonus question:__ are the events $A$ and $B$ independent? Why
or why not?
:::


(sec:prob_random_variables)=
## Random variables

Random variables are often introduced introductory probability courses
and in introductory statistics courses. Chapter 4 of {cite}`Law:13`
provides a fast-paced overview of the topic. These notes are based on
that book, but also on {cite}`Taylor:84`. Note that Law uses $S$ to
denote the sample space. We will stick with~$\Omega$.

**Overview:** this section covers the following topics in quick
succession. Note that we sometimes abbreviate random variable as ``r.v.''.
-  Random variable
-  The distribution function of a random variable
-  Discrete random variables and continuous random variables
-  Probability mass function and probability density function
-  Mean (aka expected value, aka expectation) of a random variable
-  Variance and standard deviation of a random variable
-  Joint distribution functions
-  Independence of random variables
-  Covariance and correlation of jointly distributed random variables.


**Random variable:** Let $\Omega$ be a sample space of an
experiment with a family of events~$\mathcal{F}$. A random variable $X$ on
$\Omega$ is a function:\footnote{\extra subject to certain conditions
that you will find described in the extra reading on page ???}
```{raw} latex
\begin{equation*}
  X \colon \Omega \longrightarrow \mathbb{R}
\end{equation*}
```
It is customary to use uppercase letter to denote random variables such
as $X$, $Y$, and $Z$. The random variable $X$ thus assigns to each
sample point $\omega \in \Omega$ a value $X(\omega)$.



**Example 4.3 (Law) - expanded:** In this experiment we roll a
pair of normal dice. The sample space in this case is
```{raw} latex
\begin{equation*}
\Omega = \{(1,1), (1,2), \ldots, (1,6), (2,1), \ldots, (6,6)\} \;.
\end{equation*}
```
Here $(a,b) \in \Omega$ encodes that $a$ appeared on the first die and
$b$ on the second. We define $X \colon \Omega \longrightarrow
\mathbb{R}$ to be the sum of the dice, that is $X\bigl((a,b)\bigr) =
a+b$.

We may also define the random variable $Y \colon \Omega
\longrightarrow \mathbb{R}$ by $Y\bigl((a,b)\bigr) = 1$ if $a=b$ and
$0$ otherwise. A zero-one random variable like this is often called an
__indicator random variable}. (You may remember this from the
first lecture on Buffon's needle.)


**Example (the coin-toss experiment): \cite{Taylor:84}** For the
coin toss experiment, we define three random variable. We let $X_n$ be
1 if the nickel was $H$ and 0 otherwise; we let $X_d$ be 1 if the dime
was $H$ and 0 otherwise; and we let $Z$ be the total number of heads,
which we may write as $Z = X_n + X_d$. The values of the random
variables are specified in Table~\ref{tab:rv_cointoss}.
```{raw} latex
\begin{table}[ht]
  \centerline{
    \begin{tabular}{|c|c|c|c|}
      \hline
      $\omega \in \Omega$ & $X_n(\omega)$ & $X_d(\omega)$ & $Z(\omega)$ \\
      \hline
      $(H,H)$ & 1 & 1 & 2 \\
      $(H,T)$ & 1 & 0 & 1 \\
      $(T,H)$ & 0 & 1 & 1 \\
      $(T,T)$ & 0 & 0 & 0 \\
      \hline
    \end{tabular}
  }
  \caption{The random variables in the coin tossing experiment.}
  \label{tab:rv_cointoss}
\end{table}
```

\textbf{Distribution function:} The distribution function (or
cumulative distribution function, or cdf for short) of a random
variable $X$ over a sample space $\Omega$ is the function $F \colon
\mathbb{R} \longrightarrow [0,1]$ defined by
\begin{equation*}
 F(x) = \Pr(X \le x) \;.
\end{equation*}
With more than one random variable, we may write $F_X$, $F_Y$, and so
on.


## Discrete and continuous random variables: ##

A random variable is a _discrete random variable_ if there is a
finite or denumerable set of distinct values $x_1$, $x_2$, $\ldots$ such that
\begin{equation*}
  a_i = \Pr( X = x_i ) > 0 \quad \text{for $i=1,2,\ldots$ and}\quad \sum_i a_1 = 1 \;.
\end{equation*}
The function $p$ defined by $p(x_i) = a_i$ for $i=1,2,\ldots$ is the
_probability mass function for $X$_. The distribution function
for $X$ is given by
```{raw} latex
\begin{equation*}
 F(x) = \sum_{x_i \le x} p(x_i) \;.
\end{equation*}
```

**Example: (Law 4.5)** Here $X$ is the discrete random variable
given by $x_1 = 1$, $x_2 = 2$, $x_3=3$, $x_4 = 4$ and $p(x_1) = 1/6$,
$p(x_2) = 1/3$, $p(x_3) = 1/3$ and $p(x_4) = 1/6$. \textbf{For the
  reader:} draw the graph of (a) the probability mass function and (b) the
distribution function of $X$.


A random variable $X$ for which $\Pr(\{X = x\}) = 0$ for all $x$ is
called a _continuous random variable_. If there is a non-negative
function $f(x) = f_X(x)$ defined on $\mathbb{R}$ such that
```{raw} latex
\begin{equation*}
\Pr( \{a < X \le b\} ) = \int_a^b f(x)dx \quad{\text{for}}\quad -\infty < a < b <\infty\,
\end{equation*}
```
then $f(x)$ is called the _probability density function_ for the
random variable $X$. If $X$ has a probability density function $f(x)$,
then $X$ is continuous and
```{raw} latex
\begin{equation*}
  F(x) = \int_{-\infty}^x f(\xi) d\xi, \quad
\end{equation*}
```
Finally, if $F(x)$ is differentiable, then
```{raw} latex
\begin{equation*}
 f(x) = \frac{d}{dx} F(x) = F'(x), \quad  -\infty < x < \infty \;.
\end{equation*}
```

**Example: (\cite[2.13]{Ross:24}** - a general version of Law
  4.7)} The uniform random variable on the interval $(a,b) \subset
\mathbb{R}$ has probability density function given by
```{raw} latex
\begin{equation*}
  f(x) =
  \begin{cases}
    \frac{1}{b-a} & a < x < b\\
    0, & \text{otherwise.}
  \end{cases}
\end{equation*}
```
We will construct the function $F(x)$. There are three cases:

(1) $x \le a$. In this interval $F(x)$ equals 0.

(2) $x \ge b$. For any such value of $x$ we have $F(x) = 1$. We now have to bridge from $a$ to $b$.

(3) $a < x < b$. In this case, we use the definition above to compute
```{raw} latex
\begin{equation*}
  F(x) = \int_{-\infty}^x f(\xi) d\xi = \int_{a}^x \frac{1}{b-a} d\xi = \frac{1}{b-a}[\xi]_{a}^x = \frac{x-a}{b-a} \;.
\end{equation*}
```
**For the reader:** (a) draw $f(x)$ and $F(x)$. See also Law
Table 6.3. Chapter 6 of Law contains a wealth of distributions for
common random variables.




**Expectation and Variance of a Random Variable:**
The expectation of a random variable $X$, which is written $E(X)$ or $\mu_X$, is given by
\begin{equation*}
  \mu_X = E[X] =
  \begin{cases}
    \sum\limits_i x_i p_X(x_i) & \text{if $X$ is discrete, and}\\
    &\phantom{a}\\
    \int\limits_{-\infty}^{\infty} x f_X(x) dx & \text{if $X$ is continuous,}
  \end{cases}
\end{equation*}
where $p_X$ and $f_X$ is the corresponding probability mass function
and probability density function.

The _variance_ of the random variable $X$ is
```{raw} latex
\begin{equation*}
\operatorname{Var}[X] = E[ (X-\mu_X)^2]\;.
\end{equation*}
```
It is straightforward to show that $ \operatorname{Var}[X] = E[X^2] -
\mu_X^2$. Sometimes the variance of $X$ is denoted by
$\sigma_X^2$. The variance of $X$ measures deviation from the mean
$\mu_X$.

The _standard deviation_ of $X$ is $\sigma_X = \sqrt{\operatorname{Var}[X]}$.


The _median_ of a random variable is any value $\nu$ that satisfies
```{raw} latex
\begin{equation*}
 \Pr(\{X \ge \nu\} \ge 1/2\quad \text{and} \quad  \Pr(\{X \le \nu\} \ge 1/2 \;.
\end{equation*}
```

If $g$ is a function and $X$ is a random variable, then $Y = g(X)$ is a random variable and the expectation of $Y$ is $E[g(X)]$, which, in the case of $X$ discrete, becomes
```{raw} latex
\begin{equation*}
 E[g(X)] = \sum\limits_i g(x_i) p_X(x_i) \;.
\end{equation*}
```
\extra Can you find an example of a random variable $X$ that is
continuous and a function $g$ such that $Y=g(X)$ is discrete?


We also incorporate some other quantities that we may encounter in the course:
  -  The $m$\th moment of a random variable $X$ is $E(X^m)$, provided this quantity converges.
  -  Skewness is defined as $E\Bigl[
    \Bigl(\frac{X-\mu}{\sigma}\Bigr)^3\Bigr]$. Skewness measures
    asymmetry of $X$ about its mean $\mu$.
The Excel plugin XLRisk will report estimates for some of
these quantities when you apply the Monte Carlo method.



**Example: $X$ is $U(a,b)$ (continued):** For this continuous distribution we have
```{raw} latex
\begin{equation*}
  E(X) = \int\limits_{-\infty}^{\infty} x f(x) dx
  = \int\limits_{a}^{b} x \frac{1}{b-a} dx
  = \frac{1}{b-a} [x^2/2]_{a}^{b} = (b^2-a^2)\frac{1}{2(b-a)}
  = (b+a)/2 \;,
\end{equation*}
```
and variance given by

```{raw} latex
\begin{align*}
  \operatorname{Var}(X) &= E(X^2) - \mu^2
  = \int\limits_{-\infty}^{\infty} x^2 f(x) dx  - \mu^2
  = \int\limits_{a}^{b} x^2 \frac{1}{b-a} dx  - \mu^2\\
  &= \frac{1}{b-a} [x^3/3]_{a}^{b} - \mu^2
  = \frac{b^3-a^3}{3(b-a)} - (\frac{b+a}{2})^2\\
  &= \frac{(b-a)^2}{12}\;.
\end{align*}
```
Again, see Law Table 6.3.


**Joint distribution functions:** Let $X$ and $Y$ be random
variables. Their _joint distribution function_ is the function
$F_{XY}$ of two variables defined by
```{raw} latex
\begin{equation}
  \label{eq:joint2}
  F_{XY}(x,y) = \Pr( X \le x \text{ and } Y \le y)\;.
\end{equation}
```
If there is a function $f_{XY}$ of two real variable such that
```{raw} latex
\begin{equation*}
  F_{XY}(x,y) = \int\limits_{-\infty}^{y}\int\limits_{-\infty}^{x} f_{XY}(\xi,\eta) \, d\xi\, d\eta
  \quad\text{for all $x$, $y$}\;,
\end{equation*}
```
then we call $f_{XY}$ a _joint probability density function_.

We call
```{raw} latex
\begin{equation*}
  F_X(x) = \lim_{y\to\infty} F(x,y)  \quad{\text{and}}\quad
  F_Y(y) = \lim_{x\to\infty} F(x,y)
\end{equation*}
```
the _marginal distribution function_ of $X$ and $Y$,
respectively. If $F$ has a joint density function~$f$, then the
marginal density functions for $X$ and $Y$ are
```{raw} latex
\begin{equation*}
  f_X(x) = \int\limits_{-\infty}^{\infty} f(x,y) dy
  \quad  \text{and} \quad
  f_Y(y) = \int\limits_{-\infty}^{\infty} f(x,y) dx
\end{equation*}
```



We note that the notion of joint distribution function extends
directly to the case of $n$ random variable $X_1$, $X_2$, $\ldots$,
$X_n$, as does the notion of independence.


**The discrete case:** This is very similar to the continuous
case: see Law (page 220) for the case where $X$ and $Y$ are discrete
random variables.

**The mixed case:** One may similarly construct the joint
distribution function for the case where $X$ is continuous and $Y$ is
discrete. If you start from the base definition of joint distribution
function in Eq.~\eqref{eq:joint2} you should have no trouble providing
the various definitions.



**Independence of random variables**


If the joint distribution function of random variable $X$ and $Y$ satisfies
```{raw} latex
\begin{equation*}
  F(x,y) = F_X(x) \times F_Y(y) \quad \text{ for all $(x,y)$} \;,
\end{equation*}
```
then the random variable $X$ and $Y$ are _independent_.

If $X$ and $Y$ are independent with joint density function $f(x,y)$
then we conclude from
\begin{equation*}
  F_X(x)F_Y(y) = F_{XY}(x,y) =
  \int\limits_{-\infty}^{y}\int\limits_{-\infty}^{x} f_{XY}(\xi,\eta)\, d\xi\, d\eta
\end{equation*}
and the fundamental theorem of calculus (applied for both $x$ and $y$) that
\begin{equation*}
f_{XY}(x,y) = f_{X}(x)f_{Y}(y) \;.
\end{equation*}



**Covariance and correlations of jointly distributed random variables:** to measure dependence of jointly distributed random
variables $X$ and $Y$, one may use _covariance_,
written~$\sigma_{XY}$ and $\operatorname{Cov}[X,Y]$ and defined as
```{raw} latex
\begin{equation*}
  \operatorname{Cov}[X,Y] = \sigma_{XY} = E[ (X-\mu_x)(Y-\mu_Y)] = E[XY] - \mu_X \mu_Y \;,
\end{equation*}
```
where the latter equality follows directly from the definition of
expectation.

The random variables $X$ and $Y$ are _uncorrelated_ if
$\sigma_{XY} = 0$. Independent random variables are uncorrelated, but
the converse is not true.

It is often useful to normalize $\sigma_{XY}$ (in parts to remove
units), and one defines the correlation~$\rho_{XY}$ by
```{raw} latex
\begin{equation*}
  \rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} \quad
  \text{for which we have}\quad -1 \le \rho_{XY} \le 1 \;.
\end{equation*}
```



## Rules for evaluation of expectation, variance and covariance: ##

Some useful results and facts. Here $X$, $Y$, $X_i$ and so on denote
random variable, $c$, $c_i$ denotes constants (real numbers).

-  $E[cX] = cE[X]$
-  $E[X + Y] = E[X] + E[Y]$
-  $\operatorname{Var}[X] \ge 0$
-  $\operatorname{Var}[cX] = c^2 \operatorname{Var}[X]$
-  $\operatorname{Var}X+Y] = \operatorname{Var}[X] + \operatorname{Var}[Y] + 2 \operatorname{Cov}[X,Y]$
-  $\operatorname{Cov}[X,Y] = \operatorname{Cov}[Y,X]$
-  $\operatorname{Cov}[X + c, Y] = \operatorname{Cov}[Y,X]$
-  $\operatorname{Cov}[c_1 X, c_2 Y] =  c_1 c_2 \operatorname{Cov}[X,Y]$

If $X$ and $Y$ are uncorrelated then $\operatorname{Var}[X + Y] = \operatorname{Var}[X] + \operatorname{Var}[Y]$
```{raw} latex
%% $
%% \operatorname{Cov}[c_1 X, c_2 Y] = E[(c_1 X) (c_2 Y)] - E[c_1X]E[c_2Y]
%% = c_1 c_2 E[XY] - c_1 c_2 E[X]E[Y] = c_1 c_2 \\operatorname{Cov}[X,Y]
%% $
```

```{raw} latex
\begin{align*}
  \operatorname{Var}[X+Y]
  &= E[(X+Y)^2] - (\mu_X + \mu_Y)^2 \\
  &= (E[X^2] - \mu_X^2) + (E[Y^2] - \mu_Y^2) + 2(E[XY] + \mu_X \mu_Y ) \\
  &= \operatorname{Var}[X] + \operatorname{Var}[Y] + 2 \operatorname{Cov}[X,Y]
\end{align*}
```

**Exercise:** Generalize the identity $\operatorname{Var}[X+Y] = \operatorname{Var}[X] +
\operatorname{Var}[Y] + 2 \operatorname{Cov}[X,Y]$ from $X+Y$ to $X_1 + X_2 + \cdots + X_n$. We
will need this result when we conduct output analysis of simulations.




# Stochastic Processes #

You will learn about stochastic processes in Robert Riggs' SDM
course. A brief overview is given here.

A stochastic process is a collection of random variables indexed by a
set $T$ (the _index set_) defined over a common probability space
$(\Omega, \mathcal{F}, \Pr)$ where $\Omega$, $\mathcal{F}$ and $\Pr$
are as before. We write $\{X(t) : t \in T\}$. Often, $T$ represents
time, and $X(t)$ is a random variable representing a value observed at
time $t$.


When one wants to be very precise, one may write the stochastic
process as $\{X(\omega, t) : t \in T\}$ to point out that it is a
function of two variables, $t\in T$ and $\omega \in \Omega$.

In 3062 there will be two main cases. The easiest case is when the
random variables $X(t)$ are independent and identically
distributed. This is the case for the example with Buffon's needle.

A second case happens in queuing systems where $X(t)$ could be the size
of a queue at time $t$. In this case, the random variables $X(t)$ are
generally not independent. For this class, one may consider
_stationary stochastic processes_ where all the random variables
$X(t)$ are identically distributed. Another class is that of
_covariance stationary_ stochastic processes which we will likely
return to when analyzing queuing systems.


## Some less typical examples and advanced concepts ##

This material in this section is optional and will not be included in
homework or exams. It is meant for those who want to know some more
of the details behind random variables.


**Example (coin-tossing):** We return to the coin tossing
example. Recall the table:
```{raw} latex
  \centerline{
  \begin{tabular}{|l|l|l|l|}
    \hline
    $A \in \mathcal{F}$ & $\Pr(A)$ & $A \in \mathcal{F}$ & $\Pr(A)$ \\
    \hline
    $\varnothing$ & 0 & $\Omega$ & 1 \\
    $\{(H,T)\}$ & 1/4 & $\{(H,T),(T,H),(T,T)\}$ & 3/4 \\
    $\{(H,H)\}$ & 1/4 & $\{(H,H),(T,H),(T,T)\}$ & 3/4 \\
    $\{(T,H)\}$ & 1/4 & $\{(H,H),(H,T),(T,H)\}$ & 3/4 \\
    $\{(T,T)\}$ & 1/4 & $\{(H,H),(H,T),(T,H)\}$ & 3/4 \\
    $\{(H,H),(H,T)\}$ & 1/2 & $\{(T,T),(T,H)\}$ & 1/2 \\
    $\{(H,H),(T,H)\}$ & 1/2 & $\{(T,T),(H,T)\}$ & 1/2 \\
    $\{(H,H),(T,T)\}$ & 1/2 & $\{(H,T),(T,H)\}$ & 1/2 \\
    \hline
  \end{tabular}
  }
  ```

We define three random variables $X_n$, $X_d$ and $Z = X_n + X_d$
with values as specified in the following table:
```{raw} latex
\centerline{
  \begin{tabular}{|c|c|c|c|}
    \hline
    $\omega \in \Omega$ & $X_n(\omega)$ & $X_d(\omega)$ & $Z(\omega)$ \\
    \hline
    $(H,H)$ & 1 & 1 & 2 \\
    $(H,T)$ & 1 & 0 & 1 \\
    $(T,H)$ & 0 & 1 & 1 \\
    $(T,T)$ & 0 & 0 & 0 \\
    \hline
  \end{tabular}
}
```

We want to find the distribution function for the random variable
$X_n$. In other words, we want to specify $F_{X_n}(x) = \Pr(\{\omega |
X_n(\omega) \le x \})$ for all $x$. There are three cases (you see this
from the table above for the $X_n$ column).

Case 1: $x < 0$. Here $\{\omega | X_n(\omega) < x\} = \varnothing$ and
$F_{X_n}(\{\omega | X_n(\omega) \le x\}) = 0$.

Case 2: $0\le x < 1$. For this case, $\{\omega | X_n(\omega) < x\} = \{(T,H), (T,T) \}$ an event with probability $1/2$, which means that $F_{X_n} = 1/2$.

Case 3: $x\ge 1$. Here we see that $\{\omega | X_n(\omega) < x\} =
\Omega$ and therefore $F_{X_n} = 1$.

We summarize this step-function as follows:
```{raw} latex
\begin{equation*}
  F_{X_n}(x) =
  \begin{cases}
    0,& x < 0 \\
    1/2, &0 \le x < 1\\
    1, &x \ge 1
  \end{cases}
\end{equation*}
```
You may want to plot this function and reflect on the fact that the
elements of $\Omega$ do not appear on the $x$-axis.

To construct the distribution function $F_Z$ you will find that there are four cases:

Case 1: $x<0$. $\{\omega | Z(\omega) < x\} = \varnothing$

Case 2: $0\le x < 1$. $\{\omega | Z(\omega) < x\} = \{(T,T)\}$

Case 3: $1 \le x < 2$. $\{\omega | Z(\omega) < x\} = \{(T,T), (T,H), (H,T)\}$

Case 4: $x \ge 2$. $\{\omega | Z(\omega) < x\} = \Omega$

This leads to

```{raw} latex
\begin{equation*}
  F_{Z}(x) =
  \begin{cases}
    0,& x < 0 \\
    1/4, &0 \le x < 1\\
    3/4, &1 \le x < 2\\
    1, &x \ge 2 \;.
  \end{cases}
\end{equation*}
```

\textbf{(**)} The $\sigma$-algebra generated by $X_n$ is
```{raw} latex
\begin{equation*}
\mathcal{F}{(X_n)} = \{\varnothing, \Omega, \{(T,H),(T,T)\}, \{(H,T),(H,H)\}  \}\;.
\end{equation*}
```
What does that mean exactly? It means the following:
$\mathcal{F}(X_n)$ is the smallest collection of events $\mathcal{F}$
that we can pick such that the sets $\{\omega | X_n(\omega) \le
x\}$ are contained in $\mathcal{F}$ for all choices of $x$.

If there would be such a set that is not contained in $\mathcal{F}$,
with a matching value $x$, then the value of the distribution function
$F$ at $x$ would be undefined. Things do not work out.

Earlier in this example, we took $\mathcal{F}$ to be the power-set of
$\Omega$, that is, the set of all subsets of $\Omega$. That will
certainly work, but as we just saw in the case of $X_n$, this
may be an overkill.


The $\sigma$-algebra generated by $Z$ is the following
$8$-element subset of $\mathcal{F}$:
```{raw} latex
\begin{align*}
  \mathcal{F}{(Z)} =
  \{& \varnothing, \Omega, \{(T,T)\}, \{(T,T),(T,H),(H,T)\}, \{(H,H)\}, \\
    &\{(H,H),(H,T),(T,H)\},\{(H,T),(T,H)\}, \{(H,H),(T,T) \}\;.
\end{align*}
```


Again, the crux in all the above is that to have a random variable
$X$, the set $\{ \omega | X(\omega) \le x\}$ needs to be an element of
$\mathcal{F}$ for all~$x$. For most introductory courses on random
variables, the cases considered are ``nice'' and this property holds
automatically.



**Example: (a biased coin)** Include this?? Gabe: I think that might be good to include, particular if we reuse the coin idea when talking about binominals as convulations.

**Example (Buffon's needle):** In the lecture we modeled the
needle toss using the function. In this case, we have a product
probability space of $U(0,d)$ and $U(-\pi/2,\pi/2)$.
