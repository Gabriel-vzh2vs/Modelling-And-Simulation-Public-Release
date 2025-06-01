(sec:pre-labs)=
# Pre-Labs

Pre-labs are made to aid the reader with the concepts presented in the
Laboratory Section of this book. These pre-labs consist of structured
activities linked with the lab with the same number (e.g: Pre-Lab 1 connects to Lab 1).

There are two categories of Pre-Lab: Read and Do. Pre-Labs marked with "Read" are
functionally equivalent to a typical section of the book as in the reader sees examples
and learns similarly to the rest of the sections of the book. In contrast,
Pre-Labs marked with "Do" ask the reader to complete an exercise step-by-step that
helps the reader comprehend the tasks they need to do for the associated lab. Additionally,
Pre-labs marked with "Do" may not be as theory-based as labs marked with "Read".

Some pre-labs might be marked with "short", this means that they are pre-labs
that rely on the rest of the book for support - often these are used to transition
between topics and introduce different topics.

Grading for the Pre-Labs is at the instructor's discretion as described in
{ref}`sec:labs`; additionally, we recommend completing a pre-lab for each lab
at a 1 to 1 ratio (meaning, if a reader does 8 labs, they should do 8 pre-labs,
which is the expected number of pre-labs and labs for a course) However, if you
are self-studying, you can choose which pre-labs you do based on your knowledge level.

:::{note} Pre-Lab Status
To Henning, this section is getting content at a decent speed. It should be
fully-drafted by June 6th at the current rate of improvement. The topics are
all there, along with basic information and sections.

Partially-Drafted Pre-Labs

- Pre-lab 1 (Provisionally Complete)
- Pre-lab 2 
- Pre-Lab 3
- Pre-lab 6 (Provisionally Complete - In Progress of Moving Theory)
- Pre-lab 7 (Provisionally Complete)
- Pre-lab 8 (This might be going into the weeds of Stochastic Calculus)
:::

(prelab-1)=
## Pre-Lab 1: On Excel Skills and Python (Read)

The first pre-lab will introduce some important details you should know
about Excel if you choose to use it, and will teach the readers who do not
want (or can not) use Excel about data management, a critical skill for
using a computer effectively for computing tasks such as simulation.

::::{tab-set}

:::{tab-item} Fundamental Excel Skills (Read and Watch)

Excel is a useful tool for doing basic data cleaning, making toy models,
looking at excel files made by other people, using visual basic, running
statistical tests in prototyping, or for visualizing matrix algebra. It is
ubiquitous in business, education, and more because has a minimal learning curve
to get started with basic operations, but it is difficult to master. So it is
important for any reader (or engineer) to learn. This pre-lab cannot and will not
teach you all of Excel, only the parts you need to understand for this course.

If you want to learn more about Excel or are confused by the topics in this pre-lab,
watch the video embedded below or read {cite}`brown2017beginning`.

<!-- for the editor: in the written form of this text, remove "watch the video embedded below or" -->

```{iframe} https://www.youtube.com/watch?v=IInFoJxxPPA
This video is a hour long and describes all of the basic features of Excel, which a useful subset
are written below.
```

