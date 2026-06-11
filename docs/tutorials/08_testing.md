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
import torch as t
#1110_2326_3326_4211_5000_6121_7000
specificaiton =[
    [1, 1, 1, 0],
    [2, 3, 2, 6],
    [3, 3, 2, 6],
    [4, 2, 1, 1],
    [5, 0, 0, 0],
    [6, 1, 2, 1],
    [7, 0, 0, 0]
]

specificaiton_tensor = t.tensor(specificaiton)
specification_manager.to_terms(specificaiton_tensor)
```




    [Term(attribute_id=1, transform_id=1, taste_id=1, covariate_id=0),
     Term(attribute_id=2, transform_id=3, taste_id=2, covariate_id=6),
     Term(attribute_id=3, transform_id=3, taste_id=2, covariate_id=6),
     Term(attribute_id=4, transform_id=2, taste_id=1, covariate_id=1),
     Term(attribute_id=6, transform_id=1, taste_id=2, covariate_id=1)]




```python
backend_specification = specification_manager.to_backend(specificaiton_tensor)
backend_specification
```




    {'rows': [{'att_id': 1, 'trans_id': 1, 'taste_id': 1, 'cov_id': 0},
      {'att_id': 2, 'trans_id': 3, 'taste_id': 2, 'cov_id': 6},
      {'att_id': 3, 'trans_id': 3, 'taste_id': 2, 'cov_id': 6},
      {'att_id': 4, 'trans_id': 2, 'taste_id': 1, 'cov_id': 1},
      {'att_id': 6, 'trans_id': 1, 'taste_id': 2, 'cov_id': 1}],
     'key': '1110_2326_3326_4211_5000_6121_7000',
     'attribute_ids': [1, 2, 3, 4, 6],
     'transformation_ids': [1, 3, 3, 2, 1],
     'taste_ids': [1, 2, 2, 1, 2],
     'covariate_ids': [0, 6, 6, 1, 1]}




```python
apollo_specification = generator.build_apollo_specification(backend_specification)
apollo_specification.estimated_parameters
```




    ['ASC_car',
     'ASC_bus',
     'ASC_air',
     'L_time',
     'b_car_time_box_cox_business_0',
     'b_car_time_box_cox_business_1',
     'b_bus_time_box_cox_business_0',
     'b_bus_time_box_cox_business_1',
     'b_air_time_box_cox_business_0',
     'b_air_time_box_cox_business_1',
     'b_rail_time_box_cox_business_0',
     'b_rail_time_box_cox_business_1',
     'L_cost',
     'b_car_cost_box_cox_business_0',
     'b_car_cost_box_cox_business_1',
     'b_bus_cost_box_cox_business_0',
     'b_bus_cost_box_cox_business_1',
     'b_air_cost_box_cox_business_0',
     'b_air_cost_box_cox_business_1',
     'b_rail_cost_box_cox_business_0',
     'b_rail_cost_box_cox_business_1',
     'b_access_generic_log_female_0',
     'b_access_generic_log_female_1',
     'b_air_service_female_0',
     'b_air_service_female_1',
     'b_rail_service_female_0',
     'b_rail_service_female_1']




```python
print(apollo_specification.utility_code)
```

    V <- list()
    
    V[["car"]] <-
          ASC_car +
          b_car_time_box_cox_business_0 * (business == 0) * ((time_car^L_time - 1) / L_time) +
          b_car_time_box_cox_business_1 * (business == 1) * ((time_car^L_time - 1) / L_time) +
          b_car_cost_box_cox_business_0 * (business == 0) * ((cost_car^L_cost - 1) / L_cost) +
          b_car_cost_box_cox_business_1 * (business == 1) * ((cost_car^L_cost - 1) / L_cost)
    
    V[["bus"]] <-
          ASC_bus +
          b_bus_time_box_cox_business_0 * (business == 0) * ((time_bus^L_time - 1) / L_time) +
          b_bus_time_box_cox_business_1 * (business == 1) * ((time_bus^L_time - 1) / L_time) +
          b_bus_cost_box_cox_business_0 * (business == 0) * ((cost_bus^L_cost - 1) / L_cost) +
          b_bus_cost_box_cox_business_1 * (business == 1) * ((cost_bus^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_bus) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_bus)
    
    V[["air"]] <-
          ASC_air +
          b_air_time_box_cox_business_0 * (business == 0) * ((time_air^L_time - 1) / L_time) +
          b_air_time_box_cox_business_1 * (business == 1) * ((time_air^L_time - 1) / L_time) +
          b_air_cost_box_cox_business_0 * (business == 0) * ((cost_air^L_cost - 1) / L_cost) +
          b_air_cost_box_cox_business_1 * (business == 1) * ((cost_air^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_air) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_air) +
          b_air_service_female_0 * (female == 0) * service_air +
          b_air_service_female_1 * (female == 1) * service_air
    
    V[["rail"]] <-
          ASC_rail +
          b_rail_time_box_cox_business_0 * (business == 0) * ((time_rail^L_time - 1) / L_time) +
          b_rail_time_box_cox_business_1 * (business == 1) * ((time_rail^L_time - 1) / L_time) +
          b_rail_cost_box_cox_business_0 * (business == 0) * ((cost_rail^L_cost - 1) / L_cost) +
          b_rail_cost_box_cox_business_1 * (business == 1) * ((cost_rail^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_rail) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_rail) +
          b_rail_service_female_0 * (female == 0) * service_rail +
          b_rail_service_female_1 * (female == 1) * service_rail



```python
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
          b_car_time_box_cox_business_0 * (business == 0) * ((time_car^L_time - 1) / L_time) +
          b_car_time_box_cox_business_1 * (business == 1) * ((time_car^L_time - 1) / L_time) +
          b_car_cost_box_cox_business_0 * (business == 0) * ((cost_car^L_cost - 1) / L_cost) +
          b_car_cost_box_cox_business_1 * (business == 1) * ((cost_car^L_cost - 1) / L_cost)
    
    V[["bus"]] <-
          ASC_bus +
          b_bus_time_box_cox_business_0 * (business == 0) * ((time_bus^L_time - 1) / L_time) +
          b_bus_time_box_cox_business_1 * (business == 1) * ((time_bus^L_time - 1) / L_time) +
          b_bus_cost_box_cox_business_0 * (business == 0) * ((cost_bus^L_cost - 1) / L_cost) +
          b_bus_cost_box_cox_business_1 * (business == 1) * ((cost_bus^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_bus) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_bus)
    
    V[["air"]] <-
          ASC_air +
          b_air_time_box_cox_business_0 * (business == 0) * ((time_air^L_time - 1) / L_time) +
          b_air_time_box_cox_business_1 * (business == 1) * ((time_air^L_time - 1) / L_time) +
          b_air_cost_box_cox_business_0 * (business == 0) * ((cost_air^L_cost - 1) / L_cost) +
          b_air_cost_box_cox_business_1 * (business == 1) * ((cost_air^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_air) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_air) +
          b_air_service_female_0 * (female == 0) * service_air +
          b_air_service_female_1 * (female == 1) * service_air
    
    V[["rail"]] <-
          ASC_rail +
          b_rail_time_box_cox_business_0 * (business == 0) * ((time_rail^L_time - 1) / L_time) +
          b_rail_time_box_cox_business_1 * (business == 1) * ((time_rail^L_time - 1) / L_time) +
          b_rail_cost_box_cox_business_0 * (business == 0) * ((cost_rail^L_cost - 1) / L_cost) +
          b_rail_cost_box_cox_business_1 * (business == 1) * ((cost_rail^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_rail) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_rail) +
          b_rail_service_female_0 * (female == 0) * service_rail +
          b_rail_service_female_1 * (female == 1) * service_rail
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
            



