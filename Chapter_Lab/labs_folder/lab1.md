:::{admonition} Lab 1
:class: tip dropdown

(lab-1)=
# Lab 1: Computing $\pi$ with Monte Carlo Methods (Excel or Python)

## Lab 1 Prerequisites

### Pre-labs

- {ref}`prelab-1`

### Required Chapters

- {ref}`sec:preface`
- {ref}`sec:prob_stats`
- {ref}`sec:buffons_needle_summary`

## Purpose and Patterns

### Statement of Model Purpose

This model's purpose is to demonstrate the concept of Monte Carlo Integration through calculating $\pi$
through random sampling from a uniform random variable.

### Patterns

#### Pattern 1. Unit Circle of Radius 1 and Square with Side Length 2

This pattern describes how $\pi$ is calculated with well-defined shapes without respect to units.
In this pattern, we obtain $\pi$ from our calculations in Excel when we consider
indicator variable to be equal to one when an experiment is within the union of the unit circle
and square with side-length 2. **This is the pattern that you should try to replicate.**

#### Pattern 2. Unit Circle of Radius 2 and Square with Side Length 1

This pattern describes a different region for Monte Carlo Integration,
as it fails to calculate $\pi$ as the circle surpasses the area of the square, and now it
calculates the area of the square instead as the area of integration is defined
through the greater of the two regions. **This is a malignant pattern.**

## Entities, State Variables, and Scales

### State Variables and Scale

In this context, the state variables relate to trials, in this instance,
a trial is represented as a point in a 2-dimensional plane.
Once you have enough trials, the indicator variable converges into
$\pi$ by the fact that a sufficient number of points reside in the union of
interest.

```{raw} latex
\begin{tabular}{llll}
\hline
\textbf{Variable} & \textbf{Scale} & \textbf{Type} & \textbf{Description} \\
\hline
$x$ & [-1 - 1] & Double & A sample of U[0,1] that determines the x-position of the trial \\
$y$ & [-1 - 1] & Double &  A sample of U[0,1] that determines the y-position of the trial \\
$z = x^2 + y^2 $ & [0 - 1] & Double & This refers to the variable that represents a circle's standard form.  \\
$|z| <= 1 $ & 0 or 1 & Binary & This is the binary that states is the point in the circle. \\
$x_{in}$ & [0 - 1] & Product of Double and Binary & The product of z and x that is used to show a point that exists within the circle. \\
$y_{in}$ & [0 - 1] & Product of Double and Binary & The product of z and y that is used to show a point that exists within the circle. \\
Darts in Circle, $D_{in}$ & [0 - $\infty$] & Double & This variable represents the summation over z. \\
Darts out of Circle, $D_{out}$ & [0 - $\infty$] & Double & The total number of points minus Darts in Circle. \\
Pi Approximation, $\hat{\pi}$ & [0 - $\infty$] & Double & The ratio of Darts in Circle over Darts out of Circle.\\
Percent Error & [0 - $\infty$] & Double & The percent difference ($\frac{|\hat{\pi}-\pi|}{\pi}$) between the approximation and $\pi$. \\
\hline
\end{tabular}
```

## Process Overview and Scheduling

### Processes

The model is developed to demonstrate the process of Monte Carlo Integration.
It is structured within three subprocesses, one related to the generation of samples
(updated samples from a uniform distribution into two variables, x and y) and their
placement onto a 2-D chart to show the uniformity of the random number generator,
another subprocess concerns the if statement determining whether any specific
point resides in the unit circle,
and the final subprocess referring to the construction of the state
variables $x_in$ and $y_in$, with a zero referring to a point that is out
of the unit circle and then removing the point or coloring it
differently than a point that is marked with its calculated value, along with
summing on z to calculate $D_{in}$, using this state variable along
with the total number of points in the circle to define the new state variables:
$D_{out}$, $\hat{\pi}$ (through the ratio, $\frac{D_{in}}{D_{out}}$), and
percent error with the process defined in state variables and scale.

The state variables are updated once at the beginning of the simulation when
the system is initialized. During this process, the user determines the number
of points, which changes the accuracy of the simulation.

### Scheduling (Lab 1)

