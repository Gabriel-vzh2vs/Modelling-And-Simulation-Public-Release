
(sec:distribution_modeling)=
# Distribution modeling


## Overview

We follow {cite}`Krzysztofowicz:25` in the approach for distribution
modeling. As a starting point, we will assume that we have a sample
$S$ of a one-dimensional (uni-variate) random variable $X$ whose
distribution function is $F$. The process is split into the following
steps:

- Construct the empirical distribution function $\tilde{F}$ of $X$
  using the sample $S$

- Specify the sample space $\Omega$ of $X$

- Hypothesize parametric models

- Estimate the parameters of each hypothesized model

- Evaluate the goodness of fit of each model, including statistical
  testing

- Choose the best one

We will go through each step in the upcoming. The description will be
a combination of theory and practice where we illustrate concepts
through Python code and the tool Phitter (introduced in {cite}`sec:??`).


Note that distribution modeling is a large scientific area, and that
the goal of this chapter is to establishing a workable foundation for
its theory and application in the context of modeling and simulation
science.


Text books approach this in their own ways. Should you use some of
these, here is this organization.

- {cite}`Law:13` breaks this down as three ``activities'': (1)
  hypothesizing families of distributions ($\S 6.4$), (2) estimation
  of parameters ($\S 6.5$), and (3) determining how representative the
  fitted distributions are ($\S 6.6$).
- {cite}`Banks:14` ... Indicate


## Running example

Throughout this section, we will use the sample $S$ provided in the
Python code block below (and assigned to the variable
$\text{\texttt{sample}}$).

```{code} python
sample = [
    4.875, 5.74, 10.149, 6.197, 11.357, 3.9048, 8.07, 8.055,
    7.067, 9.737, 4.3757, 6.451, 13.023, 10.513, 6.978, 3.7117, 6.919,
    11.466, 7.338, 12.409, 4.4195, 6.729, 4.2673, 14.4, 11.214, 7.777,
    19.62, 3.9662, 4.154, 5.586, 7.619, 5.009, 25.05, 15.58, 7.171,
    6.534, 4.888, 7.841, 5.192, 3.52463, 6.46, 8.074, 17.82, 6.677,
    14.22, 10.826, 7.343, 4.2477, 7.067, 3.6041, 6.675, 11.254, 6.385,
    5.32, 6.44, 9.429, 6.303, 25.78, 8.152, 14.02, 6.199, 10.185,
    7.446, 4.689, 25.74, 6.621, 7.157, 6.158, 7.01, 3.8648, 7.492,
    4.1367, 11.988, 4.4746, 4.838, 5.829, 11.613, 15.36, 5.073, 17.51,
    11.151, 9.558, 4.949, 9.332, 4.4172, 8.342, 19.47, 3.6985, 17.9,
    4.4053, 8.112, 8.617, 7.575, 3.9138, 4.4023, 5.279, 4.4784, 5.007,
    22.66, 5.847
]
```

As practice, you should construct and visualize the empirical
distribution function $\tilde{F}$ of $S$.

::::{tip} Python - Empirical distribution function for running example
:class:dropdown
```{code} python
import matplotlib.pyplot as plt
from scipy import stats

sample = [
    4.875, 5.74, 10.149, 6.197, 11.357, 3.9048, 8.07, 8.055,
    7.067, 9.737, 4.3757, 6.451, 13.023, 10.513, 6.978, 3.7117, 6.919,
    11.466, 7.338, 12.409, 4.4195, 6.729, 4.2673, 14.4, 11.214, 7.777,
    19.62, 3.9662, 4.154, 5.586, 7.619, 5.009, 25.05, 15.58, 7.171,
    6.534, 4.888, 7.841, 5.192, 3.52463, 6.46, 8.074, 17.82, 6.677,
    14.22, 10.826, 7.343, 4.2477, 7.067, 3.6041, 6.675, 11.254, 6.385,
    5.32, 6.44, 9.429, 6.303, 25.78, 8.152, 14.02, 6.199, 10.185,
    7.446, 4.689, 25.74, 6.621, 7.157, 6.158, 7.01, 3.8648, 7.492,
    4.1367, 11.988, 4.4746, 4.838, 5.829, 11.613, 15.36, 5.073, 17.51,
    11.151, 9.558, 4.949, 9.332, 4.4172, 8.342, 19.47, 3.6985, 17.9,
    4.4053, 8.112, 8.617, 7.575, 3.9138, 4.4023, 5.279, 4.4784, 5.007,
    22.66, 5.847
]

emp_dist = stats.ecdf(sample)

# Use matplotlib to visualize:
ax = plt.subplot()
emp_dist.cdf.plot(ax)

# r-strings permit LaTeX formatting. This is optional, but looks professional.
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'Empirical CDF $\tilde{F} of running example$')
plt.show()
```

