
(sec:differential_equations)=
# Differential Equations

:::{note} Refinement DE 1:
All of the existing content in this chapter should be considered provisional at best.
:::

We have previously discussed techniques such as the Monte Carlo Method, System Dynamics, and Random Variate Generation. While these are essential for simulation, they are not sufficient for a complete understanding of modeling. Engineers and simulation practitioners must also be familiar with Differential Equations (DEs), as they are frequently used to approximate real-world behaviors into deterministic or stochastic models.

The goal of this chapter is to provide a review of ODEs, PDEs, and SDEs, highlighting their application in simulation.

## Classification of Differential Equations

In general, a differential equation relates a function to its derivatives. The canonical Ordinary Differential Equation (ODE) takes the form:

```{math}
y^{'} + p(x)y = q(x)
```

However, the landscape of differential equations is broad. We can classify them based on the nature of their independent variables and the presence of stochastic elements.

### Differential Equations Overview

While you are likely familiar with ODEs, other types expand on this concept significantly.

:::{table}
:label: DEs-Types

| Feature                                   | PDEs (Partial Differential Equations)                                     | SDEs (Stochastic Differential Equations)                                  | IDEs (Integro-Differential Equations)                                     |
| :---------------------------- |:------------------------------------------------------------------------ | :------------------------------------------------------------------------ | :------------------------------------------------------------------------ |
| **Unknown Function Depends On**  | Two or more independent variables (e.g., $u(x,t)$ or $f(x,y,z)$).         | One or more independent variables, and also on random processes.        | One or more independent variables.                                        |
| **Derivatives Involved**   | Partial derivatives (e.g., $\frac{\partial u}{\partial x}$, $\frac{\partial^2 u}{\partial t^2}$, $\frac{\partial^2 u}{\partial x \partial y}$). | Ordinary or partial derivatives, plus terms involving stochastic differentials (e.g., $dW_t$ for Wiener process). | Ordinary or partial derivatives, and also integrals of the unknown function. |
| **General Form Example** | $F(x, t, u, u_x, u_t, u_{xx}, u_{tt}, u_{xt}, \dots) = 0$                   | $dX_t = a(t, X_t)dt + b(t, X_t)dW_t$                                  | $\frac{dy}{dx} = f(x, y(x), \int_{a}^{b} K(x,s,y(s))ds)$                     |
| **Key Characteristics** | - Describes systems evolving in multiple dimensions or involving rates of change with respect to multiple variables. <br> - Solutions are functions of multiple variables. <br> - Often more complex to solve than ODEs; boundary conditions are crucial. | - Incorporate random noise or fluctuations. <br> - Solutions are stochastic processes (collections of random variables). <br> - Used to model systems with inherent uncertainty. <br> - Often uses stochastic calculus (e.g., Itô calculus). | - Combine differential and integral operators acting on the unknown function. <br> - Arise when the rate of change depends on the accumulated past history or spatial distribution of the quantity. <br> - Can be linear or non-linear. |
| **Typical Applications** | - Heat flow (Heat equation) <br> - Wave propagation (Wave equation) <br> - Electrostatics (Laplace's/Poisson's equation) <br> - Fluid dynamics (Navier-Stokes equations) <br> - Quantum mechanics (Schrödinger equation) | - Financial modeling (stock prices, option pricing - e.g., Black-Scholes model) <br> - Physical systems with thermal fluctuations (Brownian motion, Langevin equation) <br> - Biological systems with noise (e.g., gene expression) <br> - Signal processing with noise | - Population dynamics with memory effects <br> - Epidemiology (spread of diseases with non-local interactions) <br> - Viscoelasticity <br> - Radiative transfer <br> - Neural networks with delays or spatial integration |
| **Solution Notes** | - Analytical methods for simpler cases and specific geometries (e.g., separation of variables, Fourier transforms, Green's functions). <br> - Numerical methods are very common (e.g., finite difference, finite element, finite volume). | - Analytical solutions are rare, often limited to linear SDEs. <br> - Focus on properties of the solution process (e.g., mean, variance). <br> - Numerical methods (e.g., Euler-Maruyama, Milstein schemes) are used for simulation. | - Sometimes transformed into pure ODEs or PDEs if the kernel is deterministic or separable. <br> - Numerical methods often involve discretizing both the derivative and the integral. <br> - Volterra and Fredholm integro-differential equations are common types. |

:::

### Ordinary Differential Equations (ODEs)

ODEs are the most common form encountered in basic system modeling. They are often solved analytically in textbooks, but in simulation, we frequently rely on automated solvers. These solvers are often limited by the "stiffness" of the equation or the lack of a closed-form solution.

#### Analytic Solution Methods

For a simulation practitioner, understanding the type of ODE helps in selecting the correct numerical method.

:::{table}
:label: ODE-Types

| ODE Type                      | General Form / Definition                                                                 | Key Characteristics / Solution Notes                                                                                                                               |
| :---------------------------- | :---------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First-Order ODEs** |                                                                                           | Involves only the first derivative of the dependent variable.                                                                                                      |
| Separable Equations           | $\frac{dy}{dx} = g(x)h(y)$ or $M(x)dx + N(y)dy = 0$                                        | Can be rearranged so each side of the equation contains only one variable and its differential. Solved by direct integration.                                       |
| Linear Equations              | $\frac{dy}{dx} + P(x)y = Q(x)$                                                            | $P(x)$ and $Q(x)$ are functions of $x$ (or constants). Solved using an integrating factor: $I(x) = e^{\int P(x)dx}$.                                                   |
| Homogeneous Equations (Type 1)| $\frac{dy}{dx} = F(\frac{y}{x})$                                                          | Can be transformed into a separable equation by the substitution $v = \frac{y}{x}$ (so $y = vx$).                                                                   |
| Exact Equations               | $M(x,y)dx + N(x,y)dy = 0$, where $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | There exists a function $f(x,y)$ such that $df = Mdx + Ndy = 0$. The solution is $f(x,y) = C$. If not exact, sometimes an integrating factor can be found.        |
| Bernoulli Equations           | $\frac{dy}{dx} + P(x)y = Q(x)y^n$, where $n \neq 0, 1$                                      | Non-linear. Can be transformed into a linear equation by the substitution $v = y^{1-n}$.                                                                            |
| Riccati Equations             | $\frac{dy}{dx} = P(x)y^2 + Q(x)y + R(x)$                                                  | Non-linear. No general solution method unless a particular solution $y_1(x)$ is known. Then $y = y_1 + u$ transforms it to a Bernoulli eq. for $u$.                   |
| **Higher-Order Linear ODEs** | $a_n(x)\frac{d^ny}{dx^n} + a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1(x)\frac{dy}{dx} + a_0(x)y = g(x)$ | Involves derivatives of order 2 or higher. $g(x)=0$ is homogeneous; $g(x) \neq 0$ is non-homogeneous.                                                              |
| Homogeneous with Constant Coefficients | $ay'' + by' + cy = 0$ (for 2nd order)                                                   | Solved using the characteristic (auxiliary) equation $ar^2 + br + c = 0$. Solutions depend on the nature of the roots (real distinct, real repeated, complex).      |
| Non-homogeneous with Constant Coefficients | $ay'' + by' + cy = g(x)$ (for 2nd order)                                                | General solution is $y = y_c + y_p$, where $y_c$ is the complementary solution (from the homogeneous part) and $y_p$ is a particular solution (found by undetermined coefficients or variation of parameters). |
| Cauchy-Euler (Equidimensional) Equation | $ax^2y'' + bxy' + cy = g(x)$ (for 2nd order)                                              | Can be transformed into a linear ODE with constant coefficients by the substitution $x = e^t$.                                                                   |
| **Systems of ODEs** | $\frac{d\mathbf{y}}{dt} = \mathbf{F}(t, \mathbf{y})$, where $\mathbf{y}$ is a vector of functions | Describes the interaction of multiple dependent variables. Linear systems with constant coefficients can be solved using eigenvalues and eigenvectors.                |
| **Non-linear ODEs (General)** |                                                                                           | Equations that do not satisfy the conditions for linearity. Often difficult to solve analytically; may require qualitative analysis, numerical methods, or series solutions. |
| Autonomous Equations          | $\frac{dy}{dx} = f(y)$  |  Autonomous differential equations are separable and can be solved by direct integration.

:::

## Modeling in the Real World

In practice, the choice between using an ODE, SDE, or PDE depends on the fidelity required by the model. While closed-form solutions (like those for the M/M/1 queue from {sec}`sec:queueing_systems`) are elegant, real-world systems often require the numerical approximation of these differential equations, bridging the gap between mathematics and computational simulation.
