(prelab-5)=
# Pre-Lab 5: Improving the Monte Carlo Method: Correlations (Do)

**Objective:** In this pre-lab, we move beyond simple expected values.
 We will explore how to model relationships between variables (correlations)
and how to quantify the
 risk in the tails of our distributions (skewness and kurtosis).

These tasks will be implemented using XLrisk (for Excel users)
and PyMC (for Python users).

---

## Part 1: Theoretical Concepts

### 1. Modeling Dependencies: The Correlation Problem

In the real world, variables rarely move independently.
For example, if fuel prices rise, shipping costs likely rise with them.
In a simulation, ignoring this relationship (assuming independence) leads
to an incorrect interpretation of magnitude and likelihood of extreme events.

To model this, we often need to transform independent random noise into
correlated data. The standard mathematical technique for this is the **Cholesky Decomposition**.

#### The Cholesky Decomposition

```{raw} latex
We use the \textbf{Covariance Matrix} of returns ($\Sigma$) to generate correlated random variables
from uncorrelated noise. The transformation formula is:

\[
R_{\text{correlated}} = \mu + L \cdot Z
\]

Where:

\begin{itemize}
    \item $Z$: A vector of uncorrelated random numbers $\sim N(0, 1)$.
    \item $L$: The lower triangular matrix from the Cholesky decomposition ($\Sigma = LL^T$).
    \item Result: Variables that "move together" according to the specified covariance.
\end{itemize}
```

### 2. Measuring Risk: Skewness and Kurtosis

When analyzing the results of a simulation, the looking at the common stats: Mean and Variance only tell part of the story.
 To understand the likelihood of extreme events (often discussed as risk), we look at the shape of the distribution.

**Skewness (Asymmetry):** Measures whether the data leans to one side.

* *Positive Skew:* The tail is longer on the right. (e.g., Insurance payouts: mostly zero, occasionally massive).
* *Negative Skew:* The tail is longer on the left.

**Kurtosis (Tailedness):** Measures the "heaviness" of the tails relative to a normal distribution.

* *Leptokurtic (High):* Sharp peak, fat tails. High probability of extreme outliers (high risk).
* *Platykurtic (Low):* Flat peak, thin tails. Low probability of outliers.

---

## Part 2: Implementation & Tools

:::{tab-set}

:::{tab-item} Python (PyMC & Scipy)

### 1. Generating Correlations

Python users have two ways to handle correlations: the manual approach,
way and using a package like PyMC way which is easier to use for modelling.

#### Method A: The Manual Cholesky Approach

This demonstrates the mathematical concept defined in Part 1.

```{code} python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Define Parameters
mu = np.array([0, 0])
# Covariance matrix with High positive correlation (0.8)
sigma = np.array([[1.0, 0.8], 
                  [0.8, 1.0]]) 

# 2. Perform Cholesky Decomposition (Sigma = L * L.T)
L = np.linalg.cholesky(sigma)

# 3. Generate Uncorrelated Noise (Z)
Z = np.random.normal(size=(2, 1000))

# 4. Apply Transformation: R = mu + L * Z
R_correlated = mu[:, np.newaxis] + np.dot(L, Z)

# Visualize
sns.jointplot(x=R_correlated[0], y=R_correlated[1], kind="hex", color="#4CB391")
plt.show()

```

#### Method B: The PyMC Workflow

In PyMC, correlations are often handled by
defining a **Multivariate Normal**[^3] distribution,
which handles the Cholesky decomposition internally.

1. **Define Marginals:** Create your univariate distributions (e.g., Normal, Exponential).
2. **Define Covariance:** Set up the covariance matrix based on desired correlations.
3. **Sample:** Use `pm.MvNormal` or similar constructs to sample dependent values.

### 2. Case Study: The Monty Hall Problem

We can use simulation to solve the classic probability puzzle: *Should you switch doors?*
 We will also analyze the skewness of the results to understand the distribution of wins.

