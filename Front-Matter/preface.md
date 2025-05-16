(sec:preface)=
# Preface #

This book contains a sequence of topics that can form the basis for
an advanced undergraduate or a graduate course in simulation and
modeling. It covers theory and practice. While you may learn a lot
from just studying theory, it is the authors' opinion that "getting
your hands dirty" with implementing models and running simulations
will truly deepen your understanding in a way that theory alone cannot
do.

The book includes exercises spanning theory and practice. They range
in difficulty which we have tried to estimate and indicate. [example]

````{exercise}
:label: exer:test
define a symbol

Exercise here.
````

````{solution} exer:test
:label: my-solution
:hidden: false
```{code-block} python
def factorial(n):
    k = 1
    for i in range(n):
        k = k * (i + 1)
    return k

factorial(4)
```
````

For implementations we all have to commit to a language or a
tool. This book has has a strong focus on Python. Reasons for this
include that Python is mature, free, runs on virtually any platform,
and has great libraries covering most things needed in this book. If
you can point to aspects where Python runs short, we have no doubt you
are also sophisticated enough to know how you would address this,
perhaps in a different framework. Code is included inline in the text
and also in this book's repository.

Spreadsheet-based simulations are used in many professional
settings. We have included examples and exercises that are suited for
tools like Excel. Here you will greatly benefit from plugins such as
[XLRisk](https://github.com/pyscripter/XLRisk), described in more
detail in {ref}`sec:xlrisk`.

There are dedicated, professional simulation tools for many systems
classes such as queueing systems. The authors think that one should
certainly consider such tools in one's professional work. After all,
development of a solid tool is a complex and time-consuming process,
so why spend time reinventing a "mediocre wheel"? However, we have
found that almost all such tools are only supported under the MS
Windows platform. While one may "solve" this using virtual machine
technology, it tends to be cumbersome. A big reason for relying less
on these types of tools is their complexity and their learning curve:
there is a non-trivial time investment to be paid before one becomes
proficient enough to do anything interesting. For a course, this is
time taken away from fundamentals.

We have strived to make this book self-contained, but given the nature
of the field, we encourage the reader to explore the literature. The
following resources shaped a lot of the content in this book:

- {cite}`Banks:14`: comments

- {cite}`Law:13` : Describes theory in detail; has an extensive list
  of references;

- More

We have attempted the lofty goal of making a book that combines the
strengths of these resources turning this into an exposition that is
suited for advanced undergraduate students and graduate students
headed for careers in industry and academia tackling both theory and
practice.



Gabriel A. Lawrence

Henning S. Mortveit



```{bibliography}
:filter: docname in docnames
```
