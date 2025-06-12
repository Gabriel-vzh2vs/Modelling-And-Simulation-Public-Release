---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


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

:::{admonition} Note: Discretization
:class: hint dropdown

In many instances, PDEs are discretized (made into discrete systems of differential equations)
particularly for numerical solutions. This note is here to advise the reader that more information
about discretization is in {ref}`sec:system_modeling`, as some of the code and language in this section
would be confusing without that context.
:::

All ODEs are special cases[^2] of the greater family of Partial Differential Equations,
and in this section of this pre-lab, the reader will be exposed to some common applications
of Partial Differential Equations.

### Example 1: The Heat Equation

The heat equation refers to a parabolic[^3] Partial Differential Equation that describes
how heat is transmitted through different materials. Moreover, this equation has found its way
into almost every Partial Differential Equation textbook and into many fields of study in different
ways: the Black–Scholes equation is an implementation of the heat equation, Fokker–Planck equation in
Brownian motion, and back to physics through Schrödinger's equation. Here's a link to a
dynamic visualization [link](https://visualpde.com/sim/?preset=heatEquation). It can also be
considered as a Markov Chain.

This text describes of the most common examples of the heat equation: the transportation of
heat across a finite, one dimensional rod with homogeneous boundary conditions. The reader might
be wondering, what does that mean? In this case, we are considering a metal rod that is made
up of consistent material, with boundaries that perfectly remove heat from the system such as an ice
block, and that the rod has a width approaching zero (one-dimensional).

These conditions allow for the application of the following boundary problem in the context of an
1-D Heat Equation which is often used for solving Initial Value Problems:

```{math}
\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2} &   & 0 < t; 0 \leq x \leq L 
```

```{figure} ../../Figs/Chapter_Lab/PDE_Example.png
:label: fig:PDE_Example

This is a visualization of the finite difference method compared with exact solutions
for the 1-d heat equation described above.
```

```{admonition} Code for this PDE (Heat Equation)
:class: tip dropdown

:::{code-block} python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Method of Manufactured Solutions: exact solution
def u_exact(x, t):
    return np.exp(-t) * np.cos(x)

# Parameters
t_span = [0.0, 1.0]
x_span = [0.0, 1.0]
dx = 0.1
nx = int(x_span[1] / dx) + 1
x = np.linspace(x_span[0], x_span[1], nx)
t_eval = np.arange(t_span[0], t_span[1] + 0.2, 0.2)

# Initial condition for IVP
u0 = u_exact(x, t_span[0])

# PDE function (discretized in space)
def pde_func(t, u):
    dudt = np.zeros_like(u)
    
    # Central difference for 2nd derivative
    for i in range(1, nx - 1):
        dudt[i] = (u[i-1] - 2*u[i] + u[i+1]) / dx**2
        
    # Boundary conditions
    dudt[0] = 0 # Corresponds to u(t, 0) boundary condition.
    dudt[-1] = 0 # Corresponds to u(t, 1) boundary condition

    return dudt

# Create a function to handle the boundary conditions within the solver
def ode_with_bcs(t, u):
    dudt = pde_func(t, u)
    u[0] = np.exp(-t)
    u[-1] = np.exp(-t) * np.cos(1)
    return dudt

# Solve the ODE problem
sol = solve_ivp(ode_with_bcs, t_span, u0, t_eval=t_eval, rtol=1e-6, atol=1e-6)

# Plot results and compare with exact solution
plt.figure(figsize=(10, 6))

for i, t_point in enumerate(sol.t):
    plt.plot(x, sol.y[:, i], 'o-', label=f'Numerical, t={t_point:.1f}')
    plt.plot(x, u_exact(x, t_point), 'x--', label=f'Exact, t={t_point:.1f}')

plt.xlabel('x')
plt.ylabel('u(t, x)')
plt.title('Heat Equation Numerical vs. Exact Solution')
plt.legend()
plt.grid(True)
plt.show()
:::
```

Now, assume that more detail is added to this problem where
$k$ refers to the thermal conductivity of the material, and this example
will assume that the thermal conductivity of a Copper - Aluminum Bronze (95% Cu, 5% Al)
alloy which is $83$ Watts per meter-Kelvin[^4]. And a temperature of 200 C that is localized to
20 percent of the rod's surface, to make it easier to visualize the heat equation along
a 1-D line. Additionally, one of the typical methods for solving this heat equation is using
[fourier series](https://en.wikipedia.org/wiki/Heat_equation#Solving_the_heat_equation_using_Fourier_series),
but this work will use a different method, which is the finite difference method which was discussed above in
the code.

```{figure} ../../Figs/Chapter_Lab/heat_diffusion.gif
:label: fig:hd_gif

This is a visualization of the heat equation has been modified to meet the 
requirements above, and shows the _forward_ progression of simulated 
heat throughout a 1-D rod. 
```

:::{admonition} Code for the visualization above (Heat Diffusion)
:class: tip dropdown

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve
import ipywidgets as widgets
from IPython.display import display

def solve_heat_equation(L=1, T=200.0, Nx=100, Nt=5000, center_temp=200):
    """
    Solves the 1D heat equation with a central point heat source as the initial condition.
    """
    x = np.linspace(0, L, Nx + 1)
    t = np.linspace(0, T, Nt + 1)
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    # Thermal properties for Copper-Aluminum Bronze (95% Cu, 5% Al)
    k = 83      # Thermal conductivity in W/mK
    rho = 7450  # Density in kg/m^3
    cp = 419    # Specific heat capacity in J/kgK
    alpha = k / (rho * cp)

    F = alpha * dt / dx**2

    u = np.zeros((Nx + 1, Nt + 1))

    # The rod starts at 0°C
    u[:, 0] = 0.0
    
    # Heat a small region in the center of the rod to simulate a point source
    center_index = Nx // 2
    # Heat a region approximately 2% of the rod's length
    heat_width = max(1, int(Nx * 0.02)) 
    start_index = center_index - heat_width // 2
    end_index = center_index + heat_width // 2
    u[start_index:end_index + 1, 0] = center_temp

    # Boundary conditions remain 0
    u[0, :] = 0
    u[Nx, :] = 0

    # Create the diagonals for the sparse matrix A
    main_diag = (1 + 2 * F) * np.ones(Nx - 1)
    off_diag = -F * np.ones(Nx - 1)
    A = spdiags([off_diag, main_diag, off_diag], [-1, 0, 1], Nx - 1, Nx - 1).tocsc()

    # Solve the system of equations at each time step
    for n in range(Nt):
        b = u[1:Nx, n]
        u[1:Nx, n + 1] = spsolve(A, b)

    return x, t, u

def plot_heat_distribution(t_val, center_temp):
    """
    Plots the temperature distribution at a specific time.
    """
    L = 1
    T = 200.0   # Maximum time for the simulation
    Nx = 100
    Nt = 5000   # Number of time steps

    x, t, u = solve_heat_equation(L, T, Nx, Nt, center_temp)
    
    # Find the index in the time array corresponding to the slider's value
    t_index = np.argmin(np.abs(t - t_val))

    plt.figure(figsize=(10, 6))
    plt.plot(x, u[:, t_index])
    plt.title(f'Temperature Distribution at t = {t[t_index]:.2f} s')
    plt.xlabel('Position along the rod (m)')
    plt.ylabel('Temperature (°C)')
    plt.ylim(-5, center_temp + 10)
    plt.grid(True)
    plt.show()

# Create interactive widgets
time_slider = widgets.FloatSlider(
    value=0.1,
    min=0.0,
    max=200.0,
    step=0.1,
    description='Time (s):',
    continuous_update=False,
    readout_format='.1f',
)

temp_slider = widgets.FloatSlider(
    value=200,
    min=50,
    max=500,
    step=10,
    description='Center Temp (°C):', 
    continuous_update=False,
)

# Link the plotting function to the widgets
widgets.interactive(plot_heat_distribution, t_val=time_slider, center_temp=temp_slider)
```

:::

### Example 2: SIR

:::{admonition} Note: ABM Version
:class: warning dropdown

There is a ABM (graph and non-graph) version of this model in {ref}`prelab-10`.
As this model is mostly made to show an application of a PDE that has some
practical use as a tool to explain and model human behavior.

:::

The compartmental model for disease spread has existed for over a century and SIR was the
first and simplest model to exist, it is often expressed as three ODEs (often called the SIR
model without birth and death) however, that assumes a impossibly homogeneous population leading to
different models which some are discussed throughout this work such as SIRVD (introduces death
and immunity through vaccination), SIRVB (post-vaccine infections added), and more advanced models
using ABM (discussed in later pre-labs such as {ref}`prelab-10` and {ref}`sec:agent_based_models`)
and Bayesian Models.

This example concerns a subtype of Bayesian SIR known as a spatially coupled SIR model which is
expressed as a PDE because of the multiple independent variables with their equations (diffusivity
which is the ease of infection through a population, infection rate and recovery rate). The series
of Differential Equations are the following:

```{math}
\partial_{t} s = D \nabla^{2} s - \beta is\\
\partial_t i = D \nabla^{2} y + \beta is - \gamma i\\
\partial_t r = D \nabla^{2} r + \gamma i\\
```

![PDE]( ../../Figs/Chapter_Lab/sir_from_storage.mp4)

```{figure} # ../../Figs/Chapter_Lab/sir_from_storage.mp4
:label: fig:SIR_PDE

This is the graphical visualization of a Spatially-Coupled SIR PDE 
with parameters beta=0.3, gamma=0.9, diffusivity=0.1, and in this 
visualization using the py-pde package, the concept of an "infection"
wave can be seen.
```

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

:::{tab-item} Example 2: Brownian Motion

Brownian Motion is often used to predict stock prices (although it is dubious in accuracy
on its own), simulate the movement of particles in suspension in fluids[^5], prediction of
star movement in galaxies, and is often used to solve PDEs as a Stochastic Differential
Equation.

In this case, this work considers the SDE variant of Brownian Motion (Weiner)
to solve the heat equation from Example 1. Moreover, this example will discuss some of the
mathematics involved in using the concept of Brownian Motion to solve PDEs _backwards_, which
is an important quality of Brownian motion.

Brownian Motion is defined through the 

```{figure} #fig:MCvis_Brownian
:label: fig:brownian_motion

This is an visualization of a Monte Carlo Method Instance (n = 100) on for Brownian Motion 
using the aleatory Python package for simulation and visualization. 

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
previous reactions to calculate the values for the [rate equation](https://chem.libretexts.org/Bookshelves/General_Chemistry/Chemistry_1e_(OpenSTAX)/12%3A_Kinetics/12.04%3A_Rate_Laws) and then solving. This work is not a work on dynamics in chemical engineering, so these
concepts will not be covered in detail.

[^2]: This is controversial, but in a general sense,
ODEs are a single independent variable and function species of a PDE.
This leads to other differences between PDEs and ODEs such as geometry
and the fact that uniqueness and existence theorems matter for solution methods
unlike an ODE.

[^3]: There are three general types of PDE: Elliptic (Steady-State such as Laplace's Equation),
Parabolic (time-dependent and dynamic), and Hyperbolic (wave-like with well-defined IVPs). Read
{ref}`sec:differential_equations` for more details, or if you want an extensive book on the topic,
{cite}`bers1964partial`.

[^4]: In customary units, this is 48 BTU/(h⋅ft⋅°F), if the reader is using customary
units for engineering, at least one of the authors would recommend reconsidering that
choice.

[^5]: Air is a fluid.
