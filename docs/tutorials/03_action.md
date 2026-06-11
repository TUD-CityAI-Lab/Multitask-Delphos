```python
import sys
from pathlib import Path
ROOT = Path.cwd().parent
sys.path.insert(0, str(ROOT / "code"))

from mdp.task import Task
from mdp.catalogue import Catalogue
from mdp.state import Specification, Term
from mdp.action import *
```

A. Load task and create a catalogue


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
specification_manager = Specification(catalogue=catalogue)
specification_manager.summary()
```




    {'n_attributes': 7,
     'attribute_ids': (1, 2, 3, 4, 5, 6, 7),
     'covariate_ids': (1, 2, 3, 4, 5, 6, 7),
     'transform_ids': (1, 2, 3),
     'taste_ids': (1, 2),
     'device': 'cpu',
     'shape': (7, 4)}



## Create a action manager from null model


```python
# Define one task
task = task_1
print(task, task.dataset_path)

action_space = ActionSpace(task, catalogue, specification_manager,linear_additive=False)

action_space.summary()
```

    Task(name='task_0', alternatives=4, attributes=5, covariates=3) /Users/gnova/Developer/Delphos-core/dataset/dataset_1/2019_apollo_modechoice_formatted.csv





    {'num_actions': 304,
     'linear_additive': False,
     'task': 'task_0',
     'n_catalogue_attributes': 7,
     'n_catalogue_covariates': 8,
     'task_actions': 106}



D. Inspect global action catalogue


```python
print(f"Total actions: {action_space.num_actions}")

for idx in range(20):
    print(idx, action_space.idx_to_action[idx])
```

    Total actions: 304
    0 Action(type=<ActionType.TERMINATE: 0>, attribute_id=None, transform_id=None, taste_id=None, covariate_id=None)
    1 Action(type=<ActionType.ADD: 1>, attribute_id=1, transform_id=None, taste_id=None, covariate_id=None)
    2 Action(type=<ActionType.ADD: 1>, attribute_id=2, transform_id=None, taste_id=None, covariate_id=None)
    3 Action(type=<ActionType.ADD: 1>, attribute_id=3, transform_id=None, taste_id=None, covariate_id=None)
    4 Action(type=<ActionType.ADD: 1>, attribute_id=4, transform_id=None, taste_id=None, covariate_id=None)
    5 Action(type=<ActionType.ADD: 1>, attribute_id=5, transform_id=None, taste_id=None, covariate_id=None)
    6 Action(type=<ActionType.ADD: 1>, attribute_id=6, transform_id=None, taste_id=None, covariate_id=None)
    7 Action(type=<ActionType.ADD: 1>, attribute_id=7, transform_id=None, taste_id=None, covariate_id=None)
    8 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=0)
    9 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=1)
    10 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=2)
    11 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=3)
    12 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=4)
    13 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=5)
    14 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=6)
    15 Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=7)
    16 Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=0)
    17 Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=1)
    18 Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=2)
    19 Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=3)


E. Create a null model 


```python
specification = action_space.create_initial_specification()
specification
```




    tensor([[1, 0, 0, 0],
            [2, 0, 0, 0],
            [3, 0, 0, 0],
            [4, 0, 0, 0],
            [5, 0, 0, 0],
            [6, 0, 0, 0],
            [7, 0, 0, 0]])



F. Identify valid actions for this specification


```python
valid_indices = action_space.get_valid_action_indices(specification,set(),)

for i in valid_indices:
    print(action_space.get_action(i))
```

    Action(type=<ActionType.TERMINATE: 0>, attribute_id=None, transform_id=None, taste_id=None, covariate_id=None)
    Action(type=<ActionType.ADD: 1>, attribute_id=1, transform_id=None, taste_id=None, covariate_id=None)
    Action(type=<ActionType.ADD: 1>, attribute_id=2, transform_id=None, taste_id=None, covariate_id=None)
    Action(type=<ActionType.ADD: 1>, attribute_id=3, transform_id=None, taste_id=None, covariate_id=None)
    Action(type=<ActionType.ADD: 1>, attribute_id=4, transform_id=None, taste_id=None, covariate_id=None)
    Action(type=<ActionType.ADD: 1>, attribute_id=6, transform_id=None, taste_id=None, covariate_id=None)


F. Apply first `ADD` action


```python
specification, done = action_space.apply_action(specification, 1)
print(f"Current specification:\n\n{specification}\n")
print(f"terminate?: {done}")

