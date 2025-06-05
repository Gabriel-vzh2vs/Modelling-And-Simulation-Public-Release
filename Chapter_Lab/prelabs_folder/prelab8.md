(prelab-8)=
# Pre-Lab 8: Demonstration of Differential Equations in Simulation and Modelling (Read)

:::{admonition} Advisory: Chapter Reading
:class: warning dropdown

It is highly recommended that the reader read {ref}`sec:system_modeling`
before reading this pre-lab, as it provides more details and critical context
about the topics discussed as this pre-lab covers a bit about modelling.

:::

## ODEs for Modelling and Simulation

::::{tab-set} ODEs for Modelling

These examples of using ODEs for modelling are inspired by
{cite}`harte1988consider`, which might sound a bit silly if you read the title,
but it is a landmark work in modelling and problem-solving in Environmental Science.

:::{tab-item} Example 1: Depleting Resources

## Example 1: Depleting Resources

If the current rate of coal consumption in the United States of America increases by 6 percent annually,
what is the length of $T$, the amount of time before the depletion of coal reserves?

This example assumes that coal consumption is increasing monotonically and exponentially.
Although, this is unrealistic ([as coal usage is declining](https://www.eia.gov/energyexplained/coal/imports-and-exports.php)),
it is a useful assumption for simply modelling this as an Ordinary Differential Equation.

Based on the information above the instantaneous consumption rate is defined as the following:

```{math}
I(t) = I(0) * e^{rt}
```

Now, the initial rate for coal consumption must be defined, which in this case, this book
uses the rate from [US Energy Information Administration](https://www.eia.gov/energyexplained/coal/use-of-coal.php),
which is defined as $F(0) = 512.6 * 10^6$ short tons per year. And we have our rate constant, $r$ with units ($yr^{-1}$),
because of the the 6 percent annual figure which is defined as $e^{r(1)} = 1.06$ which becomes r = 0.0582689 through
$log_e(1.06) = 0.0582689$.

If $C(t)$ is the amount of coal remaining at time $t$, then $C(0) = 250 * 10^9$ short tons,
which comes from the EIA again, then the rate of change of $C(t)$ is defined as the separable ODE:

```{math}
\frac{dC}{dt} = -I(0) e^{r * t}
```

Which, as with all separable ODEs is integrated into its solution, with the integration variable, $t'$
being defined with the bounds of 0 to t:

```{math}
\int_{C(0)}^{C(t)} dC = - \int_{0}^{t} dt^{'} * I(0) * e^{rt'} \rightarrow C(t) - C(0) = \frac{-I(0)}{r} e^{rt} + \frac{I(0)}{r}
```

When C becomes zero, the coal resources will be depleted as seen below in a simplified form (after applying logs to both sides):

```{math}
rT = log(1 + \frac{r * I(0)}{C(0)})
```

And once we substitute $r$, $I(0)$, and $C(0)$ for our value and perform algebra, we will get the final value of T.

```{math}
T = 58.035 
```

### Python Implementation

```{code} python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Given values
I0 = 512.6 * 10**6
C0 = 250 * 10**9 
r = sp.ln(1.06) 

# Define the symbols
t = sp.symbols('t')
T = sp.symbols('T')

# Standard Solution Steps...
equation = sp.Eq(r * T, sp.ln(1 + (r * C0) / I0))
T_solution = sp.solve(equation, T)[0]
# print(f"The time until coal reserves are depleted is approximately {T_solution.evalf()} years.")
C_t = C0 - (I0 / r) * (sp.exp(r * t) - 1)

# Prep for Plot.
C_t_func = sp.lambdify(t, C_t, modules=['numpy'])
time_values = np.linspace(0, float(T_solution), 500)
coal_reserves = C_t_func(time_values)

# Plot the coal reserves over time
coal_fig = plt.figure(figsize=(7, 5))
plt.plot(time_values, coal_reserves, label='Coal Reserves Over Time')
plt.axhline(0, color='red', linestyle='--', label='Depletion Point')
plt.xlabel('Time (years)')
plt.ylabel('Coal Reserves (short tons)')
plt.title('Coal Reserves Over Time with Exponential Consumption Growth')
plt.legend()
plt.grid(True)
plt.show()
```

"By-Hand" Calculations for T from the final step:

```{code} python
import math

I0 = 512.6e6 # Initial consumption rate in short tons/year
r = math.log(1.06) # Growth rate per year
C0 = 250e9  # Initial coal reserves in short tons

# Solve for T using the equation rT = ln(1 + (r * C0) / I0)
T = math.log(1 + (r * C0) / I0) / r
print(T)

58.03467863647038
```

Output:

```{figure} ../../Figs/Chapter_Lab/Coal_Reserves.png
:label: fig:Coal_Res

A visualization of the ODE representing the exhaustion of the coal reserves in the
United States of America as an ODE model.
```

:::

:::{tab-item} Example 2: Chemical Kinetics

## Example 2: Chemical Kinetics

A common use for modelling ODEs is to improve the manufacturing processes of
chemical manufacturing, and this general concept is called **Chemical Kinetics.**

This example will focus on one of the most common reactions in chemistry, a synthesis
via dissolution reaction between sulfur trioxide ($SO_{3}$) and water ($H_{2}O$) that
produces sulfuric acid ($H_{2}SO_{3}$), a [common reagent](https://www.ams.usda.gov/sites/default/files/media/Sulfuric%20acid%20report.pdf) 
used in food acids (i.e. citric acid), high-fructose corn syrup, fertilizer production,
and electronic chip production.



:::

::::

## PDEs for Modelling and Simulation

PDEs ...

::::{tab-set}

:::{tab-item} Example 1: Heat flow in a uniform rod

:::

:::{tab-item} Example 2: Brownian motion

```{figure} #fig:MCvis_Brownian
:label: fig:brownian_motion

This is an visualization of a Monte Carlo Method Instance (n = 100) on for Brownian Motion 
using the aleatory Python package for simulation and visualization. 
```

:::

::::

## SDEs for Modelling and Simulation

SDEs ....

::::{tab-set}

:::{tab-item} Example 1: Poisson Point Process (Pure Birth Process)

https://personal.ntu.edu.sg/nprivault/MA5182/stochastic-calculus-jump-processes.pdf (Source)

```{figure} #fig:MCvis_poi
:label: fig:poisson_process

This is an visualization of a Monte Carlo Method Instance (n = 100) on a Poisson Point Process 
using the aleatory Python package for simulation and visualization. 
```

:::

:::{tab-item} Example 2: Cholera Epidemiology
https://onlinelibrary.wiley.com/doi/10.1155/2023/7232395 (Source)
:::

::::

## IDEs for Modelling and Simulation

IDEs ...

::::{tab-set}

:::{tab-item} Example 1: SEIR Model
https://web.archive.org/web/20200321190642/http://people.oregonstate.edu/~medlockj/other/IDE.pdf (Source)

:::

:::{tab-item} Example 2: City Growth and Emergence
https://royalsocietypublishing.org/doi/10.1098/rsif.2022.0176 (Source)

:::

::::

## Solving DEs with Python

### ODE45

### Runge-Kutta Methods

### Approximations and Their Methods