(sec:intro_warmup)=
# Preview, prerequisites, preparation, pronto!  #

Do you already know modeling and simulation? Do you have the required
prerequisites for this book? We will work through a few problems to
see where things stand. If you have already tackled very similar
problems and feel confident, feel free to skip. If not, we recommend
that you break out your pen, paper, and computer. Give it a good
effort. Hold off on using Copilot, ChatGPT, and similar tools for
now. We are not trying to assess those tools!


(sec:intro_breakdown)=
## System Breakdown ##

```{exercise}
:label: ex:breakdown1
:enumerator: (System breakdown - part 1)

__Description__: a mechanical system $S$ accumulates fatigue over
time. If the accumulated level of fatigue exceeds a specified
threshold the
system will experience a critical failure. A basic model of this
system is as follows.

- The system is deployed in year 0 with with no built up fatigue.

- For year $k$, the added fatigue is modeled by a random variable $X_k
  \sim U(0,1)$. We assume that the random variables $X_1$, $X_2$,
  $\ldots$ are independent.

- If the cumulative fatigue exceeds $\tau = 1$, the system fails.


__Question 1a:__ Determine the expected time to failure using
simulation. Seeing the numerical estimate, can you hypothesize the exact
value for the expected time to failure?

__Comment:__ Before tackling __(1a)__ you will need to carefully write
down a formal model $M$ capturing how the system evolves. You will
have to introduce the required variables, parameters, preferably using
standard notation.

__Question 1b:__ Determine the expected time to failure
analytically. Does it match your hypothesis from __(1a)__?

```


::::::{solution} ex:breakdown1
:label: sol_breakdown1
:hidden: false

:::::{tip} __1a__ Simulation approach
:class:dropdown

Define $Y_n = \sum_{i=1}^n X_i$ where there $X_i$'s are IID $U(0,1)$
random variables and $N = \min_n Y_n \ge \tau = 1$. We want to
determine $\mathbb{E}[N]$, the expected number of years until
failure. The following Python code is a standard use of the __Monte
Carlo method__. It is a basic code and uses $n=100000$ samples and is
based on Python's default random number generator.

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

def SampleX() :
    n = 0
    sum = 0.0
    while True :
        sum += uniform.rvs()
        n+=1
        if sum >= 1.0 :
            break
    return n

print(np.average( [SampleX() for i in range(nSamples)] ) )
```
::::

For the particular instance, we got the estimate $\frac{1}{n}
\sum_{i=1}^n x_i = 2.71899$. Since no random number seed was provided,
Python will pick one for you at at random. Because of this, you will
get a different estimate every time you run this code. We have a small
hunch that the exact answer may be $e$, the base of the natural
logarithms.

If you used a small sample size (e.g., 10), you may get a very
different answer. It is natural to ask how sample size influences
one's estimate. We adapt the code above to estimate the expected value
in steps of 100. That is, we estimate using 100 sample, then 200
samples, 300 samples and so. You find the updated code below.


::::{tip} Python - Estimating E[N] as a function of sample size
:class:dropdown

```{code-block} python
/bin/env python3
#

# Synopsis: Code estimating E[N] for the sum-of-uniforms breakdown
# problem as a function of sample size n.

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

nSamples=100000
step=100 # We only visualize the average for every 100 steps.

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
most notably for small values of $n$. As we will learn, as $n$ gets
large, differences will disappear (strong law of large numbers).

```
:::::



:::::{tip} __1b__ Analytic approach
:class:dropdown

To derive the answer analytically, we set

\begin{equation*}
N_x = \min \{n\ge 1 \mid \sum_{i=1}^n X_k \ge x \}
\end{equation*}

and determine $\mathbb{E}[N_1]$. For this, we use the continuous
version of total expectation theorem and condition on $X_1$ the first
random variable of the sequence:

\begin{equation*}
\mathbb{E}[N_x \mid X_1 = u] =
\begin{cases}
1,& u \ge x\\
1 + \mathbb{E}[N_{x-u}],& u < x
\end{cases}
\end{equation*}

We then have

\begin{align*}
\mathbb{E}[N_x]
&= \mathbb{E}[\mathbb{E}[N_x \mid X_1 = u]\\
&= \int_0^1 \mathbb{E}[N_x \mid X_1 = u] du \\
&= \int_0^x (1+\mathbb{E}[N_x-u]) du  + \int_x^1 1 du\\
&= 1 + \int_{0}^x \mathbb{E}[N_{x-u}] du \\
&= 1 + \int_0^x \mathbb{E}[N_\xi] d\xi\;,
\end{align*}

and, perhaps using the technique of "ocular inspection", one will see that
$\mathbb{E}[N_x] = e^x$ is a solution. If you prefer a more systematic
approach, introduce $m(x) = \mathbb{E}[N_x]$ and then differentiate
the identity above. This leads to the differential equation

\begin{equation*}
\frac{dm}{dx} = m
\end{equation*}

whose general solution is $m(x) = A e^x$. Here $A=1$ since $m(0) = 1$,
the latter following from the  equation upstairs. The sought after expectation value corresponds to $x=1$, and we get

\begin{equation*}
\mathbb{E}[N_1] = e \;,
\end{equation*}

precisely as the simulation approach indicated in the previous problem.

:::::


::::::



```{exercise}
:label: ex:breakdown2
:enumerator: (System breakdown - part 2)

