
(sec:intro_sim)=
# Simulation and Modeling #

What do we mean by simulation and modeling? It will always be with
reference to some _system_ that we want to study. While one may
sometimes experiment with the system directly, there are many reasons
why one will not be able to rely on this approach alone. This is where
models and modeling enter the picture.

## Modeling ##

To analyze the system $S$ a first step is to develop a _model_ for
$S$. This model can be a _physical_ model such as a scaled down
version of an airplane wing placed in a wind-tunnel. One may then
measure lift and other forces as a function of wind speed, angles of
attack, and so on. However, building physical models is time-consuming
and costly. Moreover, obtaining all the kinds of measurements one
would needs under all the conditions one would need to explore may be
both challenging and time-consuming. For some systems, building
physical models may by very unrealistic. [Example: planning
scenarios for various disaster events.] As a result, we will also
develop _mathematical models_ to represent the system. The overview
of approaches are shown in {numref}`modelingOverview`.

:::{figure} ../Figs/system-analysis-approaches.png
:align: center
:label: modelingOverview
Elements involved in the processing of modeling and simulation of a system.
:::

In practice, complex modeling projects will often rely on a
combination of physical- and mathematical models.  The focus of this
book, however, is on the mathematical models, associated theory, and
construction of _simulation models_ and the analytics and
methodologies that go with these. These are indicated by the red paths in
{numref}`modelingOverview`.

## Mathematical models ##

For some mathematical models you may be able to derive a closed form
solution, perhaps with some help from software performing symbolic
computations such as Mathematica and SageMath. While one should
certainly embrace this when possible, this situation is relatively
rare, but see the section {ref}`sec:intro_validation` below.

We should also clarify that when we say mathematical model we really
mean a formally specified model. A precise, algorithmic description of
a system may often be a more natural way to capture it. For a complex
system, it is not uncommon to employ a combination of mathematical and
algorithmic descriptions. We note that the term _formal methods_ (see,
e.g., <https://en.wikipedia.org/wiki/Formal_methods>) has a specific
meaning in computer science and, by association, so does _formal
models_. For this reason, we stick with the term mathematical model
where we include algorithmic descriptions.

Many systems will have one or more _stochastic components_. Analysis
of such models is a central part of this book, and a good foundation
in probability theory and statistics will definitely be helpful. We
have included a chapter that tersely covers this material, but
it is no substitute for a course or a book on this topic.

```{note} add references here and link to prob/stats.
```

## Simulation ##

(sec:intro_validation)=
## Validation ##

In practice, one may be able to determine certain properties or invariants


## Verification ##


## MBSE and SysML ##


## Stochastic models ##

Types of uncertainties.


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

Modeling is generally
done in response to a set of questions about $S$.

```{bibliography}
:filter: docname in docnames
```
