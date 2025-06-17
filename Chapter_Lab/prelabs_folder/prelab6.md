(prelab-6)=
# Pre-Lab 6: Applications of Queuing Theory (Short Do)

:::{admonition} Advisory: Pre-Lab 6 Chapter Reading
:class: warning dropdown

It is highly recommended that the reader read {ref}`sec:queuing_systems`
before reading this pre-lab, as it provides more details and critical context
about the topics discussed as this pre-lab is about applying queuing, which
is more difficult without context and will consist of three exercises with
solutions.

:::

## Exercises

This pre-lab focuses on the application of queuing theory by showing examples of differing
levels of complexity, which is important for simulating industrial and business processes.
Details of queuing theory are seen in {ref}`sec:queuing_systems`. Exercises are marked with
Ex_number, and their solutions are marked in a similar scheme: Sol_number.

::::{tab-set}

:::{tab-item} Example_1
A queue for a fairly-popular chicken sandwich restaurant on a college campus, Jimmy's,
has an _mean_ service rate of 5 customers per minute and an arrival rate of 3 customers
per minute during two hours of peak hours. They are asking you, a consultant to determine
if they should reduce their service rate to cut costs.

The cost of three servers (considered one server) providing the average service rate of 5
is around 45 United States dollars a hour. While the cost of two servers (still considered one
server) that might yield an average service rate of 3.5 customers per minute is about 30 dollars
an hour. Note that at any given moment if waiting time is over 1 minute for a single customer,
Jimmy's will be given a penalty charge of 10 dollars by the college, and the customer will have a mean
20 percent chance defined through a of bulking,
reducing revenue by an additional 10 dollars.

Based on this information, a queue simulation and the metrics: Queue Length and Wait time.
Determine if the change of reducing the number of staffers is worth the changes and possible
charges over an appropriate number of simulation trials each 20 lunch periods long (representing two weeks
of lunches.)
:::

:::{tab-item} Sol_1

Based on the nature of wait times and service times, an exponential distribution is often considered.
And it is assumed in this Exercise that the arrival rates and service rates are exponential.

