
(sec:intro_warmup)=
# Preview, prerequisites, and preparation  #

Do you already know modeling and simulation? Do you have the required
prerequisites for this book? Give the following problems a try to see
where you stand. If you have already tackled very similar problems and
feel confident, feel free to skip. If not, we recommend that you break
out your pen, paper, and computer. Give them a good effort. Do not use
Copilot, ChatGPT, or similar tools. That would be utterly pointless.

(sec:intro_breakdown)=
## System Breakdown ##

```{exercise}
:label: ex:breakdown
:enumerator: System breakdown!

__Description__: we have a mechanical system $S$ where fatigue
accumulates over time. If the accumulated level of fatigue exceeds a
threshold the system will experience a critical failure. A basic model
of this system is as follows.

- The system is deployed in year 0 with with no built up fatigue.

- For year $k$, the added fatigue is modeled by a random variable $X_k
  \sim U(0,1)$. We assume that the random variables $X_1$, $X_2$,
  $\ldots$ are independent.

- If the cumulative fatigue exceeds $\tau = 1$, the system fails.


__Question 1a:__ Determine the expected time to failure through
simulation. Seeing the numerical estimate, hypothesize what the exact
value is.

__Question 1b:__ Determine the expected time to failure
analytically. Does it match your hypothesis from 1a?


The system operator seeks to increase longevity, and schedules
maintenance taking place at the beginning of each yearly cycle. Note
that no maintenance is scheduled for the beginning of year 1 since the
system is then just put into operation. Their maintenance protocol is
as follows:

- Measure the current system fatigue $Y$.

- If $Y$ exceeds $\tau_c$ where $\tau_c < 1$, limited maintenance will
  take place. Maintenance in year $k$, if conducted, lowers the
  accumulated fatigue by an amount captured by a random variable $R_k
  \sim U(0.1, 0.3)$. Of course, system fatigue can never become
  negative.

__Question 2a:__ Using simulation, graph the expected time to failure
as a function of $\tau_0$. We denote this by $E(\tau_0)$.

__Question 2b:__ Using simulation, determine and graph the probability
$p_{\tau_0}$ that the system fails prior to $E(\tau_0)$ as a function
of $\tau_0$.

__Question 3:__ Based on your findings, would you offer any
recommendations to the system operator?

__Comments on modeling:__ Why use $U(0,1)$ for the yearly fatigue and
not $U(0,a)$ for some $a \in \mathbb{R}$? Because we are considering a
__scaled version__ of the problem. And that is why $\tau$ equals $1$
and not some quantity $\tau_{\text{critical}}$. For mathematical
modeling, re-scaling the original model like this is par for the
course and an established practice.

__Broader application context__: This kind of buildup can arise in
many systems. You can look up topics such as stochastic threshold
systems, trigger phenomena, and cascade failures.
```

:::::{solution} ex:breakdown
:class:dropdown
:label: sol_breakdown
:hidden: false

1a. Define $Y_n = \sum_{i=1}^n X_i$ where there $X_i$'s are IID -
$U(0,1)$ and $N = \min_n Y_n \ge \tau = 1$. We want to determine
$\mathbb{E}[N]$, the expected number of years until failure. The
following Python code is a standard use of the __Monte Carlo method__, and
the Python code below is a basic way to execute this using
$n=100000$ samples.

::::{tip} Python - Estimating E[N] for the breakdown problem
:class:dropdown

```{code-block} python
#!/usr/bin/env python3
#
# Synopsis: Code estimating E[N] for the sum-of-uniforms breakdown
#   problem

import numpy as np
from scipy.stats import uniform

nSamples=100000
sampleArray = np.zeros(nSamples)

for i in range(0, nSamples) :
    n = 0
    sum = 0.0
    while True :
        sum += uniform.rvs()
        n+=1
        if sum >= 1.0 :
            break
    sampleArray[i] = n

print(np.average(sampleArray))
```
::::

For the particular instance, we got the estimate $\frac{1}{n}
\sum_{i=1}^n x_i = 2.71899$. Since no random number seed was provided,
you will get a different estimate every time you run this code. We
have a small hunch that the exact answer may be $e$, the base of the
natural logarithms.

If you used a small sample size (e.g., 10), you may get a very
different answer. It is natural to ask how the sample size influences
one's estimate. We adapt the code above to estimate the expected value
in steps of 100. That is, we estimate using 100 sample, then 200
samples, 300 samples and so. The updated code looks like this:


::::{tip} Python - Estimating E[N] as a function of sample size
:class:dropdown

