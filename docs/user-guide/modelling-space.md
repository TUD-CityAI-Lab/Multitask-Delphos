# Control the Modelling Space

The task defines everything Delphos is allowed to consider. Restricting that space is the most important way to keep proposals interpretable, computationally manageable, and aligned with your research question.

## Inspect the default task

```python
import delphos as dp

task = dp.load_dataset("Swissmetro")

print([item.name for item in task.attributes])
print([item.name for item in task.transformations])
print([item.name for item in task.tastes])
print([item.name for item in task.covariates])
```

The automatically added `ASC` attribute represents alternative-specific constants. The remaining attributes map modelling concepts such as time and cost to the corresponding columns for each alternative.

## Start with a compact space

```python
compact_task = dp.configure_modelling_space(
    task,
    attributes=["ASC", "time", "cost"],
    transformations=["linear", "log"],
    tastes=["generic"],
    covariates=[],
)
```

`configure_modelling_space()` returns a new task; it does not mutate the original one. Selectors may use names or global identifiers.

Generate proposals from the restricted task:

```python
model = dp.load_agent()
proposals = model.propose(compact_task, n_models=10, seed=123)
```

## Add flexibility deliberately

Expand one modelling dimension at a time:

```python
behavioural_task = dp.configure_modelling_space(
    task,
    attributes=["ASC", "time", "cost", "headway"],
    transformations=["linear", "log", "box_cox"],
    tastes=["generic", "specific"],
    covariates=["income", "purpose"],
)
```

This makes it possible to distinguish whether additional complexity came from functional form, alternative-specific tastes, or observed heterogeneity.

## Control covariate levels

Large categorical variables can create many parameters. Keep only levels that are meaningful and sufficiently represented:

```python
behavioural_task = dp.set_covariate_levels(
    behavioural_task,
    income=[1, 2, 3, 4],
    purpose=[1, 2],
)
```

Check reference coding and minimum group sizes before estimation. Delphos generates the interactions, but it cannot determine whether the chosen coding is substantively appropriate.

## Recommended expansion sequence

1. Linear additive attributes with generic tastes.
2. Non-linear transformations for continuous attributes.
3. Alternative-specific tastes where theory supports them.
4. A small set of pre-specified covariate interactions.
5. Broader searches only after the simpler spaces have been reviewed.

This mirrors a transparent manual specification process and makes the resulting candidate set easier to explain.