Using this information, the construction of an $M/M/1$ queue is required to simulate and model this system
as described with a base and modified queue system represented within the code. Note: parts of this
code are based on the ciw documentation (as code using a library should be - but that's a soapbox.)

When an version of this simulation is ran, there is a significant increase in the mean cost associated
with balking; moreover, this change is consistent with the increases in mean waiting time (0.286 vs. 1.94)
and mean time in system (1.71 vs. 6.94).

```{code}
--- Cost Analysis Results ---

Base System (Service Rate = 5.0, Cost = $45/hr)
  Total Server Cost: $1,800.00
  Total Penalty Cost: $5,050.00
  Total Revenue Loss (from Balking): $970.00
  Overall Total Cost: $7,820.00
  Customers Penalized: 505
  Customers Balked: 97

Modified System (Service Rate = 3.5, Cost = $30/hr)
  Total Server Cost: $1,200.00
  Total Penalty Cost: $39,250.00
  Total Revenue Loss (from Balking): $7,880.00
  Overall Total Cost: $48,330.00
  Customers Penalized: 3925
  Customers Balked: 788
```

Here's the implementation of this simulation using Python:

```{code} python
:tags: drop-down
import ciw, random

# System Parameters
BASE_ARRIVAL_RATE = 3.0
BASE_SERVICE_RATE = 5.0
MODIFIED_SERVICE_RATE = 3.5 # Modified System
NUM_SERVERS = 1

# Simulation Parameters
TIME_LENGTH = 120 * 20 # 2,400 minutes (40 hours)
WARMUP = 200 # Warmup period in minutes
SEED = 42

# Cost and Behavior Parameters
BASE_HOURLY_COST = 45.0
MODIFIED_HOURLY_COST = 30.0
PENALTY_THRESHOLD = 1.0 # 1 minute wait time
PENALTY_CHARGE = 10.0
BALKING_PROBABILITY = 0.20 # 20% chance if wait > 1 min
REVENUE_LOSS_ON_BALK = 10.0

# Set a seed for reproducibility for both ciw and random
ciw.seed(SEED)
random.seed(SEED)

# Base System: 3 servers combined, service rate = 5.0
base_system = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=BASE_ARRIVAL_RATE)],
    service_distributions=[ciw.dists.Exponential(rate=BASE_SERVICE_RATE)],
    number_of_servers=[NUM_SERVERS]
)

# Modified System: 2 servers combined, service rate = 3.5
modified_system = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=BASE_ARRIVAL_RATE)],
    service_distributions=[ciw.dists.Exponential(rate=MODIFIED_SERVICE_RATE)],
    number_of_servers=[NUM_SERVERS]
)

# --- Simulation ---

# Run base model simulation
Q_base = ciw.Simulation(base_system)
Q_base.simulate_until_max_time(TIME_LENGTH)
recs_base = Q_base.get_all_records()

# Run modified model simulation
Q_modified = ciw.Simulation(modified_system)
Q_modified.simulate_until_max_time(TIME_LENGTH)
recs_modified = Q_modified.get_all_records()

# --- Cost Analysis Function ---

def calculate_total_cost(records, hourly_server_cost, sim_duration_mins, warmup_period):
    """
    Calculates total operational cost from simulation records.
    
    Args:
        records (list): A list of ciw data records.
        hourly_server_cost (float): The cost of servers per hour.
        sim_duration_mins (int): Total simulation time in minutes.
        warmup_period (int): The warmup period in minutes.
        
    Returns:
        dict: A dictionary containing the breakdown of costs.
    """
    
    # 1. Calculate total server cost
    sim_duration_hours = sim_duration_mins / 60.0
    total_server_cost = hourly_server_cost * sim_duration_hours
    
    # 2. Calculate penalties and revenue loss from balking
    penalty_cost = 0.0
    balking_revenue_loss = 0.0
    customers_penalized = 0
    customers_balked = 0
    
    # Filter out records from the warmup period
    valid_records = [r for r in records if r.arrival_date > warmup_period]
    
    for rec in valid_records:
        if rec.waiting_time > PENALTY_THRESHOLD:
            # Apply penalty for exceeding wait time threshold
            penalty_cost += PENALTY_CHARGE
            customers_penalized += 1
            
            # Simulate balking with a 20% probability
            if random.random() < BALKING_PROBABILITY:
                balking_revenue_loss += REVENUE_LOSS_ON_BALK
                customers_balked += 1
                
    # 3. Calculate final total cost
    total_cost = total_server_cost + penalty_cost + balking_revenue_loss
    
    return {
        "Total Server Cost": total_server_cost,
        "Total Penalty Cost": penalty_cost,
        "Total Revenue Loss (from Balking)": balking_revenue_loss,
        "Overall Total Cost": total_cost,
        "Penalizations from Customers Bulking": customers_penalized,
        "Customers Balked": customers_balked
    }

# --- Results ---

# Calculate costs for both systems
base_costs = calculate_total_cost(recs_base, BASE_HOURLY_COST, TIME_LENGTH, WARMUP)
modified_costs = calculate_total_cost(recs_modified, MODIFIED_HOURLY_COST, TIME_LENGTH, WARMUP)

# Print the results
print("--- Cost Analysis Results ---")

print("\nBase System (Service Rate = 5.0, Cost = $45/hr)")
for key, value in base_costs.items():
    if "Cost" in key or "Loss" in key:
        print(f"  {key}: ${value:,.2f}")
    else:
        print(f"  {key}: {value}")

print("\nModified System (Service Rate = 3.5, Cost = $30/hr)")
for key, value in modified_costs.items():
    if "Cost" in key or "Loss" in key:
        print(f"  {key}: ${value:,.2f}")
    else:
        print(f"  {key}: {value}")
```

:::

:::{tab-item} Example_2
Often times, in the real-world, there is a series of queues (or processes) that are
connected to each other such as in government institutions, and this example seeks
to demonstrate how that can be modelled through queuing networks.

This example is based on the [ciw documentation](https://ciw.readthedocs.io/en/latest/Tutorial/tutorial_iii.html)
to a great extent

:::

:::{tab-item} Sol_2
A factory machine produces items in batches. Over 25 consecutive production runs, the number of defective
items found in each run are represented the data below

```{code} python
14, 15, 11, 10, 12, 5, 10, 7, 10, 17, 7, 11, 
13, 6, 8, 9, 13, 12, 7, 9, 9, 12, 11, 12, 9
```

Estimate the sample mean and the standard deviation of the number of defective items. Then use the observed
properties of the distribution (e.g: making a histogram, assessing its natural bounds), to determine the
possible hypothesis for the posterior distribution. Then test these hypothesis using a software package like
Fitter/Phitter or a statistical package.
:::

:::{tab-item} Example_3
A factory machine produces items in batches. Over 25 consecutive production runs, the number of defective
items found in each run are represented the data below

```{code} python
14, 15, 11, 10, 12, 5, 10, 7, 10, 17, 7, 11, 
13, 6, 8, 9, 13, 12, 7, 9, 9, 12, 11, 12, 9
```

Estimate the sample mean and the standard deviation of the number of defective items. Then use the observed
properties of the distribution (e.g: making a histogram, assessing its natural bounds), to determine the
possible hypothesis for the posterior distribution. Then test these hypothesis using a software package like
Fitter/Phitter or a statistical package.
:::

:::{tab-item} Sol_3
A factory machine produces items in batches. Over 25 consecutive production runs, the number of defective
items found in each run are represented the data below

```{code} python
14, 15, 11, 10, 12, 5, 10, 7, 10, 17, 7, 11, 
13, 6, 8, 9, 13, 12, 7, 9, 9, 12, 11, 12, 9
```

Estimate the sample mean and the standard deviation of the number of defective items. Then use the observed
properties of the distribution (e.g: making a histogram, assessing its natural bounds), to determine the
possible hypothesis for the posterior distribution. Then test these hypothesis using a software package like
Fitter/Phitter or a statistical package.
:::

::::
