
(sec:intro_chefs)=
# The Three Chefs #

(This problem is inspired by an exercise from {cite}`Banks:14`.)

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
normalization). Here $U(a,b)$ denotes the uniform distribution across
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
merit of modeling bacon cooking times as short as 0 minutes (nor
eating under-cooked bacon); this re-scaling will make the following
computations more pleasant.

__(a)__ With the above assumptions on distributions, what is the
expected time, the minimal time, and the maximal time for preparing
each of the three items?

__(b)__ Write down a (stochastic) model for the time $T$ needed to prepare
a single, complete breakfast meal in terms of the expressions for
$T_{\text{egg}}$, $T_{\text{toast}}$ and $T_{\text{bacon}}$.

<!--
__(c)__ In your tool of choice (e.g., Python, Excel, XLRisk), construct $n
= 5000$ simulation instances for your model for $T$. For each instance
you will also want to record $T_{\text{egg}}$, $T_{\text{toast}}$ and
$T_{\text{bacon}}$.  Estimate the expected total time $T$, and provide
a $1-\alpha$ confidence interval for $\alpha=0.05$. Construct a
histogram across $[0,3]$ using 250 bins of equal width and comment on
its shape.
-->

__(c)__ For a particular simulation instance, we call the path that
took the longest to complete the __critical path__ for that
instance. Which of the paths $A$, $B$ and $C$ is most likely to be the
critical path? Solve using simulation.

Introduce the random variable $\mathcal{C}$ that assigns 1 to outcomes
where $C$ is the critical path, 2 to those where $B$ is the critical
path, and 3 to those for which $A$ is the critical path. Estimate and
visualize the probability mass function (PMF) of $\mathcal{C}$,
written $p_{\mathcal{C}}$.

__(d)__ For question (c), can you solve the question analytically?  In
other words can you determine the order of $p_{\mathcal{C}}(1)$,
$p_{\mathcal{C}}(2)$, and $p_{\mathcal{C}}(3)$ without simulation?
Explain.

__(e)__ In case you answered "yes" in problem (d) consider this
follow-up problem. The customer is on the Atkins diet and tells the
cooks to skip the toast. Considering the model adapted from $T$ by
omitting the tast component $T_{\text{toast}}$, which of the two
remaining paths, $A$ and $C$, is most likely to be the critical path?
Does your analytic argument from (d) actually work?

<!--
__(g)__ Challenge: determine the probabilities $\Pr(A)$, $\Pr(B)$ and
$\Pr(C)$ of the corresponding paths $A$, $B$ and $C$ being the
critical path using an analytic argument via the joint distribution
of the six random variables involved.
-->

::::{tip} Solution
:asdf-class:dropdown

__(a)__ The minimal and maximal times are $t_{\min} = 0$ and $t_{\max}
= 3$ across all paths. The expected time is 3/2 across all paths. You
show this using linearity of expectation and basic properties of the
uniform distribution.

__(b)__ Here we have
\begin{align*}
  T_{\text{egg}} &= T_{A_1} + T_{A_2} + T_{A_3} \\
  T_{\text{toast}} &= T_{B_1} + T_{B_2} \\
  T_{\text{bacon}} &= T_{C_1}
\end{align*}

where the random variables appearing on the right have the uniform
distributions as shown in the figure, but with modified parameters as
per the text. The time $T$ is given by

\begin{equation}
 T = \max \{ T_{\text{egg}}, T_{\text{toast}}, T_{\text{bacon}} \} \;.
\end{equation}


__(c)__ From simulation, it appears that bacon is the critical path,
followed by toast, and then egg. Using $n=10000$ sample points, we
arrived at {ref}`tab:breakfast`, and using $n=50000$ sample points, we
got the normalized histogram visualized in
{ref}`fig:fe-9f`. Simulations clearly indicate that path $C$, bacon,
is the critical path among the three candidates.

```{raw} latex
\begin{table}[ht]
\centerline{
\begin{tabular}{l|rrr}
\hline
Path & Eggs & Toast & Bacon \\
\hline
Count & 2884 & 3192 & 3924 \\
Frequency & 0.288 & 0.319 & 0.392\\
\hline
\end{tabular}
}
\caption{Frequency statistics for the three paths.}
\label{tab:breakfast}
\end{table}
```

:::{figure} figs/fe-9f.png
:align: center
:width: 600
:label: fig:fe-9f

