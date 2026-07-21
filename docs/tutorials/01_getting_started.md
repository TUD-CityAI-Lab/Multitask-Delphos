# 01 - Getting started with Delphos

This notebook is the shortest path from a trained Delphos checkpoint to candidate choice-model specifications.

You will learn how to:

- list datasets
- load the pretrained Delphos agent
- propose and estimate models
- inspect terms, parameters, and generated Apollo code
- save a proposal table for later review


## 1. Import Delphos



```python
import delphos as dp

print("Delphos is ready")

```

    Delphos is ready


## 2. See datasets

The package ships with example datasets that are already mapped to the trained Delphos catalogue.



```python
datasets = dp.list_datasets()
for item in datasets:
    print(f"{item.id:>2} | {item.name:<24} | {item.folder}")

# training and inference datasets (inference_datasets())
# Swissmetro wasnt used for training, so we will apply Delphos on Swissmtro

```

     1 | ApolloModeChoice         | dataset_1
     2 | SwissmetroRouteChoice    | dataset_2
     3 | Decisions                | dataset_3
     4 | Swissmetro               | dataset_4
     5 | NLModeChoice             | dataset_5
     6 | NorwayVTT                | dataset_6
     7 | Arentze2013              | dataset_7
     8 | SpainParkingchoice       | dataset_8
     9 | LondonModeChoice         | dataset_9
    10 | Optima                   | dataset_10
    11 | VanCranenburghVOT        | dataset_11


## 3. Load unseen dataset and the trained agent

The default checkpoint is the production multitask checkpoint included in `checkpoints/full_agent_task_10_seed_123`.



```python

dataset = dp.load_dataset("Swissmetro")

agent = dp.load_agent()

print(dataset)
print(agent.agent.summary())

```

    Task(name='Swissmetro', alternatives=3, attributes=5, covariates=11)
    {'agent': 'DelphosAgent', 'mode': 'inference', 'encoder_kind': 'deepset', 'state_dim': 64, 'num_actions': 297, 'z_cfg': {'K': 7, 'T': 3, 'G': 2, 'C': 7, 'd_att': 16, 'd_tr': 8, 'd_taste': 8, 'd_cov': 16, 'd_term': 64, 'd_state': 128, 'context_dim': 0, 'head_flag': False, 'pooling': 'mean', 'attention_heads': 4, 'attention_layers': 1, 'attention_dropout': 0.0}, 'device': 'cpu'}


## 4. Propose models without estimation

`estimate=False` is the default. This is fast because Delphos only searches the modelling space and builds Apollo-ready specifications. It does not call R.



```python
models = agent.propose(
    dataset,
    n_models=5,
    estimate=True
)

models.to_dataframe()
# do not show the 

```

    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.





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
      <th>task_id</th>
      <th>task_name</th>
      <th>specification_key</th>
      <th>episode_length</th>
      <th>search_strategy</th>
      <th>attempt_found</th>
      <th>estimated</th>
      <th>reward</th>
      <th>n_terms</th>
      <th>action_indices</th>
      <th>...</th>
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
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2124_3212_4110_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>0</td>
      <td>True</td>
      <td>0.080552</td>
      <td>5</td>
      <td>[125, 17, 215, 27, 74, 75, 106, 105, 201, 21]</td>
      <td>...</td>
      <td>0.266062</td>
      <td>0.264052</td>
      <td>0.128452</td>
      <td>0.126406</td>
      <td>10251.258636</td>
      <td>10346.738089</td>
      <td>-7.165797</td>
      <td>1.132897</td>
      <td>14</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2212_3212_4324_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>1</td>
      <td>True</td>
      <td>0.096403</td>
      <td>5</td>
      <td>[215, 74, 21, 106, 201, 27, 75, 215, 149, 201]</td>
      <td>...</td>
      <td>0.278470</td>
      <td>0.276173</td>
      <td>0.143186</td>
      <td>0.140799</td>
      <td>10082.426811</td>
      <td>10191.546185</td>
      <td>-1.686022</td>
      <td>1.417425</td>
      <td>16</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2124_3210_4214_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>2</td>
      <td>True</td>
      <td>0.077291</td>
      <td>5</td>
      <td>[21, 125, 17, 215, 27, 201, 106, 73, 21, 125]</td>
      <td>...</td>
      <td>0.263514</td>
      <td>0.261791</td>
      <td>0.125426</td>
      <td>0.123721</td>
      <td>10282.754558</td>
      <td>10364.594089</td>
      <td>-9.808499</td>
      <td>0.697092</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2121_3212_4111_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>3</td>
      <td>True</td>
      <td>0.082602</td>
      <td>5</td>
      <td>[21, 125, 106, 17, 215, 21, 27, 18, 201, 75]</td>
      <td>...</td>
      <td>0.267665</td>
      <td>0.265511</td>
      <td>0.130355</td>
      <td>0.128138</td>
      <td>10230.934350</td>
      <td>10333.233764</td>
      <td>-7.155435</td>
      <td>2.857019</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2212_3210_4222_5000_6126_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>4</td>
      <td>True</td>
      <td>0.097835</td>
      <td>5</td>
      <td>[73, 27, 17, 21, 215, 106, 17, 27, 149, 131]</td>
      <td>...</td>
      <td>0.279593</td>
      <td>0.277152</td>
      <td>0.144519</td>
      <td>0.141962</td>
      <td>10068.785960</td>
      <td>10184.725296</td>
      <td>-1.118034</td>
      <td>1.279611</td>
      <td>17</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
