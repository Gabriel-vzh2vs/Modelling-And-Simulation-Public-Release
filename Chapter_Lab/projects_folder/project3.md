(project-3)=
# Project 3 (Extension Project _Queuing-Based Project_): Modelling and Simulating a Supermarket Queue

## Project 3-linked Skills

This project focuses on developing the following skills:

1. Basic Modelling in the context of queues;
2. Distribution Fitting;
3. Interpreting System Metrics;
4. Using Specialized Simulation Software;

## Project 3 Prerequisites

And this project relies on the following prerequisites:

### Labs for Project 3

1. {ref}`lab-5`
2. {ref}`lab-6`
3. {ref}`lab-7`

### Mandatory Chapters for Project 3

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`sec:building_simulation_models`
- {ref}`sec:random_number_generation`
- {ref}`sec:system_modeling`

## Supermarket Modelling Context and Information

You are a consultant for an Oslo-Based high-end consulting firm that has a simulation division, and one of your clients, a supermarket chain named Valg 1000, comes to your consultancy and asks for a simulation study to identify several inefficiencies in their checkout process, which are both hurting customer experience and their profits.

The client provided the following information during your first meeting with them on April 2nd, which is likely to be important for the construction of your model in SIMIO, Anylogic, or Python's Ciw.  

Customers will on average arrive in the check-out area of the store through the following around 40 customers per hour from 4:00 p.m. until 5:00 p.m., 60 customers per hour from 5:00 p.m. until 7:00 p.m., 30 customers per hour from 7:00 p.m. until 8:00 p.m., and of 20 customers per hour from 8:00 p.m. until 11:00 p.m - they assure you that the inter-arrival times are exponentially distributed within each time segment.

Each check-out lane will serve customers according to a service process with a mean of 3 minutes, they did not perform statistical tests or models on this data, and the data is attached below, and they are relying on you to do the proper statistical tests and modeling:

{download}`Service Time Data <../Source_Code/Chapter_Lab/Service_Time_Data.xlsx>` (When this is given to the students, it should link to the Public GitHub Directory....)

Due to a contract with the union, Arbeiderforbund, there must be the same 4 cashier stations open at any given time (to ensure a minimum amount of payment to the workers), and there are a total of 10 stations in each of the supermarkets. Your client wants the non-union mandated stations to be checked every 15 minutes to ensure that they are receiving customers, which your client defines as: "A queue is considered to be receiving customers if the overall average queue length is less than or equal to one, the additional lane will close after each customer in that lane has been served".  

Your supervisor gives you a hint that "If the length of the queue in each open check-out lane is two or more, and if another check-out lane can be opened, another check-out lane will be opened."  

## Metrics

Your firm's resident mathematician, a Dane named Dr. Erlang, recommends that you obtain several important metrics along with their 95% confidence intervals with a series of one-hundred replications to validate that the system that you designed works as he has a distrust of models, he has purposed the critical metrics below based on his experiences and discussion with the client.

- The average number of lanes open during the 4:00 p.m. – 8:00 p.m. period & average number of lanes open during the 8:00 p.m. – 11:00 p.m. period;

- The average number of times an additional lane was opened during the 4:00 p.m. – 8:00 p.m. time period and the average number of times an additional lane was opened during the 8:00 p.m. – 11:00 p.m. time period.

- The average proportion of time additional lanes were open during the 4:00 p.m. – 8:00 p.m. time period and the average proportion of time additional lanes were open during the 8:00 p.m. – 11:00 p.m. time period.

- The average number of customers waiting for service during the 4:00 p.m. – 8:00 p.m. time period and the average number of customers waiting for service during the 8:00 p.m. – 11:00 p.m. time period.

- The average waiting time for service during the 4:00 p.m. – 8:00 p.m. time period and the average waiting time for service during the 8:00 p.m. – 11:00 p.m. time period.

- The average system utilization, average length of lines, and average delay.

## Project 3, Example Model Output