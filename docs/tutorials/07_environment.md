```python
import sys
from pathlib import Path

ROOT = Path.cwd().parent
sys.path.insert(0, str(ROOT / "code"))

from mdp.task import Task
from mdp.catalogue import Catalogue
from mdp.state import Specification, Term
from mdp.action import *
from env.apollo.generator import ApolloGenerator
from env.environment import evaluate_specification
from env.result_cache import ResultCache

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

# Define one task
task = task_1
catalogue = Catalogue.from_tasks(tasks)
specification_manager = Specification(catalogue=catalogue)
action_space = ActionSpace(task, catalogue, specification_manager,linear_additive=True)
generator = ApolloGenerator(task)
```

1. Linear additive


```python
print("rewards_path", task.rewards_path)
print("yaml_path", task.yaml_path)
print("dataset_path",task.dataset_path)
```

    rewards_path /Users/gnova/Developer/Delphos-core/dataset/dataset_1/rewards.sqlite
    yaml_path /Users/gnova/Developer/Delphos-core/dataset/dataset_1/dataset.yaml
    dataset_path /Users/gnova/Developer/Delphos-core/dataset/dataset_1/2019_apollo_modechoice_formatted.csv



```python
specification = action_space.create_initial_specification()
backend_specification = specification_manager.to_backend(specification)
apollo_specification = generator.build_apollo_specification(backend_specification)

evaluate_specification(
    task,
    apollo_specification
    ) 
```




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
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ApolloModeChoice</td>
      <td>1110_2110_3110_4110_5000_6110_7000</td>
      <td>7.0</td>
      <td>5600.0</td>
      <td>-4670.988194</td>
      <td>5.802145e-07</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4670.988194</td>
      <td>0.293034</td>
      <td>0.291975</td>
      <td>0.139922</td>
      <td>0.139185</td>
      <td>9355.976387</td>
      <td>9402.39004</td>
      <td>-25.901553</td>
      <td>0.442298</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
specification_2 = action_space.create_initial_specification()
specification_2, _ = action_space.apply_action(specification_2, action_index=3)

backend_specification_2 = specification_manager.to_backend(specification_2)
apollo_specification_2 = generator.build_apollo_specification(backend_specification_2)



evaluate_specification(
    task,
    apollo_specification_2,
    ) 
```




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
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ApolloModeChoice</td>
      <td>1112_2110_3110_4110_5000_6110_7000</td>
      <td>16.0</td>
      <td>5600.0</td>
      <td>-4554.368737</td>
      <td>1.481029e-07</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4554.368737</td>
      <td>0.310685</td>
      <td>0.308263</td>
      <td>0.161395</td>
      <td>0.159001</td>
      <td>9140.737474</td>
      <td>9246.825824</td>
      <td>-6.232372</td>
      <td>1.012997</td>
      <td>16.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