The three chefs: statistics by path/number of random variables in
sum. Here '1' indicates the bacon path, '2' indicates the toast path,
and '3' indicates the egg path. The histogram is the estimate for the PMF
$p_{\mathcal{C}}$.

:::

__(d)__

Can one arrive at the conclusion from the simulation-based estimate of
$p_{\mathcal{D}}$ using intuition? Perhaps, but that would be quite
impressive. An example of misguided reasoning is as follows: compare
the egg path, which is a sum of three $U(0,1)$ random variables and
the bacon path, which is just a $U(0,3)$ random variable.  One might
argue that to have a large, positive deviation from the mean in the
former case, all three $U(0,1)$ random variables need to deviate
positively from their mean. For these three ''dials'' to all align in
this manner is less likely than for the single dial in the case of
bacon (path $C$). "Ergo", path $C$ is more likely than path $1$ to be
the critical path. The same "reasoning" applies when comparing the
toast and bacon paths. This is all good except that the reasoning is
flawed.

We are asked to estimate the probability:

\begin{equation}
\label{eq:p}
\Pr( T_{C_1} \ge T_{B_1} + T_{B_2} \text{ AND } T_{C_1} \ge T_{A_1} + T_{A_2} + T_{A_3})\;,
\end{equation}

How do you estimate that? You integrate the joint probability density
function of the six random variables above across the region $R$ which
is the subset of the six-dimensional space $[0,1]^3 \times [0, 3/2]^2
\times [0,3]$ given by

\begin{equation*}
T_{C_1} \ge T_{B_1} + T_{B_2} \text{ AND } T_{C_1} \ge T_{A_1} + T_{A_2} + T_{A_3}\;
\end{equation*}

which we view as an __event__ $E$. Since we assume that all the random
variables involved in the cooking are independent, the joint PDF is

\begin{equation*}
f(x_1, x_2, x_3, y_1, y_2, z) = 1/ \bigl( 1^3 (3/2)^2 3\bigr) = {4\over27} \;,
\end{equation*}

and the probability of the event $E$ is thus
\begin{equation}
\label{eq:cp_prob}
\Pr(E) = \int \int \!\!\!\!\int\limits_R\!\!\!\! \int \int \int {4\over 27} dx_1 dx_2 dx_3 dy_1 dy_2 dz
\end{equation}

which is surprisingly resistant to evaluation, the challenge being the specification of $R$.

__(e)__
It turns out to be much easier when we only compare pairs of paths. To
see this, consider the comparisons of paths $B$ and $C$. Here we want

\begin{equation}
\label{eq:pcb}
\Pr( T_{C_1} \ge T_{B_1} + T_{B_2})\;,
\end{equation}

and since the joint probability of the three random variables involved
is $f(y_1, y_2, z) = 1/\bigl( (3/2)^2 3\bigr) = 4/27$ we obtain

\begin{align*}
  \Pr( Y \ge Y_1 + Y_2 )
  &= \int_0^{3/2}\int_{0}^{3/2}\int_{y_1 + y_2}^3 f(y_1, y_2, z)\, dz\, dy_2\,dy_1\\
  &= \frac{4}{27} \int_0^{3/2}\int_{0}^{3/2} (3-y_1 - y_2) \, dy_2\,dy_1\\
  &= \frac{4}{27} \int_0^{3/2} [ (3-y_1)y_2 - \frac{1}{2} y_2^2]_0^{3/2} \,dy_1\\
  &= \frac{4}{27} \int_0^{3/2} (3-y_1)(3/2) -  9/8 \,dy_1\\
  &= \frac{4}{27} \int_0^{3/2} \frac{27}{8} - \frac{3}{2} y_1 \,dy_1\\
  &= \frac{4}{27}(\frac{27}{8}\frac{3}{2} - \frac{3}{4} \frac{9}{4}) = \frac{1}{4} ( 3 - 1 )
  = \frac{1}{2} \;.
\end{align*}

In other words, paths $B$ and $C$ are equally likely to be the
critical paths. One can show that the same holds for the other
pairwise comparisons. This shows that the "intuitive" argument earlier
is flawed. We have not found a good way to evaluate {ref}`eq:cp_prob` -
if you have a good solution we are eager to see it!

<!--
\begin{equation}
\label{eq:pca}
\Pr( T_{C_1} \ge T_{A_1} + T_{A_2} + T_{A_3})  \;,
\end{equation}