```{code-block} python

#!/usr/bin/env python3
#

# Synopsis: Code estimating E[N] for the sum-of-uniforms breakdown
# problem as a function of sample size n.

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

nSamples=100000
step=100 # We only visualize the average for every 100 steps.

sampleArray = np.zeros(nSamples)

def SampleX() :
    n = 0
    sum = 0.0
    while True :
        sum += uniform.rvs()
        n+=1
        if sum >= 1.0 :
            break
    return n

sampleArray = [SampleX() for i in range(nSamples)]

nSubSamples = int(nSamples / step)
subSampleArray = np.zeros(nSubSamples)
indexArray = np.zeros(nSubSamples)

# Create estimates as a function of number of samples in increments of 'step':

for i in range(0, nSubSamples) :
    indexArray[i] = step * (i+1)
    subSampleArray[i] = np.average( sampleArray[0:(step * (i+1))] )

# This gives the estimate:
print( subSampleArray[-1] )

# Now plot the evolution:
fig, ax = plt.subplots(1, 1)
ax.plot(indexArray, subSampleArray, 'b-', lw=1, alpha=0.6, label=r'$\hat{E}[N](n)$')
ax.legend(loc='best', frameon=False)
plt.xlabel(r'$n$')
plt.savefig('system_breakdown_n.svg')
plt.show()

```
::::

```{figure} system_breakdown_n.svg
:width: 600
:label: fig:breakdown_n

The diagram shows the estimate of $\mathbb{E}[N]$ for the system
breakdown problem as a function of the sample size $n$. Here the
estimates were constructed based on the Monte Carlo method. Note that
different seed values will generally produce quite different curves,
most notably for small values of $n$.

```


1b. Analytic solution





:::::




(sec:intro_chefs)=
## The Three Chefs ##

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

:::{tip} Solution
:class:dropdown

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

__(c)__ This problem was solved using Python.


```{code} python
import numpy as np
import matplotlib.pyplot as plt



```

For the
sample generated we have:

```{code} python
DescribeResult(
  nobs=25,
  minmax=(np.float64(8.242095828902297), np.float64(11.747219968630734)),
  mean=np.float64(10.576055816186042),
  variance=np.float64(1.0619764557044438),
  skewness=np.float64(-1.2069468524530453),
  kurtosis=np.float64(0.2615107022714347))
```

We used $n=25$ sample points giving the estimated mean preparation
time of
\begin{equation*}
\bar{T}(n) = 10.58\text{ minutes.}
\end{equation*}
We also have~$\sqrt{\hat{S}^2(n)} = 1.062$ from which we deduce that
the half-length of the confidence interval is
\begin{equation*}
 t_{(25-1),1-0.05/2} \sqrt{S^2(n)/n}
  = 2.064 \sqrt{1.062/25} = 0.43\;
\end{equation*}
with confidence interval $[10.13, 11.01]$.  The normalized histogram
is shown in Figure~\ref{fig:9f}.
\begin{figure}[ht]
\centerline{\includegraphics[width=0.6\textwidth]{fe-9-time-distribution}}
\caption{Problem 9f: distribution of preparation time using a sample
  of size~$n=50000$.}
\label{fig:9f}
\end{figure}

__(d)__




From simulation, it appears that bacon is the critical path,
followed by toast, and then egg. Using $n=10000$ sample points, we
arrived at Table~\ref{tab:breakfast}, and using $n=50000$ sample
points, we got the normalized histogram visualized in
Figure~\ref{fig:fe-9f}.

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
\caption{Statistics for the critical paths in the breakfast setup.}
\label{tab:breakfast}
\end{table}

\begin{figure}[ht]
\centerline{\includegraphics[width=0.6\textwidth]{fe-9f}}
\caption{Problem 9f: statistics by path/number of random variables in
  sum. Here '1' indicates the bacon path, '2' indicates the toast
  path, and '3' indicates the egg path. }
\label{fig:fe-9f}
\end{figure}

__(e)__

Can one arrive at the conclusion from the computational
analysis of~\pPart{e} by intuition? Perhaps, but this would be quite
impressive. A misguided reasoning may be as follows: compare the egg
path, which is a sum of three $U(2,4)$ random variables and the bacon
path, which is just a $U(6,12)$ random variable.  One might argue that
to have a large, positive deviation from the mean in the former case,
all three $U(2,4)$ random variables need to deviate positively from
their mean. For these three ''dials'' to all align in this manner is
less likely than for the single dial in the latter case. Ergo, the
bacon path is more likely than the egg path to be the critical
path. The same "reasoning" applies when comparing the toast and
bacon paths. This is all good except that the reasoning is flawed.

Let us start by estimating the probabilities
\begin{equation}
\label{eq:pcb}
\Pr( T_{C_1} \ge T_{B_1} + T_{B_2})\;,
\end{equation}
\begin{equation}
\label{eq:pca}
\Pr( T_{C_1} \ge T_{A_1} + T_{A_2} + T_{A_3})  \;,
\end{equation}

and

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
:::
