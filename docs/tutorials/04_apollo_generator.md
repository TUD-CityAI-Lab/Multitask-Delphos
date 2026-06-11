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

# Define one task
task = task_1
catalogue = Catalogue.from_tasks(tasks)
specification_manager = Specification(catalogue=catalogue)
action_space = ActionSpace(task, catalogue, specification_manager,linear_additive=True)
```

B. Create ApolloGenerator


```python
from env.apollo.generator import ApolloGenerator

generator = ApolloGenerator(task)
```

1. Linear additive


```python
specification = action_space.create_initial_specification()
backend_specification = specification_manager.to_backend(specification)
backend_specification
```




    {'rows': [{'att_id': 1, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 2, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 3, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 4, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 6, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0}],
     'key': '1110_2110_3110_4110_5000_6110_7000',
     'attribute_ids': [1, 2, 3, 4, 6],
     'transformation_ids': [1, 1, 1, 1, 1],
     'taste_ids': [1, 1, 1, 1, 1],
     'covariate_ids': [0, 0, 0, 0, 0]}




```python
apollo_specification = generator.build_apollo_specification(backend_specification)
```


```python
# Check Apollo betas
apollo_specification.apollo_beta
```




    {'ASC_car': 0.0,
     'ASC_bus': 0.0,
     'ASC_air': 0.0,
     'ASC_rail': 0.0,
     'b_time_generic': 0.0,
     'b_cost_generic': 0.0,
     'b_access_generic': 0.0,
     'b_service_generic': 0.0}




```python
# Check Apollo beta fixed
apollo_specification.apollo_fixed
```




    ['ASC_rail']




```python
# Inspect Apollo probabilities code
print(apollo_specification.probability_code)
```

    
            apollo_probabilities <- function(apollo_beta, apollo_inputs, functionality = "estimate") {
    
                apollo_attach(apollo_beta, apollo_inputs)
                on.exit(apollo_detach(apollo_beta, apollo_inputs))
                P = list()
                V = list()
                V <- list()
    
    V[["car"]] <-
          ASC_car +
          b_time_generic * time_car +
          b_cost_generic * cost_car
    
    V[["bus"]] <-
          ASC_bus +
          b_time_generic * time_bus +
          b_cost_generic * cost_bus +
          b_access_generic * access_bus
    
    V[["air"]] <-
          ASC_air +
          b_time_generic * time_air +
          b_cost_generic * cost_air +
          b_access_generic * access_air +
          b_service_generic * service_air
    
    V[["rail"]] <-
          ASC_rail +
          b_time_generic * time_rail +
          b_cost_generic * cost_rail +
          b_access_generic * access_rail +
          b_service_generic * service_rail
                mnl_settings = list(
                    alternatives = c(car=1, bus=2, air=3, rail=4),
                    avail = list(car=av_car, bus=av_bus, air=av_air, rail=av_rail),
                    choiceVar = choice,
                    utilities = V
                )
                P[["model"]] = apollo_mnl(mnl_settings, functionality)
                P = apollo_panelProd(P, apollo_inputs, functionality)
                P = apollo_prepareProb(P, apollo_inputs, functionality)
                return(P)
            }
            


E.2. Rich examples


```python
specification_1 = action_space.create_initial_specification()
specification_1
```




    tensor([[1, 1, 1, 0],
            [2, 1, 1, 0],
            [3, 1, 1, 0],
            [4, 1, 1, 0],
            [5, 0, 0, 0],
            [6, 1, 1, 0],
            [7, 0, 0, 0]])




```python
valid_actions = action_space.get_valid_actions(specification_1, visited_specifications=set())

valid_actions[:20]
```




    [Action(type=<ActionType.TERMINATE: 0>, attribute_id=None, transform_id=None, taste_id=None, covariate_id=None),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=1),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=2),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=1, transform_id=1, taste_id=1, covariate_id=6),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=1),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=2),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=1, covariate_id=6),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=0),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=1),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=2),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=1, taste_id=2, covariate_id=6),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=1, covariate_id=0),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=1, covariate_id=1),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=1, covariate_id=2),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=1, covariate_id=6),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=2, covariate_id=0),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=2, covariate_id=1),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=2, covariate_id=2),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=2, taste_id=2, covariate_id=6),
     Action(type=<ActionType.CHANGE: 2>, attribute_id=2, transform_id=3, taste_id=1, covariate_id=0)]




```python
specification_2, _ = action_space.apply_action(specification_1, action_index=3)
specification_2, _ = action_space.apply_action(specification_2, action_index=15)

backend_specification_2 = specification_manager.to_backend(specification_2)
apollo_specification_2 = generator.build_apollo_specification(backend_specification_2)
print(apollo_specification_2.utility_code)
```

    V <- list()
    
    V[["car"]] <-
          ASC_car +
          ASC_car_income_1 * (income == 1) +
          ASC_car_income_2 * (income == 2) +
          ASC_car_income_3 * (income == 3) +
          ASC_car_income_4 * (income == 4) +
          b_time_generic * time_car +
          b_time_generic_business_0 * (business == 0) * time_car +
          b_time_generic_business_1 * (business == 1) * time_car +
          b_cost_generic * cost_car
    
    V[["bus"]] <-
          ASC_bus +
          ASC_bus_income_1 * (income == 1) +
          ASC_bus_income_2 * (income == 2) +
          ASC_bus_income_3 * (income == 3) +
          ASC_bus_income_4 * (income == 4) +
          b_time_generic * time_bus +
          b_time_generic_business_0 * (business == 0) * time_bus +
          b_time_generic_business_1 * (business == 1) * time_bus +
          b_cost_generic * cost_bus +
          b_access_generic * access_bus
    
    V[["air"]] <-
          ASC_air +
          ASC_air_income_1 * (income == 1) +
          ASC_air_income_2 * (income == 2) +
          ASC_air_income_3 * (income == 3) +
          ASC_air_income_4 * (income == 4) +
          b_time_generic * time_air +
          b_time_generic_business_0 * (business == 0) * time_air +
          b_time_generic_business_1 * (business == 1) * time_air +
          b_cost_generic * cost_air +
          b_access_generic * access_air +
          b_service_generic * service_air
    
    V[["rail"]] <-
          ASC_rail +
          ASC_rail_income_1 * (income == 1) +
          ASC_rail_income_2 * (income == 2) +
          ASC_rail_income_3 * (income == 3) +
          ASC_rail_income_4 * (income == 4) +
          b_time_generic * time_rail +
          b_time_generic_business_0 * (business == 0) * time_rail +
          b_time_generic_business_1 * (business == 1) * time_rail +
          b_cost_generic * cost_rail +
          b_access_generic * access_rail +
          b_service_generic * service_rail