\begin{equation}
\label{eq:pcab}
\Pr(T_{A_1} + T_{A_2} + T_{A_3} \ge  T_{B_1} + T_{B_2} )  \;,
\end{equation}
To carry out this analysis, we first rescale and normalize,
letting~$T_{\text{egg}} = X_1 + X_2 + X_3$ where~$X_i \sim U(0,1)$, $T_{\text{toast}}
= Y_1 + Y_2$ where $Y_i \sim U(0,3/2)$, and $T_\bacon = Z$ where~$Z
\sim U(0,3)$. To tackle~\eqref{eq:pcb} we note that the joint PDF of
$Y_1$, $Y_2$ and $Z$ is $f(y_1, y_2, z) = 1/\bigl( (3/2)^2 3\bigr) = 4/27$
and that
\begin{align*}
  \Pr( Y \ge Y_1 + Y_2 )
  &= \int_0^{3/2}\int_{0}^{3/2}\int_{y_1 + y_2}^3 f(y_1, y_2, z)\, dz\, dy_2\,dy_1\\
  &= \frac{4}{27} \int_0^{3/2}\int_{0}^{3/2} (3-y_1 - y_2) \, dy_2\,dy_1\\
  &= \frac{4}{27} \int_0^{3/2} [ (3-y_1)y_2 - \frac{1}{2} y_2^2]_0^{3/2} \,dy_1\\
  &= \frac{4}{27} \int_0^{3/2} (3-y_1)(3/2) -  9/8 \,dy_1\\
  &= \frac{4}{27} \int_0^{3/2} \frac{27}{8} - \frac{3}{2} y_1 \,dy_1\\
  &= \frac{4}{27}(\frac{27}{8}\frac{3}{2} - \frac{3}{4} \frac{9}{4}) = \frac{1}{4} ( 3 - 1 )
  = \frac{1}{2} \;.
\end{align*}
One can compute $\Pr( Y \ge X_1 + X_2 + X_3 )$ in precisely the same
manner, albeit now with one more dimension to the integral, to obtain
the same answer of~$1/2$.

The situation with~\eqref{eq:pcab} is almost the same where
\begin{equation*}
  \Pr(X_1 + X_2 + X_3 \ge  Y_1 + Y_2 )
  = \int_{0}^{1}\int_{0}^{1}\int_{0}^{1} \int_0^{3/2}\int_{0}^{3/2}\int_{0}^{x_1+x_2+x_3-y_1}
     \frac{4}{9}\, dy_2\, dy_1\,dx_3\,dx_2\,dx_1 \;,
\end{equation*}
which also simplifies to $\frac{1}{2}$.

Thus any "intuition" involving a pair of random variables
from~$\{T_\bacon, T_{\text{egg}}, T_\toast\}$ appearing in their sums will
likely be misguided.

The question is therefore: how does one explain the non-uniformity in
Figure {ref}`fig:fe-9f` and the frequencies in
Table {ref}`tab:breakfast`? We are not aware of any solution that plays
to intuition, which, one may argue, makes a solid case for simulation.

To provide an analytic answer we can proceed as above using the joint
probability density function of $X_1$, $X_2$, $X_3$, $Y_1$, $Y_2$ and
$Z$ which is
\begin{equation}
  f(x_1, x_2, x_3, y_1, y_2, z)
  = \frac{1}{1^3 (3/2)^2 3} = \frac{4}{27} \;.
\end{equation}
Here the sample space is $\Omega = [0,1]^3 \times [0,3/2]^2 \times
[0,3]$. We first consider
\begin{equation}
p_1 = \Pr(Z \ge X_1 + X_2 + X_3 \quad\text{and}\quad Z \ge Y_1 + Y_2) \;,
\end{equation}
the probability that the ``modified bacon path'' is the critical
path. We consider the subregions $\Omega_1, \Omega_2 \subset \Omega$ where
\begin{equation}
  \Omega_1 = \{ \omega \in \Omega | X_1 + X_2 + X_3 \ge Y_1 + Y_2  \}\quad\text{and}\quad
  \Omega_2 = \Omega \setminus \Omega_1\;.
\end{equation}
Furthermore, we set
%%
$\Omega_1' = \{\omega \in \Omega_1 | z \ge x_1 + x_2 + x_3 \}$
and
%%
$\Omega_2' = \{\omega \in \Omega_2 | z \ge y_1 + y_2 \}$
and can now express determine $p_1$ as:
\begin{align*}
  p_1
  &= \int_{\Omega_1'} \frac{4}{27} d\omega + \int_{\Omega_2'} \frac{4}{27} d\omega\\
  &= \int_0^1 \int_0^1 \int_0^1 \int_0^{3/2} \int_0^{x_1+x_2+x_3 - y_1} \int_{x_1+x_2+x_3}^{3}
  \frac{4}{27} \, dz\, dy_2\, dy_1\, dx_3\, dx_2\, dx_1 \\
  &\phantom{=} +
   \int_0^1 \int_0^1 \int_0^1 \int_0^{3/2} \int_{x_1+x_2+x_3 - y_1}^{3/2} \int_{y_1+y_2}^{3}
         \frac{4}{27} \, dz\, dy_2\, dy_1\, dx_3\, dx_2\, dx_1
