(sec:MCMC)=
# Markov Chain Monte Carlo (MCMC)

## What is MCMC?

In general, Markov Chain Monte Carlo methods
refer to a family of algorithms that estimate
a posterior distribution through a Markov Chain.
This chain represents a random sequence of
samples following the Markovian property.
Through this method, it becomes possible to
draw from the unknown posterior distribution
using a density representing the transition
rates in the irreducible, aperiodic and
recurrent Markov Chain. Note that these
properties of the Markov Chain make give
MCMC an asymptotic convergence to the posterior
distribution. These requirements
can be presented as the following expression:

```{raw} latex
\begin{figure}[htbp]
    \[
        \pi(\boldsymbol{\theta}^{(s)} \mid \boldsymbol{y}) = \int_{\Theta} q(\boldsymbol{\theta}^{(s)} \mid \boldsymbol{\theta}^{(s-1)}) \pi(\boldsymbol{\theta}^{(s-1)} \mid \boldsymbol{y}) \, d\boldsymbol{\theta}^{(s-1)}.
    \]
    \caption{\textbf{Global Balance Equation for the Posterior.} This expression illustrates the condition for stationarity in a Markov Chain. $\pi(\boldsymbol{\theta} \mid \boldsymbol{y})$ represents the target posterior density, and $q(\boldsymbol{\theta}^{(s)} \mid \boldsymbol{\theta}^{(s-1)})$ represents the transition kernel probability of moving from state $s-1$ to $s$. The equation shows that marginalizing the joint density of the transition and the previous state over the entire parameter space $\Theta$ yields the target distribution again, proving that $\pi$ is the stationary distribution of the chain.}
    \label{fig:posterior_stationarity}
\end{figure}
```

The proofs supporting this process are found
in pg. 205 - 247 of the book {cite}`robert1999monte`,
as that is outside the scope of this chapter.

Now, that we have discussed the fundamental requirements
and purposes of MCMC, there are three major implementations
of MCMC used in practice:

- Metropolis-Hastings
- Gibbs Sampling
- Hamiltonian Monte Carlo

### Metropolis-Hastings Algorithm (MHA)

Metropolis-Hastings is a common type of MCMC that
aims to provide a method of sampling from a
posterior distribution, $\pi(x)$ that does not have
a fixed equation for its density. In this case,
it is still required that you have an equation
for the probability $p(x)$ from the unknown
posterior distribution $\pi$.

In this case, MHA starts with a MCMC-compliant
Markov chain to generate a sequence of $\theta^{s}$
that asymptotically converge to the posterior
distribution. Now, we select an arbitrary state
on the Markov chain, $\theta^{(0)}$, and we want to move
to $\theta^{(1)}$.

The first step for this process is to generate a candidate
state $\theta^c$ which originates from a
candidate distribution, $\alpha$ that we know how to sample from,
this is similar to rejection sampling from {ref}`sec:random_variates`, for example, a
Gaussian, $\alpha|\theta^{(s-1)} \sim \mathcal{N}(x_{n}, \sigma^2)$.

After doing this step, we then move on to the accept-reject
step. Where the acceptance probability, which is defined through this expression:

```{raw} latex
\begin{figure}[htbp]
    \[
        \alpha(\boldsymbol{\theta}^{(s-1)}, \boldsymbol{\theta}^{c}) = \min \left\{ \frac{q(\boldsymbol{\theta}^{(s-1)} \mid \boldsymbol{\theta}^{c})\pi(\boldsymbol{\theta}^{c} \mid \boldsymbol{y})}{q(\boldsymbol{\theta}^{c} \mid \boldsymbol{\theta}^{(s-1)})\pi(\boldsymbol{\theta}^{(s-1)} \mid \boldsymbol{y})}, 1 \right\},
    \]
    \caption{\textbf{Acceptance-Rejection Ratio.} This equation defines the acceptance probability $\alpha(\boldsymbol{\theta}^{(s-1)}, \boldsymbol{\theta}^{c})$ for a proposed move in the Metropolis-Hastings algorithm. The ratio compares the posterior density $\pi$ and proposal density $q$ of the candidate state $\boldsymbol{\theta}^c$ against the current state $\boldsymbol{\theta}^{(s-1)}$. By accepting moves according to this probability, the algorithm corrects for asymmetry in the proposal distribution and ensures the Markov chain converges to the correct target posterior.}
    \label{fig:mh_acceptance_ratio}
\end{figure}
```

The overall algorithm can be expressed using this
sequence based on {cite}`robert1999monte`:

```{raw} latex
\begin{algorithmic}[1]
    \State \textbf{Initialization:} Choose an initial value $\boldsymbol{\theta}^{(0)}$ satisfying $\pi(\boldsymbol{\theta}^{(0)} \mid \boldsymbol{y}) > 0$.
    \State Set iteration counter $s = 1$.
    \While{$s \leq N$}
        \State \textbf{Proposal:} Generate a candidate state $\boldsymbol{\theta}^c$ from the proposal distribution:
        \[
            \boldsymbol{\theta}^c \sim q(\cdot \mid \boldsymbol{\theta}^{(s-1)})
        \]
        \State \textbf{Acceptance Probability:} Calculate the acceptance ratio $\alpha$:
        \[
            \alpha = \min \left\{ \frac{\pi(\boldsymbol{\theta}^c \mid \boldsymbol{y}) q(\boldsymbol{\theta}^{(s-1)} \mid \boldsymbol{\theta}^c)}{\pi(\boldsymbol{\theta}^{(s-1)} \mid \boldsymbol{y}) q(\boldsymbol{\theta}^c \mid \boldsymbol{\theta}^{(s-1)})}, 1 \right\}
        \]
        \State \textbf{Accept/Reject:} Generate a uniform random number $u \sim \mathcal{U}(0,1)$.
        \If{$u \le \alpha$}
            \State $\boldsymbol{\theta}^{(s)} \gets \boldsymbol{\theta}^c$ \Comment{Accept the candidate}
        \Else
            \State $\boldsymbol{\theta}^{(s)} \gets \boldsymbol{\theta}^{(s-1)}$ \Comment{Reject; stay at current state}
        \EndIf
        \State Increment $s \gets s + 1$.
    \EndWhile
\end{algorithmic}
```

