# 03 - Control the modelling space

Choice modellers often want to ask focused questions:

- What if I only search transformations?
- What if I only switch between generic and alternative-specific tastes?
- What changes when I add covariates?
- What happens if I change covariate levels?

Delphos lets you do this by creating task copies with a smaller search space.


## 1. Load a task and inspect the default space



```python
import delphos as dp
from delphos.grammar import build_runtime

agent = dp.load_agent()
task = dp.load_dataset("Swissmetro")

print("Attributes:", task.attribute_names)
print("Transformations:", task.transform_names)
print("Tastes:", task.taste_names)
print("Covariates:", task.covariate_names)

```

    Attributes: ('ASC', 'time', 'cost', 'headway', 'seat')
    Transformations: ('linear', 'log', 'box_cox')
    Tastes: ('generic', 'specific')
    Covariates: ('purpose', 'first', 'ticket', 'who', 'luggage', 'age', 'male', 'income', 'ga', 'origin', 'dest')


## 2. Helper to count available actions



```python
def count_task_actions(task, linear_additive=True):
    runtime = build_runtime(
        task=task,
        catalogue=agent.catalogue,
        linear_additive=linear_additive,
        device="cpu",
    )
    return int(runtime.action_space.task_mask.sum().item())

print("Default task actions:", count_task_actions(task))

```

    Default task actions: 151


## 3. Transformation-only search

Keep tastes fixed to generic and remove covariates. Delphos can still choose linear, log, or Box-Cox transformations.



```python
transformation_task = dp.configure_modelling_space(
    task,
    tastes=["generic"],
    covariates=[],
)

print("Transformations:", transformation_task.transform_names)
print("Tastes:", transformation_task.taste_names)
print("Covariates:", transformation_task.covariate_names)
print("Actions:", count_task_actions(transformation_task))

transformation_models = agent.propose(
    transformation_task,
    n_models=3,
    strategy="topk",
    top_k=3,
    seed=123,
)
transformation_models.to_dataframe()

```

    Transformations: ('linear', 'log', 'box_cox')
    Tastes: ('generic',)
    Covariates: ()
    Actions: 14





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_id</th>
      <th>task_name</th>
      <th>specification_key</th>
      <th>episode_length</th>
      <th>search_strategy</th>
      <th>attempt_found</th>
      <th>estimated</th>
      <th>reward</th>
      <th>n_terms</th>
      <th>action_indices</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2310_3310_4110_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[25, 73, 9, 121, 25, 57, 9, 41, 105, 89]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2110_3210_4310_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[25, 73, 121, 137, 217, 121, 9, 105, 137, 201]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2210_3310_4110_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[73, 121, 25, 137, 9, 57, 121, 25, 105, 89]</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Taste-only search

Freeze transformations to linear and remove covariates. Delphos then searches generic vs alternative-specific tastes.



```python
taste_task = dp.configure_modelling_space(
    task,
    transformations=["linear"],
    covariates=[],
)

print("Transformations:", taste_task.transform_names)
print("Tastes:", taste_task.taste_names)
print("Covariates:", taste_task.covariate_names)
print("Actions:", count_task_actions(taste_task))

taste_models = agent.propose(
    taste_task,
    n_models=3,
    strategy="topk",
    top_k=3,
    seed=124,
)
taste_models.to_dataframe()

```

    Transformations: ('linear',)
    Tastes: ('generic', 'specific')
    Covariates: ()
    Actions: 10





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_id</th>
      <th>task_name</th>
      <th>specification_key</th>
      <th>episode_length</th>
      <th>search_strategy</th>
      <th>attempt_found</th>
      <th>estimated</th>
      <th>reward</th>
      <th>n_terms</th>
      <th>action_indices</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3120_4110_5000_6110_7000</td>
      <td>7</td>
      <td>topk</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[65, 209, 57, 17, 65, 201, 0]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2110_3120_4110_5000_6120_7000</td>
      <td>9</td>
      <td>topk</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[65, 113, 209, 57, 17, 65, 105, 9, 0]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2110_3120_4120_5000_6110_7000</td>
      <td>7</td>
      <td>topk</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[65, 17, 57, 113, 65, 9, 0]</td>
    </tr>
  </tbody>
</table>
</div>



## 5. Add covariates deliberately

Start with one or two covariates, then expand. This keeps estimation manageable and makes interpretation easier.



```python
covariate_task = dp.configure_modelling_space(
    task,
    transformations=["linear", "log"],
    tastes=["generic", "specific"],
    covariates=["income", "purpose"],
)

print("Covariates:", covariate_task.covariate_names)
print("Actions:", count_task_actions(covariate_task))

covariate_models = agent.propose(
    covariate_task,
    n_models=3,
    strategy="topk",
    top_k=5,
    temperature=0.9,
    seed=125,
)
covariate_models.to_dataframe()

```

    Covariates: ('purpose', 'income')
    Actions: 52





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_id</th>
      <th>task_name</th>
      <th>specification_key</th>
      <th>episode_length</th>
      <th>search_strategy</th>
      <th>attempt_found</th>
      <th>estimated</th>
      <th>reward</th>
      <th>n_terms</th>
      <th>action_indices</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2124_3212_4214_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[21, 27, 17, 131, 125, 75, 73, 27, 21, 75]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3212_4210_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[73, 125, 75, 17, 21, 27, 105, 13, 17, 121]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2114_3210_4222_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>3</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[17, 21, 73, 125, 17, 13, 27, 25, 131, 13]</td>
    </tr>
  </tbody>
</table>
</div>



## 6. Search only selected attributes

Use an attribute subset when you want a compact model family. `ASC` is attribute id 1 and is commonly kept.



```python
compact_task = dp.configure_modelling_space(
    task,
    attributes=["ASC", "time", "cost"],
    transformations=["linear", "log"],
    covariates=[],
)

print("Attributes:", compact_task.attribute_names)
print("Actions:", count_task_actions(compact_task))

```

    Attributes: ('ASC', 'time', 'cost')
    Actions: 10


## 7. Change covariate levels

Covariate levels control how many interaction parameters Apollo creates. Collapsing levels is often useful for quick experiments.



```python
collapsed_task = dp.set_covariate_levels(
    task,
    income=[1, 2],
    purpose=[1, 2],
)

for cov in collapsed_task.covariates:
    if cov.name in {"income", "purpose"}:
        print(cov.name, cov.levels)

```

    purpose (1, 2)
    income (1, 2)


## 8. Recommended workflow

1. Start with transformations only.
2. Add taste variation.
3. Add one covariate family at a time.
4. Estimate a small number of models.
5. Expand the search only after the simple space behaves well.

