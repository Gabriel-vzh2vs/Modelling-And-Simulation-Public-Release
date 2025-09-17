
(prelab-4)=
# Pre-Lab 4: Fundamentals of Debugging For Simulation (Short Do)

Now that this text has covered a substantial amount of theory,
it is important for the reader to identify and consider malignant
patterns in simulation, which is what this pre-lab aims to aid in
doing. This pre-lab unlike {ref}`prelab-3` focuses on using technological
verification instead of structural validation.

A critical part of working with complex systems and software is debugging.
In this case, this text defines debugging as a reliable, systematic method
for figuring out what is not working within a system. Traditionally,
debugging was an act of trial-and-error until the system behaved in-line
with expectations. However, there are several methods to improve debugging
and through this act, to improve the verification state of the system, which
include:

- Breakpoints
- Unit Testing
- Formal Methods

As a general concept, each of these are a part of system verification. Verification
is proving the system meets system requirements and specifications. Moreover, each of these
listed processes are required but not sufficient for robust, supported verification.
For example, breakpoints prove that the program can run without errors or invalid instructions;
unit tests prove that the behavior of the program is consistent with use cases; formal
methods prove that the model as a whole meets specifications. Each of these method
add value to the other methods when combined.

Some of these methods are discussed in more detail in {ref}`sec:output_analysis`,
and {ref}`sec:validation` as these methods are generally considered a branch of
verification and validation.

::::{tab-set}


:::{tab-item} Breakpoints
In most IDEs (such as VS Code), the concept of a breakpoint generally exists, and a
breakpoint is generally used to ensure that the code in question runs. In this case run refers
to the program/model completing its tasks - *not* that the tasks are correctly done,
but that the program begins and terminates without issue. If an error does prevent
execution at a breakpoint, then the IDE will allow the practitioner to look at the
data structures, the trace of the events before the error (a trace is a list of
operations called or performed by the program), maybe an error message
(depending on the packages).

The reason why breakpoints are useful might be apparent to some readers, particularly by now, but
essentially, a breakpoint allows a practitioner to discover hints about why their program
is unable to complete execution. This use usually involves moving through a series of
operations and functions trying to find the source of the error. Moreover, breakpoints have
another use, to analyze why a output from a program or function is incorrect. A practitioner
can leverage breakpoints to determine where a calculation goes wrong or which assumption in a
model was either inconsistent programmatically or incorrectly implemented.

Here is a toy example for the reader that might show why breakpoints are important in
software implementations of models. In this example, there is a single function
with an error someone within its logic.

```{code} python3
def find_magic_sum(data_list):
    """
    This function is supposed to sum all numbers in a list that are > 5.
    """
    magic_sum = 0
    for number in data_list:
        if number > 5:
            magic_sum += 1 # This line might be of interest.
            
    return magic_sum

# --- Executing the Function  ---
numbers = [2, 8, 4, 10, 6]
expected_result = 8 + 10 + 6  # Should be 24
actual_result = find_magic_sum(numbers)

print(f"List of numbers: {numbers}")
print(f"Expected sum (> 5): {expected_result}")
print(f"Actual function result: {actual_result}") # Why is 3 the result?
```

Once the reader runs this script, they get the statement that the actual result
is 3, when the expected result is 24. The reason for that is that the magic
sum is adding 1 for each of the numbers instead of summing the number itself
to a variable named 'magic_sum'. If the reader places a breakpoint
on the line marked with magic_sum += 1 and steps through the cycle three times
they will see the variable go from 1 to 2 to 3, instead of the correct
sequence based on the list of 8, 18, and 24.

One of the issues when using breakpoints is the problem of "where", as in,
where should you place an breakpoint within a program. The reason why this is
an problem is that if the error occurs before the breakpoint, the breakpoint is
never activated. With the example above, if the reader places it on the print statement,
they might miss the source of the error as it will only show the end results without the
context that precedes it. One of the solutions to this problem is
to combine breakpoints with the next technique, unit testing, which will narrow
the search area for possible issues (in ideal circumstances).
:::

:::{tab-item} Unit Testing
What is a Unit Test? A unit test is a (hopefully small) program that allows for the
verification of program outputs per function or a group of closely-related functions.
A unit test usually consists of the testable function, a test case (such as $2 + 2 = 4$)
with a boolean result that is _true_ when the function's output matches the expected
test case output, and _false_ otherwise (this is called an assert statement by programmers).
Through this structure, unit testing helps to provide a level of software verification as a
correctly-written unit test will _surely_ fail if the system's requirements are not met.

