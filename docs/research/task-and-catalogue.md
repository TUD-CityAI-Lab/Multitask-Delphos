# Tasks and the Global Catalogue

A **task** describes one discrete choice modelling problem. A **catalogue** gives compatible concepts the same identity across tasks. This distinction is the basis of multitask learning.

## The task is dataset-specific

For a task $\tau$, Delphos records

$$
T_\tau=(\mathcal J_\tau,\mathcal X_\tau,\mathcal C_\tau,\mathcal F_\tau,\mathcal G_\tau),
$$

where $\mathcal J$ contains alternatives, $\mathcal X$ attributes, $\mathcal C$ covariates, $\mathcal F$ transformations, and $\mathcal G$ taste structures.

In user code, these concepts remain inspectable:

```python
import delphos as dp

task = dp.load_dataset("Swissmetro")

print(task.alternative_names)
print(task.attribute_names)
print(task.covariate_names)
print(task.transform_names)
print(task.taste_names)
```

The task also keeps the mapping back to the actual data. A global `travel_time` attribute, for example, can map to a different CSV column for each alternative.

## The catalogue is shared

Variable names are not transferable. The modelling meaning is. A catalogue constructs the unions

$$
\mathcal X=\bigcup_\tau\mathcal X_\tau,
\qquad
\mathcal C=\bigcup_\tau\mathcal C_\tau,
\qquad
\mathcal F=\bigcup_\tau\mathcal F_\tau,
\qquad
\mathcal G=\bigcup_\tau\mathcal G_\tau
$$

and assigns stable identifiers to those concepts. The agent then sees identifiers such as “travel time” and “log transformation”, not `SM_TT` or `rail_ivt`.

This is a semantic contract. Two variables should share an identifier only when they represent the same modelling concept. Similar spelling is not enough.

## Terms and actions use the same grammar

A term is encoded as

```text
(attribute_id, transformation_id, taste_id, covariate_id)
```

Examples include:

```text
(travel_time, linear, generic, none)
(travel_cost, log, generic, income)
(headway, box_cox, specific, none)
```

The catalogue enumerates modelling actions in this same space. This gives all tasks a common policy output, even when a particular task exposes only a subset of the catalogue.

## Task masks preserve feasibility

For task $\tau$, a binary mask indicates which global concepts are present. State-dependent validation then removes actions that would be invalid in the current specification.

For example, a task without headway data masks every headway action. If a linear generic travel-time term is already present, the identical addition is also masked. A common action space therefore does not imply that every action is possible for every dataset.

## What makes a new task transferable

A new task can use a pretrained policy when:

- its concepts map correctly to identifiers known by the checkpoint;
- its allowed transformations and taste structures are represented in that catalogue;
- its data schema is sufficient for Apollo code generation; and
- its task masks can be constructed without ambiguity.

An unseen variable concept is not made transferable by assigning it a convenient existing identifier. It should instead be introduced through catalogue and training work, with an explicit cross-task definition.

See [Use Your Own Dataset](../datasets/own-data.md) for the final-user workflow and [Multitask Training](training.md) for catalogue construction during research.
