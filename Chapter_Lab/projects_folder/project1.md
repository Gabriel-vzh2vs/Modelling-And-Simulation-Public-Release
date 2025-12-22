## Project 1 Prerequisites

This Budgeting Project builds on the following prerequisites:

### Labs for Project 1

- {ref}`lab-1`
- {ref}`lab-2`
- {ref}`lab-3`

### Mandatory Chapters for Project 1

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`

### Recommended Chapters for Project 1

- {ref}`sec:building_simulation_models`
- {ref}`sec:random_number_generation`

## Budget Modelling Context and Information

This project is based on [Zhijing Eu's Project]https://medium.com/analytics-vidhya/building-a-probabilistic-risk-estimate-using-monte-carlo-simulations-cf904b1ab503 
with some modifications to make it into a case study. 

We are planning a trip to Fantasy Island and we have to consider several different variates for our trip, and more detail is in the attached Excel Sheet

(build table with variate information)

- The plane fare
- The accommodation costs (hotel)
- Food
- Shopping Expenses
- Activities
- Clothing

You also need to figure out the distributions to pick from for each of these categories as you progress through the Excel spreadsheet.  

{download}`Student Copy of Project 1 <../Source_Code/Chapter_Lab/SYS3062StudentLabProject1.xlsx>` (When this is given to the students, it should link to the Public GitHub Directory....)

### Patterns

#### Pattern 1

#### Pattern 2

#### Pattern 3

#### Pattern 4

## Project 1, Model Example Output

The example is included to help the reader verify their attempt at the project.

:::{figure} #fig:Gross_Cost_Project1
:label: fig:B

This figure shows the expected output for project 1, at least a series of 10,000 experiments for pattern 3.
:::

And Pattern 4 has the following values for key metrics, which are rounded to the nearest
cent when appropriate (as the US hasn't had a https://en.wikipedia.org/wiki/Mill_(currency) coin in over a century):

- Kurtosis: 0.7371250027808007
- Skewness: 0.6462940440468395
- Median Cost: $14,934.22
- Mean Cost: $15,118.27