The simulation starts when the sheet or program is initialized by the user.
Once it has been initialized, the first subprocess begins by starting the
random number generation for the first two state variables, $x$ and $y$
is the first task, because the subsequent state variables and subprocesses
depend on these initial variables. Afterwards, the subprocess for the placement of
points activates, plotting the points, triggering the third subprocess of determining
through an if statement the validity of the points (are they within the circle). Finally,
the fourth subprocess builds the state variables $x_in$, $y_in$, Darts in Circle,
Darts out of Circle, Pi Approximation, and Percent Error, based on the results of
state variables $z$, $x$, and $y$.

```{raw} latex
\begin{enumerate}
    \item \textbf{System Initialization:}
    \begin{enumerate}
        \item User defines the total number of random points ($N$) to be generated for the simulation.
        \item Initial state variables are set (e.g., $D_{in} = 0$, $D_{out} = 0$).
    \end{enumerate}

    \item \textbf{Random Sample Generation and Placement:}
    \begin{enumerate}
        \item Generate $N$ random $x$-coordinates from a uniform distribution (typically between -1 and 1, or 0 and 1 if considering a quadrant).
        \item Generate $N$ random $y$-coordinates from a uniform distribution (similarly, between -1 and 1, or 0 and 1).
        \item Plot the generated $(x, y)$ points on a 2-D chart.
    \end{enumerate}

    \item \textbf{Point Evaluation (In-Circle Check):}
    \begin{enumerate}
        \item For each generated point $(x, y)$:
        \begin{enumerate}
            \item Calculate $z = x^2 + y^2$.
            \item If $z \le 1$, the point is inside or on the unit circle.
            \item If $z > 1$, the point is outside the unit circle.
        \end{enumerate}
    \end{enumerate}

    \item \textbf{State Variable Construction and Calculation:}
    \begin{enumerate}
        \item For each point:
        \begin{enumerate}
            \item If the point is inside the unit circle (from step 3.1.2):
            \begin{enumerate}
                \item Assign the point's coordinates to $x_{in}$ and $y_{in}$ (or simply mark it as 'in').
                \item Increment the count of points inside the circle ($D_{in}$).
                \item Color or mark the point differently to distinguish it as inside.
            \end{enumerate}
            \item If the point is outside the unit circle (from step 3.1.3):
            \begin{enumerate}
                \item Assign a zero or null value to $x_{in}$ and $y_{in}$ for this point (or simply mark it as 'out').
                \item Remove the point or color it differently to distinguish it as outside.
                \item Increment the count of points outside the circle (or calculate $D_{out} = N - D_{in}$ after all points are processed).
            \end{enumerate}
        \end{enumerate}
        \item Calculate the approximation of Pi: $\hat{\pi} = 4 \times \frac{D_{in}}{N}$ (assuming the square enclosing the circle spans from -1 to 1 in both $x$ and $y$, thus having an area of 4; if using a quadrant, the ratio is multiplied by 4).
        \item Calculate the percent error: $Percent Error = \frac{|\hat{\pi} - \pi_{actual}|}{\pi_{actual}} \times 100\%$.
    \end{enumerate}
\end{enumerate}
```

## Design Concepts

### Basic Principles

This model depicts a classic problem of numerical integration using random numbers to
compute a multidimensional definite integral using $N$ uniform samples also known as Monte Carlo Integration through Crude Monte Carlo (CMC).
Moreover, this process leverages the Law of Large Numbers that allows for the average of the indictor variable, $\hat{\pi}$ to
converge to $\pi$ with a sufficient number of trials. In this case, we define the Law of Large Numbers as
Khinchin's Weak Law of Large Numbers: the observation that the average of the results obtained from a large number of
i.i.d random samples converges to the value, if it exists,
which is supported by Proof 1 in the appendix {ref}`sec:proofs`. {cite}`shum2024laws`
Additionally, the foundations of Monte Carlo Integration are further elaborated in one of the prerequisite chapters,
{ref}`sec:buffons_needle_summary`.

### Stochaticity

Stochaticity is used when initializing the model to build the uniform state variables
$x$ and $y$; this process allows for the usage of Monte Carlo Integration within the
defined region (the unit circle embedded within a square with side length of 2).
During the simulation, stochaticity is used to define the sample ($x, y$ points) that
defines the estimate of $\hat{\pi}$ and the visual representations of the points
through the subprocesses defined through the processes section.

## Input Data

There is no input data beyond then number of samples and the regions defined in
the functions that define the subprocesses.

## Questions left to the reader to answer

1. What happens to the estimate of $\pi$ when $N$, the number of points increases or decreases?
2. Why did we use the ODD approach for organizing our model despite its simplicity?  
:::