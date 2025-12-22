(sec:means_variance)=
# Cleanup Needed: Means and variance

\hmbullet\textbf{Overview:} These slides are a condensed version of
the lectures for January~28 and~30.
\begin{itemize}
\item The system, mathematical model, and simulation model breakdown
\item Types of uncertainties and implications for modeling
\item The model as a ``complex random variable''
\item Generating outcomes through simulation runs
\item Ensuring that simulation runs are independent
\item An overview of other elements involved when experimenting with
  simulation models.
\item Output analysis: the setup
  \begin{itemize}
    \item Estimating means, variances and constructing confidence
      intervals for estimates.
    \item The role of the Central Limit Theorem and the Strong Law of
      Large numbers
    \item Skewness and implications to construction of confidence
      intervals and the number of replications.
  \end{itemize}
\item \textbf{Reading:} Law 3.1--3.3, 4.3 (preview), 4.4--4.6, and
  9.1--9.2 (preview).
\end{itemize}



\frametitle{Models and simulations models / Random variables}

\hmbullet Model $M$ and simulation model $\mathcal{M}$.

\hmbullet We capture model output for the $k$\th instance (run) by a
random variable $X_k$.

\hmbullet In practice, a model has more than one output. Thus $X_k =
(X_{k,1}, X_{k,2}, \ldots, X_{k,m})$.

\hmbullet Here we assume that each of the $X_{i,j}$'s are real-valued
random variables. (What are other possibilities?)

\hmbullet We take care to ensure that different invocations/runs of
the simulation model $\mathcal{M}$ are independent (e.g., use
different sets of random numbers; each run use precisely the same
initial conditions; saved data from run $k$ is not used in any way in
subsequent runs)

\hmbullet Simulation run $k$ (with $1\le k \le n$) produces an outcome $x_k =
(x_{k,1}, x_{k_2}, \ldots, x_{k,m})$

\hmbullet We record the collection of outcomes as a matrix:

\begin{equation}
  \label{eq:outcome_matrix}
\begin{matrix}
  x_{1,1} & x_{1_2} & \ldots & x_{1,m}  \\
  x_{2,1} & x_{2_2} & \ldots & x_{2,m}  \\
  \vdots & \vdots & \ddots & \vdots \\
  x_{n,1} & x_{n_2} & \ldots & x_{n,m}  \\

\end{matrix}
\end{equation}

\end{frame}


%% ----------------------------------------------------------------------

\begin{frame}
  \frametitle{Law \S 4.4--4.6 Means, variances and confidence intervals}

\hmbullet This part of the course covers the case of IID random
variables $X_1$, $X_2$, $\ldots$, $X_n$ with finite mean $\mu$ and
finite variance $\sigma^2$.

\hmbullet  This analysis can be applied to each column
in~\eqref{eq:outcome_matrix} on slide \pageref{eq:outcome_matrix}, separately.

\hmbullet Analysis across columns in~\eqref{eq:outcome_matrix} will be
addressed later -- generally we have to address dependence in this case.

\hmbullet The current goal: estimate the expectation $\mu$, the variance
$\sigma^2$, and provide a confidence interval for the estimate of
$\mu$.
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Estimating $\mu$}

\hmbullet We use the following estimator for the mean:
\begin{equation*}
 \bar{X}(n) = \frac{1}{n} \sum_{i=1}^n X_i
\end{equation*}
\hmbullet Note that $\bar{X}(n)$ is a random variable.

\hmbullet Why can we be sure that this approach using $\bar{X}(n)$
works? Answer:

\textbf{The strong law of large numbers:} For any sequence $X_1$,
$X_2$, $X_3$, $\ldots$ of IID random variables with finite
expectation, then with probability~1
\begin{equation*}
\lim_{n\to \infty} \frac{1}{n}\sum_{i=1}^n X_i = E(X)\;.
\end{equation*}
What this really means:
\begin{equation*}
\Pr\Bigl(\lim_{n\to \infty} \frac{1}{n}\sum_{i=1}^n X_i = E(X)\Bigr) = 1\;
\end{equation*}
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Estimating $\mu$}

\hmbullet $\bar{X}$ is a random variable. As such (and with the
assumptions on $\mu$ on $\sigma^2$), it has expectation and variance.