```python
from env.apollo.estimator import generate_apollo_r_script
current_path =  ''

code = generate_apollo_r_script(task, apollo_specification, output_directory= current_path, summary_file=current_path)

print(code)
```

    
        suppressMessages(library(apollo))
    
        apollo_initialise()
    
        apollo_control <- list(
            modelName="1110_2326_3326_4211_5000_6121_7000",
            modelDescr="MNL proposed by Delphos",
            indivID="id",
            outputDirectory="/Users/gnova/Developer/Delphos-core/tutorials"
        )
    
        database_1 <- read.csv("/Users/gnova/Developer/Delphos-core/dataset/dataset_1/2019_apollo_modechoice_formatted.csv", header=TRUE, sep=",")
        set.seed(123)
        individuals <- unique(database_1$id)
        n_individuals <- length(individuals)
        train_individuals <- sample(individuals, size=0.8*n_individuals)
        test_individuals <- setdiff(individuals,train_individuals)
        database_1$test <- ifelse(database_1$id %in% test_individuals, 1, 0)
        in_sample <- subset(database_1,test==0)
        database <- in_sample
    
        apollo_beta <- c("ASC_car"=0.0,
        "ASC_bus"=0.0,
        "ASC_air"=0.0,
        "ASC_rail"=0.0,
        "L_time"=1.0,
        "b_car_time_box_cox_business_0"=0.0,
        "b_car_time_box_cox_business_1"=0.0,
        "b_bus_time_box_cox_business_0"=0.0,
        "b_bus_time_box_cox_business_1"=0.0,
        "b_air_time_box_cox_business_0"=0.0,
        "b_air_time_box_cox_business_1"=0.0,
        "b_rail_time_box_cox_business_0"=0.0,
        "b_rail_time_box_cox_business_1"=0.0,
        "L_cost"=1.0,
        "b_car_cost_box_cox_business_0"=0.0,
        "b_car_cost_box_cox_business_1"=0.0,
        "b_bus_cost_box_cox_business_0"=0.0,
        "b_bus_cost_box_cox_business_1"=0.0,
        "b_air_cost_box_cox_business_0"=0.0,
        "b_air_cost_box_cox_business_1"=0.0,
        "b_rail_cost_box_cox_business_0"=0.0,
        "b_rail_cost_box_cox_business_1"=0.0,
        "b_access_generic_log_female_0"=0.0,
        "b_access_generic_log_female_1"=0.0,
        "b_air_service_female_0"=0.0,
        "b_air_service_female_1"=0.0,
        "b_rail_service_female_0"=0.0,
        "b_rail_service_female_1"=0.0)
        apollo_fixed <- c("ASC_rail")
    
        apollo_inputs <- apollo_validateInputs()
    
        
            apollo_probabilities <- function(apollo_beta, apollo_inputs, functionality = "estimate") {
    
                apollo_attach(apollo_beta, apollo_inputs)
                on.exit(apollo_detach(apollo_beta, apollo_inputs))
                P = list()
                V = list()
                V <- list()
    
    V[["car"]] <-
          ASC_car +
          b_car_time_box_cox_business_0 * (business == 0) * ((time_car^L_time - 1) / L_time) +
          b_car_time_box_cox_business_1 * (business == 1) * ((time_car^L_time - 1) / L_time) +
          b_car_cost_box_cox_business_0 * (business == 0) * ((cost_car^L_cost - 1) / L_cost) +
          b_car_cost_box_cox_business_1 * (business == 1) * ((cost_car^L_cost - 1) / L_cost)
    
    V[["bus"]] <-
          ASC_bus +
          b_bus_time_box_cox_business_0 * (business == 0) * ((time_bus^L_time - 1) / L_time) +
          b_bus_time_box_cox_business_1 * (business == 1) * ((time_bus^L_time - 1) / L_time) +
          b_bus_cost_box_cox_business_0 * (business == 0) * ((cost_bus^L_cost - 1) / L_cost) +
          b_bus_cost_box_cox_business_1 * (business == 1) * ((cost_bus^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_bus) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_bus)
    
    V[["air"]] <-
          ASC_air +
          b_air_time_box_cox_business_0 * (business == 0) * ((time_air^L_time - 1) / L_time) +
          b_air_time_box_cox_business_1 * (business == 1) * ((time_air^L_time - 1) / L_time) +
          b_air_cost_box_cox_business_0 * (business == 0) * ((cost_air^L_cost - 1) / L_cost) +
          b_air_cost_box_cox_business_1 * (business == 1) * ((cost_air^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_air) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_air) +
          b_air_service_female_0 * (female == 0) * service_air +
          b_air_service_female_1 * (female == 1) * service_air
    
    V[["rail"]] <-
          ASC_rail +
          b_rail_time_box_cox_business_0 * (business == 0) * ((time_rail^L_time - 1) / L_time) +
          b_rail_time_box_cox_business_1 * (business == 1) * ((time_rail^L_time - 1) / L_time) +
          b_rail_cost_box_cox_business_0 * (business == 0) * ((cost_rail^L_cost - 1) / L_cost) +
          b_rail_cost_box_cox_business_1 * (business == 1) * ((cost_rail^L_cost - 1) / L_cost) +
          b_access_generic_log_female_0 * (female == 0) * log(1+access_rail) +
          b_access_generic_log_female_1 * (female == 1) * log(1+access_rail) +
          b_rail_service_female_0 * (female == 0) * service_rail +
          b_rail_service_female_1 * (female == 1) * service_rail
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
            
    
    
        settings <- list(printLevel=0, writeIter=FALSE, silent=TRUE)
    
        model <- apollo_estimate(
            apollo_beta,
            apollo_fixed,
            apollo_probabilities,
            apollo_inputs,
            estimate_settings=settings
        )
    
        summary_df <- data.frame(
            specification="1110_2326_3326_4211_5000_6121_7000",
            numParams = model$numParams,
            numResids = model$numResids,
            maximum = model$maximum,
            vcHessianConditionNumber = model$vcHessianConditionNumber,
            successfulEstimation = model$successfulEstimation,
            LL0 = model$LL0,
            LLC = model$LLC,
            LLout = model$LLout,
            rho2_0 = model$rho2_0,
            adjRho2_0 = model$adjRho2_0,
            rho2_C = model$rho2_C,
            adjRho2_C = model$adjRho2_C,
            AIC = model$AIC,
            BIC = model$BIC,
            eigValue = model$eigValue[1],
            timeTaken = model$timeTaken,
            nFreeParams = model$nFreeParams
        )
    
        write.csv(summary_df, "/Users/gnova/Developer/Delphos-core/tutorials", row.names=FALSE)
        



```python


evaluate_specification(
    task,
    apollo_specification
    ) 

    #1110_2126_3122_4320_5000_6322_7000
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
      <td>1110_2326_3326_4211_5000_6121_7000</td>
      <td>27.0</td>
      <td>5600.0</td>
      <td>-4166.019859</td>
      <td>0.0</td>
      <td>0</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4166.019859</td>
      <td>0.369463</td>
      <td>0.365376</td>
      <td>0.232902</td>
      <td>0.228483</td>
      <td>8386.039718</td>
      <td>8565.063809</td>
      <td>-2.147484e+09</td>
      <td>4.239867</td>
      <td>27.0</td>
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