</div>



## 5. Inspect the first proposal

Motivation -> specify the goal. LL and BIC



```python
proposal = models.proposals[0]

print("Specification key:", proposal.specification_key)
print("Episode length:", proposal.episode_length)
print("Action indices:", proposal.action_indices)
print("Terms:")
for term in proposal.terms:
    print(term)

```

    Specification key: 1110_2124_3212_4110_5000_6110_7000
    Episode length: 10
    Action indices: [125, 17, 215, 27, 74, 75, 106, 105, 201, 21]
    Terms:
    Term(attribute_id=1, transform_id=1, taste_id=1, covariate_id=0)
    Term(attribute_id=2, transform_id=1, taste_id=2, covariate_id=4)
    Term(attribute_id=3, transform_id=2, taste_id=1, covariate_id=2)
    Term(attribute_id=4, transform_id=1, taste_id=1, covariate_id=0)
    Term(attribute_id=6, transform_id=1, taste_id=1, covariate_id=0)


## 6. Inspect generated Apollo components

These objects are what Delphos sends to the environment when `estimate=True`.



```python
apollo_spec = proposal.apollo_specification

print("Number of parameters:", apollo_spec.n_parameters)
print("First parameters:", apollo_spec.parameter_names[:10])
print()
print("Utility code preview:")
print()
print(apollo_spec.utility_code)

```

    Number of parameters: 16
    First parameters: ['ASC_TRAIN', 'ASC_SM', 'ASC_CAR', 'b_TRAIN_time', 'b_SM_time', 'b_CAR_time', 'b_cost_generic_log_income_1', 'b_cost_generic_log_income_2', 'b_cost_generic_log_income_3', 'b_cost_generic_log_income_4']
    
    Utility code preview:
    
    V <- list()
    
    V[["TRAIN"]] <-
          ASC_TRAIN +
          b_TRAIN_time * train_tt_scaled +
          b_cost_generic_log_income_1 * (income == 1) * log(1+train_cost_scaled) +
          b_cost_generic_log_income_2 * (income == 2) * log(1+train_cost_scaled) +
          b_cost_generic_log_income_3 * (income == 3) * log(1+train_cost_scaled) +
          b_cost_generic_log_income_4 * (income == 4) * log(1+train_cost_scaled) +
          b_TRAIN_headway_box_cox_purpose_1 * (purpose == 1) * ((train_he_scaled^L_headway - 1) / L_headway) +
          b_TRAIN_headway_box_cox_purpose_2 * (purpose == 2) * ((train_he_scaled^L_headway - 1) / L_headway)
    
    V[["SM"]] <-
          ASC_SM +
          b_SM_time * sm_tt_scaled +
          b_cost_generic_log_income_1 * (income == 1) * log(1+sm_cost_scaled) +
          b_cost_generic_log_income_2 * (income == 2) * log(1+sm_cost_scaled) +
          b_cost_generic_log_income_3 * (income == 3) * log(1+sm_cost_scaled) +
          b_cost_generic_log_income_4 * (income == 4) * log(1+sm_cost_scaled) +
          b_SM_headway_box_cox_purpose_1 * (purpose == 1) * ((sm_he_scaled^L_headway - 1) / L_headway) +
          b_SM_headway_box_cox_purpose_2 * (purpose == 2) * ((sm_he_scaled^L_headway - 1) / L_headway) +
          b_seat_generic * sm_seats_scaled
    
    V[["CAR"]] <-
          ASC_CAR +
          b_CAR_time * car_tt_scaled +
          b_cost_generic_log_income_1 * (income == 1) * log(1+car_co_scaled) +
          b_cost_generic_log_income_2 * (income == 2) * log(1+car_co_scaled) +
          b_cost_generic_log_income_3 * (income == 3) * log(1+car_co_scaled) +
          b_cost_generic_log_income_4 * (income == 4) * log(1+car_co_scaled)


## 7. Save proposals

This is a useful pattern when you want to inspect models first, then estimate them later.



```python
output_path = "getting_started_proposals.csv"
models.to_dataframe().to_csv(output_path, index=False)
print(f"Saved {len(models)} proposals to {output_path}")

```

    Saved 5 proposals to getting_started_proposals.csv

