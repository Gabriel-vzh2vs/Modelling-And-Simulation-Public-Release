

(sec:preface)=
# Preface #


Our philosophy is that simulation by itself makes little sense. And
that modeling by itself makes little sense. Models arrive in response
to questions about a system. The nature of the questions and the level
of detail requested dictate what type of models we reach for. The
types of simulations, programs, scripts, or apps that we prepare are
informed by the questions as well as the type of model we chose.

In this book we harp on modeling, but we do not go full bore into
mathematical modeling. The models have enough depth to give
interesting illustrations of the simulation techniques and analyses
that form the core of the book.  The textbook contains a collection of
topics that (eventually) can form the basis for an advanced
undergraduate or a graduate course in simulation and modeling.

The book covers theory and practice. While you may learn a lot from
just studying theory, it is the authors' opinion that nothing firms up
your understanding more than "getting your hands dirty" implementing
models, running simulations, and putting that theory to
practice. Having to figure out why a simulation does not work, and why
it produces non-intuitive results can be one of the greatest catalysts
for learning. The book has exercises covering theory and practice and
at various difficulty levels. Do the exercises!

<!--
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
-->

For code and tools we had to make a choice.  We chose, however, to
focus on Python for the programming and code. It is a language that is
popular and known by students, it is reasonably mature, free, runs on
virtually any platform, and has great libraries covering most things
needed in this book. If you are smart enough to know aspects where
Python runs short, we have no doubts you are also sophisticated enough
to know about solutions. Code is included inline in the text and also
in this book's repository.

Spreadsheet-based simulations are used in many professional
settings. We have included examples and exercises that are suited for
tools like Excel. Here you will greatly benefit from plugins such as
[XLRisk](https://github.com/pyscripter/XLRisk), described in more
detail in {ref}`sec:lab`.


There are excellent commercial tools for a range of simulation models
such as queueing systems. The authors think that one should certainly
consider such tools in one's professional work. After all, development
of a solid tool is a complex and time-consuming process, so why spend
time reinventing a "mediocre wheel"? There are a few reasons for our
choice of Python and XLRisk. First, an advanced, professional solution
is a complex piece of software with a significant learning curve. So
much so that it can come in the way of learning the
fundamentals. While it is certainly advantageous to know a
professional tool, we believe that issuing a basic "simulation
driver's license" should come first first. Another second reason for
our choice is that most professional products focus squarly on MS
Windows as their platform. While it may be true that most
professionals in the field use that platform, that is certainly not
true for students. In our experience, working with virtual machines
causes a lot of frustration, even it a student gets it installed and
configured correctly.


<!--
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
-->


_Gabriel A. Lawrence & Henning S. Mortveit_


<!--

```{literalinclude} ../src/python/buffons-needle.py
:language: python
```

```{bibliography}
:filter: docname in docnames
```

-->
