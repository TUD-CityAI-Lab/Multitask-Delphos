# 04 - Delphos search parameters

This notebook explains the knobs in `agent.propose(...)` and when to use them.


## Main parameters

| Parameter | Meaning | Practical use |
| --- | --- | --- |
| `n_models` | Number of unique model specifications to return | Increase for broader search |
| `max_attempts` | Maximum search attempts before stopping | Increase when duplicates are common |
| `strategy` | `greedy`, `stochastic`, `boltzmann`, or `topk` | Controls exploration |
| `epsilon` | Random-action probability for stochastic search | Higher means more random exploration |
| `temperature` | Softmax temperature for boltzmann/top-k sampling | Higher means more diversity |
| `top_k` | Candidate action pool for top-k search | Higher means broader local search |
| `horizon_kappa` | Search depth multiplier over attributes | Higher allows longer model edits |
| `linear_additive` | Start from a linear additive model | Set false to start from null model |
| `estimate` | Call Apollo/R environment | Use after proposal settings look good |
| `seed` | Reproducible stochastic search | Use for reports and comparisons |


## 1. Load baseline objects



```python
import delphos as dp

agent = dp.load_agent(device="cpu")
task = dp.load_dataset("Swissmetro")

```

## 2. Greedy search

Greedy is deterministic and useful as a baseline. It usually returns one dominant path.



```python
greedy = agent.propose(
    task,
    n_models=1,
    strategy="greedy",
)
greedy.to_dataframe()

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2212_3210_4214_5000_6110_7000</td>
      <td>10</td>
      <td>greedy</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 17, 201, 125, 21, 215, 17, 27, 201, 73]</td>
    </tr>
  </tbody>
</table>
</div>



## 3. Top-k search

Top-k is a good default for final users: it stays near high-value actions while still producing diverse models.



```python
topk = agent.propose(
    task,
    n_models=5,
    max_attempts=80,
    strategy="topk",
    top_k=5,
    temperature=0.8,
    seed=42,
)
topk.to_dataframe()

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2124_3212_4111_5000_6126_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[21, 27, 17, 125, 74, 215, 27, 21, 75, 106]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2124_3211_4214_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[17, 125, 21, 73, 27, 17, 74, 149, 21, 125]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2124_3210_4110_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 27, 21, 106, 17, 74, 105, 73, 201, 21]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3212_4214_5000_6110_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>3</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 74, 201, 73, 21, 125, 74, 75, 27, 17]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3210_4111_5000_6126_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>4</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[17, 73, 125, 149, 27, 106, 17, 21, 215, 17]</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Boltzmann search

Boltzmann samples from all valid actions after weighting by Q-value. Increase temperature for more exploration.



```python
boltzmann = agent.propose(
    task,
    n_models=5,
    max_attempts=80,
    strategy="boltzmann",
    temperature=1.2,
    seed=43,
)
boltzmann.to_dataframe()

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2210_3312_4211_5000_6314_7000</td>
      <td>10</td>
      <td>boltzmann</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[26, 225, 50, 19, 91, 45, 237, 123, 122, 25]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3314_4110_5000_6211_7000</td>
      <td>10</td>
      <td>boltzmann</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[37, 21, 42, 239, 21, 17, 71, 218, 75, 93]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2313_3213_4124_5000_6116_7000</td>
      <td>10</td>
      <td>boltzmann</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[137, 12, 81, 207, 11, 13, 91, 44, 117, 76]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2220_3314_4113_5000_6112_7000</td>
      <td>10</td>
      <td>boltzmann</td>
      <td>3</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[17, 205, 119, 108, 41, 209, 92, 93, 33, 203]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1114_2121_3310_4120_5000_6313_7000</td>
      <td>10</td>
      <td>boltzmann</td>
      <td>4</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[58, 18, 91, 140, 92, 131, 113, 236, 5, 89]</td>
    </tr>
  </tbody>
</table>
</div>



## 5. Stochastic search

Stochastic search is epsilon-greedy. It is useful for stress-testing the action space.



```python
stochastic = agent.propose(
    task,
    n_models=5,
    max_attempts=80,
    strategy="stochastic",
    epsilon=0.15,
    seed=44,
)
stochastic.to_dataframe()

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3212_4110_5000_6126_7000</td>
      <td>10</td>
      <td>stochastic</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 82, 201, 17, 215, 27, 201, 75, 17, 215]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2212_3322_4214_5000_6126_7000</td>
      <td>10</td>
      <td>stochastic</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 17, 201, 125, 21, 215, 17, 27, 101, 99]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2212_3110_4214_5000_6110_7000</td>
      <td>10</td>
      <td>stochastic</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 17, 201, 125, 21, 42, 215, 17, 27, 201]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2212_3210_4110_5000_6126_7000</td>
      <td>10</td>
      <td>stochastic</td>
      <td>3</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 17, 201, 210, 27, 201, 73, 17, 215, 27]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1110_2120_3114_4110_5000_6110_7000</td>
      <td>10</td>
      <td>stochastic</td>
      <td>4</td>
      <td>False</td>
      <td>None</td>
      <td>5</td>
      <td>[215, 17, 58, 201, 21, 215, 27, 61, 201, 17]</td>
    </tr>
  </tbody>
</table>
</div>



## 6. Search depth

`horizon_kappa` multiplies the number of task attributes to set a maximum number of actions. Larger values allow more edits but may create more complex specifications.



```python
shallow = agent.propose(task, n_models=3, strategy="topk", horizon_kappa=1.0, seed=45)
deep = agent.propose(task, n_models=3, strategy="topk", horizon_kappa=3.0, seed=45)

print("Shallow episode lengths:", shallow.to_dataframe()["episode_length"].tolist())
print("Deep episode lengths:", deep.to_dataframe()["episode_length"].tolist())

```

    Shallow episode lengths: [5, 5, 5]
    Deep episode lengths: [15, 15, 15]


## 7. Start from null instead of linear additive

The default workflow starts from a linear additive specification. Set `linear_additive=False` when you want Delphos to build up from an empty model.



```python
from_null = agent.propose(
    task,
    n_models=3,
    strategy="topk",
    linear_additive=False,
    seed=46,
)
from_null.to_dataframe()

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1000_2000_3000_4000_5000_6220_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1</td>
      <td>[6, 224, 210, 211, 218, 252, 220, 209, 219, 232]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1000_2110_3000_4000_5000_6121_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>2</td>
      <td>[6, 210, 225, 218, 226, 219, 211, 252, 217, 2]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Swissmetro</td>
      <td>1000_2000_3000_4326_5000_6000_7000</td>
      <td>10</td>
      <td>topk</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>1</td>
      <td>[4, 131, 126, 136, 138, 122, 124, 121, 142, 158]</td>
    </tr>
  </tbody>
</table>
</div>



## 8. Custom checkpoints

The default checkpoint is bundled. Advanced users can pass another checkpoint trained elsewhere.



```python
# custom_agent = dp.load_agent("/path/to/latest_checkpoint.pt", device="cpu")
# custom_models = custom_agent.propose(task, n_models=10)

```
