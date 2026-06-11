---
hide:
  - toc
---

# Using Your Own Datasets

While Delphos includes several datasets in its Catalogue, you will often want to apply Delphos to your own discrete choice dataset. To do so, you must define a Task describing the modelling problem. A task specifies:

- The dataset location.
- The alternatives available to decision-makers.
- The attributes associated with each alternative.
- The socio-demographic variables available for taste heterogeneity.
- The modelling structures Delphos is allowed to explore.

There are two ways to create a task:

1. Using a YAML configuration file (recommended).
2. Using Python classes directly.

---

## Option 1: Defining a Task with a YAML File

The simplest way to define a new task is through a YAML file. A minimal example is shown below:

```yaml
df_name: my_dataset
path_choice_dataset: data/my_dataset.csv

choice:
  column: choice
  id: respondent_id
  panel: false

alternatives:
  car:
    id: 1
    avail: av_car
  bus:
    id: 2
    avail: av_bus

attributes:
  travel_time:
    id: 2
    mapping:
      car: tt_car
      bus: tt_bus
  travel_cost:
    id: 3
    mapping:
      car: cost_car
      bus: cost_bus

covariates:
  income:
    id: 1
    levels: [0, 1, 2]
  gender:
    id: 2
    levels: [0, 1]
```

The YAML file describes the model specification task and can be shared independently from the Delphos codebase.

**Alternatives** define the available options from which decision-makers choose. You must define:

- their name (car, bus, ...).
- their id (value in the choice column).
- their availability (binary variable indicating whether the alternative is available in the dataset).

```yaml
alternatives:
  car:
    id: 1
    avail: av_car
  bus:
    id: 2
    avail: av_bus
```

**Attributes** describe the alternatives. You must define:

- their name (column name in the dataset).
- their id (ID value from the Catalogue).
- their mapping (which dataset column corresponds to the attribute for each alternative).

```yaml
attributes:
  travel_time:
    id: 2 # ID value retrieved from the Catalogue. Please see the catalogue list for valid IDs.
    mapping:
      car: tt_car # column name in the dataset
      bus: tt_bus # column name in the dataset
  travel_cost:
    id: 3
    mapping:
      car: cost_car
      bus: cost_bus
```

!!! example "Step 1: Load a Task from YAML"

```python
from delphos.mdp.task import Task

task = Task.from_yaml(
    id=1,
    yaml_path="dataset.yaml"
)
```

Inspect the task:

```python
print(task)
```

Example output:

```python
Task(
    name='my_dataset',
    alternatives=2,
    attributes=3,
    covariates=2
)
```

**Covariates** are variables that can be used to model systematic taste heterogeneity. You must define:

- their name (column name in the dataset).
- their id (ID value from the Catalogue).
- their levels (categories available for interaction effects).

```yaml
covariates:
  income:
    id: 1
    levels: [0, 1, 2]
  gender:
    id: 2
    levels: [0, 1]
```

---

## Option 2: Creating a Task Manually

Alternatively, you can define tasks directly in Python.

!!! example "Step 1: Create Alternatives"

```python
from delphos.mdp.task import Alternative

car = Alternative(
    id=1,
    name="car",
    choice=1,
    availability="av_car"
)

bus = Alternative(
    id=2,
    name="bus",
    choice=2,
    availability="av_bus"
)
```

!!! example "Step 2: Create attributes"

```python
from delphos.mdp.task import Attribute

travel_time = Attribute(
    id=2,
    name="travel_time",
    alternative={
        1: "tt_car",
        2: "tt_bus"
    }
)

travel_cost = Attribute(
    id=3,
    name="travel_cost",
    alternative={
        1: "cost_car",
        2: "cost_bus"
    }
)
```

!!! example "Step 3: Create attributes"

```python
from delphos.mdp.task import Covariate

income = Covariate(
    id=1,
    name="income",
    levels=(0, 1, 2)
)
```

!!! example "Step 4: Create the Task"

```python
from pathlib import Path
from delphos.mdp.task import (
    Task,
    Transformation,
    Taste
)

task = Task(
    id=1,
    name="my_dataset",
    dataset_path=Path("data/my_dataset.csv"),
    choice_column="choice",
    id_column="respondent_id",
    is_panel=False,
    alternatives=(car, bus),
    attributes=(travel_time, travel_cost),
    covariates=(income)
)
```

!!! example "Step 5: Validate the Task"

Inspect the resulting task:

```python
print(task)
```

Inspect its components:

```python
task.alternative_names
task.attribute_names
task.covariate_names
```

## Which Approach Should I Use?

For most users, the YAML approach is recommended because:

- It is easier to read and modify.
- It can be version controlled.
- It separates modelling metadata from Python code.
- It is the format used internally by the Delphos Catalogue.

---

## Next Step

Continue to Custom Objectives to learn how to customise the reward function used by Delphos during model specification.
