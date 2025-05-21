
(sec:buffons_needle)=
# Buffon's needle #


The goal of this section is to give a tour of concepts related to
simulation and modeling. And what better way to start that than with
[Buffon's needle](https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)?

__Description:__ The experiment has a table made of parallel strips of
wood all of the same width $d$. One also has a needle of length $\ell
< d$. The needle is tossed repeatedly onto the table $n$ times, and
for each case one records whether the needle crosses two strips when
it has come to rest. The original goal was to estimate the propability
$p$ that the needle crosses strips. This is illustrated in Figure
{ref}`df`. As we will see, this experiment can also be used to
estimate $\pi$.

__Modeling:__ How can we capture the above system $S$ as a precise
mathematical model? We can start by introducing a coordinate system on
the table as shown in the figure. For a needle toss, we let $x$ denote
the distance from the leftmost endpoint $P$ of the needle to the
nearest left-edge of the wood strip containing $P$. Next, we let
$\theta$ denote the angle that the needle forms with the $x$-axis.


```{code-cell} python3
print(2 + 3)
```




__Simulation:__ Independence


__Output analysis:__


__Reflection:__ Did we make any assumptions?



```{literalinclude} ../src/python/buffons-needle.py
:language: python
```