\end{align*}
After tedious calculations, one obtains $p_1 = \frac{7}{18}$ which is
approximately $0.389$ which is quite close to the estimated value of
$0.392$ in Table~\ref{tab:breakfast}.


How about the toast path being the critical path? We are now looking at
\begin{equation*}
p_2 = \Pr(Y_1 + Y_2 \ge X_1 + X_2 + X_3 \quad\text{and}\quad Y_1 + Y_2
\ge Z) \;.
\end{equation*}
Define subregions $\Omega_1^2, \Omega_2^2 \subset \Omega$ where
\begin{equation}
  \Omega_1^2 = \{ \omega \in \Omega | X_1 + X_2 + X_3 \ge Z  \}\quad\text{and}\quad
  \Omega_2^2 = \Omega \setminus \Omega_1^2\;.
\end{equation}
As above, we set
%%
${\Omega_1^2}' = \{\omega \in \Omega_1^2 | y_1 + y_2 \ge x_1 + x_2 + x_3 \}$
and
%%
${\Omega_2^2}' = \{\omega \in \Omega_2 | y_1 + y_2 \ge z \}$
and can now determine $p_2$ as:
\begin{align*}
  p_2
  &= \int_{{\Omega_1^2}'} \frac{4}{27} d\omega + \int_{{\Omega_2^2}'} \frac{4}{27} d\omega\\
  &= \int_0^1 \int_0^1 \int_0^1 \int_0^{3/2} \int_{x_1+x_2+x_3 - y_1}^{3/2} \int_0^{x_1+x_2+x_3}
  \frac{4}{27} \, dz\, dy_2\, dy_1\, dx_3\, dx_2\, dx_1 \\
  &\phantom{=} +
   \int_0^1 \int_0^1 \int_0^1 \int_0^{3/2} \int_{0}^{3/2} \int_{x_1+x_2+x_3}^{y_1+y_2}
         \frac{4}{27} \, dz\, dy_2\, dy_1\, dx_3\, dx_2\, dx_1
\end{align*}

While we could determine $p_3$ from $p_3 = 1 - p_1 - p_2$, we will do
this the hard way.  We are now looking at
\begin{equation*}
p_2 = \Pr( X_1 + X_2 + X_3 \ge Y_1 + Y_2 \quad\text{and}\quad X_1 +
X_2 + X_3 \ge Z) \;.
\end{equation*}
Define subregions $\Omega_1^3, \Omega_2^3 \subset \Omega$ where
\begin{equation}
  \Omega_1^3 = \{ \omega \in \Omega | Y_1 + Y_2 \ge Z  \}\quad\text{and}\quad
  \Omega_2^3 = \Omega \setminus \Omega_1^3\;.
\end{equation}
As above, we introduce
%%
${\Omega_1^3}' = \{\omega \in \Omega_1^3 | x_1 + x_2 + x_3 \ge y_1 + y_2  \}$
and
%%
${\Omega_2^3}' = \{\omega \in \Omega_2^3 | x_1 + x_2 + x_3 \ge z \}$
and can now determine $p_3$ as:
\begin{align*}
  p_3
  &= \int_{{\Omega_1^3}'} \frac{4}{27} d\omega + \int_{{\Omega_2^3}'} \frac{4}{27} d\omega\\
  &= \int_0^1 \int_0^1 \int_0^1 \int_0^{3/2} \int_{0}^{x_1+x_2+x_3 - y_1} \int_0^{y_1+y_2}
  \frac{4}{27} \, dz\, dy_2\, dy_1\, dx_3\, dx_2\, dx_1 \\
  &\phantom{=} +
   \int_0^1 \int_0^1 \int_0^1 \int_0^{3/2} \int_{0}^{3/2} \int_{y_1+y_2}^{x_1+x_2+x_3}
         \frac{4}{27} \, dz\, dy_2\, dy_1\, dx_3\, dx_2\, dx_1
\end{align*}

-->
