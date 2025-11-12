:::{admonition} Lab 4
:class: danger dropdown
(lab-4)=
# Lab 4: Simulating Stochastic Processes with Monte Carlo Methods (Python + Excel)

## Lab 4 Prerequisites

### Pre-labs

- {ref}`prelab-4`

### Mandatory Chapters for Lab 4

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`sec:distribution_modeling`

### Optional Chapters for Lab 4

- {ref}
- {ref}

## Purpose and Patterns

### Statement of Model Purpose
This set of models serve a singular purpose: to demonstrate different techniques of
simulating stochastic processes based on observed data using Monte Carlo. Additionally,
this lab will also show the limitations of traditional Monte Carlo, if the reader has
led the optional chapters, then the alternative sampling methods are guaranteed to be
an improvement or the same.

### Patterns

## Entities, State Variables, and Scales

### State Variables and Scales (Lab 4)

```{raw} latex
\begin{tabular}{llll}
\hline
\textbf{Variable} & \textbf{Scale} & \textbf{Type} & \textbf{Description} \\
\hline
$p_{0}$ & $[0 - \infty]$ & Double & The initial value of the principal. \\
$r$ & $[-\infty - \infty]$ & Double & The rate of return which is often [0-100] percent, but can be any number. \\
$\bar{r}$ & $[0 - \infty]$ & Double & The average rate of return defined by the user. \\
$\sigma$ & $[0 - \infty]$ & Double & The standard deviation of the rate of return defined by the user. \\
$t$ & $[0 - 1]$ & Integer & The time horizon for the model. \\
$p_{t}$ & $[-\infty - \infty]$ & Double & The value of the return at step t. \\
$n$ & $[1 - \infty]$ & Integer & The number of experiments performed. \\
\hline
\end{tabular}
```

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
:::