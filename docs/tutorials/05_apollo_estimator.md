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
from mdp.action import *
from env.apollo.generator import ApolloGenerator
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

```python
from env.apollo.estimator import apollo_info
from env.apollo.estimator import run_apollo_estimation

apollo_info()
```

    {'r_version': 'R version 4.5.1 (2025-06-13)',
     'r_home': '/Library/Frameworks/R.framework/Resources/R',
     'libpaths': ['/Users/gnova/Library/R/arm64/4.5/library',
      '/Library/Frameworks/R.framework/Versions/4.5-arm64/Resources/library'],
     'apollo_installed': True,
     'apollo_loaded': False,
     'apollo_ready': False}

1. Linear additive

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
specification = action_space.create_initial_specification()
backend_specification = specification_manager.to_backend(specification)
apollo_specification = generator.build_apollo_specification(backend_specification)

results = run_apollo_estimation(task, apollo_specification, output_directory=Path("./outputs"), info=True)
```

    Apollo ignition sequence completed
    2026-06-03 12:21:21,430 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2110_3110_4110_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com

    Model name                                  : 1110_2110_3110_4110_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-06-03 12:21:21.493206
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -25.901553
         reciprocal of condition number         : 5.79547e-07
    Number of individuals                       : 400
    Number of rows in database                  : 5600
    Number of modelled outcomes                 : 5600

    Number of cores used                        :  1
    Model without mixing

    LL(start)                                   : -6607.09
    LL at equal shares, LL(0)                   : -6607.09
    LL at observed shares, LL(C)                : -5430.89
    LL(final)                                   : -4670.99
    Rho-squared vs equal shares                  :  0.293
    Adj.Rho-squared vs equal shares              :  0.292
    Rho-squared vs observed shares               :  0.1399
    Adj.Rho-squared vs observed shares           :  0.1392
    AIC                                         :  9355.98
    BIC                                         :  9402.39

    Estimated parameters                        : 7
    Time taken (hh:mm:ss)                       :  00:00:0.49
         pre-estimation                         :  00:00:0.21
         estimation                             :  00:00:0.07
         post-estimation                        :  00:00:0.21
    Iterations                                  :  9

    Unconstrained optimisation.

    Estimates:
                         Estimate        s.e.   t.rat.(0)    Rob.s.e. Rob.t.rat.(0)
    ASC_car               0.54624    0.123957       4.407    0.133607         4.088
    ASC_bus              -1.47293    0.153407      -9.601    0.172698        -8.529
    ASC_air               0.32776    0.107392       3.052    0.119419         2.745
    ASC_rail              0.00000          NA          NA          NA            NA
    b_time_generic       -0.01035  5.9618e-04     -17.362  6.4412e-04       -16.070
    b_cost_generic       -0.05536    0.001587     -34.896    0.001948       -28.427
    b_access_generic     -0.01956    0.002771      -7.059    0.002869        -6.820
    b_service_generic     0.18133    0.027893       6.501    0.026975         6.722

```python
specification_2 = action_space.create_initial_specification()
specification_2, _ = action_space.apply_action(specification_2, action_index=3)

backend_specification_2 = specification_manager.to_backend(specification_2)
apollo_specification_2 = generator.build_apollo_specification(backend_specification_2)



results = run_apollo_estimation(task, apollo_specification_2, output_directory=Path("./outputs"), info=True)

```

    2026-06-03 12:22:16,917 [INFO] Delphos.apollo: Starting Apollo estimation: 1112_2110_3110_4110_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com

    Model name                                  : 1112_2110_3110_4110_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-06-03 12:22:16.952767
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -6.232372
         reciprocal of condition number         : 1.42808e-07
    Number of individuals                       : 400
    Number of rows in database                  : 5600
    Number of modelled outcomes                 : 5600

    Number of cores used                        :  1
    Model without mixing

    LL(start)                                   : -6607.09
    LL at equal shares, LL(0)                   : -6607.09
    LL at observed shares, LL(C)                : -5430.89
    LL(final)                                   : -4554.37
    Rho-squared vs equal shares                  :  0.3107
    Adj.Rho-squared vs equal shares              :  0.3083
    Rho-squared vs observed shares               :  0.1614
    Adj.Rho-squared vs observed shares           :  0.159
    AIC                                         :  9140.74
    BIC                                         :  9246.83

    Estimated parameters                        : 16
    Time taken (hh:mm:ss)                       :  00:00:0.89
         pre-estimation                         :  00:00:0.09
         estimation                             :  00:00:0.1
         post-estimation                        :  00:00:0.69
    Iterations                                  :  10

    Unconstrained optimisation.

    Estimates:
                         Estimate        s.e.   t.rat.(0)    Rob.s.e. Rob.t.rat.(0)
    ASC_car_income_1      0.90387    0.140752      6.4217    0.156224        5.7857
    ASC_car_income_2      0.74704    0.143879      5.1922    0.159046        4.6970
    ASC_car_income_3      0.30417    0.140976      2.1576    0.173668        1.7515
    ASC_car_income_4      0.34375    0.140415      2.4481    0.159469        2.1556
    ASC_bus_income_1     -0.55237    0.174510     -3.1653    0.212535       -2.5990
    ASC_bus_income_2     -1.37272    0.190187     -7.2178    0.227283       -6.0397
    ASC_bus_income_3     -2.24625    0.222305    -10.1043    0.274287       -8.1894
    ASC_bus_income_4     -2.34079    0.228997    -10.2219    0.270069       -8.6674
    ASC_air_income_1      0.05081    0.132066      0.3848    0.160835        0.3159
    ASC_air_income_2      0.28631    0.135226      2.1173    0.147495        1.9412
    ASC_air_income_3      0.45062    0.130468      3.4539    0.160362        2.8100
    ASC_air_income_4      0.65158    0.130995      4.9741    0.163511        3.9849
    ASC_rail_income_1     0.00000          NA          NA          NA            NA
    ASC_rail_income_2     0.00000          NA          NA          NA            NA
    ASC_rail_income_3     0.00000          NA          NA          NA            NA
    ASC_rail_income_4     0.00000          NA          NA          NA            NA
    b_time_generic       -0.01064  6.0321e-04    -17.6467  6.4463e-04      -16.5130
    b_cost_generic       -0.05685    0.001622    -35.0447    0.002041      -27.8483
    b_access_generic     -0.02011    0.002810     -7.1573    0.002899       -6.9367
    b_service_generic     0.18294    0.028208      6.4853    0.027679        6.6092
