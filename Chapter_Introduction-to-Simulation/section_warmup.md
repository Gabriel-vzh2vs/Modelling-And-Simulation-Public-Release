
(sec:intro_warmup)=
# Preview, prerequisites, and preparation  #

Do you already know modeling and simulation? Do you have the required
prerequisites for this book? Give the following problem a shot and see
for yourself. Unless you have solved this or a very similar problem
before, we recommend that you actually break out your pen, paper, and
your computer. You may be surprised. It is inspired by a problem that
appears in {cite}`Banks:14`.


(sec:intro_chefs)
## The Three Chefs ##

Three friends, let us call them $A$, $B$ and $C$, run a lodge where
they have just started offering breakfast. Now wanting to complicate
matters, and mostly catering to carnivorous guests, they have
standardized on a single-item breakfast menu: eggs, toast and
bacon. They split the meal preparation as follows:

- $A$ prepares the eggs which involves ($A_1$) cracking the eggs,
  ($A_2$) scrambling the eggs, and ($A_3$) cooking the eggs.

- $B$ is in charge of preparing toast consisting of the steps ($B_1$)
  making toast, and ($B_2$) buttering toast.

- $C$ prepares the bacon consisting of a single step ($C_1$) frying
  bacon.

They have noticed that time taken to prepare each of the items, and
their sub-steps is somewhat variable or uncertain. As a result, they
want to estimate the time needed to prepare a breakfast meal so that
they can better advise their guests when to arrive at the breakfast
table. The process and the steps are illustrated in {ref}`fig:three_chefs`.

:::{figure} ../Figs/the_three_chefs.png
:align: center
:width: 600
:label: fig:three_chefs

Breakfast preparation and associated distributions (prior to
normalization). Here $U(a,b)$ denotes the uniforma distribution across
the interval $[a,b]$.

:::

Initially, they model the time taken for each of the steps using
uniform distributions as indicated in the figure, where the time unit
is minutes.

Let $T_{\text{toast}}$ denote the random variable capturing the total
time taken to prepare the toast. Then $T_{\text{toast}} = T_{B_1} +
T_{B_2}$ with random variables $T_{B_1} \sim U(3,6)$ and $T_{B_2} \sim
U(3,6)$. And yes, $B$ takes great care buttering the toast. A meal is
ready only when all three items have been prepared.

For the purpose of this problem, however, we replace each of the
distributions for the $A_i$ steps by $U(0,1).$ Similarly, we replace
the distributions for the $B_i$ steps by $U(0,3/2)$, and the
distribution for the $C_1$ step by $U(0,3)$. We do not debate the
modeling bacon cooking times as short as 0 minutes.

__(a)__ With the above assumptions on distributions, what is the expected
time, the minimal time, and the maximal time for preparing each of the
three items?

__(b)__ Write down a (stochastic) model for the time $T$ needed to prepare
a single, complete breakfast meal in terms of the expressions for
$T_{\text{egg}}$, $T_{\text{toast}}$ and $T_{\text{bacon}}$.

__(c)__ In Python, Excel, XLRisk, or any tool of your choice, construct $n
= 5000$ simulation instances for your model for $T$. For each instance
also record $T_{\text{egg}}$, $T_{\text{toast}}$ and
$T_{\text{bacon}}$.  Estimate the expected total time $T$, and provide
a $1-\alpha$ confidence interval for $\alpha=0.05$. Construct a
histogram across $[0,3]$ using 250 bins of equal width and comment on
its shape.

__(d)__ For a particular simulation instance, we call the path that took
the longest to complete the _critical path_ of that instance. Based on
the sample you generated in (c) which of the paths $A$, $B$ and $C$ is
most likely to be the critical path? Formalize this by introducing the
random variable $\mathcal{C}$ that assigns 1 to sample points for
which $C$ is the critical path, 2 to sample points for which $B$ is
the critical path, and 3 to sample points for which $A$ is the
critical path. Estimate and visualize the PMF (probability mass
function) of $\mathcal{C}$.

__(e)__ For question (d), could you have determined this without
simulation? Specifically, could you have determined the order of
$p_{\mathcal{C}}(1)$, $p_{\mathcal{C}}(2)$, and $p_{\mathcal{C}}(3)$
without simulation? Explain. Here $p_{\mathcal{C}}$ denotes the PMF of
$\mathcal{C}$.

__(f)__ In case you answered "yes" in problem (e) consider this follow-up
problem. The customer is on the Atkins diet and tells the cooks to
hold the toast. Considering the model adapted from $T$ by omitting
$T_{\text{toast}}$, which of the two remaining paths, $A$ and $C$, is
most likely to be the critical path? Does your reasoning from (e) hold
water?

__(g)__ Challenge: determine the probabilities $\Pr(A)$, $\Pr(B)$ and
$\Pr(C)$ of the corresponding paths $A$, $B$ and $C$ being the
critical path using an analytic argument using the joint distribution
of the six random variables involved.
