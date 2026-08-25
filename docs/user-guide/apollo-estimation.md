# Estimate with Apollo

Delphos uses Apollo as the estimation environment. It generates the R objects required for an MNL specification, sends them to Apollo through `rpy2`, and converts the model summary into a pandas dataframe.

## Inspect before estimating

```python
proposal = proposals.proposals[0]
apollo_spec = proposal.apollo_specification

print(apollo_spec.parameter_names)
print(apollo_spec.utility_code)
print(apollo_spec.probability_code)
```

Check the utility functions, availability mapping, fixed parameters, reference alternative, variable scaling, and transformations exactly as you would in an Apollo script.

## Estimate an existing proposal set

```python
proposals.estimate(
    task,
    info=True,
    save=False,
    save_summary_file=False,
    max_free_parameters=30,
)
```

This two-stage approach is recommended because you can inspect and filter the proposals before Apollo is called.

Alternatively, estimate during generation:

```python
proposals = model.propose(
    task,
    n_models=5,
    estimate=True,
    estimate_kwargs={
        "info": True,
        "max_free_parameters": 30,
    },
    seed=123,
)
```

## Save Apollo output selectively

Apollo output can become large. Once the current `ProposalSet` contains only the candidates you want to preserve, save their complete outputs:

```python
proposals.estimate(
    task,
    info=True,
    save=True,
    save_summary_file=True,
    max_free_parameters=40,
)
```

Apollo files are written under the task's `outputs/` directory. Summary rows are also stored in the task's SQLite result cache.

## Debug a failed model

```python
from pathlib import Path
from delphos.env.environment import evaluate_specification

debug_path = Path("debug_apollo") / proposal.specification_key

outcome = evaluate_specification(
    task=task,
    apollo_specification=apollo_spec,
    debug_apollo=True,
    debug_path=debug_path,
    raise_on_error=False,
)
```

The debug directory records generated beta names, fixed parameters, probability code, and the captured error when available.

## Read failures as modelling information

A failed estimation is not only a software problem. Common causes include:

- unavailable or incorrectly scaled variables;
- a transformation outside its valid domain;
- unidentified generic or alternative-specific parameters;
- empty interaction levels;
- excessive parameter counts; and
- a singular or ill-conditioned Hessian.

Correct the data or modelling space rather than repeatedly increasing the search budget.

## Apollo and Biogeme terminology

| Delphos object | Apollo view | Biogeme view |
| --- | --- | --- |
| `Task` | Database, alternatives, availabilities, utility inputs | Database plus modelling-expression catalogue |
| `ApolloSpecification.parameters` | `apollo_beta` and `apollo_fixed` | `Beta` expressions and fixed-status definitions |
| `utility_code` | `V <- list(...)` | Utility-expression dictionary |
| `probability_code` | `apollo_probabilities` | `loglogit`/probability expression |
| `ProposalSet.to_dataframe()` | Compact model-output comparison | Compiled estimation-results table |

For a detailed walkthrough, open [Apollo and Outputs](../tutorials/end-user/08_environment_and_outputs.ipynb).
