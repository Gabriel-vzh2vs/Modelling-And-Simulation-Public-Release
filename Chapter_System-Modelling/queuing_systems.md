(sec:queuing_systems)=
# Queuing Systems 

:::{note} Refinement 1
All of the existing content in this section should be considered provisional at best.
:::

## Introduction to Queues

We have previously introduced the concept of discrete event simulation and various modeling paradigms. Queueing systems represent a fundamental class of models used to analyze congestion, waiting lines, and resource sharing.

At its core, a queuing system is defined by three components:

- The Input Process: How customers (or jobs, packets) arrive at the system.
- The Service Mechanism: How long it takes to serve a customer and how many servers are available.
- The Queue Discipline: The rules describing how customers are selected for service (e.g., First-Come, First-Served).

Why do queues form? For example, if the average service rate is faster than the average arrival rate, why is there a queue? The answer lies in variability. If arrivals and service times were perfectly deterministic (e.g., exactly one customer every 5 minutes, and service takes exactly 4 minutes), no queue would ever form. Queues arise because of the stochastic nature in when customers arrive and how long it takes to serve them.

### The Exponential and Poisson Distributions

In probability courses and textbooks you may have heard about
the exponential distribution, one of the most prototypical
queuing systems ($M/M/1$) relies on the
Poisson and Exponential Distributions for its inter-arrival times and service rates respectively.


#### Poisson Distribution

The Poisson process is the most common mathematical model for "random" arrivals. If we say *singular* arrivals follow a Poisson process with rate $\lambda$, we imply:

- Independence: An arrival occurring now does not influence when the next arrival will occur.
- Stationarity: The average rate $\lambda$ is constant over time.

The probability of seeing exactly k arrivals in a time period t is given by the Poisson distribution's PMF:

```{math}
P(N(t) = k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}
```

The exponential distribution's CDF is defined as the following:

:::{math}
1-e^{x \lambda}
:::

Now, what are the properties that make exponential distributions useful for queuing's service rates?

:::{table}

| Property          | Description                                                                                                | Relevance to Queueing Models                                                                                                                                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Memoryless** | The probability of an event occurring in the future is independent of how much time has already elapsed. $P(T > s+t \mid T > s) = P(T > t)$. | Which Simplifies analysis significantly. For example, the remaining service time for a customer is independent of how long they've already been served. Similarly, the time until the next arrival doesn't depend on when the last arrival occurred. |
| **Relationship to Poisson Process** | If the number of arrivals in a given time interval follows a Poisson distribution, then the inter-arrival times (the time between successive arrivals) are exponentially distributed. | Many real-world arrival patterns (e.g., customers at a bank, calls to a call center) can be reasonably approximated by a Poisson process, making the exponential distribution a natural choice for inter-arrival times.                        |
| **Mathematical Tractability** | The mathematical form of the exponential distribution (PDF: $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$) often leads to simpler analytical solutions for queueing metrics like average wait time, queue length, and server utilization. | Allows for the derivation of closed-form analytic solutions for many queueing models (e.g., M/M/1, M/M/c).                                               |
| **Constant Hazard Rate** | The instantaneous probability of an event (e.g., service completion or arrival) occurring is constant over time. The hazard rate is equal to the rate parameter $\lambda$. | Reflects situations where the likelihood of an event happening in a small time interval doesn't change based on how long the process has been running. This can be a reasonable assumption for many service or arrival processes.          |
| **Single Parameter** | The distribution is characterized by a single parameter, $\lambda$ (the rate parameter), which is the inverse of the mean ($1/\mu$ where $\mu$ is the mean time between events). | Simplifies parameter estimation from observed data. Only one value needs to be determined to define the distribution for either arrival rates or service rates.                                                                            |

:::

## Little's Law

Before diving into specific queue configurations, we must
introduce one of the most powerful theorems in queuing theory:
Little's Law.

It states that for any _stable_ queuing system, the average
number of customers in the system (L) is equal to the average
effective arrival rate ($\lambda$) multiplied by the average
time a customer spends in the system (W).

```{math}
L = \lambda W
```

Which we can extend to the Queue itself through $L_q$:

```{math}
L_q = \lambda W_q
```

In this case, a stable queuing system means that the average
arrival rate of customers is lower than the average service
rate of the system ($W < \lambda$).

Intuition: Imagine a crowded nightclub. If people are arriving
at a rate of 50 per hour ($λ=50$) and every person stays inside
for an average of 2 hours ($W=2$), then at any given time, you
can expect to find $50 \cdot 2=100$ people inside ($L=100$).

This law allows us to calculate waiting times if we know the queue length, or vice versa, without knowing the complex probability distributions involved.

## Specifying the System

To mathematically analyze a queue, we must rigorously define its characteristics. This is standardized through a shorthand known as Kendall's Notation.

### Kendall's Notation for Queues

