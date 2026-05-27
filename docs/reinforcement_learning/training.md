---
hide:
  - navigation
---
# Training Delphos

Training Delphos on a new discrete choice dataset involves three main steps.

---

## Step 1 — Define the dataset

Each dataset is configured through a `dataset.yaml` file.

The YAML configuration defines:

- alternatives,
- attributes,
- covariates,
- transformations,
- baseline metrics,
- and dataset paths.

Example:

```yaml
alternatives:
  alt1:
    id: 1
    avail: "avail_1"

  alt2:
    id: 2
    avail: "avail_2"

attributes:
  time:
    id: 2
    mapping:
      alt1: "time_1"
      alt2: "time_2"

covariates:
  income:
    id: 1
    levels: [1, 2, 3]

ll_null: -1000.0
ll_linear: -800.0
n_obs: 2500

path_choice_dataset: "my_data_formatted.csv"
```

---

## Step 2 — Register the dataset as a Task object

Datasets are registered through the task registry.

Example:

```python
from mdp.task import Task
from configs.task_configuration import PROJECT_ROOT

TASKS_YAML: list[Task] = [
    Task.from_yaml(
        0,
        PROJECT_ROOT.parent / "dataset/my_custom_dataset/dataset.yaml"
    ),
]
```

The framework automatically:

- parses the YAML configuration,
- generates masks,
- builds state spaces,
- and exposes the task to the RL environment.

---

## Step 3 — Run the Pipeline

Launch training through one of the scripts in `scripts/`.

Example:

```bash
python scripts/run_small_full_pipeline.py
```

---

# Training Workflow

The training process follows three main stages.

## 1. Infrastructure Validation

Delphos validates:

- dataset configurations,
- state spaces,
- action spaces,
- and estimation environments.

## 2. Rollout Initialization

Random rollouts are executed to:

- initialize caches,
- validate Apollo integration,
- and populate replay buffers.

## 3. Reinforcement Learning

The agent progressively explores the specification space while receiving rewards from the estimation environment. Model estimations are executed dynamically using Apollo.