Python documentation
- [scipy.ecdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ecdf.html)
::::

Using Python and matplotlib, we generated the CDF shown in
{ref}`fig:empirical_distribution_running_example`.

:::{figure} ../Figs/empirical_distribution_example_running_example.svg
:align: center
:width: 600
:label: fig:empirical_distribution_running_example
The empirical distribution function $\tilde{F}$ for the running example.
:::

## Specifying the sample space $\Omega$ of $F$

Specification of $\Omega$ will generally involve one's knowledge of
the random variable $X$ and one's assessment of the sample $S$.  For
example, barring any mistakes, the sample $S = \{x_1, x_2, \ldots,
x_n\}$ will be a proper subset of $\Omega$, that is $S \subset \Omega$. This can guide
one towards classifying $\Omega$ into on of the following four
following categories:

\begin{equation*} 1.~\Omega = (-\infty,\infty), 2.~\Omega =
(\eta,\infty), 3.~\Omega = (\eta_L, \eta_U),\text{ or } 4.~\Omega
= (-\infty,\eta)
\end{equation*}

Insights about the underlying system can further help identify which
of the cases 1 through 4 to consider.

Looking at the CDF from
{ref}`fig:empirical_distribution_running_example`, what category does
the random variable from the example belong to? It seems quite
plausible that we have $\Omega = (\eta, \infty)$, which is the second
category. Could one argue that it is $\Omega = (\eta_L, \eta_U)$?
Maybe. This is where knowledge of the system or domain can help
guide. Not having any additional information, we will take $\Omega =
(\eta, \infty)$. With this choice, does it seem plausible that $\eta =
0$? From the sample size and the figure, it does not seem very likely
that $\eta = 0$. This offers a small hint that we may have to consider
a non-zero _location parameter_.


## Hypothesizing parametric models

Having chosen a candidate for the sample space $\Omega$ of $X$ narrows
down the set of distribution candidates. Examining a table of
candidates (see e.g. $\S~6.2$ in {cite}`Law:13` or
{cite}`Krzysztofowicz:25`) will allow one to quickly hone in on the
more relevant candidates. Later, we will also show how a tool like
Phitter can help one in this regard.

Once you have gone through such tables, or perhaps used distribution
fitting tools such as Phitter, you will arrive at an even smaller set
of candidates. What can you do from here?

Knowledge of the system where the random variable lives and what it
captures can also help guide. In earlier examples, we have seen that
the Weibull distribution is often appropriate when it comes to
capturing lifetimes of machine parts. Sometimes, a log-normal
distribution may also be appropriate for this. If you are dealing with
arrival processes, then Poisson distributions and exponential
distributions naturally come to mind.

