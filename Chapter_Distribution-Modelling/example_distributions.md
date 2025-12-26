
(sec:distribution_examples)=
# Examples of statistical distributions

In this section, we review fundamental concepts regarding standard statistical distributions, providing a foundation for selecting appropriate models for simulation input.

Background and introductory examples: We begin by establishing the necessity of understanding the behavior of various distribution families. For a comprehensive primer, see, e.g., {cite}`Law:13` Section 6.1.

Location, scale, and shape parameters: A key aspect of understanding continuous, parametric distributions is recognizing how specific parameters alter the distribution's geometry.

  - Location parameters (often denoted as γ or μ) shift the distribution along the x-axis without changing its appearance.

  - Scale parameters (often denoted as β or σ) compress or expand the distribution; for example, in a normal distribution, this controls the spread.

  - Shape parameters (often denoted as α or k) fundamentally alter the configuration of the density function, such as the skewness or tail behavior.

Common continuous and discrete parametrized distributions: We illustrate these concepts using standard examples found in the literature, such as Sections 6.2.2 and 6.2.3 in {cite}`Law:13` or the Wikipedia.

- Continuous examples often include the Normal, Exponential, Gamma, and Weibull distributions.

- Discrete examples often include the Poisson, Binomial, and Geometric distributions.

Maximum Likelihood Estimators (MLEs): Most listings of these distributions will include their associated MLEs. These are the estimators for the parameters of the distribution that maximize the likelihood function, making the observed sample $Z$ most probable under the assumed statistical model.

```{raw} latex

\subsection{Continuous Distributions}

Continuous distributions are defined for random variables that can take values on a continuous scale. In simulation, these are frequently used to model time-based variables (e.g., inter-arrival times, service times) or physical quantities.

\begin{itemize}
    \item \textbf{Exponential Distribution}
    \begin{description}
        \item[Usage:] Ideally suited for modeling inter-arrival times in Poisson processes (random arrivals). It is the only continuous distribution with the ``memoryless'' property.
        \item[Parameters:] Rate $\lambda > 0$ (scale parameter is $1/\lambda$).
        \item[PDF:] 
        \[
        f(x) = \lambda e^{-\lambda x} \quad \text{for } x \ge 0
        \]
        \item[MLE:] The estimator for the rate is the inverse of the sample mean:
        \[
        \hat{\lambda} = \frac{n}{\sum_{i=1}^n z_i} = \frac{1}{\bar{z}}
        \]
    \end{description}

    \item \textbf{Normal (Gaussian) Distribution}
    \begin{description}
        \item[Usage:] Often describes errors or sums of independent random variables (due to the Central Limit Theorem).
        \item[Parameters:] Location $\mu$ (mean) and scale $\sigma$ (standard deviation).
        \item[PDF:] 
        \[
        f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
        \]
        \item[MLEs:]
        \[
        \hat{\mu} = \bar{z}, \quad \hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^n (z_i - \bar{z})^2
        \]
        \emph{Note: The MLE for variance $\hat{\sigma}^2$ divides by $n$, whereas the standard unbiased sample variance $S^2$ divides by $n-1$.}
    \end{description}

    \item \textbf{Weibull Distribution}
    \begin{description}
        \item[Usage:] Widely used in reliability engineering to model time-to-failure. It can represent increasing, decreasing, or constant failure rates depending on the shape parameter.
        \item[Parameters:] Shape $\alpha > 0$ and scale $\beta > 0$.
        \item[PDF:] 
        \[
        f(x) = \frac{\alpha}{\beta} \left(\frac{x}{\beta}\right)^{\alpha-1} e^{-(x/\beta)^\alpha} \quad \text{for } x \ge 0
        \]
        \item[MLEs:] The MLEs for $\alpha$ and $\beta$ generally do not have closed-form solutions and must be found numerically by solving simultaneous equations.
    \end{description}
\end{itemize}

\subsection{Discrete Distributions}

Discrete distributions describe random variables that take on a countable number of distinct values (often non-negative integers). In simulation, these usually model counts (e.g., number of customers in a queue, number of defective items in a batch).

\begin{itemize}
    \item \textbf{Poisson Distribution}
    \begin{description}
        \item[Usage:] Models the number of events occurring in a fixed interval of time or space, given a constant mean rate.
        \item[Parameters:] Rate $\lambda > 0$ (which is both the mean and the variance).
        \item[PMF:] 
        \[
        p(k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for } k = 0, 1, 2, \ldots
        \]
        \item[MLE:] 
        \[
        \hat{\lambda} = \bar{z}
        \]
    \end{description}

    \item \textbf{Geometric Distribution}
    \begin{description}
        \item[Usage:] Models the number of Bernoulli trials needed to get the first success (or sometimes the number of failures before the first success).
        \item[Parameters:] Probability of success $p \in (0, 1)$.
        \item[PMF:] 
        \[
        p(k) = (1-p)^{k-1}p \quad \text{for } k = 1, 2, \ldots \quad (\text{modeling number of trials})
        \]
        \item[MLE:] 
        \[
        \hat{p} = \frac{1}{\bar{z}}
        \]
    \end{description}

    \item \textbf{Binomial Distribution}
    \begin{description}
        \item[Usage:] Models the number of successes in a fixed number of independent Bernoulli trials.
        \item[Parameters:] Number of trials $n$ (known) and probability of success $p$.
        \item[PMF:] 
        \[
        p(k) = \binom{n}{k} p^k (1-p)^{n-k}
        \]
        \item[MLE:] 
        \[
        \hat{p} = \frac{\bar{z}}{n}
        \]
    \end{description}
\end{itemize}
```