<!-- for the editor: in the written form of this text, remove the ```{iframe} ....-->

### The Cell

The fundamental element of any spreadsheet is the cell, which is a piece of data, anything
could be stored in an Excel cell, from a string of text, to a formula to a floating point number.

An example of a cell is the following image:

```{figure} ../Figs/Chapter_Lab/ExcelScreenShot.png
```

Which shows the number 42, a integer stored as a floating point number existing in a cell. And this
equivalent to a 1 x 1 matrix with 42 stored inside.

### References and Ranges

A cell can also 'reference' another cell, by this, it can include the data stored in one cell in
another cell, which is usually used by formulas. A range is a references that spans several cells
similar to a vector from linear algebra.

```{figure} ../Figs/Chapter_Lab/ExcelScreenShot2PreLab1.png
```

In this case, the cell stores a reference to A1, which is the location of the first cell on the spreadsheet,
referencing A1, which we know is 42.

### Formulas

A formula can be thought of as a operation that resides in the cell, taking in data from other
cells that contain different parts of data through references. For example, if you want to calculate skewness,
you take several cells that are referenced from a range. Such as the following formula: `=kurt(A1:A3)`,
which represents the calculation of the skewness of the range of numbers stored in A1, A2, and A3 as a single unit.
Additionally, other useful formulas are available from {ref}`sec:software`, which should read in conjunction
with this pre-lab.

### When you should consider using Something Else

An important part of any tool is using it appropriately. This might become a
soapbox unlike every other pre-lab, which this text tends to avoid being at times.

Consider using different tools than Excel when you need to

- store data that needs to be assessed by other software or requires access control, instead use DBMSs like PostgreSQL, MariaDB.
- have speed at processing data and information, instead use programming languages like Rust, Python with Pypy, or Java.
- simulate complex systems, particularly ones with any form of Differential Equation determining their behaviors, instead use simulation software like simpy, Anylogic, SIMIO.
- analyzing big data, for reference big data is greater than 500 entities in a list, instead use programming languages with frameworks to handle it like R, Python's Dask/PySpark, Apache's Flink/Samza/Storm.
:::

:::{tab-item} Python Review (Read)

As discussed in {ref}`sec:preface`, Python will be a critical tool throughout this book because it is
ubiquitous in simulation literature, software development, data science and engineering; thus, we have 
included a short Python review as a Pre-lab in this text.

### Functions

A function is a piece of reusable code which is analogous to a mathematical function that can be called
with the following syntax (i.e. a series of characters that represents something) `function_name()`,
which has two components: a signature and a body. A signature is the first line of a Python function,
which is where the parameters/variables (the objects that enter the function) for the function are defined,
the name of the function, and optionally where the type of the outputs and inputs are defined. In the
following example, a and b are integers (int) that exit the function as a integer through a return,
which will be discussed later in this section.

```{code-cell} python
def add(a: int, b: int) -> int # Signature
    x = a + b # Body
    return x # End of Body
```

The second part of the function is the body of the function, which is what transforms the parameters
from two integers into one integer, `x`, and a similar idea exists with all functions, which transform
one or more objects into another as we see above with `x = a + b`. Additionally, we see a `return` statement,
which defines the accessible output of the function which can be obtained through the statement below.

```{code} python
returned_value = add(3,5) # A Function Call
```

Now, to use a function, you must call it, and an example of this idea is above. In this case, we are calling
the function with the parameters `3` and `5` and storing the return into a variable called `returned_value`.

Moreover, it must be noted that both of the parameters are integers, if they were floats, a number with a
decimal, or strings, a set of characters like the ones you are reading right now, the function would return
an error stating that the type of the parameter does not match the type(s) specified in the signature, and
the variable `returned_value` would not exist (this idea is represented as a `null` in Python).

Now, when the `print` function is called on the variable, `returned_value`, it will return the value stored
inside of it, which if the reader calculates it should be equal to eight. And when the print function
is called, as seen below, the result as expected.

```{code} python
print(returned_value)
8
```

Note: You might see functions without parameters, because they act on parameters outside of the function,
and we call these parameters, global variables as any function can alter or act upon them. Otherwise, the
parameters inside of a function are referred to as local variables. And some functions come from modules
which are Python files (.py) that come from external sources, which will be discussed in the next section.

#### Libraries and Modules

Fundamentally, a module is a set of different functions that was typically made for a specific purpose that
typically belongs to a library, which is a set of modules; in this case, it might be helpful to think
about a module being a book in a library. To allow the usage of a library in your code, you must use a
import statement such as the one below.

```{code} python
import scipy as sp
```

There is also something different about this import statement, that it includes an `as` after the
`import scipy`, this is known as an alias, and it is used to reduce the amount of time spent typing
the entire name of the library when it is referenced (although it also reduces the size of the file
slightly, but that is not relevant outside of resource-constrained systems).

It is also possible that an import statement will be formatted as `from library import package`. A package
is a container of several modules, to the point where some libraries will be organized as a series of
packages which are a set of modules, for most practical purposes, the difference between libraries and
packages is meaningless. Now, here is an example of using this different form of import statement.

```{code} python
from scipy import stats as stats
```

In the code above, `from scipy import stats` is the second form of import statement that was discussed previously
along with an alias `as stats`. Now, to use a function from a library, it is typical to use the following syntax:
`alias.function_name`. An example of this is below.

```{code} python
from scipy import stats as stats

