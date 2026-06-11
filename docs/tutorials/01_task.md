---
hide:
  - toc
---

```python
import sys
from pathlib import Path

ROOT = Path.cwd()
if ROOT.name == 'tutorials':
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "code"))

from mdp.task import (
    Alternative,
    Attribute,
    Covariate,
    Transformation,
    Taste,
    Task,
)
```

A. Create task manually

1. Modelling space definition

```python
alternatives = (
    Alternative(
        id=1,
        name="car",
        choice=1,
        availability="av_car",
    ),
    Alternative(
        id=2,
        name="bus",
        choice=2,
        availability="av_bus",
    ),
)

attributes = (
    Attribute(
        id=1,
        name="ASC",
        alternative={},
    ),
    Attribute(
        id=2,
        name="cost",
        alternative={
            1: "cost_car",
            2: "cost_bus",
        },
    ),
)

covariates = (
    Covariate(
        id=1,
        name="income",
        levels=(0, 1, 2),
    ),
)

transformations = (
    Transformation(id=1, name="linear"),
    Transformation(id=2, name="log"),
)

tastes = (
    Taste(id=1, name="generic"),
    Taste(id=2, name="specific"),
)
```

2. Task definition

```python
task = Task(
    id=1,
    name="Example",

    yaml_path="",
    dataset_path="data.csv",
    rewards_path="rewards.csv",

    choice_column="choice",
    id_column = 'id',
    is_panel=False,

    ll_null=-100,
    ll_linear=-90,
    n_obs=500,

    alternatives=alternatives,
    attributes=attributes,
    covariates=covariates,
    transformations=transformations,
    tastes=tastes,
)
print(task)

```

    Task(name='Example', alternatives=2, attributes=2, covariates=1)

B. Create Task from YAML file

```python
task_1 = Task.from_yaml(id=0, yaml_path= ROOT / "dataset/dataset_1/dataset.yaml")
print(task_1)
```

    Task(name='ApolloModeChoice', alternatives=4, attributes=5, covariates=3)

C. Load multiples tasks

```python
# List of task configurations intended for multi-task RL training
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

```

D. Create a Catalogue

```python
from mdp.catalogue import Catalogue

catalogue = Catalogue.from_tasks(tasks)
```

```python
# Inspect tasks
for task in catalogue.tasks:
    print(task, task.dataset_path)
```

    Task(name='ApolloModeChoice', alternatives=4, attributes=5, covariates=3) /Users/gnova/Developer/Delphos-core/dataset/dataset_1/2019_apollo_modechoice_formatted.csv
    Task(name='SwissmetroRouteChoice', alternatives=2, attributes=5, covariates=4) /Users/gnova/Developer/Delphos-core/dataset/dataset_2/2018_apollo_routechoice_formatted.csv
    Task(name='Decisions', alternatives=6, attributes=4, covariates=11) /Users/gnova/Developer/Delphos-core/dataset/dataset_3/2020_decisions_formatted.csv
    Task(name='NLModeChoice', alternatives=2, attributes=5, covariates=4) /Users/gnova/Developer/Delphos-core/dataset/dataset_5/1987_netherlands_modechoice_formatted.csv
    Task(name='NorwayVTT', alternatives=2, attributes=3, covariates=4) /Users/gnova/Developer/Delphos-core/dataset/dataset_6/2009_norway_vtt_formatted.csv
    Task(name='Arentze2013', alternatives=3, attributes=6, covariates=1) /Users/gnova/Developer/Delphos-core/dataset/dataset_7/2013_Arentze_formatted.csv
    Task(name='SpainParkingchoice', alternatives=3, attributes=3, covariates=3) /Users/gnova/Developer/Delphos-core/dataset/dataset_8/2014_spain_parkingchoice_formatted.csv
    Task(name='LondonModeChoice', alternatives=4, attributes=6, covariates=4) /Users/gnova/Developer/Delphos-core/dataset/dataset_9/2018_london_modechoice_formatted.csv
    Task(name='Optima', alternatives=2, attributes=5, covariates=5) /Users/gnova/Developer/Delphos-core/dataset/dataset_10/2018_optima_modechoice_formatted.csv
    Task(name='VanCranenburghVOT', alternatives=3, attributes=3, covariates=4) /Users/gnova/Developer/Delphos-core/dataset/dataset_11/2019_vanCranenburgh_vot_formatted.csv

E. Gloabl ids

```python
# See catalogue ids
print(f"Attribute ids: {catalogue.attribute_ids}")
print(f"Transformation ids: {catalogue.transform_ids}")
print(f"Taste ids: {catalogue.taste_ids}")
print(f"Covariate ids: {catalogue.covariate_ids}")
```

    Attribute ids: (1, 2, 3, 4, 5, 6, 7)
    Transformation ids: (1, 2, 3)
    Taste ids: (1, 2)
    Covariate ids: (1, 2, 3, 4, 5, 6, 7)

F. Task masks

```python
print(f"Attributes available in task 1: {catalogue.attribute_mask(task_1)}")
print(f"Covariates available in task 1: {catalogue.covariate_mask(task_1)}")
```

    Attributes available in task 1: [ True  True  True  True False  True False]
    Covariates available in task 1: [ True  True False False False  True False]

G. Task looup

```python
catalogue.get_task(1)
```

    Task(id=1, name='SwissmetroRouteChoice', yaml_path=PosixPath('/Users/gnova/Developer/Delphos-core/dataset/dataset_2/dataset.yaml'), dataset_path=PosixPath('/Users/gnova/Developer/Delphos-core/dataset/dataset_2/2018_apollo_routechoice_formatted.csv'), rewards_path=PosixPath('/Users/gnova/Developer/Delphos-core/dataset/dataset_2/rewards.sqlite'), choice_column='choice', id_column='id', is_panel=True, ll_null=-1933.88063376224, ll_linear=-1337.88755786563, n_obs=2790, alternatives=(Alternative(id=1, name='alt1', choice=1, availability='av_1'), Alternative(id=2, name='alt2', choice=2, availability='av_2')), attributes=(Attribute(id=1, name='ASC', alternative={}), Attribute(id=2, name='time', alternative={1: 'tt1', 2: 'tt2'}), Attribute(id=3, name='cost', alternative={1: 'tc1', 2: 'tc2'}), Attribute(id=4, name='headway', alternative={1: 'hw1', 2: 'hw2'}), Attribute(id=5, name='interchanges', alternative={1: 'ch1', 2: 'ch2'})), covariates=(Covariate(id=2, name='hh_inc_abs', levels=(0, 1, 2, 3, 4)), Covariate(id=5, name='car_availability', levels=(0, 1)), Covariate(id=6, name='business', levels=(0, 1)), Covariate(id=4, name='purpose', levels=(1, 2, 3, 4))), transformations=(Transformation(id=1, name='linear'), Transformation(id=2, name='log'), Transformation(id=3, name='box_cox')), tastes=(Taste(id=1, name='generic'), Taste(id=2, name='specific')))

H. ID retrival

```python
catalogue.get_task(1).id_column
```

    'id'
