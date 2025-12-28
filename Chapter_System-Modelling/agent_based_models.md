(sec:agent_based_models)=
# Agent-Based Modelling (ABMs)

:::{note} "Thick" Outline
To Henning, this is a quick outline to start this section:
however, this outline is based on your slides from week
14 + 15.  It is not in any way qualified as a formal
draft.
:::

Agent-Based Modeling (ABM) is about modeling and analyzing systems consisting of discrete entities, or agents, that interact within an environment. What is the relevance of this to modeling and simulation? It allows us to observe how complex macro-level system behaviors—such as the spread of a rumor or the resilience of a power grid—emerge from the micro-level interactions of individual agents.

Assume that we have a System $S$, that can be modelled as a
set of agents $A = {a_1, a_2, ..., a_n}$? What do we need
to make a model $M$ based on this information? The typical
structure has the following elements based on the ODD frame
work:

- Agent Properties: The internal state or "DNA" of an agent. If the agent is "intelligent," this might include a utility function that guides their decisions.
- Environment: The medium in which agents exist and interact, which can be spatial (like a road network) or abstract (like a social network).
- Interaction Rules: The logic governing how agents influence one another. For example, in a belief propagation model, this defines how a person updates their opinion based on their neighbors.
- Heterogeneity: Unlike many physics-based models where particles are identical, agents often exhibit distinct diverse characteristics and behaviors.

(sec:abm:what_is_an_agent)=
## What is an Agent?

Defining an "agent" is the first step in constructing an ABM. A useful definition provided by Chris Barrett is that an agent is something (an entity or person) that mediates its own behavior.

This definition helps distinguish agents from passive objects:

- The Billiard Ball Test: A billiard ball is not an agent because it reacts purely to external physics without internal mediation.

- The Traffic Driver: In a standard traffic micro-simulation, a car might just be a discretized cell moving along a lane. However, if the driver observes the environment, assesses their safety against an internal belief, and chooses to change lanes based on a utility function, they act as an agent.

### Case Study: Belief Propagation

To make the concept of agent interaction tangible, consider the modeling of a rumor or belief spreading through a population (e.g., in Charlottesville/Albemarle).

Designing this model requires answering specific structural questions:

- State Representation: How do we mathematically represent a person's belief?.

- Network Topology: How do we capture "who listens to whom"? This defines the agent's neighborhood or social network.

- Update Functions: What is the precise function an agent uses to update their belief based on peer pressure or new information?.

(sec:abm:digital_twins_resilience)=
### Case Study 2: Digital Twins 

Advanced ABMs often rely on Digital Twins—high-fidelity virtual representations of the real world—to provide a realistic environment for agents.

We explore this through the CoPe Project (Coastal Lines and People), which studies the impact of storm surges on the Eastern Shore of Virginia. This model integrates several complex layers:

- Synthetic Populations: A statistically accurate "digital twin" of the population, including household locations and demographics.

- Infrastructure Layers: Digital representations of road networks, hospitals, and emergency services.

- Environmental Data: Inundation maps derived from storm surge models (like ADCIRC) are spatially joined with road networks to simulate flooding impacts.

By simulating agents (residents) within this digital twin, researchers can assess resilience metrics, such as evacuation times or the ability to reach critical care during a flood

(sec:abm:formalism_tools)=
## Formalisms and Tools

While ABM is a younger field compared to equation-based modeling, several frameworks attempt to formalize the design process to improve rigor and reproducibility:

- ODD Protocol: Stands for "Overview, Design concepts, and Design Details," a standard format for describing ABMs.

- DREAM: Descriptive Agent-based Modeling framework.

There is often a tension in these frameworks: highly expressive frameworks may be difficult to analyze mathematically, while tractable ones may lack the complexity needed for real-world applications.

For implementation, a variety of tools exist:s

- NetLogo: Highly recommended for prototyping.

- Mason, Mesa and GAMA Platform: Libraries supporting more complex large-scale simulations.

- AnyLogic: A commercial tool often used in industry.

## Micro-simulations