You can also inspect the shape of the empirical distribution function
$\tilde{F}$.  With practice, perhaps __a lot__ of practice, one may be
able to discern an appropriate parametric model through the shape of
the empirical distribution. It is also good practice to visualize the
data through __histograms__ (see, e.g., {cite}`Law:131). At a basic
level, you construct a histogram by partitioning the sample space
$\Omega$ into $n$ bins, and count how many samples fall into each
bin. Most common tools will do this for you, as well as giving you the
option to normalize to construct and empirical probability mass
function.

We have already examined the empirical CDF of the sample for the
running example. Let us see what histograms look like. In
{ref}`fig:histogram_5_running_example` through
{ref}`fig:histogram_30_running_example` we have shown (raw) histograms
and normalized versions for $n\in\{5,10,15,20,30\}$.

<!-- https://sphinx-subfigure.readthedocs.io/en/latest/ -->

:::{figure} ../Figs/histogram_n_5_example_running_example.svg
:align: center
:width: 600
:label: fig:histogram_5_running_example
A histogram for the running example with $n=5$ bins.
:::
:::{figure} ../Figs/histogram_n_10_example_running_example.svg
:align: center
:width: 600
:label: fig:histogram_10_running_example
A histogram for the running example with $n=10$ bins.
:::
:::{figure} ../Figs/histogram_n_15_example_running_example.svg
:align: center
:width: 600
:label: fig:histogram_15_running_example
A histogram for the running example with $n=15$ bins.
:::
:::{figure} ../Figs/histogram_n_20_example_running_example.svg
:align: center
:width: 600
:label: fig:histogram_20_running_example
A histogram for the running example with $n=20$ bins.
:::
:::{figure} ../Figs/histogram_n_30_example_running_example.svg
:align: center
:width: 600
:label: fig:histogram_30_running_example
A histogram for the running example with $n=30$ bins.
:::

Inspecting these figures, you will see bin counts matter. Although it
was not illustrated here, the choice of bin (divider) points can also
make a difference. As mentioned before, it is healthy to exercise
caution regarding histograms where you scan some a range of values,
and possibly also shift the bin range around. Histograms are not bad,
nor is taking the time to stare at the data.

We note that there are other types of summary statistics and quantile
maps (see, e.g., {cite}`Law:13` $\S~6.4.1$ and $\S~6.4.3$).


### Distribution parameters

In the business of distirbution modeling it is common to split
parameters into the following categories:

- __location parameters__; (e.g., $\mu$ for the normal distribution)

- __scale parameters__; (e.g., $\sigma$ for the normal distribution)

- __shape parameters__ (also called form parameters); (e.g., $\alpha$
  and $\beta$ for the beta distribution)

- __shift parameters__

While these are certainly reflected in the cumulative distribution
function, they may be more easily discerned for the matching
probability density functions.

We will hypothesize distributions for the running example in
{ref}`sec:distribution_modeling_phitter`.


(sec:estimating_parameters)=
## Estimating the parameters of a hypothesized model

We have now reached the point where we have one or more hypothesized
candidate distributions, and where we need to estimate their
parameters.  For this there are various techniques such as __Maximum
Likelihood Estimators__ (MLEs), Least-Squares (LS) estimators, as well
as others.  While each variant has its merits we will not go into
those here, but you can read more in {cite}`Law:13` ($\S~6.5$) and
{cite}`Krzysztofowicz:25` (Appendix B). Here we will focus on the
__MLE__.

Scanning the table in $\S~6.2$ of {cite}`Law:13`, you will find that
almost all entries has their MLE(s) listed. For example, in the case
of a uniform distribution $U(a,b)$, the MLE for $a$ and $b$ are

\begin{equation*}
\hat{a} = \min_{1\le i \le n} X_i
\quad\text{ and }\quad
\hat{b} = \max_{1\le i \le n} X_i \;.
\end{equation*}

As before, we are working with a sample

\begin{equation*}
S = \{x_1, x_2, \ldots, x_n \}\;.
\end{equation*}

For a single-parameter, univariate continous distribution with
probability density function $f_\theta(x)$ with parameter $\theta$ we
form the __likelihood function__
\begin{equation}
\label{eq:likelihoodfunction}
L(\theta) = f_\theta(x_1) f_\theta(x_n)  \cdots f_\theta(x_n)  \;.
\end{equation}
The MLE $\hat{\theta}$ of $\theta$ is the value of $\theta$ that
maximizes $L$ in~\eqref{eq:likelihoodfunction} over the range of
permissible values $\theta$.
%%
In practice, it will often be easier to determine the value $\theta$
that maximizes $\ln [L(\theta)] = \sum_{i=1}^n \log f_\theta(x_i)$, an
approach that holds since the natural logarithm function is strictly
increasing.

\textbf{Example:} We illustrate the MLE for the exponential
distribution which has density function $f(x) = e^{-x/\beta}\bigl /
\beta$ for $x\ge 0$ and $f(x) = 0$ otherwise.
Here, writing $s = \sum_i x_i$, we have
\begin{equation}
\ell(\theta) = \ln L(\theta) = -s/\beta - n \ln \beta
\end{equation}
with derivative
\begin{equation}
\frac{d\ell}{d\theta} = -n/\beta + s/\beta^2
\end{equation}
which equals $0$ for $\hat\theta = s/n = \frac{1}{n} \sum_{i=1}^n
x_i$. Here you should verify that $\frac{d^2\ell}{d\theta^2}$ is
negative at $\theta = \hat\theta$.

The process above becomes more complicated for distributions with more
than one parameter. The approach, however, is exactly the same when
forming $L(\bm{\theta)} = (\theta_1, \theta_2, \ldots, \theta_k))$ and
the corresponding log-likelihood function $\ln L(\bm{\theta})$.

\textbf{Homework III:} You will get to demonstrate that for $N(\mu,
\sigma^2)$ we have MLEs
\begin{equation*}
  \hat{\mu} = \frac{1}{n} \sum_{i=1}^n x_i,
  \quad\text{and}\quad
  \hat{\sigma} = \Bigl[\frac{n-1}{n} S^2(n) \Bigr]^{1/2}\;.
\end{equation*}


\subsection{Goodness-of-fit tests}


Goodness-of-fit tests are use to assess if observations $X_1, X_2, \ldots,
X_n$ are an independent sample from a particular distribution with
distribution function $F$ using as null hypothesis:
\begin{equation*}
\text{$H_0$: The $X_i$'s are IID random variables with distribution
  function $F$}
\end{equation*}
\textbf{Note 1:} not rejecting $H_0$ does not mean accepting $H_0$ as
true.

\textbf{Note 2:} (sample size) this class of tests is not that
sensitive to small discrepanices between distributions for
small/moderate samples sizes $n$. However, for very large $n$, even
tiny deviations will be detected causing rejection of the null
hypothesis. These are tools that should be used judiciously keeping
these factors in mind.


%% ----------------------------------------------------------------------
\subsection{The Kolmogorov-Smirnov Test}
\label{sec:ks}
The Kolmogorov-Smirnov (KS) test is used to assess how well a
hypothesized distribution $\hat{F}$ of a continuous random variable
$X$ matches a observed sample data $x_1, x_2, \ldots, x_n$ and their
corresponding empirical distribution~$F$ as defined
in~\ref{eq:empirical}.
%%
The KS-statistic $D_n$ is defined as the supremum (sup)
\begin{equation}
  D_n = \sup_{x} |F(x) - \hat{F}(x)| \;.
\end{equation}
Here supremum is used rather than maximum. For example, the  interval
$(0,1) \subset \mathbb{R}$ does not have a maximum, however, the
supremum exists and equals~1. You can read about supremum and infimum
\href{https://en.wikipedia.org/wiki/Infimum_and_supremum}{here}.

The computation of the KS-statistic can be carried out via
\begin{equation}
  D^+_n = \max_{1\le i \le n} \bigl\{ \bigl|i/n - \hat{F}(x_i)\bigr|\bigr\},\quad
  D^-_n = \max_{1\le i \le n} \bigl\{ \bigl|\hat{F}(x_i) - (i-1)/n \bigr|\bigr\},
\end{equation}
as
\begin{equation}
 D_n = \max \{ D^+_n, D^-_n \} \;.
\end{equation}
See Figure~\ref{fig:ks}. The distances appearing in $D^+$ are the
gaps between the solid circles and $\hat{F}(x)$; the distances appearing in
$D^-$ are the gaps between hollow circles and $\hat{F}(x)$.

\begin{figure}[ht]
\centerline{\includegraphics[width=0.75\textwidth]{figs/KS-illustration}}
\caption{The KS-statistic for a sample of size five with fitted
  distribution $\hat{F}(x)$.}
\label{fig:ks}
\end{figure}


There are two main cases to cover: (i) all parameters of $\hat{F}$ are
known (none were estimated from the data), and (ii) one or more
parameters were estimated from the data.
%%
Naturally, one may split $S$ as $S_1 \dot\cup S_2$ where $S_1$ is used
for distribution modeling (fitting) and $S_2$ is used for the
goodness-of-fit test, leading to case (i). Of course, this will
diminish the strength of the test.

\textbf{Case (i):} If none of the data $S$ was used to estimate
parameters of $\hat{F}$, then the distribution of the test statistic
$D_n$ does not depend on $\hat{F}$ and there are tables for the
percentiles $d_{n,1-\alpha}$. One will then reject the null hypothesis
if $D_n > d_{n,1-\alpha}$.

As pointed out in Law, there is an accurate approximation that
eliminates the $n$-dimension from the tabulated data: this adjusted
KS-statistic is
\begin{equation*}
D'_n = \bigl( \sqrt{n} + 0.12 + 0.11/\sqrt{n} \bigr) D_n
\end{equation*}
and one rejects the null hypothesis if $D'_n > c_{1-\alpha}$ where the
$c_{1-\alpha}$ values for some selected levels $\alpha$ are provided
in Table~\ref{tab:ks_mod} (which is part
of~\cite[Tab. 6.15]{Law:13}).
\begin{table}[ht]
\centerline{
\begin{tabular}{|l|lllll|}
\hline
$1-\alpha$ & 0.850 & 0.900 & 0.950 & 0.975 & 0.999 \\
\hline
$c_{1-\alpha}$ & 1.138 & 1.224 & 1.358 & 1.480 & 1.628 \\
\hline
\end{tabular}
}
\caption{Some $c$-values for the adjusted KS-statistic.}
\label{tab:ks_mod}
\end{table}

\textbf{Case (ii):} This case is significantly more complex.




Recall the definition of $F$ from~\eqref{eq:empirical}



\textbf{The two-sample Kolmogorov-Smirnov test.}
%%
This test is used for assessing whether two one-dimensional
probability distributions differ. Assume we have samples $S_1$ with
$|S_1| = n$ and $S_2$ where $|S_2| = m$ and matching empirical
distributions $F_{1,n}$ and $F_{2,m}$. The test statistic~$D_{n,m}$ in
this case is,
\begin{equation*}
  D_{n,m} = \sup_{x} | F_{(1,n)}(x) - F_{(2,m)}(x)| \;,
\end{equation*}
and, for large samples, the null hypothesis is rejected at level $\alpha$
if
\begin{equation*}
D_{n,m} > \sqrt{-\ln\bigl(\frac{\alpha}{2}\bigr)\, \frac{m+n}{mn}\Bigr/2 }\;.
\end{equation*}
You can read more about this under
\href{https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test#Test_with_estimated_parameters}{Two-sample
  Kolmogorov–Smirnov test}.



%% ----------------------------------------------------------------------
\subsection{The $\chi^2$-Test}
\label{sec:chi}

The $\chi^2$ test (or Pearson's $\chi^2$ test) is a test used with
categorical data and the following setup:
\begin{itemize}
\item There are categories $1, 2, \ldots, k$
\item There are $N$ samples
\item The number of samples in category $i$ is $N_i$, and $\sum_i N_i
  = N$.
\item The null hypothesis is that the data is sampled from
  $\text{Multinomial}(N, p_1, p_2, \ldots, p_k)$
\item The test statistic is the random variable
\begin{equation}
\chi^2 = \sum_{i=1}^k \frac{(N_i-N p_i)^2}{N p_i}
\end{equation}
which, in the limit $N\to \infty$ approaches the $\chi^2$
distribution with $k-1$ degrees of freedom.
\end{itemize}

\textbf{Assumptions:} samples are IID, sample size is sufficiently
large, sample counts within each category are sufficiently large.


\textbf{Example:} Two shopkeepers in neighboring store are trying to
settle an argument. Shopkeeper $A$ has for the longest time claimed
that he always gets the same number of customers every day Monday
through Friday. ``50 customers, and my day is done!'' To prove him
wrong, shopkeeper $B$, who happens to have just completed a
correspondence course in statistics, finally decides to camp out at
$A$'s store for an entire week and record the total customer counts,
making sure not to miss or double-count a single customer. He has
heard about IID random variables, and has taken laudable precautions
to not influence customer counts during this week.
Shopkeeper $B$'s recorded is given in Table~\ref{tab:shopkeeper_data}.
\begin{table}[ht]
\centerline{
\begin{tabular}{|l|r|r|r|r|r|r|}
\hline
Category &  Monday & Tuesday & Wednesday & Thursday & Friday \\
\hline
Observed &  50 & 60 & 40 & 47 & 53 \\
Expected &  50 & 50 & 50 & 50 & 50 \\
\hline
\end{tabular}
}
\caption{The visitor count data of shopkeeper $B$.}
\label{tab:shopkeeper_data}
\end{table}

Here we have $Np_i = 50$ (more about this later) and the test
statistic becomes
\begin{equation*}
\chi^2 = \frac{1}{50}( 0 + 10^2 + 10^2 + 3^2 + 3^2 ) = 218/50 = 4.36 \;.
\end{equation*}
The $p$-value for this case, which has $k-1 = 4$ degree of freedom, is
$0.359$. Shopkeeper $B$, being unable to reject the null hypothesis,
concedes for now and, more determined than ever, signs up for an
advanced statistics correspondence course.

What if we had to estimate one or more parameters in the distribution
for customers across days? In general, we drop one degree of freedom
for every estimated parameter, a fact discussed in the next section.

\url{https://online.stat.psu.edu/stat415/book/export/html/832}


\section{$\chi^2$ and Goodness-of-Fit Testing}

Recall that the $\chi^2$ test is intended for categorical data. Our
fitted distributions are usually continuous distributions. After the
basic description of this test, we will address this mismatch and
related concerns.

The standard recipe for the $\chi^2$-test when applied to our setting
with sample data $X_1, X_2, \ldots, X_n$ is to first divide the entire
range of the fitted distribution into $k$ adjacent intervals of the
form
\begin{equation}
\label{eq:chi_intervals}
  [a_0,a_1), \quad [a_0,a_1), \quad \ldots \quad [a_{k-1}, a_k)\;,
\end{equation}
where the first and last intervals can include the possibilities
$(-\infty, a_1)$ and $[a_{k-1}, \infty)$.
%%
Next, we let $N_i$ denote the number of samples $X_j$ that fall into
the $j$th interval $[a_{j-1}, a_j)$.
%%
Following this, one uses the fitted distribution function to estimate
expected proportions $p_j$ of the sample points that fall into
interval~$j$ as
\begin{equation*}
 p_j = \int_{a_{j-1}}^{a_j} f(x) dx
\end{equation*}
where $f$ is the probability density function of the fitted
distribution for the continuous case, or as
\begin{equation*}
p_j = \sum_{a_{j-1} \le x_i < a_j} p(x)
\end{equation*}
where $p$ is the fitted probability mass function in the discrete
case. If one has the cumulative distribution function, one may of
course use that instead of the previous expressions.
%%
In both cases, the test statistic is
\begin{equation*}
\chi^2 = \sum_{i=1}^k \frac{(N_j - n p_j)^2}{n p_j} \;,
\end{equation*}
which, for the purpose of hypothesis testing, we expect to be small if
the null hypothesis is true.
%%
There are two cases:
\begin{itemize}
  \item (a) no parameters were estimated to construct the candidate
  distribution, and
  \item (b) one or more parameters where estimated.
\end{itemize}
For case (a), if $H_0$ is true, then $\chi^2$ converges to a
$\chi^2_{k-1}$ distribution with $k-1$ degrees of freedom as $n$
approaches infinity. At level $\alpha$, the rejection criterion for is
$\chi^2 > \chi^2_{k-1,1-\alpha}$.

For case (b) with $m \ge 1$ estimated (or fitted) parameters via
maximal likelihood estimation (MLE), it has been shown (see, e.g.,
Law~\cite{Law:13}) that $\chi^2$ converges to a distribution function
bounded above and below by $\chi^2_{k-1}$ and $\chi^2_{k-m-1}$
distribution functions. Denoting by $\chi^2_{1-\alpha}$ the
$1-\alpha$ percentile of the asymptotic distribution of $\chi^2$, we
have (see \cite[Fig. 6.46]{Law:13}):
\begin{equation*}
 \chi^2_{k-m-1,1-\alpha} \le \chi^2_{1-\alpha} \le \chi^2_{k-1,1-\alpha}
\end{equation*}
Therefore, one should reject the null hypothesis if $\chi^2 >
\chi^2_{k-1,1-\alpha}$, and one should not reject if $\chi^2 <
\chi^2_{k-m-1,1-\alpha}$. What one does for $\chi^2 \in [
  \chi^2_{k-m-1,1-\alpha}, \chi^2_{k-1,1-\alpha} ]$ can be debated;
you can read about this in~\cite[p. 348]{Law:13} where it is argued
that for large $n$ and a modest number~$m$ of estimated parameters the
difference in these two $(1-\alpha)$ percentiles will not be
``large'', with the recommended approach to reject $H_0$ if and only
if $\chi^2 > \chi^2_{k-1,1-\alpha}$, which is the same as the
all-parameters-known case. You will have to discern if your sample
size is appropriate for this.


\textbf{The concern related to the $\chi^2$-test and non-categorical
  data:} Applying the $\chi^2$-test to categorical data requires
binning data into a finite collection of bins. In the case of a
univariate distribution, this takes the form of the intervals
in~\eqref{eq:chi_intervals}. What is the issue? We made a choice of
the the $a_i$'s; other choices may lead to different
conclusions. Example~6.17 from~\cite{Law:13} provides an example
demonstrating exactly this. While several approaches have been
developed to alleviate this issue, one example is that of equiprobable
intervals, there is no principled approach. Nontheless, the
$\chi^2$-test is widely used, one reason being that it can be
generalized to dimension $\ge 2$.






(sec:distribution_modeling_phitter)=
## The Phitter distribution modeling tool
