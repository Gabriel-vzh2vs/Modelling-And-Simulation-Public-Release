
(sec:intro_sim)=
# Simulation and Modeling #

What do we mean by _simulation_ and _modeling_? To start this journey
off, we first introduce some context. First, these two activities are
rarely performed by themselves, but are done with respect to some
_system_ that we want to study. Typically, we start from a list of
questions about this system, and we want answer these as accurately as
the situation deems necessary. In this book we will make all this much
more precise through a combination of theory and examples including
hands-on projects. In the remainder of this section we provide a
preview of many of these elements and close by listing a roadmap that
can be used for navigating the content.


## Physical models ##

Sometimes, we may may be able to experiment directly with the
system. Or one may be able to construct a _physical_ model in the form
of a scaled down version of the system, such as an airplane wing
placed in a wind-tunnel. One may then measure lift and other forces as
a function of wind speed, angles of attack, and so on. However,
building physical models is time-consuming and costly. Moreover,
obtaining all the kinds of measurements one needs under all relevant
conditions can be both challenging and time-consuming. For some
systems, building physical models may be unrealistic, examples
including planning and response for scenarios involving natural and
human-initiated disaster events.  As you you can imagine there are
many reasons why this approach may be challenging, including ethical
considerations.

This is where _models_, _modeling_, and _simulation_ enter the
picture. Modeling and simulation are two of the main pillars of
[systems
engineering](https://en.wikipedia.org/wiki/Systems_engineering), and
are the central topic of this book. However, while this is our focus
we note that a serious analysis will often involve a combination of
physical models and experimentation developed in conjunction with
models and simulations in an iterative manner. An overview of
approaches to system analysis are shown in {numref}`modelingOverview`
where our focus is indicated by the red paths.


:::{figure} ../Figs/system-analysis-approaches.png
:align: center
:label: modelingOverview
Elements involved in the process of modeling and simulation of a system.
:::



## Terminology ##

We will talk about systems, models and simulations. Here we typically
use $S$ to denote systems, and $M$ to denote models. We do not have a
good symbol for simulations, $S$ being taken already.

```{note} A reference slide set with terminology for military context:
[overview](https://ndia.dtic.mil/wp-content/uploads/2019/systems/Mon_Coolahan.pdf)
```

## Mathematical models ##

What is a mathematical model of a system $S$? In short, it is a
mathematical description of $S$, its properties, structure, and how it
operates or evolves with time. We denote models by $M$, $M_1$ or
$M'$. Models come in many varieties. For example, their time
evoluation may be captured through ordinary- or partial differential
equations, or they may evolve in discrete time steps. Naturally, there
are also hybrid models involving both paradigms.

```{note}
Reference/link to chapter with background on modeling paradigms.
```


Models of even basic systems will often have one or more _stochastic
components_. Analysis of such models is a central part of this book,
and a good foundation in probability theory and statistics will
definitely be helpful. We have included a chapter that tersely covers
this background material, but it is no substitute for an actual course
or a book on this topic.

```{note} add references here and link to prob/stats.
```

We should also clarify that when we say mathematical model we really
mean a formally specified model. A precise, algorithmic description of
a system may sometimes be more natural.  For a complex system, it is not
uncommon to employ a combination of mathematical- and algorithmic
descriptions. We note that the term _formal methods_ (see, e.g.,
<https://en.wikipedia.org/wiki/Formal_methods>) has a specific meaning
in computer science and, by association, so does _formal models_. For
this reason, we stick with the term mathematical model, and we take
this to also include algorithmic descriptions.

What is a good model? We address that briefly later in this section
under {ref}`sec:intro_validation` and in more detail in
```{note}
Link to V&V
```

For some mathematical models you may be able to derive an analytic or
_closed form solution_, perhaps with help of software performing
symbolic computations such as Mathematica and SageMath. While one
should certainly embrace and take advantage of this whenever possible,
this situation is relatively rare. This is where simulations come into
play.


(sec:intro_simulation)=
## Simulation ##

In this book, a _simulation_ will mean a program or script that
implements a model $M$ of a system $S$. One may execute or run a
simulation, possibly providing input data and configurations, and
generate output data. Common terminology includes "running a
simulation" (executing the simulation software), "a simulation run"
(an instance or invocation of the simulation), and "simulation output
data" (the data generated by one or more simution runs). If we want to
emphasize that we are not simply operating any old piece of code or
executable, but that it is actually tied to a model of a system, we
may use the phrase _simulation model_. What forms can simulations
take? Here are some examples:

- A spreadsheet model in Excel, possibly using a plugin such as XLRisk.

- A Python script exectured by the Python interpreter launched from a
  terminal window (i.e., using the commandline) or through a Jupyter
  notebook.

- C++ source code compiled into an executable that:

  - Is invoked on the commandline on a desktop

  - That may require advanced hardware archictures such as a cluster,
    and is invoked through a job submission system (e.g., slurm) for a
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
adequately represent such effects by including for appropriate random
variables.

In many cases, one may have a sample containing measurements or
observations system components reflecting such stochastic
elements. The process of mapping such observations into appropriate
random variables is called _distribution modeling_ and is the topic of
{ref}`sec:distribution_modeling`. Another common phrase for this
process is _input analysis_, but we reserve that broader term to mean
more.


(sec:intro_validation)=
## Validation and verification ##

How can we trust data generated by simulations? How do we know we can
trust it? This brings us to the core of the simulation-based system
analysis, namely:

- The model $M$ must capture the system $S$ sufficiently well.

- The mathematical model $M$ must be implemented correctly as a
  simulation model.

What is sufficiently well? It is important to keep in mind that the
precursor to any modeling and simulation is generally a set of
questions about $S$. The goal of simulation-based analysis is to
provide meaningful answers to those questions. Ensuring "sufficiently
well" entails aspects such as having the model include the required
features to answer the questions (_fidelity_), and the features need
to have adequate _resolution_. The model must also be able to assert
meaningful bounds on the estimates it can generate which ties into the
area of uncertainty quantification and sensitivity analysis (UQ and
SA). In practice, this is often a challenging task, but fundamentally
it involves two steps.


::::{prf:definition} Validation and verification

The process of ensuring that $M$ represent $S$ in a sufficiently
accurate way is called _validation_.  Similarly, the process of
ensuring that the model $M$ is correctly mapped to a simulation model
(i.e., an implementation), is called _verification_.

::::

Both validation and verification can be quite complex, and we will
have more to say about that in {ref}`sec:validation`. We also note
that validation without a baseline (e.g., a set of questions and
requirements) is not very meaningful.

::::{prf:remark} "Have you validated your model?"
:class:dropdown

If you present work that involve modeling and simulation, you will
likely be confronted with the following question: "Have you validated
your model?" And if you say "yes", then the follow-up question "How
did you validate your model?"

If you do not have a baseline or reference frame, your model can
always be criticized for missing something: it is highly unlikely that
you specified your model down to the smallest atom or electron. And if
you did, there is always someone in the crowd that has heard about quarks.
::::

Of course, the overall goal of V&V is the two-step argument that when
the mathematical model and its implementation are both good, then the
data generated by the similation tool can be used to reason about the
system $S$ and the questions we originally set out to address. This
brings us to the topic of _output analysis_.


## Output analysis ##

Once we have checked the box regarding V&V, we can generate output
data. However, since the models will generally involve random
variables (see {ref}`sec:prob_random_variables`) one will generally
have to generate a series of measurements and carry out appropriate
statistical analysis. In this book we will describe the basic
techniques for estimating system measures and their uncertainties
while accounting for aspects such as (i) limited sample size, (ii)
skewness, and (iii) lack of independence and correlation.


## Summary ##

The process of modeling, construction of simulation models, running
simulations, and processing data is typically an iterative process. It
requires a broad range of skills and expertise, including:

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

- Domain expertise for the system that we are studying.

Needless to say, one can have a professional career in any of the
areas listed above. This book, we will cover all of the above with an
overall focus on their integration. In practice, this means that we
have to make some compromises. For example, we will generate models of
systems, but the focus is not to show off how complex we can make
things, that would be the topic of a course in mathematical modeling
combined with specialty from a domain. Similarly, we will not generate
models that rely on access to HPC facilities, nor how to run software
on such architectures.


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
