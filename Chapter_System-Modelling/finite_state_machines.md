(sec:finite_state_machines)=
# Finite State Machines #

:::{note} "Thick" Outline
To Henning, this is a quick outline to start this section:
however, this outline is based on your slides from week
13 + 14 combined with some information from my SYSML
course. It is not in any way qualified as a formal
draft.
:::

## Introduction to State Machine Modeling

State machine modeling is about mapping the dynamic behavior of system entities to a formal structure known as a finite state machine (FSM). What is the relevance of this to modeling and simulation? To ensure we have a valid model that supports verification and validation, we need a blueprint that captures how system components evolve over time. What does that mean in practice? It requires us to describe the "states" an entity can occupy and the logic governing the transitions between those states.

To make this concept more tangible, we will use a robot-assisted search-and-rescue mission as a running example throughout this chapter. Imagine a team deployed in a hostile environment containing an unknown number of victims. This team consists of a medic, an Unmanned Aerial Vehicle (UAV), and several Unmanned Ground Vehicles (UGVs). The goal is to prioritize the treatment of critical cases while minimizing execution time and energy use. We will specifically focus on modeling the behavior of the UGV using state machines to handle its complex decision-making, such as when to explore, when to report data, and when to triage victims.

<Insert Image for UGV State Machine>

Assume we have a system $S$ whose model $M$ contains an entity $E$. In a state machine, Model $M$ requires the following pieces of information:

- States: A discrete collection of conditions that the entity E can be in. For example, a search-and-rescue UGV might be in a state of Standby, Explore, or Triage & Explore.

- Events: Occurrences that "happen" and potentially trigger a transition from one state to another. Examples include a Launch event, Victim detected, or Exploration complete.

- Transitions: The directed paths between states, determined by events and often conditional logic.

- Actions: Specific functions or processes executed while the entity is in a specific state. For instance, while in an Explore state, a robot might execute actions such as SetWaypoint, LIDARObserveEnvironment, or EngageMotion.

- System Variables: Data stored by the entity that may influence transitions or track performance, such as currentVictimCount or environmentMap.

In this section, we will give an introduction to this topic. The formal foundation of state machines is critical for structuring complex agent behaviors and for using industry tools such as SYSML. It is structured as follows:

- We first introduce the formal components of a state machine, focusing on states and events used to capture "things happening".

- Following this, we explore the iterative design process of a state machine using the robot-assisted search-and-rescue scenario (involving UGVs, UAVs, and Medics) as a primary case study. We will demonstrate how a model evolves from a simple sketch to a comprehensive blueprint by adding missing logical elements like return-to-base triggers or data transfer states.

- We discuss how to enhance the model by incorporating actions (continuous control logic within a state) and system variables (memory of the system) to create a high-fidelity representation of the system's operation.

- Finally, we touch upon the connection between state machines and broader systems engineering frameworks like Model Based Systems Engineering (MBSE) and SysML.

As you likely guessed, we focus on the core utility of state machines as a bridge between conceptual design and simulation code, allowing for a close correspondence that facilitates automated model checking and resilience study.

(sec:state_machine_modeling:conditions)=
### Conditions

System variables often serve as the basis for conditions (or guards), which are logical checks that determine if a transition can occur. While an event might trigger a potential change, a condition validates whether the system can proceed to the next state.

In the UGV example, conditions act as decision gates for the robot's behavior. We can see this in the transition logic out of the Triage & Explore state:

- Max Victim Count Reached: The transition to Seek UAV is triggered not just by finding a victim, but by the condition that the number of victims found (n) equals a predefined limit (N).

- Max Triage Time Reached: A timer-based condition where the transition occurs if the time spent triaging (T) exceeds a specific threshold.

- Victim Priority: A condition might check if a Victim in critical condition is found, prompting an immediate transition to Seek UAV to report the urgent data, bypassing further exploration.

(sec:state_machine_modeling:states)=
### States

A state represents a distinct condition or situation in which an entity exists. An entity is always in exactly one state at any given time, and it remains there until a specific event triggers a transition. In modeling complex systems, defining the correct set of states is the first step in characterizing behavior.

(sec:state_machine_modeling:events)=
### Events and Transitions

Events are the drivers of dynamic behavior; they capture "things happening" within the system. When an event occurs, it acts as a trigger that may cause the entity to transition from its current state to a new one.

(sec:state_machine_modeling:actions)=
### Actions within States

While states define where an entity is in its logic, actions define what the entity is actually doing while residing in that state. Actions represent the functions or processes being executed by the entity; in our example, the Unmanned Ground Vehicle (UGV)—specific to its current state.

For the UGV model, we can specify actions that are continuously executed by the control logic associated with a particular state. Consider the Explore state; the UGV does not simply sit idle. Instead, it actively cycles through specific operational functions:

(sec:state_machine_modeling:system_variables)=
### System Variables

To support the logic of transitions and actions, the state machine must often maintain a memory of the system's status. We can add system variables to our model to track this internal data.

These variables are critical for making decisions—such as whether to continue exploring or return to base. In the context of the UGV search-and-rescue mission, relevant system variables include:

## Iterative Design Process


### Statecharts


## Transition to MBSE 


### SYSML 

{ref}`prelab-11`