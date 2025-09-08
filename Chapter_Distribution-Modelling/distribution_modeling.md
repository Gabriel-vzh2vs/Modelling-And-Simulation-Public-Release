
(sec:distribution_modeling)=
# Distribution modeling



\subsection{Process overview}

In Law, distribution modeling of a random variable $X$ with
distribution function $F = F_X$ is broken down into three
``activities'': \S 6.4-(I) hypothesizing families of distributions, \S
6.5-(II) estimation of parameters, and \S 6.6-(III) determining how
representative the fitted distributions are. We will refine this
slightly following~\cite{Krzysztofowicz:25} whose procedure is very
clean.

In the following, we assume that we have a sample of a one-dimensional
(uni-variate) random variable $X$ whose distribution function is
$F$. Here are the steps:
\begin{enumerate}
\item Construct the empirical distribution function of~$X$ using the sample
\item Specify the sample space $\Omega$ of $X$
\item Hypothesize parametric models
\item Estimate the parameters of each hypothesized model
\item Evaluate the goodness of fit of each model, including
  statistical testing
\item Choose the best one
\end{enumerate}
We will go through each of these items in the upcoming sections. Note
that distribution modeling is a large scientific area and that what we
cover here is focused on establishing a workable foundation for
simulation practice.
