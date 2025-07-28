
(prelab-5)=
# Pre-Lab 5: Fundamentals of Debugging For Simulation (Short Do)

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
In most IDEs, the concept of a breakpoint generally exists, and a breakpoint is generally
used to ensure that the code in question runs
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

A common language for making software provable is _LTL_, Linear Temporal Logic, that
allows for the application of logic on to a process or system. This work will not
in-depth about how to do LTL, but will provide an outline of some critical concepts.

LTL is composed of the following elements: variables, boolean values, and operators that make up properties (model-related traits).
Some of the operators are the "and" ($\land$), "or" ($\vee$),
"exclusive or" ($\oplus$), "not" ($\neg$), "until" (U), "next" (X), and
"eventually" ($\rightarrow$) operators. These operators can combine into compositions
in the context of variables which allow for creating statements such as
"this event will _eventually_ happen at some point in the system's lifetime _and_
be true afterward". And the path defined by LTL statements is verified by model checking - which os similar to simulating each possibility and ensuring that the behavior matches the description.  More information is available in dedicated sources on LTL like
{cite:p}`fisher2011introduction`, {cite:p}`wang2019formal`, and {cite:p}`clarke1997another`.

What follows is an example of using LTL in a Python-Based Library[^2],
PyReason. Suppose there is a traffic light that has three states: green, yellow, and red, and the following transition pattern applies: $S_green \rightarrow S_yellow \rightarrow S_red \rightarrow S_green$.

Logically, three properties of this system can be defined as the following:

1. The signal cannot be in multiple states at the same time - i.e:
a light cannot be green and red:

```{math}
G(\neg(is_green \land is_red) \vee (is_red \land is_green) \vee (is_green \land is_red))
```

This can be read as the following, it is is globally true that the
light cannot be in green and red _or_ green and yellow, _or_ yellow and red. Or in using set notation, $\forall S: is_green + is_red + is_yellow = 1$.This is an *invariant* property, meaning that it remains true for all states in a system.

2. Upon every update, the system shall move from one state to another. In a specific order defined through the transition pattern above.

```{math}
G(is_red \rightarrow X(is_green)) \land G(is_green \rightarrow X(is_yellow)) \land G(is_yellow \rightarrow X(is_red))
```

Which can be read as "_if_ the light is red, the next light will be green, _AND_ _if_ the light is green, the next light will be yellow, and if the light is yellow, the next light will be red."

3. The initial state of the system shall be green.


```{code} python3
import pyreason as pr
pr.reset()

# Nodes are 'light', edges represent properties (simple graph)
graph = pr.Graph()
graph.add_node("light")
pr.add_graph(graph)

# 2. Define the initial state (Facts)
# The light is green at time t=0
initial_facts = [
    pr.Fact("is_green_fact", "light", "is_green", True, [0, 0])
]
pr.add_facts(initial_facts)

# 3. Define the transition logic (Rules)
# These rules tell the system how to move from one state to the next.
# The 't' is a variable representing time.
rules = [
    # If the light is green at time t, it will be yellow at t+1
    pr.Rule(
        "GreenToYellow",
        [pr.Fact(None, "light", "is_green", True, ["t", "t"])],
        [pr.Fact("is_yellow_fact", "light", "is_yellow", True, ["t+1", "t+1"])]
    ),
    # If the light is yellow at time t, it will be red at t+1
    pr.Rule(
        "YellowToRed",
        [pr.Fact(None, "light", "is_yellow", True, ["t", "t"])],
        [pr.Fact("is_red_fact", "light", "is_red", True, ["t+1", "t+1"])]
    ),
    # If the light is red at time t, it will be green at t+1
    pr.Rule(
        "RedToGreen",
        [pr.Fact(None, "light", "is_red", True, ["t", "t"])],
        [pr.Fact("is_green_fact", "light", "is_green", True, ["t+1", "t+1"])]
    )
]
pr.add_rules(rules)


pr.settings.verbose = False # Turn off detailed output for clarity
interpretation = pr.reason(timesteps=10)

# 5. Model Checking
print("Traffic Light State Over Time:")
for t in range(11):
    state = "unknown"
    if interpretation.nodes["light"].facts[t].get("is_green"):
        state = "Green"
    elif interpretation.nodes["light"].facts[t].get("is_yellow"):
        state = "Yellow"
    elif interpretation.nodes["light"].facts[t].get("is_red"):
        state = "Red"
    print(f"Time {t}: {state}")

# Doing output analysis: using the intervals where a property is true and matching it with expectations

green_intervals = interpretation.nodes["light"].labels["is_green"].get_intervals()
print(f"\nThe light is green during these time intervals: {green_intervals}")
```

a

a
:::
::::

[^1]: This is where the _formal_ in formal methods comes from, as it is talking about
code as a provable statement and often using proof to support the statement.

[^2]: LTL and other Temporal Logics are not well supported in Python, as it is more of a
mathematical topic than a standard programming topic, and common programming languages
that are more equipped to handle these are FizzBee, PRISM Model
Checker, UPPAAL, and GreatSPN.
