---
hide:
  - toc
---

```python
import sys
from pathlib import Path

ROOT = Path.cwd().parent
sys.path.insert(0, str(ROOT / "code"))

from mdp.task import Task
from mdp.catalogue import Catalogue
from mdp.state import Specification, Term
```

A. Load a single task and catalogue

```python
task_1 = Task.from_yaml(0,  yaml_path=ROOT / "dataset/dataset_1/dataset.yaml") # ApolloModeChoice
task_2 = Task.from_yaml(1,  yaml_path=ROOT / "dataset/dataset_2/dataset.yaml") # ApolloRouteChoice
task_3 = Task.from_yaml(2,  yaml_path=ROOT / "dataset/dataset_3/dataset.yaml") # Decisions
task_4 = Task.from_yaml(3,  yaml_path=ROOT / "dataset/dataset_5/dataset.yaml") # 1987_NL_VoT
task_5 = Task.from_yaml(4,  yaml_path=ROOT / "dataset/dataset_6/dataset.yaml") # 2009_Norway_VoT
task_6 = Task.from_yaml(5,  yaml_path=ROOT / "dataset/dataset_7/dataset.yaml") # 2013_Arentze
task_7 = Task.from_yaml(6,  yaml_path=ROOT / "dataset/dataset_8/dataset.yaml") # 2014_spain_parkingChoice
task_8 = Task.from_yaml(7,  yaml_path=ROOT / "dataset/dataset_9/dataset.yaml") # 2018 LPMC
task_9 = Task.from_yaml(8,  yaml_path=ROOT / "dataset/dataset_10/dataset.yaml") # 2018_Optima
task_10 = Task.from_yaml(9,  yaml_path=ROOT / "dataset/dataset_11/dataset.yaml") # 2019_vanCranenburgh

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10]

catalogue = Catalogue.from_tasks(tasks)
```

B. Create state manager

```python
Specification = Specification(catalogue=catalogue)
```

C. Create a null model

```python
null_model = Specification.empty()
null_model
```

    tensor([[1, 0, 0, 0],
            [2, 0, 0, 0],
            [3, 0, 0, 0],
            [4, 0, 0, 0],
            [5, 0, 0, 0],
            [6, 0, 0, 0],
            [7, 0, 0, 0]])

D. Create linear additive model

```python
# ASC
asc = Term(
    attribute_id=1,
    transform_id=1,
    taste_id=1,
    covariate_id=0,
)

# Time - linear - generic - no interaction
time = Term(
    attribute_id=2,
    transform_id=1,
    taste_id=1,
    covariate_id=0,
)

# Cost - linear - generic - no interaction
cost = Term(
    attribute_id=3,
    transform_id=1,
    taste_id=1,
    covariate_id=0,
)

linear_additive = Specification.from_terms([asc, cost,time,])

linear_additive

```

    tensor([[1, 1, 1, 0],
            [2, 1, 1, 0],
            [3, 1, 1, 0],
            [4, 0, 0, 0],
            [5, 0, 0, 0],
            [6, 0, 0, 0],
            [7, 0, 0, 0]])

E. State to Specification

```python
terms = Specification.to_terms(linear_additive)
terms
```

    [Term(attribute_id=1, transform_id=1, taste_id=1, covariate_id=0),
     Term(attribute_id=2, transform_id=1, taste_id=1, covariate_id=0),
     Term(attribute_id=3, transform_id=1, taste_id=1, covariate_id=0)]

F. Specification to Apollo

```python
backend = Specification.to_backend(linear_additive)
backend
```

    {'rows': [{'att_id': 1, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 2, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 3, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0}],
     'key': '1110_2110_3110_4000_5000_6000_7000',
     'attribute_ids': [1, 2, 3],
     'transformation_ids': [1, 1, 1],
     'taste_ids': [1, 1, 1],
     'covariate_ids': [0, 0, 0]}

```python
# State summary
Specification.summary()
```

    {'n_attributes': 7,
     'attribute_ids': (1, 2, 3, 4, 5, 6, 7),
     'covariate_ids': (1, 2, 3, 4, 5, 6, 7),
     'transform_ids': (1, 2, 3),
     'taste_ids': (1, 2),
     'device': 'cpu',
     'shape': (7, 4)}