norm_5_8 = stats.Normal(5, 8)
```

In this case, `norm_5_8` represents a Gaussian random variable with a mean of five and a standard deviation of 8. When this
segment of code is disassembled we see that `stats` represents SciPy's stats module, and the `normal` represents
the function from `stats` that substitutes the parameters into a standard Gaussian transforming it into a Gaussian
with a mean of 5 and standard deviation of 8.  

The astute reader might have notice that `import`, `from`, and `def` did not need to be imported and do not have
an associated package name, the reason for this is that they are part of Python's
[Standard Library](https://docs.python.org/3/library/index.html) which provides the foundation for Python's operation,
this also includes many functions, types (see {ref}`sec:software` for that), debugging tools, and data structures.

### Data Structures

How does Python store data? As earlier, the concept of `x` representing data as a variable was discussed earlier along
with the term _data structure_. A data structure refers to an arrangement of data along with its relations among
each other and operations to access the data. In Python, similar to many other languages, the _Standard Library_ provides
several different data structures for storing data, with more structures being added through libraries such as NumPy. And
`x` points toward a data structure that is stored within memory, in this case, memory refers to a place on the computer
that can hold hold data.

#### Built-in Data Structures

This is a table of the built-in data structures of Python with the some of the common structures
being Lists, Strings, and Dictionaries. There is also `pickle()`, a insecure method for turning Python
code into portable programs (byte streams).

```{table}
 Data Structure | Description                                      | Syntax Example                       | Key Characteristics                                                                 |
|----------------|--------------------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------|
| **List** | Ordered, mutable sequence of items.              | `my_list = [1, "hi", 3.0]`           | Ordered, Mutable, Allows duplicates, Indexed                                        |
| **Tuple** | Ordered, immutable sequence of items.            | `my_tuple = (1, "hi", 3.0)`          | Ordered, Immutable, Allows duplicates, Indexed                                      |
| **Dictionary** | Unordered (ordered in Python 3.7+) collection of key-value pairs. | `my_dict = {"key": "value", "age": 30}` | Ordered (Since Python 3.7), Mutable, Keys must be unique and immutable strings, Values can be duplicated |
| **Set** | Unordered collection of unique, immutable items. | `my_set = {1, "hi", 3.0}`            | Unordered, Mutable, No duplicates, Elements must be immutable                       |
| **String** | Ordered, immutable sequence of characters.       | `my_string = "hello"`                | Ordered, Immutable, Allows duplicates (of characters), Indexed                      |
| **Frozen Set** | Immutable version of a set.                  | `my_fset = frozenset([1, 2, 3])`     | Unordered, Immutable, No duplicates, Elements must be immutable, Can be used as dict keys |
```

#### Common Data Structures from external libraries

Many data structures are stored within additional libraries, one of which is collections, a library that
must be imported to use, although it does not have to be separately installed on most Python installation
as it is a optional part of the _common library_. And the table below is a non-exhaustive list of data structures.

```{table}
 Data Structure  | Description                                                                 | Syntax/Usage Example                                     | Key Characteristics                                                                                                |