After seeing the presentation of your of your analyses,
the system operator seeks to increase longevity: they  schedule
maintenance which is to take place at the beginning of each yearly cycle. Note
that no maintenance is scheduled for the beginning of year 1 (that
would conincide with deployment time). The  maintenance protocol is
as follows:

- Measure the current system fatigue $Y_k$ at the beginning of year
  $k$.

- If $Y_k$ exceeds $\tau_c$ where $\tau_c < 1$, limited maintenance
  will take place. Maintenance in year $k$, if conducted, lowers the
  accumulated fatigue by an amount captured by a random variable $R_k
  \sim U(0.1, 0.3)$. Note that accumulated system fatigue can never
  become negative.

__Question 2a:__ Give a precise mathematical model for $Y_k$.

__Question 2b:__ Using simulation, graph the expected time to failure
as a function of $\tau_c$. We denote this by $E(\tau_c)$.

__Question 2c:__ Using simulation, determine and graph the probability
$p_{\tau_c}$ that the system fails prior to $E(\tau_c)$ as a function
of $\tau_c$.

__Question 3:__ Based on your findings, would you offer any
recommendations to the system operator?

```

<!--

::::::{solution} ex:breakdown2
:label: sol_breakdown2
:hidden: false



:::::{tip} __2a__ Model with added maintenance
:class:dropdown

First, we see that $Y_1$, the accumulated fatigue at the end
of the first year, is $Y_1 = X_1$. If $Y_1 \ge 1$, then $Y_k = Y_1$ for
all $k\ge 1$, that is, the system remains in the failed state.

For year $k$, we first introduce $\tilde{Y}_k$ by the
following relation:

\begin{equation*}
\tilde{Y}_k =
\begin{cases}
Y_{k-1} + X_k,& \text{if $Y_{k-1} < \tau_c$}\\
\max \{Y_{k-1} - R_k, 0\} + X_k, & \text{if $Y_{k-1} \ge \tau_c$}
\end{cases}
\end{equation*}

Finally, we have $Y_k = \min \{1, \tilde{Y}_k\}$. Moreover, if
$\tilde{Y}_k \ge 1$, then $Y_{k'} = 1$ for all $k' \ge k$.


:::::

:::::{tip} __2b__ Simulation for $E(\tau_c)$ as a function of $\tau_c$
:class:dropdown

__2b__. We used Python to to estimate $E(\tau_c)$ as a function of
$\tau_c$ using the Monte Carlo method using $Y_k$ from __2a__. The
graph is shown in {ref}`fig:e_tau_c_100000`.



::::{tip} Python - Estimating $E(\tau_c)$ as a function of $\tau_c$ using Monte Carlo.
:class:dropdown

```{code-block} python

#!/usr/bin/env python3
#
# Synopsis: Code for the breakdown problem, part 2.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

a = 0.1
b = 0.3

def TimeToFailure(tau_c) :
    k = 1

    # Initialize k = 1
    Y_k = uniform.rvs()
    if Y_k >= 1 :
        return k

    while True :
        k += 1

        if Y_k < tau_c :
            Y_k += uniform.rvs()
            if Y_k >= 1 :
                return k
        else :
            R_k = uniform.rvs(loc=a, scale=(b-a))
            X_k = uniform.rvs()
            Y_k = max(0, Y_k - R_k) + X_k
            if Y_k >= 1.0 :
                return k

# This may take quite a while - consider reducing nSamples in the
# implementation and validation stage.
nSamples=100000
tau_range = np.arange(0.0, 1.0, 0.05)

exp_range = [ np.average( [TimeToFailure(tau) for i in range(nSamples)]) for tau in tau_range]

# Now plot the evolution:
fig, ax = plt.subplots(1, 1)
ax.plot(tau_range, exp_range, 'b-', lw=1, alpha=0.6, label=r'$E(\tau_c)$')
ax.legend(loc='best', frameon=False)
plt.xlabel(r'$\tau_c$')
plt.savefig(f'system-breakdown-tau_c-{nSamples}.svg')
plt.show()

```
::::


```{figure} system-breakdown-tau_c-100000-labeled.svg
:width: 600
:label: fig:e_tau_c_100000

The expected time to failure $E(\tau_c)$ as a function of $\tau_c$
estimated using a Monte Carlo approach (part __2b__).

