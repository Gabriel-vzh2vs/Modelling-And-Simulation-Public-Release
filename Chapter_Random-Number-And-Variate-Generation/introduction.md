
(chap:random_number_generation)=
# Introduction


Developing good simulation models (i.e., the software of models) is
inextricably linked to random numbers. How is that? We need to be a
little more precise: for simulating __stochastic models__, it is
essential that we have access to a good random number generator. (One
may argue that most interesting models have stochastic elements, so
that is perhaps not a real limitation.)

For a stochastic model, there will be one or more components that is
governed by random variables. How do you investigate such models? As
we have seen in other sections of this book, there are certainly cases
where one may approach such models analytically. However, that is the
exception rather than the rule. Interesting stochastic models
typically resist such approaches, and one is forced to analyze them
through carefully orchestrated computational experiments. Such
MC-based approaches rely on being able to faithfully sample from the
distributions of the random variables in the models.

Those of you familiar with programming are no doubt aware that most
programming- and scripting languages have good support for generating
uniform random number (i.e., $U(0,1)$) as well as variates from most
common (and also some not-so-common) statistical distributions.
[Python has the scipy library; C++ has; Java]

This begs the question: in this day and age, which is 2025 at the time of
typing, why should one learn about how this works? Here is list of
reasons, in no particular order:

- There is still spreadsheet software in widespread use that rate
  quite poorly in this regard. You can remedy this by buying and
  installing plugins for said software, but it still requires you to
  be aware of this shortcoming.

- Early development of random number generators went through many aha!
  moments where "gold standards" were found to have gaping flaws and
  were promptly thrown in the dust bin. While those known cases were
  mostly elminated, knowing the pitfalls of yore will sharpen your
  abilities to detect more insidious ones. And this will certainly
  make you reflect more carefully when developing your own stochastic
  models and implementing them.

- Learning about the properties associated with good random number
  generators will make you aware of what may go wrong. [Marsaglia.] It
  will teach you how to spot flaws in modeling and implementation
  which may manifest in output data and visuals looking "sus". You
  will better understand what qualifies as "sus".

- Sometimes the random distribution that you are looking for does not
  live in scipy or your favorite programming language library. What do
  you do then?

- Libraries and toolkits are still littered with remnants from the
  past. The C rand() function is one such example. A willy-nilly,
  uncritical copy-paste from stackexchange can quickly land you in
  trouble. This is just an example, and perhaps one that is becoming
  increasingly harder to fumble, but it illustrates the point.


__Chapter structure__


This chapter is split into two parts:

- [Uniform [0,1] random number generators $U(0,1)$](section_random_number_generation.md)
- [General variates](section_variates.md)

The first part we covers the generation of (pseudo-)random
$U(0,1)$-variates. As you will see, a high-quality $U(0,1)$ random
number generator is the foundation for generating variates from most
other distributions.

:::{figure} figs/dilbert-random.jpg
:label: fig:random
:width: 800pt
<!-- https://scottadams.locals.com/post/5630210/proposed-dilbert-comic-licensing-plan -->
(Included under Fair Use terms)
:::
