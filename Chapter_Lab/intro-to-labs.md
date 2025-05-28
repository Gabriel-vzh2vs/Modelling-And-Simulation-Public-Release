(sec:lab)=
# Introduction to Simulation Lab

The main purpose of the lab section is to help demonstrate the concepts discussed
throughout the book through short exercises and readings {ref}`sec:pre-labs`,
hands-on activities {ref}`sec:labs`, and replications of real-world systems and
models from literature {ref}`sec:projects`. More details about each of these
concepts are available in their sections.

The lab section consists of three sections that were discussed before
and three documents of information organized with the following structure:

- {ref}`sec:softwaresetup`
- {ref}`sec:pre-labs`
- {ref}`sec:labs`
- {ref}`sec:projects`
- {ref}`sec:GMP`
- {ref}`sec:software`

In this case, you should start with the Software Installation first, as
that gives a setup that enables the technological side of the pre-labs,
labs, and projects. Then, the reader should do a pre-lab for each
lab, and then once you do three or four labs, then should take on a
project. The other sections will appear when needed within a pre-lab,
lab or project.

## Suggested Grading Standards for Labs, Projects, and Pre-Labs

This section is mostly for readers who are either taking a course based on
this work or readers who have adopted this work for their courses (thanks for using this work!)
Additionally, we have included it here in the introduction to reduce unneeded
replication for each assignment. Keep in mind that these are suggested grading schemes, and
any instructor has the right to change, discard, or modify them for their course based on their
experiences, institutional policies, new advancements in educational science, or personal beliefs
(meaning if you are a reader with an instructor, check their syllabus for grading information!)

### Pre-Lab Grading Rubric

Generally, pre-labs should not be graded on a standard grade scale, as they are made
to help the students understand the connection between concepts and practice. However,
they should be assessed with "sufficient" completion in mind, meaning that the reader
should have made an attempt to understand the material.

```{raw} latex
\begin{tabular}{l >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth}}
\toprule
\textbf{Criteria} & \textbf{Excellent (A)} & \textbf{Proficient (B/C)} & \textbf{Needs Improvement (D/F)} \\
\cmidrule(r){1-1}\cmidrule(lr){2-2}\cmidrule(lr){3-3}\cmidrule(l){4-4}
% You can add point values here if desired, e.g., Excellent (90-100%)

\textbf{Criterion 1: Completion} &
% Excellent
Performed all of the tasks in the pre-lab, for pre-labs marked with 'read' this usually means that they wrote a paragraph about what they learned, and for pre-labs marked with 'do', they produced a functional, relevant, and commented product.  &
% Proficient
The pre-lab work is incomplete but it shows some effort in its creation. &
% Needs Improvement
Only performed pre-lab tasks superficially, or not at all. \\

\bottomrule
\end{tabular}
```

### Lab Grading Rubric

Labs are between the more informal pre-labs and the formal project assessment
meaning that grading does depend on the structure of the reader's educational
environment. For example, using the pre-lab grading rubric could be appropriate
for the labs if the labs are considered pass/fail, and the rubric below is created
in the context when labs are assessed assignments equivalent to homeworks.

```{raw} latex
\begin{tabular}{l >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth}}
\toprule
\textbf{Criteria} & \textbf{Excellent (A)} & \textbf{Proficient (B/C)} & \textbf{Needs Improvement (D/F)} \\
\cmidrule(r){1-1}\cmidrule(lr){2-2}\cmidrule(lr){3-3}\cmidrule(l){4-4}
% You can add point values here if desired, e.g., Excellent (90-100%)

\textbf{Criterion 1: Completion} &
% Excellent
Created a model that meets all of the requirements in the lab and produced a functional, relevant, and well-commented product. &
% Proficient
Completed more than half of the requirements in the lab, and produced a functional product. &
% Needs Improvement
Only performed lab tasks superficially, or not at all. \\

\textbf{Criterion 2: Insight} &
Answered the questions left for the reader with rational answers informed by the model's results and this text. &
Answers are generally well-supported and logical. Shows some weaknesses in the depth of analysis and lack references to concepts in the rest of this text. &
Answers are unclear, unoriginal, or not well-defined. Answers are weak, poorly supported, or illogical.  \\
\bottomrule
\end{tabular}
```

### Project Grading Rubric

If you are to grade the projects as an instructor, we have provided a rough framework
for evaluating the quality of student products. Moreover, the suggested weighting for
each deliverable is as follows: 30 percent for the model and 70 percent for the report.

Additionally, a report may meet multiple criterions, and it is
advised that the average of the criterions are taken. An example of this is a project report
that it is clear, well-developed, and logical, but lacks conceptual clarity -
the report should be given a B, despite most of its traits residing in the A range.