```


:::::

:::::{tip} __2c__ Probability of failure prior to $E(\tau_c)$ as a function of $\tau_c$
:class:dropdown

Here we use the saved data from part __2b__ for the estimated time to
failure as a function of $\tau_c$. The approach uses the Monte Carlo
method for each increment of $\tau_c$ applied to an indicator random
variable measuring whether failure happened prior to the expected
time. The estimates are shown in
{ref}`fig:prob_failure_prior_exp_10000`. Can you explain the sharp
transition that seems to take place at $\tau_c$ close to $0.6$?


::::{tip} Python - Estimating $E(\tau_c)$ as a function of $\tau_c$ using Monte Carlo.
:class:dropdown

```{code-block} python
#!/usr/bin/env python3
#
# Synopsis: Code for the breakdown problem, part 2c. This is about
# estimating the probability that the system breaks down prior the
# expected time to failure. Here we have used the output from the
# previous code to get the range for tau and the corresponding
# expected value.
#

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import uniform

mpl.rcParams['text.usetex'] = True
# mpl.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

a = 0.1
b = 0.3

def TimeToFailure(tau_c) :
    k = 1

    # Initialize k = 1
    Y_k = uniform.rvs()
    if Y_k >= 1 :
        return k

    while True :
        k += 1

        if Y_k < tau_c :
            Y_k += uniform.rvs()
            if Y_k >= 1 :
#                print("a")
                return k
        else :
            R_k = uniform.rvs(loc=a, scale=(b-a))
            X_k = uniform.rvs()
            Y_k = max(0, Y_k - R_k) + X_k
            if Y_k >= 1.0 :
#                print("b")
                return k

# nSamples=100000
# tau_range = np.arange(0.0, 1.0, 0.05)
# exp_range = [ np.average( [TimeToFailure(tau) for i in range(nSamples)]) for tau in tau_range]

# Saved from previous Python code for 2b using nSamples = 100000

tau_range = [ 0., 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
              0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]

exp_range = [3.50089, 3.50116, 3.48066, 3.45451, 3.40618, 3.37466,
             3.3197, 3.27293, 3.21661, 3.17628, 3.11639, 3.0729,
             3.02904, 2.98762 , 2.9485, 2.89767, 2.8611, 2.81905,
             2.78328, 2.74615]

pairs = zip(tau_range, exp_range)

nSamples=10000
indicator_prob = [ np.average( [0.0 if TimeToFailure(v[0]) < v[1] else 1.0
                                for i in range(nSamples)]) for v in pairs]

# Now plot the estimated probability as a function of tau_c
fig, ax = plt.subplots(1, 1)
ax.plot(tau_range, indicator_prob, 'b-', lw=1, alpha=0.6)
plt.title(r'Probability of failure prior to expected failure time as a function of $\tau_c$')
plt.xlabel(r'$\tau_c$')
plt.savefig('system-breakdown-2c.svg')
plt.show()


```
::::

```{figure} system-breakdown-2c-final.svg
:width: 600
:label: fig:prob_failure_prior_exp_10000

The probability that the system with the repair policy in part 2
breaks down prior to its expected time to failure $E(\tau_c)$ as a
function of $\tau_c$. The graph was constructed using a Monte Carlo
approach based on the (Monte Carlo) estimates for $E(\tau_c)$ from
part __2b__.

```
:::::

:::::{tip} __3__ Potential recommendations
:class:dropdown

With the given maintenance parameters ($a=0.1$ and $b=0.3$) and $R_k
\sim U(a,b)$, the annual fatigue overwhelms the partial repair of the
system. Can the maintenance be modified to increase $a$ and $b$?
Back-of-the-envelope estimates makes it plausible that
$\mathbb{E}[R_k]$ should be comparable to $\mathbb{E}[U(0,1)] = 1/2$
to avoid the rapid breakdown observed here. You may want to test this
conjecture.

:::::

::::::

-->


```{exercise}
:label: ex:breakdown3
:enumerator: (System breakdown - closing comments)


__Comments on modeling:__ Why use $U(0,1)$ for the yearly fatigue and
not $U(0,a)$ for some $a \in \mathbb{R}$? Because we are considering a
__scaled version__ of the problem. And that is why $\tau$ equals $1$
and not some quantity $\tau_{\text{critical}}$. For mathematical
modeling, re-scaling the original model like this is par for the
course and an established practice.

__Comments on analytic solution versus simulation:__ Did you manage to
find the analytic solution in 1a? If so, very good! However, we think
you would agree that extending the analytic
solution to incorporate the maintenance plan would be hard. And even if you somehow
managed (we would be very impressed), it is plain obvious that most
non-trivial models must be approached through simulation and
computational methods.

__Use of analytic results:__
For some models like the one in part __1__, one can derive analytic
solutions for the quantities of interest. In practice, that is
relatively rare, and one will need to use techniques such as
simulation in conjuction with the Monte Carlo method. However, the
insight we got from __1b__ is still helpful. From this, we know what
to expect at a parameter border cases (i.e., $\tau_c = 1$). This can
help with verification of the simulation model.


__Broader application context__: This kind of buildup can arise in
many systems. You can look up topics such as stochastic threshold
systems, trigger phenomena, and cascading failures.

```

