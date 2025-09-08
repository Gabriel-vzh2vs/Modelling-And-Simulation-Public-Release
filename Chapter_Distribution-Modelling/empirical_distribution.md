
(sec:empirical_distribution)=
# Empirical Distributions

Here we consider the case where we have a sample
\begin{equation}
  S = \{x_1, x_2, \ldots, x_n\} \quad\text{with}\quad x_i \in
  \mathbb{R}
\end{equation}
of a continuous random variable $X$, and where we assume that the
sample points are arranged in increasing order:
\begin{equation*}
 x_1 \le x_2 \le \cdots \le x_n
\end{equation*}
Sometimes, one needs to consider the order given by the collection
time of the sample points, but we will not be that concerned with
this case.

We define an \textbf{empirical distribution function} for the sample
$S = \{x_1, x_2, \ldots, x_n\}$ by
\begin{equation}
\label{eq:empirical}
F(x) = \bigl|\{x' \in S \mid x' \le x\}\bigr| \Bigl/ n \;.
\end{equation}
What does this function look like? Going from left to right on the
real line, the function $F$ starts out at $0$, then jumps a height of
$1/n$ as each point $x_i$ is encountered. One example of such a
function is given in Figure~\ref{fig:empirical}.
\begin{figure}[ht]
\centerline{\includegraphics[width=0.75\textwidth]{figs/empirical-distribution.pdf}}
\caption{The empirical distribution function for a sample $S =
  \{x_1, x_2, x_3, x_4, x_5\}$.}
\label{fig:empirical}
\end{figure}

The definition of the empirical distribution function $F$
in~\eqref{eq:empirical} matches Equation~(6.5)
in~\cite{Law:13}. Law gives an alternative definition of an empircal
distribution (see~\cite[p. 313]{Law:13}), and you will find yet other
ones in~\cite{Krzysztofowicz:25}.
%%
The function defined in~\eqref{eq:empirical} is a piecewise constant
non-decreasing function. It is precisely the definition of an
empirical distribution function that we need for the
Kolmogorov-Smirnov (KS) test, see Section~\ref{sec:ks}.