How do we formally represent a queue? For example, what does $M/M/1$ actually signify? In general, every queue is described by the format $A/B/c/K/N/D$, though the last three parameters are often omitted when they assume default values (infinite capacity, infinite population, FIFO).

:::{table}
:label: Kendall-Notation

| Position | Description                      | Common Symbols                                                                                                |
| :------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **A** | **Arrival Process** | M (Markovian/Poisson), D (Deterministic/Constant), E$_k$ (Erlang), G or GI (General/General Independent)                      |
| **B** | **Service Time Distribution** | M (Markovian/Exponential), D (Deterministic/Constant), E$_k$ (Erlang), G (General)                                  |
| **c** | **Number of Servers** | Integer value (1, 2, 3, ..., $\infty$)                                                                                      |
| **K** | **System Capacity** (Optional)      | Integer value (maximum number of customers in the system, including those being served), $\infty$ if omitted     |
| **N** | **Calling Population** (Optional)   | Integer value (size of the population from which customers arrive), $\infty$ (if omitted)                        |
| **D** | **Queue Discipline** (Optional)     | FIFO/FCFS (First-In, First-Out/First-Come, First-Served), LIFO/LCFS (Last-In, First-Out/Last-Come, First-Served), SIRO (Service In Random Order), PRI (Priority) |

:::

### M/M/1 Queue Example

Using the {ref}`Kendall-Notation` above, we can determine that a $M/M/1$ queue is a
queue with a Markovian Arrival Process, a Service time that is Markovian, and one server.

Consider a basic server where jobs arrive and are processed one by one. If we assume the inter-arrival times and service times are exponentially distributed, we can calculate system behaviors using closed-form formulas.

Key parameters include:
* $\lambda$: The arrival rate (customers per unit time).
* $\mu$: The service rate (customers served per unit time).
* $\rho$: The utilization factor, defined as $\lambda / \mu$.

For the system to be stable (i.e., the queue does not grow infinitely), we must assume $\rho < 1$.


:::{table}
:label: MM1Performance-Metrics

| Performance Measure                      | Symbol        | Formula                                         |
| :--------------------------------------- | :------------ | :---------------------------------------------- |
| Arrival Rate                             | $\lambda$     | Given                                           |
| Service Rate                             | $\mu$         | Given or $\frac{1}{\text{service time}}$         |
| Server Utilization (Traffic Intensity)   | $\rho$        | $\frac{\lambda}{\mu}$                           |
| Probability of an Empty System           | $P_0$   | $1 - \rho$                                            |
| Probability of $n$ customers in the system | $P_n$       | $P_0 \rho^n = (1-\rho)\rho^n$                   |
| Average Number of Customers in the System | $L$ or $L_s$ | $\frac{\lambda}{\mu - \lambda} = \frac{\rho}{1-\rho}$ |
| Average Number of Customers in the Queue  | $L_q$        | $\frac{\lambda^2}{\mu(\mu - \lambda)} = \frac{\rho^2}{1-\rho}$ |
| Average Time a Customer Spends in the System | $W$ or $W_s$ | $\frac{1}{\mu - \lambda} = \frac{L}{\lambda}$     |
| Average Time a Customer Spends in the Queue  | $W_q$     | $\frac{\lambda}{\mu(\mu - \lambda)} = \frac{L_q}{\lambda}$ |
| Probability that the number of customers in the system is greater than or equal to *n* | $P(\text{N} \ge n)$ | $\rho^n$ |
| Probability that the waiting time in the queue is greater than *t* (for $t \ge 0$) | $P(T_q > t)$ | $\rho e^{-(\mu-\lambda)t}$|
| Probability that the system time is greater than *t* (for $t \ge 0$) | $P(T_s > t)$ | $e^{-(\mu-\lambda)t}$|

:::

### Extensions

In the real world, systems are often more complex than
$M/M/1$, some examples of common systems and queuing networks
are:

- M/M/c (Multi-Server): Queues like bank tellers or airport check-in counters have multiple servers fed by a single line. The math becomes more complex (using the [Erlang-C formula](https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_C_formula)), but the concept of pooling resources generally reduces waiting times compared to separate lines for each server.

- M/G/1 (General Service): Often, service times are not exponential (memoryless). If service times are tightly clustered around a mean (low variance), queues are smaller. If service times have a high variance, queues are longer. The [Pollaczek–Khinchine](https://en.wikipedia.org/wiki/Pollaczek%E2%80%93Khinchine_formula) formula is used here, showing that queue length depends on the variance of the service time, not just the mean.

- G/G/1 (General Arrival & Service): When neither arrivals nor service times fit standard distributions, we cannot use simple formulas. This is where Discrete Event Simulation (DES) becomes the primary tool for analysis.

## Summary

Queuing systems provide a powerful framework for analyzing delays and resource utilization. While this chapter focused on the analytical tractability of the M/M/1 queue, more complex systems (like those with general distributions G/G/1) often require the simulation techniques discussed in previous chapters.