|-----------------|-----------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **`namedtuple`**| Factory function for creating tuple subclasses with named fields.           | `from collections import namedtuple; Point = namedtuple('Point', ['x', 'y']); p = Point(10, 20)` | Immutable, ordered, elements accessible by name and index, memory-efficient.                                         |
| **`deque`** | (Double-ended queue) List-like container with fast appends and pops from both ends. | `from collections import deque; d = deque(['a', 'b', 'c']); d.append('d'); d.popleft()` | Ordered, mutable, thread-safe for appends/pops from opposite ends, efficient for implementing queues and stacks. |
| **`Counter`** | Dict subclass for counting hashable objects.                                | `from collections import Counter; c = Counter(['apple', 'red', 'apple']); c['apple']` (Output: 2) | Unordered (like dicts before 3.7), mutable, elements are stored as dictionary keys and counts as values.             |
| **`defaultdict`**| Dict subclass that calls a factory function to supply missing values.       | `from collections import defaultdict; dd = defaultdict(list); dd['missing_key'].append(1)` | Unordered (like dicts before 3.7), mutable, provides a default value for keys not yet in the dictionary, avoiding `KeyError`. |
| **`ChainMap`** | Groups multiple dictionaries or other mappings together to create a single, updateable view. | `from collections import ChainMap; dict1 = {'a': 1}; dict2 = {'b': 2}; cm = ChainMap(dict1, dict2)` | Ordered (based on the order of mappings), effectively mutable (writes go to the first mapping), lookups search through mappings sequentially. |
```

Another common library is Pandas (installable through `pip install pandas`) which introduces three more data structures
which were inspired by languages such as R. Moreover, this pandas is often used within the context of object-oriented programming
in Python.

```{table}
| Data Structure | Description                                                                    | Syntax/Usage Example (requires `import pandas as pd`)                               | Key Characteristics                                                                                                |
|----------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **`Series`** | One-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The labels are collectively referred to as the index. | `s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'])` <br/> `s = pd.Series({'a': 1, 'b': 2})` | One-dimensional, size-immutable (though values can be changed), data-mutable, labeled index, can hold heterogeneous data types. |
| **`DataFrame`**| Two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Can be thought of as a dictionary-like container for Series objects. | `data = {'col1': [1, 2], 'col2': [3, 4]}; df = pd.DataFrame(data, index=['row1', 'row2'])` | Two-dimensional, size-mutable (can add/remove rows/columns), data-mutable, labeled axes (index for rows, columns for columns), can contain columns of different data types. |
| **`Index`** | An immutable array or ordered set implementing the axis labels for Series and DataFrame objects. It can contain numbers, strings, or other Python objects. | `idx = pd.Index([1, 2, 3, 'a', 'b'])` <br/> `df.index` or `df.columns` returns an Index object. | Immutable, ordered, provides labels for Series/DataFrame axes, supports set-like operations (union, intersection, etc.), can be non-unique by default but uniqueness can be enforced. |
```

### Classes

A class is a cross between a function and a data structure into an object. Objects are the fundamental core
to object-orientated programming, which will be left for other works to describe such as {cite}`OODesignPatterns`
as a reference work, or {cite}`freeman2020head` as a book. Moreover, the idea of object-oriented programming is
foundational to many simulation and modelling tools from Python's Salabim to commercial tools like
AnyLogic as they build on DEVS, the Discrete Event System Specification, which uses classes to define objects,
for example, a program using the DEVS model might have the following structure:

```{code} python
# M/M/C Queuing Code without Visualizations
# A = 1, B = 4, C = 5
# From The Salabim Documentation (MIT Licensed)

import salabim as sim

class ClientGenerator(sim.Component): # ClientGenerator Class
    def process(self): # Function Inside of a Class
        while True: # This will continue the loop until the end of the simulation
            self.hold(inter_arrival_time_dis.sample()) # Calling Data from Function
            Client() # Calls Client Class and its processes.


class Client(sim.Component): # Client Class
    def process(self): # Self means that it is referring to the client class
        self.request(clerks)
        self.hold(service_duration_dis.sample())


env = sim.Environment(trace=True) # Global Variable for Environment
number_of_clerks = 5 # Global Variable pointing to an Integer assigned to be 5.
inter_arrival_time_dis = sim.Exponential(1) # Instance of Library from Function
service_duration_dis = sim.Exponential(4) 

clerks = sim.Resource(name="clerks", capacity=number_of_clerks) 

ClientGenerator() # Calling the Class and its Process(es)
env.run() # In Salabim, this runs the simulation and its environment.
```

In this example, we see a short program made up of two classes (`ClientGenerator`, `Client`), and
seven function calls that interact with each to form a queuing system, which this text covers in
{ref}`sec:queuing_systems`, which is not needed for this pre-lab.

In `ClientGenerator`, there is a function `process` that enforces the inter-arrival times between clients
with the `hold` function, then it another class `Client` which defines the behaviors of the generated clients.
Moreover, in `Client` there is a function that calls `request`, which requests a server defined in an external
reference `clerks`, to serve the client (i.e: when a person enters a cashier from a checkout line), and `hold`
which stops the line from moving until the request is complete.

### Loops

In the example above, the reader might have notice a `while` statement, this is a type of loop, which consist, of two
main forms, for loops and while loops. A loop is when one or more expressions (a single operation within a function) runs
multiple times depending on the loop type. For a "for loop", it runs for x times, where the number of iterations is determined
by the signature of the loop. In contrast, a while loop continues until its condition, a condition is an expression that can be
true or false (which is equivalent to a preposition in mathematics), is false. Canonical examples of for and while loops are below.

#### For Loop Example

```{code} python
for i in 3 # For Loop Signature
    print(f"{i}, ") # Operation in Loop

