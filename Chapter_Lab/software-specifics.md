(sec:software)=
# Software Resources and Information

This is a chapter reference that can be used throughout the labs and the exercises
in this book. It is located in the lab section, as most of the materials
in this section relate to the pre-labs, labs, and projects.

## Excel

Excel is a spreadsheet program is a part of MS Office 365
which is used for many, many things, even when it was not made for those
applications!

However, Excel is used in workplaces for simulation, modelling, and
data storage all of which are of interest in this text. In this course,
it is an option for visualizing concepts in simulation as a visualization of a
matrix with transformations and embedded functions.

### Common Excel Functions

This is a non-exhaustive table of Excel functions, but for this text, it is sufficient enough to
perform any task needed with base Excel functions as other features are provided through Excel plugins.

:::{table}

| Excel Function | Description                                                                 | Parameters / Use Case                                                                                                                                                                                             |
| :------------- | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VAR.P()** | Calculates variance based on the entire **population**.                       | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing the entire population). <br> **Use Case:** Measuring the dispersion of a complete dataset, like the scores of all students in a specific class. |
| **VAR.S()** | Calculates variance based on a **sample** of the population.                  | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing a sample of the population). <br> **Use Case:** Estimating the population variance based on a smaller subset of data, like survey responses from a sample of a city's residents. |
| **KURT()** | Calculates the **kurtosis** of a data set (measure of "tailedness").        | **Parameters:** `number1`, `[number2]`, ... (The numbers or range for which you want to calculate kurtosis). <br> **Use Case:** Determining if a dataset has heavy tails (many outliers) or light tails (few outliers) compared to a normal distribution, often used in financial risk analysis. |
| **STDEV.P()** | Calculates standard deviation based on the entire **population**.             | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing the entire population). <br> **Use Case:** Quantifying the amount of variation or dispersion of a set of values for an entire population, such as the heights of all players on a professional sports team. |
| **STDEV.S()** | Calculates standard deviation based on a **sample** of the population.        | **Parameters:** `number1`, `[number2]`, ... (The numbers or range representing a sample of the population). <br> **Use Case:** Estimating the population standard deviation from a sample, like the variability in the lifespan of a sample of light bulbs from a production batch. |
| **SKEW()** | Calculates the **skewness** of a distribution (measure of asymmetry).       | **Parameters:** `number1`, `[number2]`, ... (The numbers or range for which you want to calculate skewness). <br> **Use Case:** Assessing the asymmetry of a dataset around its mean. For example, determining if income distribution in a region is skewed towards higher or lower incomes. |
| **T.INV()** | Returns the left-tailed inverse of the Student's **t-distribution**.          | **Parameters:** `probability`, `deg_freedom`. <br> (`probability` is the probability associated with the t-distribution; `deg_freedom` is the number of degrees of freedom). <br> **Use Case:** Finding the t-value for a given probability and degrees of freedom, often used in constructing confidence intervals or in hypothesis testing. |
| **IF()** | Performs a **logical test** and returns one value for a TRUE result and another for a FALSE result. | **Parameters:** `logical_test`, `value_if_true`, `value_if_false`. <br> (`logical_test` is any value or expression that can be evaluated to TRUE or FALSE). <br> **Use Case:** Assigning grades based on scores (e.g., IF(Score>90, "A", "B")), categorizing data, or controlling calculations based on certain conditions. |
| **XLOOKUP()** | **Searches a range or an array** for a match and returns the corresponding item from a second range or array. Default is an exact match. | **Parameters:** `lookup_value`, `lookup_array`, `return_array`, `[if_not_found]`, `[match_mode]`, `[search_mode]`. <br> **Use Case:** Finding specific information in a table, like looking up an employee's department based on their ID, or finding a product price given its name.  |

:::

### Excel Resources and Examples

In this subsection, we would like to point out some resources that may assist
the reader in understanding how to use Excel and some of the plugins that were
used when making this book.

#### Excel Video Series

#### Excel Textbooks

### XLRisk

