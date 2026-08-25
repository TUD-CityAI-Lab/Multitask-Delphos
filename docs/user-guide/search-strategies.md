# Search Strategies and Parameters

Delphos converts policy-network scores into modelling actions. The search strategy controls how strongly the generated specifications follow the highest-scoring actions and how much diversity is introduced.

## Available strategies

| Strategy | Behaviour | Useful for |
| --- | --- | --- |
| `greedy` | Always selects the highest-valued valid action | Reproducible baseline and policy inspection |
| `topk` | Samples among the `k` highest-valued valid actions | Default balance between quality and diversity |
| `stochastic` | Uses epsilon-greedy exploration | Broader searches with a clear random-exploration rate |
| `boltzmann` | Samples from a temperature-scaled score distribution | Smooth control of policy concentration |

## A practical default

```python
proposals = model.propose(
    task,
    n_models=25,
    max_attempts=250,
    strategy="topk",
    top_k=5,
    temperature=1.0,
    horizon_kappa=2.0,
    linear_additive=True,
    seed=123,
)
```

The key parameters are:

- `n_models`: number of unique specifications requested;
- `max_attempts`: maximum generation attempts, including duplicates;
- `top_k`: number of high-valued actions available to top-k sampling;
- `epsilon`: random-action probability for stochastic search;
- `temperature`: concentration of top-k or Boltzmann sampling;
- `horizon_kappa`: action horizon relative to the number of attributes; and
- `linear_additive`: whether the search starts from a linear-additive specification rather than an empty one.

## Quick diagnostic run

```python
quick = model.propose(
    task,
    n_models=5,
    max_attempts=50,
    strategy="greedy",
    horizon_kappa=1.0,
    seed=123,
)
```

Use this to confirm that the task, checkpoint, and generated Apollo code behave as expected.

## Diverse proposal run

```python
diverse = model.propose(
    task,
    n_models=100,
    max_attempts=1500,
    strategy="topk",
    top_k=10,
    temperature=1.5,
    horizon_kappa=2.5,
    seed=123,
)
```

Increasing the budget does not guarantee more useful models. Monitor duplicates, term counts, and the composition of proposals. If the same structures dominate, adjust the modelling space before increasing `max_attempts` further.

## Reproducibility

Always record the checkpoint, task schema, modelling-space restrictions, search parameters, and random seed. A seed makes a run repeatable only when the software versions and input artefacts are also unchanged.

The [Robust Results notebook](../tutorials/end-user/07_robust_results.ipynb) demonstrates a longer, resumable strategy schedule.