```{code} python
import pymc as pm
import pytensor.tensor as pt
import scipy.stats as stats

DOORS = [0, 1, 2]
NUM_SAMPLES = 5000

with pm.Model() as monty_model:
    # 1. Setup the Game
    prize_door = pm.Categorical('prize', p=[1/3, 1/3, 1/3])
    choice = pm.Categorical('choice', p=[1/3, 1/3, 1/3])
    
    # 2. Monty Opens a Door (Deterministic Logic)
    # If choice == prize, Monty opens one of the other two random doors.
    # If choice != prize, Monty MUST open the remaining empty door.
    def monty_logic(prize, choice):
        # (Simplified logic for demonstration)
        return pt.switch(pt.eq(prize, choice), (choice + 1) % 3, 3 - prize - choice)
        
    monty_opens = pm.Deterministic('monty_opens', monty_logic(prize_door, choice))
    
    # 3. Strategy Outcomes
    win_stay = pm.Deterministic('win_stay', pt.eq(choice, prize_door))
    # Switching means choosing the door that isn't your first pick AND isn't open
    win_switch = pm.Deterministic('win_switch', pt.neq(choice, prize_door))

    # 4. Simulation
    trace = pm.sample_prior_predictive(samples=NUM_SAMPLES, random_seed=42)

# Analysis
stay_prob = trace.prior['win_stay'].mean().item()
switch_prob = trace.prior['win_switch'].mean().item()

print(f"Win Probability (Stay): {stay_prob:.2%}")
print(f"Win Probability (Switch): {switch_prob:.2%}")

# Risk Metrics (Skewness/Kurtosis of the binary outcome)
print(f"Skewness (Switch): {stats.skew(trace.prior['win_switch'].values.flatten()):.4f}")

```

```{code}
--- Monty Hall Problem Simulation Results ---
Number of simulated games: 10000
Probability of winning if you STAY: 33.55%
Probability of winning if you SWITCH: 66.45%

--- Distribution Shape Statistics ---
STAY Strategy Skewness: 0.6968
STAY Strategy Kurtosis: -1.5145
SWITCH Strategy Skewness: -0.6968
SWITCH Strategy Kurtosis: -1.5145

--- Preview of 5 games ---
Game 1: Prize is behind door 1. Contestant chose 2. Monty opened 0. Switching goes to 1. Result (Stay/Switch): Lose/Win
Game 2: Prize is behind door 0. Contestant chose 2. Monty opened 1. Switching goes to 0. Result (Stay/Switch): Lose/Win
Game 3: Prize is behind door 1. Contestant chose 2. Monty opened 0. Switching goes to 1. Result (Stay/Switch): Lose/Win
Game 4: Prize is behind door 0. Contestant chose 0. Monty opened 1. Switching goes to 2. Result (Stay/Switch): Win/Lose
Game 5: Prize is behind door 2. Contestant chose 2. Monty opened 0. Switching goes to 1. Result (Stay/Switch): Win/Lose

```


:::

:::{tab-item} Excel (XLRisk)

### 1. Functions for Correlations

XLRisk hides the linear algebra (Cholesky) behind specific functions.
Instead of multiplying matrices manually, you define a correlation matrix in the spreadsheet and apply it to your random variates.

* `=RiskCorMat(MatrixRange)`: Defines the correlation structure for a set of inputs.
* `=RiskNormal(Mean, StdDev, RiskCorMat(...))`: Generates a normal variable that respects the correlation defined in the matrix.

### 2. Simulation Workflow

A trial in XLrisk follows this Latin Hypercube process:

1. **Generate:** The software generates random numbers using the *Wichmann–Hill* generator.[^1]
2. **Correlate:** It applies the correlation matrix (using Cholesky under the hood) to adjust these numbers.
3. **Calculate:** The spreadsheet updates, calculating your outputs (e.g., Total Profit).
4. **Repeat:** This happens thousands of times to build a distribution.

### 3. Analyzing Tails

Once the simulation is complete, XLRisk provides Skewness and Kurtosis in the statistics report.

* **High Kurtosis** in your output indicates heavy Tails meaning your model predicts a
higher chance of extreme events (crashes or windfalls) than a standard Normal distribution would suggest.

* **Low Kurtosis** in your output indicates light Tails meaning your model predicts a
Lower chance of extreme events (crashes or windfalls) than a standard Normal distribution would suggest.
:::

:::

[^1]: It is important to note that the Wichmann-Hill random number generator is based on three Linear Congruential Generators (LCGs) that have different prime modulus (2^31-1, 8121, and 48271) for example that are then combined into one stream, this process was discussed in {cite}`Law:13`.

[^2]: In several simulation textbooks such as {cite}`Law:13` and {cite}`Banks:14`, they describe that this property is universal and inevitable through the _strong law of large numbers_, when that is not always true, particularly with some of the projects and labs in this text. An example of a limitation of the law of large number is that some CDFs do not have an expected value, but the weak law still holds in these cases.

[^3]: This is generally referred to as a copula.