\hmbullet The expectation of $\bar{X}$ is:
\begin{equation*}
\exp[\bar{X}(n)]
= \exp[\frac{1}{n} \sum_{i=1}^n X_i]
= \frac{1}{n} \sum_{i=1}^n \exp[X_i]
= \frac{1}{n} n \, \mu = \mu\;
\end{equation*}
\hmbullet Since the mean of the estimator equals $\mu$ we call it \textbf{unbiased}

\hmbullet The variance of $\bar{X}(n)$ is (using the independence assumption):
\begin{equation*}
\var[\bar{X}(n)]
= \var[\frac{1}{n} \sum_{i=1}^n X_i]
= \frac{1}{n^2} \sum_{i=1}^n \var[X_i]
= \frac{1}{n^2} n\, \sigma^2 = \frac{\sigma^2}{n}
\end{equation*}
(The last step uses independence)

\hmbullet Challenge: we do not know $\sigma^2$ -- we need to estimate it!
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Estimating $\sigma^2$}

\hmbullet The \textbf{sample variance} is:
\begin{equation}
 S^2(n) = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}(n))^2
\end{equation}
\hmbullet It is a random variable; It is an unbiased estimator since
$\exp[S^2(n)] = \sigma^2$.

\hmbullet Combining with the above we obtain the estimator for the
variance of $\bar{X}(n)$:
\begin{equation*}
\widehat{\var}[\bar{X}(n)]
= \frac{S^2(n)}{n}
= \frac{1}{n(n-1)}\sum_{i=1}^n (X_i - \bar{X}(n))^2
\end{equation*}


\hmbullet Note: regarding pages 230.5--232: we will return to this
case later -- this is relevant for the output analysis for the
``across columns'' case where we have to consider dependence.
\end{frame}

%% ----------------------------------------------------------------------
\begin{frame}
\frametitle{Law Example 4.27 (page 236)}

\hmbullet We have 10 observations from a simulation model: 1.2, 1.5,
1.68, 1.89, 0.95, 1.49, 1.58, 1.55, 0.5, and 1.09. Estimate the mean
and the variance. (We will construct a confidence interval later.)

Switching to Excel ... part 1

\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Evaluating $S^2(n)$ -- maybe not so simple after all?}

\hmbullet The sample variance is given by:
\begin{equation}
 S^2(n) = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}(n))^2
\end{equation}

\hmbullet Question 1: In our simulation output analysis, what can go
wrong when computing $S^2(n)$?

\hmbullet Question 2: Can something go wrong when evaluating $\bar{X} =
\frac{1}{n} \sum_{i=1}^n X_i$?

\hmbullet Question 3: Can these things go wrong when you use Excel?
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Don't let your guard down I}

\hmbullet Since the questions are raised, you may already have guessed
``yes'', things can go wrong. What can go wrong and how may it happen?

\hmbullet It can get complicated when $n$ is large. Here are examples
of limitations on variables based on their types (e.g., integer, float):

\begin{itemize}
\item 4 byte int - min: -2,147,483,648
\item 4 byte int - max: +2,147,483,647
\item 8 byte int - max: +9,223,372,036,854,775,807 (or about $9.2 \times 10^{18}$)
%% ULONG MAX      = 18,446,744,073,709,551,615 (or about 18.5 x 10^{18})
\item 4 byte float max: $3.402823e+38$
%%FLT EPSILON     = 1.192093e-07
%% double min 2.2250738585072014e-308
\item 8 byte double min: $1.7976931348623158e+308$
\end{itemize}

\hmbullet The challenges: \textbf{overflow} and \textbf{underflow}
(What does that mean?)

\end{frame}