XLRisk is a Free and Open Source VBA-based plugin that is made to compete with
atRisk, a widely-used commercial program that does Monte Carlo Method calculations.

#### XLRisk Variates and Functions

This is a almost exhaustive list of XLRisk Variates and Functions, that come from
[XLRiskDocumentation](https://github.com/pyscripter/XLRisk/wiki/RiskFunctions)
refer to that resources if more XLRisk variates could be helpful.


##### XLRisk Variates

:::{table}

| XLRisk Function    | Description                                                                                                | Parameters                                                                 |
| :----------------- | :--------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **RiskBernoulli** | Generates samples from a Bernoulli distribution.                                                           | `P` (probability of success)                                               |
| **RiskBeta** | Generates samples from a Beta distribution. Optionally provide A and B as the minimum and maximum.           | `alpha`, `beta` (shape parameters), `[A]` (minimum), `[B]` (maximum)         |
| **RiskBinomial** | Generates samples from a Binomial distribution.                                                            | `N` (number of trials), `P` (probability of success)                         |
| **RiskCumul** | Generates samples from a cumulative distribution, specified by min, max, and X,Y coordinates.              | `minvalue`, `maxvalue`, `XValues` (array), `YValues` (array of cumulative probabilities) |
| **RiskDiscrete** | Generates samples from a discrete distribution where specific values have defined probabilities.              | `Values` (array or range in ascending order), `Probabilities` (array or range of respective probabilities) |
| **RiskDUniform** | Generates samples from a discrete uniform distribution where each specified value has an equal chance.      | `Values` (array or range of values)                                        |
| **RiskErlang** | Generates samples from an Erlang distribution.                                                             | `alpha` (integer shape parameter), `beta` (scale parameter)                |
| **RiskExponential**| Generates samples from an Exponential distribution.                                                        | `mean`                                                                     |
| **RiskGamma** | Generates samples from a Gamma distribution.                                                               | `alpha` (shape parameter), `beta` (scale parameter)                        |
| **RiskLogNorm** | Generates samples from a log-normal distribution.                                                          | `mean`, `stdev` (standard deviation)                                     |
| **RiskNormal** | Generates samples from a normal distribution.                                                              | `mean`, `stdev` (standard deviation)                                     |
| **RiskPert** | Generates samples from a PERT distribution (a special case of Beta, smoother version of Triangular).         | `min`, `mostlikely`, `max`                                                 |
| **RiskTriang** | Generates samples from a triangular distribution.                                                          | `min`, `mostlikely`, `max`                                                 |
| **RiskUniform** | Generates samples from a uniform distribution.                                                             | `min`, `max`                                                               |
| **RiskWeibull** | Generates samples from a Weibull distribution.                                                             | `alpha` (shape parameter), `beta` (scale parameter)                        |

:::

##### XLRisk Functions

:::{table}

| XLRisk Function         | Description                                                                                                | Parameters / Use Case                                                                                                                               |
| :---------------------- | :--------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RiskCorrmat** | Creates a link to a correlation matrix when used as an optional last argument in a Risk function.           | **Parameters:** `CorrmatRng` (range of the correlation matrix), `Index` (column/row index in the matrix for the current Risk function). <br> **Use Case:** To model dependencies between different uncertain variables in a Monte Carlo simulation by correlating their input distributions. |
| **RiskCorrectCorrmat** | Fixes a correlation matrix that is not semipositive definite and returns a valid correlation matrix.         | **Parameters:** `CorrmatRng` (range of the correlation matrix to be corrected). <br> **Use Case:** To ensure a user-defined or imported correlation matrix is mathematically valid for use in simulations, preventing errors if it's not positive semidefinite. |
| **RiskIsValidCorrmat** | Checks whether a correlation matrix is valid, including a test for semipositive definiteness. Returns TRUE/FALSE. | **Parameters:** `CorrmatRng` (range of the correlation matrix to be validated). <br> **Use Case:** To programmatically check if a correlation matrix can be used in simulations before running them, or for data validation purposes. |
| **RiskSCorrel** | Returns the Spearman's rank correlation coefficient between two arrays.                                       | **Parameters:** `Array1`, `Array2` (the two datasets/arrays for which to calculate the rank correlation). <br> **Use Case:** To measure the strength and direction of a monotonic relationship between two variables, especially when the relationship is not linear or when outliers are present. |

:::

## Python Packages

### monaco

Here is the video overview for Monaco! [Link](https://www.youtube.com/watch?v=yB539OIol_s)

And here is the function overview for Monaco!

### pyMC

The following subsection discusses common distributions, options,
sampling methods, and statistical methods that exist within the PyMC package (at least its ecosystem.)

##### Probability Distributions

:::{table}
| Distribution (`pm.*`) | Description | Key Parameters |
| :--- | :--- | :--- |
| **Continuous Distributions** | | |
| `Normal` | A continuous, symmetric, bell-shaped distribution. | `mu` (mean), `sigma` (std. dev.) |
| `HalfNormal` | A normal distribution constrained to be non-negative. | `sigma` (std. dev.) |
| `Uniform` | A continuous distribution where all values in a range are equally likely. | `lower` (lower bound), `upper` (upper bound) |
| `StudentT` | Similar to the Normal distribution but with heavier tails, making it robust to outliers. | `nu` (degrees of freedom), `mu` (mean), `sigma` (scale) |
| `Exponential` | A continuous distribution for modeling the time between events. ⏳ | `lam` (rate parameter, $\lambda$) |
| `Beta` | A continuous distribution defined on the interval [0, 1], often used for modeling probabilities or proportions. | `alpha`, `beta` (shape parameters) |
| `Gamma` | A two-parameter continuous distribution for non-negative random variables. | `alpha` (shape), `beta` (rate) |
| `LogNormal` | A distribution whose logarithm is normally distributed. Used for positive random variables. | `mu` (mean of the log), `sigma` (std. dev. of the log) |
| **Discrete Distributions** | | |
| `Bernoulli` | A distribution for a single trial with two outcomes (0 or 1, success or failure). 🪙 | `p` (probability of success) |
| `Binomial` | Models the number of successes in a fixed number of independent Bernoulli trials. | `n` (number of trials), `p` (probability of success) |
| `Poisson` | Models the number of events occurring in a fixed interval of time or space. 📊 | `mu` (rate, expected number of events) |
| `NegativeBinomial` | Models the number of successes in a sequence of Bernoulli trials before a specified number of failures occurs. | `mu` (mean), `alpha` (dispersion) |

:::

##### pyMC Statistics

Through the Arviz package. 

:::{table}
| Function (`pm.*`) | Description | Key Parameters / Usage |
| :--- | :--- | :--- |
| `summary` | Generates a DataFrame with key summary statistics for the posterior distribution, such as mean, standard deviation, effective sample size (`ess`), and the R-hat diagnostic (`r_hat`). | `trace`, `var_names` |
| `plot_posterior` | Creates a plot of the posterior distribution for specified variables, typically shown as a histogram or a Kernel Density Estimate (KDE). 📊 | `trace`, `var_names`, `hdi_prob` |
| `trace_plot` | Creates a plot showing the MCMC trace (the time series of the samples) on one side and the posterior density on the other. It's essential for diagnosing convergence issues. | `trace`, `var_names` |
| `sample_posterior_predictive` | Generates new data based on the fitted model and posterior samples. This is crucial for posterior predictive checks to see how well the model simulates new data. | `trace`, `model`, `samples` |
| `loo` | Computes the approximate Leave-One-Out cross-validation (LOO) score, a metric for estimating a model's out-of-sample predictive accuracy. Used for model comparison. | `trace`, `model` |
| `waic` | Computes the Watanabe-Akaike Information Criterion (WAIC), another popular metric for estimating out-of-sample predictive accuracy. | `trace`, `model` |
| `model_to_graphviz` | Renders a visual graph of the model's structure, showing the relationships between random variables and data. 🔗 | `model` |

:::

##### pyMC Sampling

:::{table}
| Function / Concept | Description | Key Parameters / Usage |
| :--- | :--- | :--- |
| `pm.sample()` | This is the core function used to run the MCMC sampler and draw samples from your model's posterior distribution. | `draws`, `tune`, `chains`, `cores`, `target_accept` |
| **NUTS Sampler** | The **No-U-Turn Sampler** is PyMC's default, highly efficient MCMC algorithm for sampling from continuous variables. It uses gradient information to explore the posterior. | Automatically assigned by `pm.sample()` to continuous variables. |
| `draws` | The number of samples to generate and save for each chain, *after* the tuning phase. | `draws=2000` |
| `tune` | The number of initial "warm-up" iterations per chain. These are used to adapt the sampler's parameters and are then discarded. | `tune=1000` |
| `chains` | The number of independent MCMC chains to run. Running multiple chains (e.g., 4) is essential for diagnosing whether the sampler has converged properly. | `chains=4` |
| `cores` | The number of CPU cores to use for running chains in parallel. Setting this to the number of chains speeds up sampling significantly. | `cores=4` |
| `target_accept` | The target acceptance rate for the NUTS sampler. The default is usually 0.8. Increasing it can help resolve divergence in complex models. | `target_accept=0.9` |
| **InferenceData** | The object returned by `pm.sample()`. It's an `arviz.InferenceData` object that contains all sampling results (posterior, observed data, etc.). Often called `idata` or `trace`.| This object is the input for all diagnostic and plotting functions, like `pm.summary(idata)`. |
:::

### Ciw

### Salabim
:::{table}

| Function/Method | Description |
| :--- | :--- |
| **Environment** | The `Environment` class manages the simulation time and the event queue. |
| `sim.Environment()` | Creates a new simulation environment. Sets up the event list and random stream. |
| `env.run(duration, till)` | Starts or resumes the simulation. Runs until a specific duration or time `till` is reached. |
| `env.now()` | Returns the current simulation time. |
| `env.trace(bool)` | Enables or disables the trace output (a log of all events). |
| `env.main()` | Returns the `main` component (the process that started the simulation). |
| `env.speed(float)` | Sets the animation speed (ratio of simulation time to real time). |
| `env.animate(bool)` | Enables or disables real-time animation. |
| `env.animate3d(bool)` | Enables or disables 3D animation. |
| `env.snapshot(filename)` | Takes a screenshot of the current animation window. |
| `env.video(filename)` | Records the animation to a video file (e.g., .mp4, .gif). |

| Function/Method | Description |
| :--- | :--- |
| **Components** | Components are the active entities (like cars, customers, machines) that have a process. |
| `sim.Component()` | Defines a new component. Usually subclassed by the user (e.g., `class Car(sim.Component)`). |
| `setup()` | A user-defined method called immediately after a component is created. Used for initialization. |
| `process()` | A user-defined method (generator) that describes the lifecycle/behavior of the component. |
| `self.hold(duration)` | Makes the component wait (suspend execution) for a specific duration. |
| `self.passivate()` | Makes the component passive (idle) indefinitely until activated by another component. |
| `self.activate()` | Reactivates a passive component, scheduling it to run immediately or at a specific time. |
| `self.cancel()` | Cancels the component, removing it from the event list and making it a "data" component. |
| `self.standby()` | Puts the component in standby mode; it re-evaluates its status after every simulation event. |
| `self.request(resource)` | Requests a specific quantity from a Resource. Waits if not available. |
| `self.release(resource)` | Releases a previously claimed quantity back to a Resource. |
| `self.enter(queue)` | Enters a specific Queue. |
| `self.leave(queue)` | Leaves a specific Queue. |
| `self.wait(state, value)` | Waits for a specific State to reach a certain value (e.g., `door_open.value` becomes `True`). |
| `sim.ComponentGenerator()`| Automatically generates components according to an inter-arrival time distribution. |

| Function/Method | Description |
| :--- | :--- |
| **Resources, Queues, & Stores** | These classes manage the flow of components and capacity. |
| `sim.Queue(name)` | Creates a queue (waiting line) for components. Supports FIFO, priority, etc. |
| `queue.add(component)` | Adds a component to the tail of the queue. |
| `queue.remove(component)` | Removes a specific component from the queue. |
| `queue.length()` | Returns the current number of components in the queue via the level monitor. |
| `sim.Resource(name, capacity)` | Creates a resource with a limited capacity (e.g., clerks, machines). |
| `resource.claimers()` | Returns the queue of components currently holding the resource. |
| `resource.requesters()` | Returns the queue of components waiting for the resource. |
| `resource.capacity()` | Returns or sets the total capacity of the resource. |
| `sim.Store(name, capacity)` | Creates a store, which is a queue that holds specific items (can be components or data). |
| `self.to_store(store, item)` | Puts an item into a store. Waits if the store is full. |
| `self.from_store(store)` | Retrieves an item from a store. Waits if the store is empty. |

| Function/Method | Description |
| :--- | :--- |
| **States & Synchronization** | States allow components to communicate via flags or values. |
| `sim.State(name, value)` | Creates a state variable (default value is often `False`). |
| `state.get()` | Returns the current value of the state. |
| `state.set(value)` | Sets the value of the state. Triggers components waiting for this value. |
| `state.trigger(value)` | Sets the value, triggers waiting components, and then optionally resets the value. |
| `state.waiters()` | Returns the queue of components waiting for this state to change. |

| Function/Method | Description |
| :--- | :--- |
| **Monitors** | Monitors track statistics over time. |
| `sim.Monitor(name, level)` | Creates a monitor. `level=True` tracks values over time (like queue length); `level=False` tracks occurrences (like processing time). |
| `monitor.tally(value)` | Adds a value to the monitor. |
| `monitor.mean()` | Returns the (time-weighted) mean of the collected data. |
| `monitor.print_statistics()` | Prints a summary table (mean, min, max, std dev) to the console. |
| `monitor.print_histogram()` | Prints a text-based histogram of the collected data. |
| `monitor.x()` / `monitor.xt()` | Returns the collected data as arrays (useful for plotting with Matplotlib). |

| Function/Method | Description |
| :--- | :--- |
| **Distributions** | Wrappers for statistical distributions. |
| `sim.Uniform(min, max)` | Uniform distribution. |
| `sim.Normal(mean, std)` | Normal (Gaussian) distribution. |
| `sim.Exponential(mean)` | Exponential distribution (often used for inter-arrival times). |
| `sim.Triangular(low, high, mode)` | Triangular distribution. |
| `sim.Constant(value)` | Returns a constant value (useful for testing). |
| `sim.Pdf(spec)` | Probability density function (custom discrete distribution). |
| `sim.Cdf(spec)` | Cumulative distribution function. |
| `distribution.sample()` | Returns a random sample from the defined distribution. |
| `distribution.mean()` | Returns the theoretical mean of the distribution. |

| Function/Method | Description |
| :--- | :--- |
| **Animations** | Classes used to visualize the simulation. |
| `sim.AnimateQueue()` | Automatically visualizes the contents of a queue on screen. |
| `sim.AnimateRectangle()` | Draws a rectangle. Properties (x, y, color) can be dynamic (functions of time). |
| `sim.AnimateCircle()` | Draws a circle. |
| `sim.AnimateText()` | Displays text. Useful for showing simulation clocks or counters. |
| `sim.AnimateImage()` | Displays an image (supports PNG, JPG, and animated GIF). |
| `sim.Animate3dBox()` | Creates a 3D box (cube) for 3D visualization. |
| `sim.Animate3dGrid()` | Draws a grid in the 3D space to help with orientation. |
| `sim.TrajectoryCircle()` | Defines a circular path for objects to follow during animation. |
| `sim.TrajectoryPolygon()` | Defines a path based on polygon points for objects to follow. |

:::

### PySim

:::{table}
| Function/Method | Description |
| :--- | :--- |
| **Simulation Environment & Control** | The `Environment` variable manages the simulation time and the event queue.|
| `simpy.Environment()` | Creates a new simulation environment. |
| `env.process(generator)` | Adds a generator function to the environment as a **Process**. |
| `env.run(until=X)` | Runs the simulation. If `until` is a number, it runs to that time. If it is an event, it runs until that event is processed. |
| `env.now` | Property that returns the current simulation time. |
| `env.active_process` | Property returning the currently active process (or `None`). |
| `env.timeout(delay)` | Creates a **Timeout** event that expires after `delay` time units. |
| `env.event()` | Creates a generic, manually triggered **Event**. |
| `env.all_of(events)` | Creates a condition event that triggers when **all** events in the list occur. |
| `env.any_of(events)` | Creates a condition event that triggers when **any** one event in the list occurs. |

| Function/Method | Description |
| :--- | :--- |
| **Process Interaction** |Processes are Python generators that define the behavior of active components (e.g., cars, customers). |
| `yield env.timeout(delay)` | Pauses the process for `delay` time units (the standard way to advance time). |
| `yield env.process(proc)` | Pauses the current process until the target process `proc` finishes. |
| `process.interrupt()` | Interrupts a sleeping (yielding) process. The process receives an `Interrupt` exception. |
| `yield event` | Pauses the process until the specific `event` is triggered. |
| `event.succeed(value)` | Manually triggers an event successfully, optionally passing a return `value`. |
| `event.fail(exception)` | Manually triggers an event with a failure (raises an exception in the yielding process). |

| Function/Method | Description |
| :--- | :--- |
| **Shared Resources** | SimPy resources manage congestion points where processes queue for capacity.|
| **`simpy.Resource(env, capacity)`** | **Basic Resource.** Limits the number of parallel users (e.g., a gas station with 2 pumps). |
| `resource.request()` | Request a usage slot. Used in a context manager: `with res.request() as req: yield req`. |
| `resource.release(request)` | Release a usage slot. Automatically handled when using `with` statement. |
| `resource.count` | Current number of users holding the resource. |
| `resource.queue` | List of requests currently waiting for the resource. |
| **`simpy.Container(env, capacity, init)`**| **Continuous/Bulk Resource.** Stores homogeneous matter (e.g., water in a tank, petrol). |
| `container.put(amount)` | Adds an `amount` to the container. Waits if full. |
| `container.get(amount)` | Takes an `amount` from the container. Waits if empty. |
| `container.level` | The current amount of matter in the container. |
| **`simpy.Store(env, capacity)`** | **Discrete Item Store.** Stores distinct Python objects (e.g., widgets in a bin). |
| `store.put(item)` | Puts a specific Python object/item into the store. |
| `store.get()` | Retrieves an object from the store (FIFO by default). |
| **`simpy.PriorityResource`** | Same as `Resource`, but requests are sorted by priority (integer) instead of FIFO. |
| **`simpy.PreemptiveResource`** | A `PriorityResource` where higher priority requests can kick out (preempt) active users. |

| Approach | Description |
| :--- | :--- |
| **Data Collection**| |
| **Python Lists** | Create a global list (e.g., `wait_times = []`) and `append()` data points directly inside your process code. |
| **Monitoring Process** | Create a separate process that runs alongside your simulation to sample state periodically. |
| **Monkey Patching** | Advanced users can wrap resource methods (like `request`) to auto-log data every time they are called. |

| Standard Library Function | Typical SimPy Usage |
| :--- | :--- |
| **Distributions from Random** | |
| `random.expovariate(lambda)` | Used for inter-arrival times (Exponential distribution). |
| `random.uniform(a, b)` | Used for uniform processing times. |
| `random.gauss(mu, sigma)` | Used for Normal distribution. |
| `random.randint(a, b)` | Used for discrete integer choices. |
| `random.choices(population, weights)`| Used for weighted random choices (e.g., choosing a distinct path). |

:::