Here is a trivial example of a problem that can be solved
using MHA. Let's assume that we don't have the ability
to directly sample from a exponential distribution, $\pi =
exp(-x), x \ge 0$. Then we could do the following,


In Python, this is possible to implement using this snippet
of code:

```{code} python
```

And there is a series of diagnostics that can help improve
MHA:



### Gibbs Sampling


The overall algorithm can be expressed using this
sequence based on {cite}`robert1999monte`:

```{raw} latex
\begin{algorithm}[htbp]
\caption{The Gibbs Sampler (Systematic Scan)}
\begin{algorithmic}[1]
    \State \textbf{Initialization:} Start with an arbitrary value $\boldsymbol{\theta}^{(0)} = (\theta_1^{(0)}, \dots, \theta_d^{(0)})$.
    \State Set iteration counter $s = 1$.
    \While{$s \leq N$}
        \For{$j = 1$ to $d$}
            \State \textbf{Full Conditional Update:} Sample $\theta_j^{(s)}$ from the conditional distribution given all other parameters at their most recent values:
            \[
                \theta_j^{(s)} \sim \pi(\theta_j \mid \theta_1^{(s)}, \dots, \theta_{j-1}^{(s)}, \theta_{j+1}^{(s-1)}, \dots, \theta_d^{(s-1)}, \boldsymbol{y})
            \]
        \EndFor
        \State $\boldsymbol{\theta}^{(s)} \gets (\theta_1^{(s)}, \dots, \theta_d^{(s)})$
        \State Increment $s \gets s + 1$.
    \EndWhile
\end{algorithmic}
\end{algorithm}
```

### Hamiltonian Monte Carlo (HMC)


The overall algorithm can be expressed using this
sequence:

```{raw} latex
\begin{algorithm}[htbp]
\caption{Hamiltonian Monte Carlo (HMC)}
\begin{algorithmic}[1]
    \State \textbf{Initialization:} Choose $\boldsymbol{\theta}^{(0)}$. Set step size $\epsilon$ and number of leapfrog steps $L$.
    \State Define potential energy $U(\boldsymbol{\theta}) = -\log \pi(\boldsymbol{\theta} \mid \boldsymbol{y})$.
    \State Set iteration counter $s = 1$.
    \While{$s \leq N$}
        \State \textbf{Sample Momentum:} Draw $\mathbf{p}^{(s-1)} \sim \mathcal{N}(\mathbf{0}, \mathbf{M})$ (usually $\mathbf{M} = \mathbf{I}$).
        \State \textbf{Initialize Trajectory:} Set $\boldsymbol{\theta}^* = \boldsymbol{\theta}^{(s-1)}$ and $\mathbf{p}^* = \mathbf{p}^{(s-1)}$.
        
        \State \textit{// Leapfrog Integration}
        \State $\mathbf{p}^* \gets \mathbf{p}^* - \frac{\epsilon}{2} \nabla U(\boldsymbol{\theta}^*)$
        \For{$i = 1$ to $L$}
            \State $\boldsymbol{\theta}^* \gets \boldsymbol{\theta}^* + \epsilon \mathbf{M}^{-1} \mathbf{p}^*$
            \If{$i \neq L$}
                \State $\mathbf{p}^* \gets \mathbf{p}^* - \epsilon \nabla U(\boldsymbol{\theta}^*)$
            \EndIf
        \EndFor
        \State $\mathbf{p}^* \gets \mathbf{p}^* - \frac{\epsilon}{2} \nabla U(\boldsymbol{\theta}^*)$
        \State \textbf{Momentum Flip:} $\mathbf{p}^* \gets - \mathbf{p}^*$ (for theoretical reversibility).

        \State \textbf{Metropolis Correction:} Calculate acceptance probability $\alpha$:
        \[
            H_{current} = U(\boldsymbol{\theta}^{(s-1)}) + \frac{1}{2} (\mathbf{p}^{(s-1)})^T \mathbf{M}^{-1} \mathbf{p}^{(s-1)}
        \]
        \[
            H_{prop} = U(\boldsymbol{\theta}^*) + \frac{1}{2} (\mathbf{p}^*)^T \mathbf{M}^{-1} \mathbf{p}^*
        \]
        \[
            \alpha = \min \left\{ \exp(H_{current} - H_{prop}), 1 \right\}
        \]

        \State \textbf{Accept/Reject:} Generate $u \sim \mathcal{U}(0,1)$.
        \If{$u \le \alpha$}
            \State $\boldsymbol{\theta}^{(s)} \gets \boldsymbol{\theta}^*$
        \Else
            \State $\boldsymbol{\theta}^{(s)} \gets \boldsymbol{\theta}^{(s-1)}$
        \EndIf
        \State Increment $s \gets s + 1$.
    \EndWhile
\end{algorithmic}
\end{algorithm}

```

## MCMC as a tool of Last Resort

When probabilities have higher dimensions, it becomes difficult
to use standard methods for variance reduction, requiring MCMC
instead.

## MCMC as a Method for Importance Sampling

a