\begin{frame}
\frametitle{Don't let your guard down - II}

\hmbullet There are challenges in the case of big data and/or possibly
large/small values:
\begin{itemize}
  \item If you write your own code, you should likely avoid the
    for-loop approach (e.g., \href{https://en.wikipedia.org/wiki/Kahan_summation_algorithm}{Kahan algorithm}, but be aware of compiler optimization)
  \item If you use libraries (e.g., in Python) you should likely check
    the implementation and/or documentation carefully.
  \item Also: you may have to use an online computation (data comes from a
    stream; not an option to store the data) -- this will also impose restrictions
\end{itemize}

\hmbullet Is this a problem when working in Excel?
\begin{itemize}
  \item The``big data'' problem: You may run out of memory
    trying to load/generate the amount of data in Excel before this
    becomes an issue. Do we still need to be weary?
  \item Excel supports pulling data from databases. You may enter the
    realm of big data if you pull enough data.
  \item Large values will still require care
\end{itemize}

\hmbullet \textbf{The message:} Always stay alert!
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{\S 4.5 Confidence intervals and hypothesis testing for the
  mean}

\hmbullet We have seen how to estimate the mean using $\bar{X}$. The
approach is anchored in the strong law of large numbers.

\hmbullet In addition to $\mu$, we also need to provide a guarantee
that our estimate is good, or some measure that allows us to quantify its quality.

\hmbullet The standard approach is to construct \textbf{confidence
  intervals} for the mean: determine real values $a$ and $b$ such that
we can state $a\le \mu \le b$ with a prescribed probability.

\hmbullet The approach is based on the:

\textbf{Central Limit Theorem (CLT):}
Let $X_1$, $X_2$, $X_3$, $\ldots$ be a sequence of IID random
variables with finite mean $\mu$ and finite standard deviation
$\sigma^2 > 0$, and let $Z_n$ be the random variable
\begin{equation*}
  Z_n = (\bar{X} - \mu)/\sqrt{\sigma^2/n} \;.
\end{equation*}
Then
\begin{equation*}
\Pr( Z_n \le z ) = F_{n,Z}(z)
\longrightarrow
\Phi(z) \quad \text{as $n\to \infty$}\;.
\end{equation*}
Here $\Phi$ is the distribution function of the standard normal
distribution ($\mu = 0$, $\sigma^2=1$).
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Confidence intervals for $\mu$ - Round 1}

\hmbullet Before we can proceed we need to address the fact that $Z_n$
contains $\sigma^2$, and that \textbf{we do not know $\sigma^2$}.

\hmbullet We use the estimator $S^2(n)$ and introduce the new random
variable
\begin{equation*}
t_n = (\bar{X}(n) - \mu)/\sqrt{S^2(n)/n}
\end{equation*}
which, by the CLT, has, approximately, the standard normal
distribution when $n$ is ``sufficiently large''. (Yes, what is
sufficiently large?  Stay tuned.)

\hmbullet Armed with this, we can now state that, for sufficiently
large $n$, we \textbf{approximately} have:
\begin{align*}
 \Pr\Bigl(
 & -z_{1-\alpha/2} \le (\bar{X}(n) - \mu)/\sqrt{S^2(n)/n} \le z_{1-\alpha/2}
  \Bigr)
  \\
&=
\Pr\left(
\bar{X}(n) -z_{1-\alpha/2}\sqrt{S^2(n)/n}
\le - \mu
\le \bar{X}(n) + z_{1-\alpha/2}\sqrt{S^2(n)/n}
\right) \\
&\approx 1 - \alpha
\end{align*}

\hmbullet $\alpha$ is often called the \textbf{significance level})

\hmbullet The quantity $z_{1-\alpha/2}\sqrt{S^2(n)/n}$ is called the
\textbf{half length} of the confidence interval.
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Confidence intervals}

\hmbullet The confidence interval is:
\begin{equation}
[
  \bar{X}(n) - z_{1-\alpha/2}\sqrt{S^2(n)/n},
  \bar{X}(n) + z_{1-\alpha/2}\sqrt{S^2(n)/n}
]
\end{equation}

\hmbullet How does one interpret confidence intervals?

\hmbullet For fixed $n$ and $\alpha$: if one constructs a large number
of independent $100(1-\alpha)$ confidence intervals, the fraction of
these intervals that contain (or cover) $\mu$ should be
$(1-\alpha)$. This fraction (or proportion) is called the
\textbf{coverage} for the confidence interval.

\hmbullet In other words: in your output analysis, when you have your
confidence interval, you are providing \textbf{a probabilistic
  guarantee}.

\hmbullet You may want to look at Law Example 4.26.
\end{frame}


%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Confidence intervals for $\mu$ - Round 2}

\hmbullet Knowing when ``$n$ is sufficiently large'' presents an issue.

\hmbullet The more \textbf{skewed} the underlying distribution of the
$X_i$'s, the more of an issue it becomes, and the larger $n$ will
generally have to be.

\hmbullet \textbf{Step 1:}
\begin{itemize}
\item He considers the case where the $X_i$'s are, in fact, normally
  distributed.
