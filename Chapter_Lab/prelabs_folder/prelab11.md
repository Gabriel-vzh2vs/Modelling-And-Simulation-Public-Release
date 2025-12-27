(prelab-11)=
# SYSML in Modelling and Simulation (Read)

:::{note} Notice of this being a Shell Prelab
This prelab is waiting for an expert to look at the materials and
fill in gaps of information. This is going to be Tracy since she
wants to plan a lab, therefore, she has to make a section explaining
it to the students :). Right now, I will fill in some details
from my course SYSML course: SYS 5581.
:::

Systems Modeling Language (SysML) is about mapping system requirements, structure, and behavior to a formalized architecture model. What is the relevance of this to modeling and simulation? To ensure we have a valid model, we need to rigorously define the system boundaries, component interactions, and logical flows before implementation. What does that mean in practice? It requires us to describe the system S not just as code, but as a set of interconnected blocks, states, and constraints. If we treat the simulation as an executable verification of the design, SysML provides the blueprint against which that verification occurs; this is the topic of {ref}`sec:verification` and {ref}`sec:system_modeling`.

Assume we have a system S whose model M must satisfy a set of requirements R. From this set of requirements and the structure of $S$$ we can incorporate the following
elements into Model $M$.

- A set of requirements derived from stakeholder needs.
- Known structural properties of S. Example: S is composed of subsystems ${s_1​,s_2​}$ which communicate via specific ports and interfaces (e.g., physical connections or data buses).
- Insights about the logic that governs the behavior of S, such as state transitions (e.g., a traffic light system cycling Green → Yellow → Red) or activity flows.
- Standards: established industry protocols or interface definitions (ICDs) that dictate how components must interact. If a standard exists, the SysML model acts as the enforcement mechanism for these constraints.

In this prelab, we will give an introduction to this topic. While this book is geared towards Discrete-Event and Continuous simulation, SysML provides the necessary structural backbone for Model-Based Systems Engineering (MBSE). It is structured as follows:

- We first introduce the notion of {ref}sec:structural_diagrams, specifically the Block Definition Diagram (BDD) and Internal Block Diagram (IBD). These define the "nouns" of our system. We will also introduce tools like Cameo (MagicDraw) and open-source alternatives like Gaphor.
- Following this, we will review behavioral modeling. Here we cover the "behaviors" of the system using State Machine diagrams, Activity diagrams, and Sequence diagrams; see {ref}sec:behavioral_diagrams.
- Parametrics are often the bridge between architecture and mathematical analysis; see {cite}sec:parametric_diagrams for how constraint blocks link SysML to physics-based equations.
- The process of {ref}sysml_to_sim constitutes a major portion of this prelab, discussing how to translate static architectural models into executable simulations (e.g., via fUML or FMI/FMU standards).
- Sometimes we are modeling legacy systems with poor documentation, and in this case, we are led to perform reverse engineering.

Before rounding out this introduction, we point out that "Conceptual Modeling" is another commonly used term in the simulation community for this phase. As you likely guessed, we prefer SysML or MBSE and will use these terms throughout. There are many excellent texts on this topic, see, e.g., {cite}`friedenthal2014practical`,{cite}`delligatti2013sysml`,{cite}`incose2023incose`. Details on specific diagram types are often described in the OMG specifications. Plan to spend some time on this concept: as stated in {cite}`friedenthal2014practical`, "a simulation built on a flawed architectural model is merely a precise way to arrive at the wrong answer."

## Structural Diagrams

## Behavioral Diagrams

## Sysml to Simulation