```

    Current specification:
    
    tensor([[1, 1, 1, 0],
            [2, 0, 0, 0],
            [3, 0, 0, 0],
            [4, 0, 0, 0],
            [5, 0, 0, 0],
            [6, 0, 0, 0],
            [7, 0, 0, 0]])
    
    terminate?: False



```python
specification, done = action_space.apply_action(specification, 2)

print(f"Current specification:\n\n{specification_manager.to_terms(specification)}\n")
print(f"terminate?: {done}")
```

    Current specification:
    
    [Term(attribute_id=1, transform_id=1, taste_id=1, covariate_id=0), Term(attribute_id=2, transform_id=1, taste_id=1, covariate_id=0)]
    
    terminate?: False



```python
specification, done = action_space.apply_action(specification, 0)
print(f"Current specification:\n\n{specification_manager.to_terms(specification)}\n")
print(f"terminate?: {done}")
```

    Current specification:
    
    [Term(attribute_id=1, transform_id=1, taste_id=1, covariate_id=0), Term(attribute_id=2, transform_id=1, taste_id=1, covariate_id=0)]
    
    terminate?: True


## Create a action manager from linear additive model


```python
# Define one task
task = task_1
print(task, task.dataset_path)

action_space = ActionSpace(task, catalogue, specification_manager,linear_additive=True)

action_space.summary()
```

    Task(name='task_0', alternatives=4, attributes=5, covariates=3) /Users/gnova/Developer/Delphos-core/dataset/dataset_1/2019_apollo_modechoice_formatted.csv





    {'num_actions': 297,
     'linear_additive': True,
     'task': 'task_0',
     'n_catalogue_attributes': 7,
     'n_catalogue_covariates': 8,
     'task_actions': 101}




```python
specification = action_space.create_initial_specification()
specification
```




    tensor([[1, 1, 1, 0],
            [2, 1, 1, 0],
            [3, 1, 1, 0],
            [4, 1, 1, 0],
            [5, 0, 0, 0],
            [6, 1, 1, 0],
            [7, 0, 0, 0]])




```python
valid_indices = action_space.get_valid_action_indices(specification,set(),)

for i in valid_indices[:10]:
    print(action_space.get_action(i))
```

    Action(type=<ActionType.TERMINATE: 0>, attribute_id=None, transform_id=None, taste_id=None, covariate_id=None)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=1)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=2)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=6)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=1)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=2)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=6)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=0)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=1)
    Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=2)


Apply first `Change` action


```python
specification, done = action_space.apply_action(specification, 2)
specification, done = action_space.apply_action(specification, 0)
print(f"Current specification:\n\n{specification}\n")
print(f"terminate?: {done}")
print(f"Final specification:\n\n{specification_manager.to_terms(specification)}\n")


```

    Current specification:
    
    tensor([[1, 1, 1, 1],
            [2, 1, 1, 0],
            [3, 1, 1, 0],
            [4, 1, 1, 0],
            [5, 0, 0, 0],
            [6, 1, 1, 0],
            [7, 0, 0, 0]])
    
    terminate?: True
    Final specification:
    
    [Term(attribute_id=1, transform_id=1, taste_id=1, covariate_id=1), Term(attribute_id=2, transform_id=1, taste_id=1, covariate_id=0), Term(attribute_id=3, transform_id=1, taste_id=1, covariate_id=0), Term(attribute_id=4, transform_id=1, taste_id=1, covariate_id=0), Term(attribute_id=6, transform_id=1, taste_id=1, covariate_id=0)]
    