The reasoning behind this is two-fold, it is more important that the students know and
can describe how the model works, and a functional model is required but not sufficient for
external validity (see {ref}`sec:building_simulation_models` and {ref}`sec:intro_validation`).

#### Regarding Model Functionality

Model Functionality will depend on the specifics of the Project, but here are some general
guidelines for determining the quality of a submission.

```{raw} latex
\begin{tabular}{l >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth}}
\toprule
\textbf{Criteria} & \textbf{Excellent (A)} & \textbf{Proficient (B/C)} & \textbf{Needs Improvement (D/F)} \\
\cmidrule(r){1-1}\cmidrule(lr){2-2}\cmidrule(lr){3-3}\cmidrule(l){4-4}
% You can add point values here if desired, e.g., Excellent (90-100%)

\textbf{Criterion 1: Completion} &
% Excellent
Created a project that meets all of project requirements while producing a functional, relevant, and well-commented product. &
% Proficient
Completed more than half of the requirements in the project, and produced a somewhat functional product. &
% Needs Improvement
Only attempted project requirements superficially, or not at all. \\

\textbf{Criterion 2: Structure & Organization} &
Organization of the model is logical and clear. Model components are well-developed, cohesive, and function correctly and integrate into a cohesive system. Shows evidence of robust verification and validation methods for improving the model's validity. &
Organization is clear. Model components are mostly well-developed and cohesive with adequate transitions. Shows an incomplete attempt at verification and validation. &
Organization is unclear or illogical. Model components lack coherence or structure. Model patterns are non-existent or incorrect. No Attempt at verification and validation was made. \\

\textbf{Criterion 3: Programming Implementation} &
Programming is clear, concise, and engaging. Language is precise and sophisticated. Free of errors in programming. &
Programming is generally clear. Language is appropriate. Minor errors in programming may be present but do not significantly hinder model functionality. &
Programming is unclear, awkward, or difficult to follow. Frequent or significant errors in programming impedes the running of the program. \\

\bottomrule
\end{tabular}
```

#### For the Written Report

Written report requirements will depend on the specifics of the Project, but here are some general
guidelines for determining the quality of a submission.

```{raw} latex
\begin{tabular}{l >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth} >{\raggedright\arraybackslash}p{0.25\textwidth}}
\toprule
\textbf{Criteria} & \textbf{Excellent (A)} & \textbf{Proficient (B)} & \textbf{Needs Improvement (C/D)} \\
\cmidrule(r){1-1}\cmidrule(lr){2-2}\cmidrule(lr){3-3}\cmidrule(l){4-4}
% You can add point values here if desired, e.g., Excellent (90-100%)

\textbf{Criterion 1: Argumentation & Thesis} &
% Excellent
Demonstrates a clear, insightful, and original thesis. Arguments are compelling, well-supported by evidence, and logically structured. Addresses counterfactual evidence from the model and context effectively. &
% Proficient
Presents a clear thesis. Arguments are generally well-supported and logical. May show some minor weaknesses in addressing counterarguments or in the depth of analysis. &
% Needs Improvement
Thesis is unclear, unoriginal, or not well-defined. Arguments are weak, poorly supported, or illogical. Fails to address counterarguments or does so superficially. \\

\textbf{Criterion 2: Evidence & Analysis} &
Utilizes a wide range of high-quality, relevant metrics and concepts for evidence. Evidence is expertly integrated and analyzed critically to support claims. Demonstrates sophisticated understanding of the material. &
Uses appropriate metrics and concepts as the foundation for evidence. Evidence is generally well-integrated and analyzed to support claims. Shows good understanding of the material, though analysis could be deeper. &
Relies on insufficient, irrelevant, or low-quality metrics and concepts. Evidence is poorly integrated, not analyzed, or misapplied. Shows limited understanding of the material. \\

\textbf{Criterion 3: Structure & Organization} &
Organization is exceptionally clear and logical. Paragraphs are well-developed, cohesive, and transition smoothly. Introduction, body and conclusion are effective and engaging with a strong degree of conceptual clarity. &
Organization is clear. Paragraphs are mostly well-developed and cohesive with adequate transitions. Introduction and conclusion are functional. Conceptual clarity is diluted through its presentation. &
Organization is unclear or illogical. Paragraphs lack development, coherence, or transitions. Introduction or conclusion is weak or missing. Conceptual clarity is absent.\\

\textbf{Criterion 4: Clarity, Mechanics, & Style} &
Writing is clear, concise, and engaging. Language is precise and sophisticated. Free of errors in grammar, spelling, punctuation, and citation style. &
Writing is generally clear. Language is appropriate. Minor errors in grammar, spelling, punctuation, or citation style may be present but do not significantly hinder understanding. &
Writing is unclear, awkward, or difficult to follow. Frequent or significant errors in grammar, spelling, punctuation, or citation style impede understanding. \\

\bottomrule
\end{tabular}
```
