# Use Your Own Dataset

The recommended workflow creates a self-contained task folder from your CSV and explicit schema dictionaries.

## 1. Prepare a wide-format CSV

A simple two-alternative file might contain:

```text
id,choice,av_car,av_bus,tt_car,tt_bus,cost_car,cost_bus,income
1,1,1,1,25,40,8.5,3.0,2
2,2,1,1,35,30,7.0,3.5,1
```

The current Apollo generator expects alternative-specific attribute columns. Scale continuous variables before creating the task when that makes estimation and interpretation clearer.

## 2. Define alternatives

```python
alternatives = {
    "CAR": {"id": 1, "avail": "av_car"},
    "BUS": {"id": 2, "avail": "av_bus"},
}
```

The keys become the alternative names used in generated Apollo utility code. Each `id` must match the value in the choice column.

## 3. Map attributes

```python
attributes = {
    "time": {
        "id": 2,
        "mapping": {
            "CAR": "tt_car",
            "BUS": "tt_bus",
        },
    },
    "cost": {
        "id": 3,
        "mapping": {
            "CAR": "cost_car",
            "BUS": "cost_bus",
        },
    },
}
```

Attribute identifiers refer to concepts in the trained global catalogue. Use the identifier for travel time only when the mapped variables genuinely represent that concept in compatible units and meaning.

## 4. Define candidate heterogeneity variables

```python
covariates = {
    "income": {
        "id": 2,
        "source": "income",
        "type": "categorical",
        "levels": [1, 2, 3, 4],
    },
}
```

Only include levels with adequate observations. Decide the coding and reference category before launching a search.

## 5. Create and validate the task

```python
from pathlib import Path
import delphos as dp

task = dp.create_dataset(
    Path("my_project/dataset_100"),
    name="MyModeChoice",
    csv_path=Path("my_project/mode_choice.csv"),
    choice_column="choice",
    id_column="id",
    panel=False,
    alternatives=alternatives,
    attributes=attributes,
    covariates=covariates,
    dataset_id=100,
)

print(task)
```

`create_dataset()` copies the CSV, writes `dataset.yaml`, validates required columns and identifiers, and returns a `Task`.

## 6. Check compatibility with the checkpoint

```python
model = dp.load_agent()

# Validation occurs automatically here.
proposals = model.propose(task, n_models=5, seed=123)
```

If the task uses modelling identifiers outside the trained catalogue, Delphos raises a `ValueError` describing the missing concepts. A new concept requires training-package work; it cannot be added to a fixed checkpoint by renaming a variable.

## 7. Inspect generated code before estimation

```python
proposal = proposals.proposals[0]
print(proposal.apollo_specification.utility_code)
```

Confirm that variable mappings, availability, reference alternatives, parameter sharing, and transformations match your intended choice model.

The complete executable example is available in [02. Your Own Datasets](../tutorials/end-user/02_your_own_datasets.ipynb).