\item In this case,
  \begin{equation*}
   t_n = (\bar{X}(n) - \mu)/\sqrt{S^2(n)/n}>
  \end{equation*}
  has a Student's $t$-distribution with $n-1$ degrees of freedom for
  which one has the exact confidence interval:
  \begin{equation}
    \label{eq:student_t_interval}
\bar{X}(n) \pm t_{n-1,1-\alpha/2} \sqrt{S^2(n)/n}
  \end{equation}
\item This interval is \emph{wider} (or somewhat more conservative)
  than the one constructed earlier. (For large $n$, e.g., $n\ge 100$, the difference is small)
\item Law's recommendation is to use the confidence interval~\eqref{eq:student_t_interval}.
\end{itemize}
\hmbullet Switching to Excel ...

\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Confidence intervals for $\mu$ - Skewness - (Round 2 ctd.)}

\hmbullet We will turn to Law Table 4.1 for this. Key elements:

\hmbullet The skewness of a distribution is defined to be the third
central moment, i.e.,
\begin{equation*}
\nu = \exp[(X-\mu)^3]/(\sigma^2)^{3/2}
\end{equation*}
which measures asymmetry about the mean (see Homework 1).

\hmbullet Law explores 5 common distributions with known skewness

\hmbullet For each distribution, and separately for $n=5$, $n=10$,
$n=20$ and $n=40$, he estimates coverages for 90\% confidence
intervals ($\alpha = 0.1$) through 500 independent experiments.

\hmbullet How many experiments did Law run? Anybody?

\hmbullet Switching to Law (pages 236 and 237) with discussion

\end{frame}


\begin{frame}
\frametitle{Confidence intervals for $\mu$ - The finale!}

\hmbullet The Willink confidence interval (p. 237) is:
\begin{equation}
\label{eq:willink_interval}
[
  \bar{X}(n) - G(t_{n-1,1-\alpha/2})\sqrt{S^2(n)/n},
  \bar{X}(n) + G(t_{n-1,1-\alpha/2})\sqrt{S^2(n)/n}
]
\end{equation}
where
\begin{align*}
G(r) &=
  (1+6a(r-a)^{1/3} - 1)/(2a)\\
a &=
  \frac{\hat{\mu}_3}{6\sqrt{n}(S^2(n))^{3/2}}\;,\text{ and}\\
\hat{\mu}_3 &=
  \frac{n}{(n-1)(n-1)} \sum_{i=1}^n (X_i - \bar{X}(n))^3 \;.
\end{align*}


\hmbullet Discussion while looking at the book.

\hmbullet General philosophy regarding results like~\eqref{eq:willink_interval}.

\hmbullet Learning goals for this case:
\begin{itemize}
\item You should know about the Willink interval~\cite{Willink:2005} and be
  able to use it in your own work. It will not appear on an exam.
\item Know that it incorporates empirical estimates of skewness to set
  a more conservative half length for the confidence interval compared
  to~\eqref{eq:student_t_interval}
\end{itemize}
\end{frame}

%% ----------------------------------------------------------------------

\begin{frame}
\frametitle{Hypothesis testing regarding $\mu$}

\hmbullet Setting:
\begin{itemize}
\item We assume the $X_i$'s are approximately normally distributed, and
\item have $\mu_0$ as a fixed hypothesized value for $\mu$, and
\item we want to test the null hypothesis $H_0\colon \mu = \mu_0$
  against the alternative hypothesis $H_1 \colon \mu \ne \mu_0$.
\item Under the assumption that $H_0$ is true, the test statistic
  \begin{equation*}
   t_n = (\bar{X}(n) - \mu_0)/\sqrt{S^2(n)/n}
  \end{equation*}
  has a Student's $t$-distribution with $n-1$ degrees of freedom.
\item The two-tailed hypothesis test for $H_0$ is to reject $H_0$ if
  $|t_n| > t_{n-1,1-\alpha_2}$ and fail to reject $H_0$ otherwise.
\end{itemize}
You will recognize this from Statistics. Please review as
necessary. In 3062, we will focus on confidence intervals.
\end{frame}



%% ------------------------------------------------------------
%% \frame{References}
%% ------------------------------------------------------------

\begin{frame}[allowframebreaks]
\frametitle{References}

\bibliographystyle{unsrt}
\bibliography{../../3062}

\end{frame}

\end{document}
