
# Introduction to Simulation and Modeling #

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
physical models may altogether not be an option. [Example: planning
scenarios for various disaster events.] As a result, one will also
develop _mathematical models_ to represent the system. The overview
of approaches are shown in {numref}`modelingOverview`.

:::{figure} ../Figs/system-analysis-approaches.png
:align: center
:label: modelingOverview
Elements involved in the processing of modeling and simulation of a system.
:::

While one for complex projects will often rely both physical- and
mathematical models, the focus in this book is on mathematical models as outlined in the red path in {numref}`modelingOverview`.



```{tip}
Don't do that! Yes, I am watching you.
```

In
practice, development of models

_mathematical model_ $M$ describing the system. How
precise does the model have to be?

Modeling is generally
done in response to a set of questions about $S$.


Without any
questions, one may argue that modeling is
