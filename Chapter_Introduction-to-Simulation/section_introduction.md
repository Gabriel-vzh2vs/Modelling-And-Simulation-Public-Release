
(sec:intro_sim)=
# Simulation and Modeling #

What do we mean by simulation and modeling? We first note that these
activities will always be with reference to some _system_ that we want
to study. Sometimes, we may may be able to experiment directly with
the system, but as you can imagine there are many reasons why one will
not be able to rely on this approach alone. This is where __models__,
__modeling__, and __simulation__ enter the picture. Modeling and
simulation are two of the main __pillars of [systems
engineering](https://en.wikipedia.org/wiki/Systems_engineering)__

## Modeling ##

To analyze a system $S$ a first step is to develop a _model_ for
$S$. This model can be a _physical_ model such as a scaled down
version of an airplane wing placed in a wind-tunnel. One may then
measure lift and other forces as a function of wind speed, angles of
attack, and so on. However, building physical models is time-consuming
and costly. Moreover, obtaining all the kinds of measurements one
needs under all relevant conditions can be both challenging and
time-consuming. For some systems, building physical models may be
unrealistic, examples including planning and response for scenarios
involving natural and human-initiated disaster events. Based on this,
we will develop _mathematical models_ to capture and represent the
system. The overview of approaches are shown in
{numref}`modelingOverview`.

:::{figure} ../Figs/system-analysis-approaches.png
:align: center
:label: modelingOverview
Elements involved in the process of modeling and simulation of a system.
:::

In practice, complex modeling projects will often rely on a
combination of physical- and mathematical models.  The focus of this
book, however, is on the mathematical models, associated theory, and
the construction of _simulation models_, as indicated by the
red paths in {numref}`modelingOverview`. We will also focus on
analysis methodologies spanning modeling and simulation.

## Mathematical models ##

What is a mathematical model of a system $S$? In short, it is a
mathematical description of $S$, its properties, structure, and how it
operates or evolves with time. We will denote models by $M$, $M_1$ or
$M'$. Models come in many varieties. For example, their time
evoluation may be captured through ordinary- or partial differential
equations, or they may evolve in discrete time steps. Naturally, there
are also hybrid models involving both paradigms.

Models of even quite basic systems will have one or more _stochastic
components_. Analysis of such models is a central part of this book,
and a good foundation in probability theory and statistics will
definitely be helpful. We have included a chapter that tersely covers
this background material, but it is no substitute for an actual course
or a book on this topic.

```{note} add references here and link to prob/stats.
```

We should also clarify that when we say mathematical model we really
mean a formally specified model. A precise, algorithmic description of
a system may often be a more natural way to capture it. For a complex
system, it is not uncommon to employ a combination of mathematical and
algorithmic descriptions. We note that the term _formal methods_ (see,
e.g., <https://en.wikipedia.org/wiki/Formal_methods>) has a specific
meaning in computer science and, by association, so does _formal
models_. For this reason, we stick with the term mathematical model,
and we take this to also include algorithmic descriptions.

What is a good model? We address that under {ref}`sec:intro_validation`.

For some mathematical models you may be able to derive an analytic or
closed form solution, perhaps with help of software performing
symbolic computations such as Mathematica and SageMath. While one
should certainly embrace and take advantage of this whenever possible,
this situation is relatively rare. This is where simulations come into play.


(sec:intro_simulation)=
## Simulation ##

In this book, a __simulation__ will mean a program or script that
implements a model $M$. One may execute or run a simulation, possibly
providing input data and configurations, and generate output
data. Common terminology includes "running a simulation", "a
simulation run", and "simulation output data". If we want to emphasize
that we are not simply operating any old piece of code or executable,
but that it is actually tied to a model of a system, we may use the
phrase __simulation model__. What forms can simulations take? Here are
some examples:

- A spreadsheet model in Excel, possibly using a plugin such as XLRisk.

- A Python script exectured by the Python interpreter launched from a
  terminal window (i.e., using the commandline) or through Jupyter
  notebook.

- C++ source code compiled into an executable that:
  - Is invoked on the commandline on a desktop

  - Or that may require advanced hardware archictures such as a cluster, and
    is invoked through a job submission system (e.g., slurm) for a
    computation that is distributed across multiple nodes and cores
    using technologies such as [Open MPI](https://www.open-mpi.org/)
    and [OpenMP](https://en.wikipedia.org/wiki/OpenMP)

In this book we will focus mostly on Python and Excel/XLRisk.
```{note} add reference to chapter.
```

## Stochastic models, uncertainties and distribution modeling ##

Complex systems, but also not-so-complex systems, often include
stochastic elements. An example could be arrival times of customers to
a service (e.g., a post office). It is clear that such a model must
adequately represent such effects. In many cases, one may have a
sample containing observations of such stochastic elements. The
process of mapping such observations into random variables is called
distribution modeling, and is the topic of
{ref}`sec:distribution_modeling`. Another common phrase for this
process is __input analysis__.


(sec:intro_validation)=
## Validation and verification ##

How can we trust simulation output data? This brings us to the core
of the simulation approach, namely that:

- The model $M$ captures the system $S$ sufficiently well.

- The mathematical model $M$ is implemented correctly as a simulation
  model.

What is sufficiently well? It is important to realize that the
precursor to any modeling and simulation is typically a set of
questions about $S$. The goal of simulation-based analysis is to
provide meaningful answers to those questions. Ensuring this
fundamentally involves two steps.

::::{prf:definition} Validation and verification

The process of ensuring that $M$ represent $S$ in a sufficiently
accurate way is referred to as __validation__.
Similarly, the process of ensuring that the model $M$ is correctly
mapped to a simulation model (i.e., an implementation), is called
__verification__.
::::

Both validation and verification can be highly nontrivial processes,
and we will have more to say about that in {ref}`sec:validation`. We
also note that validation without a baseline (a set of questions and
requirements) is not very meaningful.

::::{prf:remark} "Have you validated your model?"
:class:dropdown

If you present work that involve modeling, you will likely be
confronted with the following question: "Have you validated your
model?" And if you say "yes", then "how did you validate your model?"

If you do not have a baseline or reference frame, your model can
always be criticized for missing something: it is highly unlikely that
you specified your model down to the smallest atom or electron. And if
you did, someone will likely bring up quarks.
::::

Once we have validated our model and verified the implementation, we
would like to assert that the data generated by the simulation model
can be used to reason about the system $S$ and answer the questions we
originally set out to address. However, for this we also need:

## Output analysis ##

Once we have completed all the steps above we can use the simulation
model to generate output data. However, since the model will generally
involve random variables (see {ref}`sec:prob_random_variables`) one
will need to generate multiple measurements, which often requires
running a series of simulations. Later in this book, we will go
through a range of techniques for such analysis, including their
underlying theory.


## Summary ##

The process of modeling, construction of simulation models, running
simulations, and processing data is typically an iterative process. It
requires a broad range of skills and expertise such as:

- Mathematics, probability and statistics

- [Algorithmic theory](https://en.wikipedia.org/wiki/Algorithm) and
  [data structures](https://en.wikipedia.org/wiki/Data_structure)

- [Programming](https://en.wikipedia.org/wiki/Computer_programming),
  [scripting](https://en.wikipedia.org/wiki/Scripting_language) and
  code management.

- [Data management](https://en.wikipedia.org/wiki/Data_management),
  and [experimental
  design](https://en.wikipedia.org/wiki/Design_of_experiments)

- [Mathematical modeling](https://en.wikipedia.org/wiki/Mathematical_model)

Needless to say, one can have a professional career in any of the
areas listed above. This book, we will cover all of the above with an
overall focus on the integration. In practice, this means that we have
to make some compromises. As an example, we will model systems but the
focus is not to show off how complex we can make these models. That
would be the topic of a course in mathematical modeling.


## Roadmap ##

The following is an annotated outline of chapters and modules in the book.


| Chapter Number | Description |
|:-----:  | :---------- |
|Chapter 1| Introduction to Simulation: an overview (this page) followed by a tour illustrating many of the concepts. It includes an introduction to the Monte Carlo method |
|Chapter 2| Probability and Statistics. This is a standalone chapter containing reference material. Consider this the bare minimum needed for the book. You may skip this and refer back as necessary.|
|Chapter 3| Output analysis and related theory. This chapter deals with the analysis of the data generated by simulation models. What you learn here will likely also shape how you structure your modeling and simulations. |
|Chapter 4| |
|Chapter 5| |

### Monte Carlo method ###


advanced topics

calibration, SA, UQ


```{tip}
Don't do that! Yes, I am watching you. [^fn]
```

[^fn]: A footnote

```{code-cell} ipython3
note = "Python syntax highlighting"
print(note)
```

```{math}
:label: eq:zsqrt
\begin{align}
z_1&=\sqrt{x_1^2+y_1^2} \\
z_2&=\sqrt{x_2^2+y_2^2}
\end{align}
```

See Equation {eq}`eq:zsqrt`

{cite}`Chen:25`


See [link](#sec:intro_sim) for more information

_mathematical model_ $M$ describing the system. How
precise does the model have to be?


```{bibliography}
:filter: docname in docnames
```
