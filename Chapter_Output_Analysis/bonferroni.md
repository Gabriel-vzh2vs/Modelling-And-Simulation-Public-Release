# Bonferroni Correction

A significant issue when using statistics is the
[multiple comparisons problem](https://en.wikipedia.org/wiki/Multiple_comparisons_problem).
This occurs when multiple tests are performed  on the same set or when multiple inferences
are simultaneously tested on the same data set. This issue applies to testing and the
construction of confidence intervals.

The Bonferroni correction is a method to reduce the [family-wise error rate](https://en.wikipedia.org/wiki/Family-wise_error_rate)
(FWER) when doing multiple comparisons. The FWER refers to the probability of making one or more
false positives when performing multiple hypothesis tests
A statistical way of saying this is that it makes the series of tests more _conservative_, and that
they maintain their significance level.

:::{prf:definition} Bonferroni Correction
:label: bonferroni-correction
Let $m>0$ be an integer representing the number of hypotheses. Then let $\alpha_i$
represent the significance level for test $i$, and $\gamma_i$ represent the adjusted
significance level for test i. And let $\beta$ represent the overall
significance level. When written in this form:
\begin{equation}
  \gamma_i = \frac{\alpha_i}{m};
\end{equation}
it represents the significance level for each individual test, allowing
for the maintenance of $\beta$ across the family of tests when $\gamma_i$
replaces $\alpha_i$.

\begin{equation}
\beta = 1 - (1-\alpha_i)^m \rightarrow \beta = 1 - (1-\gamma_i)^m
\end{equation}
:::

## An Example of Bonferroni 
Insert Simulated Results for the Bonferroni Correction from Monte Carlo.

## Example 1 Related to Bonferroni in Output Analysis

## Problem 2 related to Bonferroni in Output Analysis