1 2 3
```

#### While Loop Example

```{code} python
i = 0 # External Variable
while i < 5: # While Loop Signature
    print(i) # Operation 1 in Loop
    i += 1 # Operation 2 in Loop

1 2 3 4 5
```

### Python and Databases

A common way to store data is with databases, a type of data structure that is managed through a DBMS,
DataBase Management System, which defines the ways that users (software and people) can access and modify the data,
this is also known as access control, which is one of the reasons why databases exist. Moreover, Python provides an
in-built DBMS tool through the `SQLite3` package, [SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
which is a suitable and reliable method (the Library of Congress recommends it) of storing data in a database.
The downside of SQLite is it was made for local purposes, and it is not a typical database as it lacks a server environment
that exists in typical SQL and Non-SQL software packages such as MySQL, MariaDB, PostgreSQL, and MongoDB.

The reason why this is important is that SQLite is not as scalable for big data nor is it suitable for network applications.
For these purposes, which are common with simulation and modelling, particularly in industry, this text recommends being
familiar with at least one other method for interacting with databases; for example, a library named `databases` which supports
MySQL, PostgreSQL and SQLite which is useful to turning a SQLite database into a scalable, server-ready server-client
infrastructure.
:::

::::

(prelab-2)=
## Pre-Lab 2: Tutorial for Monte Carlo Methods (Do)

This pre-lab uses XLrisk (for Excel users) and monaco + pandas (for Python Users)
as the main implementation method; however, these all of these tasks can be
done within other packages in python such as the pyMC and (copulas or statsmodels) packages.

In this pre-lab we will discuss the Monte Carlo Method with its implementations
and do a short example of coin-flipping that loosely relates to Lab-2. Keep in mind that
the XLRisk and monaco + pandas sections are almost identical on purpose.

::::{tab-set}

:::{tab-item} XLRisk

### Functions

In XLRisk, there is a series of functions for defining a random variate, of which the bare
minimum for this pre-lab are here, with a more extensive list in {ref}`sec:software`.

- =RiskBernolli() # For a Bernoulli Variate
- =RiskUniform() # For a Uniform Variate
- =RiskCorMat() # For Copulas

### Correlations between distributions (Copula)

In this pre-lab, we consider copulas as forcing a distribution to assume the
behavior of another one, this is known as correlation. An example of this would be if a person goes to an
expensive hotel, it is more likely that they would get expensive food, tours, and everything else on their trip.  

Copulas are joint cumulative D.Fs for which the marginal D.F of each variable is bounded by $[0, 1]$ across the domain.

And the Gaussian copula, aka two distributions linked together with a copula based on a Gaussian, can take on different
appearances, depending on the marginal distributions this is an example from a completed {ref}`project-1`.

```{figure} #fig:copula
:label: fig:A

An example of the correlation between Accommodation Prices and Meal Costs through a Correlation Matrix,
this is related to {ref}`project-1`.

