(project-4)=
# Project 4 (Extension Project _Queuing-Based Project_): Simulating and Modelling a Intensive Care Unit

This project focuses on developing the following skills:

1. Discrete Event Simulation (DES) in the context of healthcare operations;
2. Non-Homogeneous Arrival Modeling (Handling scheduled vs. random arrivals);
3. Resource Constraints (Modelling Post-Service delays such as cleaning times);
4. Scenario Analysis (Comparing Capital Investment vs. Process Improvement).

And this project relies on the following prerequisites:

### Labs

1. {ref}`lab-5`
2. {ref}`lab-6`
3. {ref}`lab-7`

### Chapters

- {ref}`sec:prob_stats`
- {ref}`sec:monte_carlo_method`
- {ref}`sec:building_simulation_models`
- {ref}`sec:random_number_generation`
- {ref}`sec:system_modeling`

## Project 4 Model Information

This model is based loosely on {cite:p}`griffiths2010simulation` for its base description. You are a consultant working for the
English healthcare system (England NHS) for the Bedfordshire Hospitals NHS Foundation Trust. Your job is to develop a simulation
that supports possible decisions of that could reduce cancellations of elective surgeries. Another thing that they are asking you do is to
reduce staffing while maintaining a reasonable amount of bed-occupancy and waiting times. The scope of your project is the beds in
the hospital along with their sources (Emergency Room, Radiology, Elective Surgery, and Hospital Transfers).

### Arrival Sources

The CCU receives patients from two distinct streams. You must model these accurately to capture the tension in the system.

Unplanned Admissions (Emergency): These patients arrive randomly from Accident & Emergency (A&E), emergency surgery, and other wards. They are critical and cannot be turned away.

- Arrival Rate: Historical data shows these patients arrive according to a Poisson process (exponentially distributed inter-arrival times). The combined rate is approximately 3.5 patients per day.
- Service Time (Length of Stay): Due to the complexity of these cases, their Length of Stay (LoS) follows a Lognormal Distribution with a mean of 4 days and a standard deviation of 3 days (derived from aggregate data in Table 1 ).

Planned Admissions (Elective): These are patients scheduled for major surgery (e.g., heart bypass) who need a CCU bed reserved in advance.

- Arrival Schedule: Highly dependent on the surgeon's schedule. Currently, surgeons prefer to operate Tuesday through Friday. The weekly schedule is:
    - Monday: 1 Patient
    - Tuesday to Friday: 5 Patients per day
    - Saturday to Sunday: 0 Patient

The Cancellation Rule: If an Elective patient arrives and no beds are free, their surgery
is cancelled immediately. They do not queue; they are sent home.

Service Time (Length of Stay): These patients are more predictable. Their
LoS follows a Normal Distribution with a mean of 2.5 days and a standard deviation of 0.5 days.

### Cleaning Time Constraints

Your contact at the hospital reminds you of a critical operational detail often missed by analysts:
A bed is not available immediately after discharge.

Deep Clean Protocol: Every bed requires 5 hours of intensive cleaning and preparation before a new patient can be admitted.
You must include this "unavailable time" in your model logic.

### Total Resources

Funded Beds: The unit currently has 24 fully funded beds.

Overflow Capacity: There are 5 extra physical beds, but they are currently unfunded.
Opening them requires hiring agency nurses at 4x the cost, so they are only used in extreme emergencies in reality,
but for this simulation, we treat the capacity as hard-capped at the scenario limit to measure cancellations.

## Metrics of Interest

Your firm's Lead Statistician, Dr. Nightingale, recommends
that you obtain several important metrics along with their 95\% confidence intervals
with a series of one-hundred replications. She wants you to focus on the trade-off
between Efficiency (High Occupancy) and Reliability (Low Cancellations).

```{raw} latex
\begin{itemize}
    \item \textbf{The Cancellation Rate:} The average percentage of Elective patients who are turned away per year (Total Elective Cancellations / Total Elective Arrivals).
    
    \item \textbf{Bed Occupancy:} The average percentage of funded beds occupied over the year.
    \begin{itemize}
        \item \textit{Note:} The International Critical Care Society recommends an occupancy of 60--70\% to safely handle surges. 
    \end{itemize}

    \item \textbf{The ``Cost'' of Cancellations:} Each cancellation costs the hospital an estimated \pounds12,200 in lost revenue and administrative rework. Calculate the Total Annual Cost of Cancellations.

    \item \textbf{Scenario Analysis:} Dr. Nightingale specifically asks you to run the following ``What-If'' scenarios to present to the board:
    \begin{enumerate}
        \item \textbf{Status Quo:} Current system (24 Beds, Electives concentrated Tue-Fri).
        \item \textbf{Capacity Expansion:} Increment the bed count from 24 up to 29. Identify the point where cancellations drop to zero.
        \item \textbf{Process Improvement (Smoothing):} Keep the bed count at 24, but convince surgeons to operate 7 days a week. Change the Elective Arrival pattern to a uniform {3 patients per day, 7 days a week (keeping the total weekly volume roughly the same). Does this reduce cancellations as effectively as buying new beds?
    \end{enumerate}
\end{itemize}
```

## Evaluation
