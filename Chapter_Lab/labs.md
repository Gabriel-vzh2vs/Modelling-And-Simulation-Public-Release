# Labs
The labs serve a dual purpose in this text, they enable the reader to apply lessons from this book to real-world examples, and they allow for assessment of the reader's knowledge of the material either through comparing models with reference models through self-assessment or by formal assessment by an external grader. It is recommended to do seven to eight labs within a course, as some labs may take longer to fully understand and go through. Additionally, lab descriptions are written with a modified ODD (Overview, Design concepts and Details) protocol that is shortened based on the model's requirements (e.g: sections that do not apply to the model, or sections that are left to the reader to complete). 
:::{note}
:class: dropdown

In this section, difficulty is expressed by a symbol and a color, which are dual indicators
meaning that they will always go together (i.e you will never see a color with a different symbol, )
- Green and Pen: Labs that we consider approachable and should take the average prepared student less than 1 hour to complete;
- Orange and Megaphone: Labs that we consider will take a bit of thought, we recommend taking 1 to 2 hours to complete this task;
- Red and Circle
Additionally, if you do not complete the pre-lab, you can move each difficulty level up by one (e.g: Green and Pen goes to Orange and Megaphone).
:::

:::{admonition} Lab 1
:class: Attention
This is an Attension Note.
:::

:::{admonition} Lab 1
:class: Danger
This is an Attension Note.
:::


:::{admonition} Lab 1
:class: tip
# Lab 1: Computing $\pi$ with Monte Carlo Methods (Excel or Python)
## Purpose and Patterns

### Statement of Model Purpose
This model's purpose is to demonstrate the concept of Monte Carlo Intergration through a canonical example of calculating $\pi$ through random sampling from a uniform space. Furthermore, this mechanism of Monte Carlo Intergration can be expressed as a transformation of Buffon's Needle as known as Buffon's Noodle uses _experiments_ to measure $\pi$, leverging the following formula for number of samples that reside within a unit circle that resides within an arbitary-defined rectangle. 

### Patterns

#### Pattern 1. Unit Circle of Radius 1 and Square with Side Length 2 #### 
This pattern describes how $\pi$ is calculated with well-defined shapes without respect to units. In this pattern, we obtain $\pi$ from our calculations in Excel when we consider the region of interest for the indicator variable to be the union of the circle and square. **This is the pattern that you should try to replicate in your environment.**

#### Pattern 2. Unit Circle of Radius 2 and Square with Side Length 1 ####
This pattern describes a different Monte Carlo Intergration, as it fails to calculate $\pi$ as the circle surpasses the area of the square, and now it calculates the area of the square instead as the area of intergration is defined through the greater of the two regions. 

## Entities, State Variables, and Scales

Note, this model does not have agents or collectives, as this is not an ABM (Agent-Based model).

### State Variables

Table:
```{raw} latex

```

### Scales
(Based on State Variables)

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
1. What happens to the estimate of $\pi$ when $N$, the number of points increases or decreases? 
2. Why did we use the ODD approach for organizing our model despite its simplicity?  
:::

# Lab 2: Retirement Calculations with Monte Carlo Methods (XLRisk or Python)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer


# Lab 3: Building a Portfolio with Monte Carlo Methods (XLRisk or Python)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
1. Are the sample variance and deviation similar enough to the population variance and deviation to state that we have a sufficient N for normality?
2. What are your 25% percentile, median, and 75% percentile values, and what do they say about the extreme values? (XLrisk will provide this), and using this information, would you say that this portfolio would pay off (have a positive value if we subtract the E[X] from the FV), in a week, which is our length of simulation.
3. Given the Kurtosis of the Model from XLrisk, what would you say about extreme events with this portfolio?
4. If you change the mixture of the stocks from all equal to only one stock, MSTR, what happens to the variance, and why? And how does connect to portfolio stategries in the real world?
# Lab 4: Posterior Probablity Estimation with Monte Carlo Methods (Python + Excel)
## Problem Statement

## Tips and Tricks

## Questions to Think about: 
# Lab 5: Foundations of Modelling (SIMIO, Anylogic, or Python)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer

# Lab 6: Markovian Queuing Methods (Python's CTW, SIMIO, or Anylogic)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
# Lab 7: General and Deterministic Queuing Methods (SIMIO, CTW, or Anylogic)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
# Lab 8: Introduction to ODEs in Simulation and Modelling (PySim/Salabim, Anylogic, or SIMIO)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
# Lab 9: Modelling the Spread of Illness via SEIR Models (PySim/Salabim, Anylogic, or SIMIO)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer
# Lab 10: Agent-Based Modelling (PySim/Salabim or Anylogic)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer

## Questions to Think about: 
# Lab 11: Optimization through Simulation (PySim/Salabim, Anylogic, or SIMIO)
## Purpose and Patterns

### Statement of Model Purpose

### Patterns

## Entities, State Variables, and Scales

### State Variables

### Scales

## Process Overview and Scheduling

## Design Concepts

### Basic Principles

## Input Data

## Questions left to the reader to answer