In Python, there is a plugin called PyUnit/unittest which allows a user to create to create
a test with the following structure.

```{code} python3
import unittest
from student_written_package import a_function

class TestCase(unittest.TestCase):
    def setup_a_function(self):
    """This function should provide the parameters that the function needs to function"""
        self.a_function = a_function()
        # r is the switch that makes it read the data in data source
        self.file = open("data_source", "r")

    def test_Clean_Up(self):
        self.file.close()

    def testCase_1(self):
        assert a_function() == 1 # This is the assert statement that verifies a behavior.

    def testCase_2(self):
        assert a_function() == "correct_element" # This is the assert statement that verifies a behavior.

if __name__ == "__main__":
    unittest.main()

```

There are several considerations when using a unit test:

1. The practitioner must have known, validated test cases and expected parameters
and a functional structure,
which goes back to {ref}`prelab-3` and its discussion on using non-technological
techniques to define and justify the model.
2. A unit testing framework should only be a part of the debugging process,
not a substitute for other methods of verification and validation.
3. Ideally, test cases would cover the most common use cases and
known extreme events.
4. The context of unit tests is per function, which means that it is
difficult to see what is going wrong within a complex model using unit cases
alone.

:::

:::{tab-item} Formal Methods
Formal methods refer to making code that is based on mathematical logic[^1] and
system specifications. In general, formal methods are difficult and time-consuming
to capture for every element of the system meaning that they should be automated and
focused to critical elements within the model.

A common language for making software provable is _CTL*_, Computational Tree Logic*, that
allows for the application of logic on to a process or system. This work will not
in-depth about how to do CTL*, but will provide an outline of some critical concepts.

CTL* is composed of the following elements: variables, boolean values, and operators that
make up properties (model-related traits).
Some of the operators are the "and" ($\land$), "or" ($\vee$),
"exclusive or" ($\oplus$), "not" ($\neg$), "until" (U), "next" (X), and
"eventually" ($\rightarrow$) operators. These operators can combine into compositions
in the context of variables which allow for creating statements such as
"this event will _eventually_ happen at some point in the system's lifetime _and_
be true afterward". And the path defined by CTL* statements is verified by model checking -
which is similar to simulating each possibility and ensuring that the behavior matches the description.  
More information is available in dedicated sources on CTL* and its subsets:
{cite:p}`fisher2011introduction`, {cite:p}`wang2019formal`, and {cite:p}`clarke1997another`.

What follows is an example of using CTL* in a Python-Based Library[^2],
PyReason. Suppose there is a system where two entities are racing each
other for a single, exclusive resource and the designer wants to ensure
that only one entity uses the resource at a time. This type of situation
is often called a race condition, and the solution is called a mutex
(mutual exclusion).

```{code} python3
from umaudemc import check

initial_term = "$ [a, wait] [b, wait]"
modules = ["MUTEX", "MUTEX-PREDS"]

# Safety property: a and b are never in critical section simultaneously
safety_formula = "[] ~(crit(a) /\ crit(b))"
safety_result = check("mutex.maude", initial_term, safety_formula, modules=modules)
print("Safety Property Result:", safety_result)

# Liveness property: if a is waiting, eventually it enters critical section
liveness_formula = "[] (wait(a) -> <> crit(a))"
liveness_result = check("mutex.maude", initial_term, liveness_formula, modules=modules)
print("Liveness Property Result:", liveness_result)

```

There is another formal methods that this text covers in later chapters called
Finite State Machines ({ref}`sec:cellular_automata`, {ref}`sec:DFA`), but this prelab
will not cover that to reduce deduplication of efforts in this text.

And many that this text does not approach as they are uncommon in simulation[^3], and a
nonexhaustive list is below along with some external texts that describe them in further
detail:

1. Static Analysis techniques such as linters (which are similar to breakpoints);
2. Automated theorem provers like LEAN, Isabelle, or RCoq (proving theorems is an exercise left to the reader);
3. And more!

:::
::::

[^1]: This is where the _formal_ in formal methods comes from, as it is talking about
code as a provable statement and often using proof to support the statement.

[^2]: LTL and other Temporal Logics are not well supported in Python, as it is more of a
mathematical topic than a standard programming topic, and common programming languages
that are more equipped to handle these are FizzBee, PRISM Model
Checker, UPPAAL, and GreatSPN.
