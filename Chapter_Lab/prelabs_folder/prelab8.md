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
via hydration reaction between sulfur trioxide ($SO_{3}$) and water ($H_{2}O$) that
produces sulfuric acid ($H_{2}SO_{3}$), a [common reagent](https://www.ams.usda.gov/sites/default/files/media/Sulfuric%20acid%20report.pdf)
used in food acids (i.e. citric acid), high-fructose corn syrup, fertilizer production,
and electronic chip production.

There is a common method for modelling this process as an set of ODEs is the
'Brusselator', a series of ODEs that applies to reactions where one or more of the reactants
is a catalyst (a chemical that reduces the energy needed to start the reaction). And this
work is inspired by [Smolander, 2010](https://www.simiode.org/resources/7211/download/2010-Smolander-DEForChemicalKinetics.pdf).

To setup the Brusselator, the chemical reaction must be defined thermodynamically per reactant
and product, e.g. the chemical that comes out of the reaction, sulfuric acid.

```{math}
\frac{\partial [H_{2}SO_{4}]}{\partial t} = k_1 [SO_3] [H_2O]\\

\frac{\partial [SO_{3}]}{\partial t} = -k_1 [SO_3] [H_2O]\\

\frac{\partial [H_{2}O]}{\partial t} = -k_1 [SO_3] [H_2O]
```

In this case, $k_1$ is defined as the rate constant[^1] of the reaction which is $5.0^-15$
mols per second by definition.

However, like most chemical reactions we have unwanted by-products, in this case, the
secondary reaction ($CH_4 + 2O_2 \rightarrow$ $CO_2 + H_2O$: k_{2}) exists because the environment has methane
and oxygen gases in the environment; there are ways in reactors to eliminate these by-products,
but seals are not perfect. This is one of the limitations of this model, it cannot handle a secondary reaction
sequences like the one above.

```{math}
\frac{\partial [CH_{4}]}{\partial t} = -k_2 [CH_4] [O_2]^{2}\\

\frac{\partial [O_{2}]}{\partial t} = - 2 k_2 [CH_4] [O_2]^{2}\\

\frac{\partial [CO_{2}]}{\partial t} = k_2 [CH_4] [O_2]^{2} \\

\frac{\partial [H_{2}O]}{\partial t} = 2 k_2 [CH_4] [O_2]^{2} \\
```

When a reader looks at [Mathematical Modelling of the Brusselator](https://www3.nd.edu/~powers/mcdowell.pdf), the following structure is revealed:

```{math}
A \rightarrow X: k_1 | \frac{\partial X}{\partial t} = -k_1[A]\\

2*X + Y \rightarrow 3X: k_2 | \frac{\partial[X]}{\partial t} = k_2 [X]^2 [Y] \text{ and } \frac{\partial[Y]}{\partial t} = -k_2 [X]^2 [Y]\\

B+X \rightarrow Y + C: k_3 |  \frac{\partial[X]}{\partial t} =  - k_3 [X]^2 [Y] \text{ and } \frac{\partial[Y]}{\partial t} = k_3 [X]^2 [Y]\\

X \rightarrow D: k_4 | - \frac{\partial X}{\partial t} k_4 [X]\\
```

Which when combined into $\frac{\partial x}{\partial t}$ and $\frac{\partial y}{\partial t}$, these equations come out:

```{math}
\frac{\partial x}{\partial t} = -k_1[A] + k_2[X]^2[Y] - k_3[X][B] -k_4[X]\\
\frac{\partial y}{\partial t} = -k_2[X]^2[Y] + k_3[X][B]
```

The graph of the general system of ODEs is below:

```{figure} ../../Figs/Chapter_Lab/ODE_Example2.png
:label: fig:Example2ODESystem

This is a visualization of the system of ODEs above, which is provided by the code below:
```

```{admonition} Code for the Specific Reaction
:class: tip dropdown

::::{code-cell} python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def brusselator(A, B, X0, Y0, t_span, t_eval):
    """
    Solves and plots the Brusselator ODE system.

    Args:
        A (float): Parameter A in the Brusselator equations.
        B (float): Parameter B in the Brusselator equations.
        X0 (float): Initial concentration of species X.
        Y0 (float): Initial concentration of species Y.
        t_span (tuple): The interval of integration (t_start, t_end).
        t_eval (numpy.ndarray): Times at which to store the computed solution.
    """
    def model(t, Z):
        X, Y = Z
        dXdt = A + X**2 * Y - (B + 1) * X
        dYdt = B * X - X**2 * Y
        return [dXdt, dYdt]

    # Initial conditions
    Z0 = [X0, Y0]

    # Solve the ODE as a IVP
    sol = solve_ivp(model, t_span, Z0, t_eval=t_eval)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(sol.t, sol.y[0], label='X(t)')
    plt.plot(sol.t, sol.y[1], label='Y(t)')
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.title(f'Brusselator Oscillations (A={A}, B={B})')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Generic Parameter Example---
if __name__ == '__main__':
    # Parameters
    A = 1.0
    B = 3.0

    # Initial conditions
    X0 = 1.5
    Y0 = 3.0

    # Time points for the solution
    t_start = 0
    t_end = 50
    t_points = 1000
    t_span = (t_start, t_end)
    t_eval = np.linspace(t_start, t_end, t_points)

    brusselator(A, B, X0, Y0, t_span, t_eval)
::::

Which there are tons of solution methods, which one is provided through SymPy:

```{figure} ../../Figs/Chapter_Lab/ODE_Example3.png
:label: fig:Example2ODEFamilySolution

This is an visualization of the family of solution to a particular instance of 
the Brusselator with the parameters related to the reaction described above. 
```

```{admonition} Code for the Specific Reaction
:class: tip dropdown

:::::{code-cell} python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# --- Model Definition ---
# This function defines the system of Ordinary Differential Equations (ODEs)
# for the reaction: SO₃ + H₂O -> H₂SO₄ with a slight excess of water.

def sulfuric_acid_kinetics(y, t, k):
    """
    Defines the ODEs for the sulfuric acid formation.
    
    y: array of concentrations [c_SO3, c_H2O, c_H2SO4]
    t: time
    k: the second-order rate constant for the reaction
    """
    c_so3, c_h2o, c_h2so4 = y
    
    # Based on the rate law: Rate = k * [SO₃] * [H₂O]
    reaction_rate = k * c_so3 * c_h2o
    
    # Rate of change for each species (Reactants are consumed, Products are formed)
    d_c_so3_dt = -reaction_rate
    d_c_h2o_dt = -reaction_rate
    d_c_h2so4_dt = +reaction_rate
    
    return [d_c_so3_dt, d_c_h2o_dt, d_c_h2so4_dt]

# --- Simulation Parameters ---
# This is a standard interpretation in chemical kinetics.
k = 5.0e-15  # L/(mol·s)

# Set the initial concentrations ([SO₃], [H₂O], [H₂SO₄]) in mol/L
c_so3_initial = 1.0  # mol/L
c_h2o_initial = 1.1  # mol/L
c_h2so4_initial = 0.0 # Start with no product
y0 = [c_so3_initial, c_h2o_initial, c_h2so4_initial]

# Set the time range for the simulation.
# NOTE: The rate constant is extremely small, so the reaction is very slow, 
# usually you would add heat to this reaction to increase the likelihood of
# collisions (reactions), and therefore reactions. 
# A characteristic time scale is ~1/(k*C_initial) = 1/(5e-15*1) = 2e14 seconds.
t_end = 5e14 # seconds
t = np.linspace(0, t_end, 10000) # Time vector from 0 to t_end

# --- Solve the ODEs ---

# Solve the system of ODEs using odeint
# The 'args' parameter passes the rate constant 'k' to our function.
sol = odeint(sulfuric_acid_kinetics, y0, t, args=(k,))

# --- Plot the Results ---

plt.figure(figsize=(10, 6))
plt.plot(t, sol[:, 0], label='[SO₃] (Sulfur Trioxide)')
plt.plot(t, sol[:, 1], label='[H₂O] (Water)')
plt.plot(t, sol[:, 2], label='[H₂SO₄] (Sulfuric Acid)')

# Formatting the plot
plt.title('Kinetics of Sulfuric Acid Formation')
plt.xlabel('Time (seconds)')
plt.ylabel('Concentration (mol/L)')
plt.legend()
plt.grid(True)
plt.show()
:::::
```
:::

::::

## PDEs for Modelling and Simulation

PDEs ...

::::{tab-set}

:::{tab-item} Example 1: Heat Equation

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

[^1]: The process of finding the rate constant is typically done through calculating the
[reaction order](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Kinetics/03%3A_Rate_Laws/3.03%3A_The_Rate_Law/3.3.03%3A_Reaction_Order), then using data about
previous reactions to calculate the values for the [rate equation](https://chem.libretexts.org/Bookshelves/General_Chemistry/Chemistry_1e_(OpenSTAX)/12%3A_Kinetics/12.04%3A_Rate_Laws) and then solving. This work is not a work on chemistry, so these
concepts will not be covered in detail.