```

In XLrisk, this behavior is implemented through the function RiskCorMat, which takes a matrix and applies it to
random variates generated by XLRisk based on user parameters.

### Trials

a

### Results

b

### Skew and Kurtosis

c

### Walk-Through

d

:::

:::{tab-item} monaco + Pandas

### monaco Functions

In monaco, there is a series of functions that make up

### monaco Correlations

### monaco Trials

### monaco Presentation of Results

### Skew and Kurtosis through Pandas

### monaco Example Walk-Through

This example will be similar to the [monaco documentation](https://monaco.readthedocs.io/en/latest/), specifically a
down-scaled version of the baseball example, as that is directly linked with physical phomena 

:::

::::

(prelab-3)=
## Pre-Lab 3: Fundamentals of Debugging For Simulation (Do)

A critical part of working with complex systems and software is debugging.
In this case, this text defines debugging as a reliable, systematic method
for figuring out what is not working within a system. Traditionally,
debugging was an act of trial-and-error until the system behaved in-line
with expectations. However, there are several methods to improve debugging
and through this act, to improve the verification state of the system, which
include:

- Input-Output Analysis
- Breakpoints
- Unit Testing
- Automated Methods (Formal Methods)

Some of these methods are dicussed in more detail

### Breakpoints

### Concept: Unit Testing

In this case 

### Concept: Formal Methods

### Examples with Walk-Throughs

::::{tab-set}

:::{tab-item} Breakpoints
a
:::

:::{tab-item} Unit Testing
b
:::

:::{tab-item} Formal Methods
c
:::
::::

(prelab-4)=
## Pre-Lab 4: Short Overview of Modelling (Short Do)
::::{tab-set}

This pre-lab focuses on exposing the reader to different modelling schemas
that will be explored later in future pre-labs, chapters, projects, and
labs once their prerequisites are met. Essentially, this is a transition
pre-lab away from Monte Carlo to help understand the foundations of modelling.

More detailed information can be found {ref}`sec:system_modeling`, but this pre-lab
gives a sampler of different modelling methodologies.

:::{tab-item} System Dynamics

### Why System Dynamics

### Examples of System Dynamics

### Toy Model for System Dynamics

:::

:::{tab-item} Discrete Event Simulation

### Why Model Discrete Events?

### Examples of DES

### Toy Model for DES

:::

:::{tab-item} Agent-Based Modelling

:::

::::
(prelab-5)=
## Pre-Lab 5: Introduction to Simulation Software (Do)

Now that this text has covered a substantial amount of theory,
it is important for the reader to consider the different implementations
and tools that exist for simulating

::::{tab-set}

:::{tab-item} Anylogic (Object-Orientated)

Anylogic

:::

:::{tab-item} Netlogo

:::

:::{tab-item} OpenModelica

:::

:::{tab-item} Python

### BPTK-Py (Systems Dynamics, Functional Programming)

### Salabim (Discrete-Event Modelling, Object-Orientated)

### SimPy (Discrete-Event Modelling, Functional Programming)

### Mesa (Agent-Based Modelling, Object-Orientated)

:::

::::

(prelab-6)=
## Pre-Lab 6: A Quick Review of Queuing Theory (Reading)

Pre-lab reconstruction....

### Exponential Distribution

In probability courses and textbooks you may have heard about the exponential
distribution, one of the most prototypical queuing systems ($M/M/1$) relies on the
exponential distribution for its service times and inter-arrival rates.

The exponential distribution's CDF is defined as the following:

:::{math}
1-e^{x \lambda}
:::

Now, what are the properties that make exponential distributions useful for queuing?

:::{table}

| Property          | Description                                                                                                | Relevance to Queueing Models                                                                                                                                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Memoryless** | The probability of an event occurring in the future is independent of how much time has already elapsed. $P(T > s+t \mid T > s) = P(T > t)$. | Which Simplifies analysis significantly. For example, the remaining service time for a customer is independent of how long they've already been served. Similarly, the time until the next arrival doesn't depend on when the last arrival occurred. |
| **Relationship to Poisson Process** | If the number of arrivals in a given time interval follows a Poisson distribution, then the inter-arrival times (the time between successive arrivals) are exponentially distributed. | Many real-world arrival patterns (e.g., customers at a bank, calls to a call center) can be reasonably approximated by a Poisson process, making the exponential distribution a natural choice for inter-arrival times.                        |
| **Mathematical Tractability** | The mathematical form of the exponential distribution (PDF: $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$) often leads to simpler analytical solutions for queueing metrics like average wait time, queue length, and server utilization. | Allows for the derivation of closed-form analytic solutions for many queueing models (e.g., M/M/1, M/M/c).                                               |
| **Constant Hazard Rate** | The instantaneous probability of an event (e.g., service completion or arrival) occurring is constant over time. The hazard rate is equal to the rate parameter $\lambda$. | Reflects situations where the likelihood of an event happening in a small time interval doesn't change based on how long the process has been running. This can be a reasonable assumption for many service or arrival processes.          |
| **Single Parameter** | The distribution is characterized by a single parameter, $\lambda$ (the rate parameter), which is the inverse of the mean ($1/\mu$ where $\mu$ is the mean time between events). | Simplifies parameter estimation from observed data. Only one value needs to be determined to define the distribution for either arrival rates or service rates.                                                                            |

:::

### Kendall's Notation for Queues

How are queues formally represented? For example, what does $M/M/1$ mean?

In general, every queue can be represented in the format A/B/c/K/N/D
with the last three often excluded in most literature.

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

Using the {ref}`Kendall-Notation` above, we can determine that a $M/M/1$ queue is a
queue with a Markovian Arrival Process, a Service time that is Markovian,
and one server. Moreover, using this information, we know that the inter-arrival
times are exponential, and the time it takes to serve someone the queue is
also exponential, and that means we can calculate queue behaviors through
closed-form formulas, as seen below in {ref}`MM1Performance-Metrics`.

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

(prelab-7)=
## Pre-Lab 7: Automated Distribution Fitters (Short Do)

### On Automated Distribution Fitters (i.e: Phitter, Fitter)

Through simulation literature and real-world applications, it is relatively rare to see
methods as seen with {cite}`Krzysztofowicz:25` for one reason, the vast majority of the
literature is not building novel distributions or meta-Gaussians, but instead often use one of
these three tests to pick from an existing distributions. Keep in mind that in general these
tests are comparing an empirical (observed data) distribution to a parametric (defined by a
closed-form formula) distribution.

- The $\chi^2$ Goodness Of Fit Test (this test can be deceptive, read {ref}`sec:distribution_modeling`) for more information about this, and that you should consider not using this for continuous distributions.
- Kolmogorov–Smirnov test (the test for comparing data to continuous distributions, which has the limitation of sensitivity to differences near the median between an empirical and parametric distribution)
- Anderson–Darling Test (similar to the K-S test, but is more sensitive to differences between the tails of the empirical and parametric distributions)

### Exercises

::::{tab-set}

:::{tab-item} Exercise 1 with Given Hypothesis
A small call center has automatically recorded the wait times (in minutes) for a sample of 20 consecutive incoming calls.

```{code} python
1.619349216, 1.570739596, 2.38882075, 1.660162223, 1.594000051, 1.939417783, 1.840022611,
2.485874562, 1.693257222, 2.091845183, 1.526335951, 1.866234179, 1.541921394, 1.520759608,
1.629551915, 1.556652485, 1.914162185, 1.594754923, 2.027844882, 1.694913864, 2.4335776
```

Based on the nature of wait times, an exponential
distribution is often considered. First, calculate the sample mean of this data. Using this
sample mean as an estimate for the mean ($\frac{1}{\lambda}$) of an exponential distribution, determine the
rate parameter $\lambda$. Then, using this estimated $\lambda$, write down the probability density function (PDF)
of the fitted exponential distribution. Finally, use a software package (Phitter, Fitter) to fit an exponential distribution to
this data and compare its estimated parameters to your by-hand calculations.
:::

:::{tab-item} Exercise 2 without Given Hypothesis
A factory machine produces items in batches. Over 25 consecutive production runs, the number of defective
items found in each run are represented the data below

```{code} python
14, 15, 11, 10, 12, 5, 10, 7, 10, 17, 7, 11, 
13, 6, 8, 9, 13, 12, 7, 9, 9, 12, 11, 12, 9
```

Estimate the sample mean and the standard deviation of the number of defective items. Then use the observed
properties of the distribution (e.g: making a histogram, assessing its natural bounds), to determine the
possible hypothesis for the posterior distribution. Then test these hypothesis using a software package like
Fitter/Phitter or a statistical package.
::::

(prelab-8)=
## Pre-Lab 8: Overview of Differential Equations in Simulation (Read)

:::{admonition} Advisory: Chapter Reading
:class: warning dropdown

It is highly recommended that the reader read {ref}`sec:system_modeling`
before reading this pre-lab, as it provides more details and critical context
about the topics discussed as this pre-lab covers a bit about modelling.

:::

Previously in this text, we discussed and worked with queuing networks, the
Monte Carlo Method, System Dynamics, Distribution Modelling,
Random Variates, Random Number Generation, and Output Analysis
which are ubiquitous throughout simulation; however, these are
required but not sufficient for understanding the field of simulation,
because you will often see ODEs, SDEs, and PDEs being used to model behavior,
and a simulation practitioner (or any engineer) should be familiar
with them. This pre-lab focuses on giving a basic review of
ODEs and their application in simulation and modelling.

In general, DEs can be used to approximate real-world behaviors into
deterministic (ODE/PDE) or Stochastic behaviors (SDEs/IDEs);
however, even the deterministic models may have unresolved behaviors
(as most PDEs and higher-order ODEs do not have closed-form solutions).

### What are DEs (i.e: ODEs, PDEs, SDEs, and IDEs)?

In general, a differential equation (DE) is an equation that relates
a function to its derivatives, an example is the canonical ordinary
differential equation:

```{math}
y^{'} + p(x)y = q(x)
```

ODEs by definition are a differential equation (DE) dependent
on a independent variable with its unknowns consisting of
of at least one function and the derivatives of those function(s).

Additionally, there are other types of DEs that expand on the idea of
ODEs, the first one of which you are likely familiar with:

- PDEs (Partial Differential Equations)
- SDEs (Stochastic Differential Equations)
- IDEs (Integro-differential equations)

Here is a table describing the differences between the several types of DEs (non-ODE)
with further examples given throughout the rest of the pre-lab:

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

### ODEs for Modelling

These examples of using ODEs for modelling are inspired by
{cite}`harte1988consider`, which might sound a bit silly if you read the title,
but it is a landmark work in modelling and problem-solving in Environmental Science.

Additionally, ODEs come within several different types of ODEs that are solved
differently analytically - however, most automated solvers will usually use the
same methods and are instead limited by stiffness or the lack of a closed-form
solution. Here's a summary of the different forms of ODE and their analytic solution:

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

::::{tab-set}

:::{tab-item} Example 1: Depleting Resources

:::

:::{tab-item} Example 2: A Warming Sphere

:::

::::

### PDEs for Modelling and Simulation

PDEs ...

::::{tab-set}

:::{tab-item} Example 1: Heat flow in a uniform rod

:::

:::{tab-item} Example 2: Brownian motion

:::

::::

### SDEs for Modelling and Simulation


SDEs ....

::::{tab-set}

:::{tab-item} Example 1: Poisson process

https://personal.ntu.edu.sg/nprivault/MA5182/stochastic-calculus-jump-processes.pdf (Source)
:::

:::{tab-item} Example 2: Cholera Epidemiology
https://onlinelibrary.wiley.com/doi/10.1155/2023/7232395 (Source)
:::

::::

### IDEs for Modelling and Simulation

IDEs ...

::::{tab-set}

:::{tab-item} Example 1: SEIR Model

:::

:::{tab-item} Example 2: City Growth and Emergence

:::

::::

### Solving DEs with Python

#### ODE45

#### Runge-Kutta Methods

#### Approximations and Their Methods

(prelab-9)=
## Pre-Lab 9: Becoming Proficient at Simulation Software (Do)

This pre-lab will be more focused on developing skills via doing and
relies on {ref}`sec:system_modeling` for its theoretical foundations.

### Queuing Systems

### Discrete Event Models

### System Dynamics-Based Models

### Hybrid Models

(prelab-10)=
## Pre-Lab 10: A Short Introduction to Agent-Based Modelling (Do)

### What is an Agent?

### Agent Topology

### Three Characteristics of Agent-Based Modelling

#### Heterogeneity

#### Complexity

#### Emergence

### Walk-Through of a Varicella Spread Model

(prelab-11)=
## Pre-Lab 11: A Review of Optimization (Read)

### What does it mean to Optimize?

### How can you Optimize a Simulation?

### Common Software for Simulation Optimization

### OpenModelica

### Optquest (Anylogic)


(prelab-12)=
# Pre-Lab 12: Comparison of Modelling Techniques (Do)

## List of Common Modelling Techniques

## Task 1

## Task 2

## Task 3
