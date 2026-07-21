# 08 - Environment, Apollo, caches, and outputs

This notebook explains what happens when Delphos estimates proposals.

The flow is:

1. Delphos proposes a specification.
2. The Apollo generator builds R code and parameter definitions.
3. `delphos.env.environment.evaluate_specification(...)` calls Apollo/R.
4. Results are converted to a dataframe.
5. The result cache stores outcomes by task and specification key.


## 1. Generate one proposal and inspect Apollo code



```python
import delphos as dp

agent = dp.load_agent()
task = dp.load_dataset("Swissmetro")
models = agent.propose(task, n_models=1, strategy="greedy")
proposal = models.proposals[0]
apollo_spec = proposal.apollo_specification

print("Specification:", proposal.specification_key)
print("Parameters:", apollo_spec.parameter_names[:15])
print()
print("Probability code preview:")
print()
print(apollo_spec.probability_code[:1500])

```

## 2. Direct environment call

This is what `estimate=True` uses internally. Keep `RUN_DIRECT_ESTIMATION = False` until R/Apollo are installed and you are ready to estimate.



```python
RUN_DIRECT_ESTIMATION = False

if RUN_DIRECT_ESTIMATION:
    from delphos.env.environment import evaluate_specification

    outcome = evaluate_specification(
        task=task,
        apollo_specification=apollo_spec,
        info=True,
        save=False,
        max_free_parameters=30,
    )
    display(outcome)
else:
    print("Skipping direct Apollo/R estimation.")

```

## 3. Result cache

The environment writes `rewards.sqlite` inside the dataset folder when you estimate. The cache avoids repeating the same Apollo run for the same task and specification key.



```python
from delphos.env.result_cache import ResultCache

cache = ResultCache(task.rewards_path)
print("Cache path:", cache.db_path)
print("Rows currently stored:", len(cache.load(task.name)))

```

## 4. Save Apollo output for final models

Use `save=True` only for the final shortlist. Apollo output files can be large, so the package ignores `dataset/**/outputs/` by default.



```python
RUN_SAVE_OUTPUT = False

if RUN_SAVE_OUTPUT:
    proposal_set = agent.propose(task, n_models=1, strategy="greedy")
    proposal_set.estimate(
        task,
        info=True,
        save=True,
        save_summary_file=True,
        max_free_parameters=40,
    )
    display(proposal_set.to_dataframe())
else:
    print("Skipping saved Apollo output.")

```

## 5. Debugging Apollo failures

For a problematic model, rerun with `debug_apollo=True`. Delphos writes generated beta names, fixed parameters, probability code, and an error file under a debug folder.



```python
RUN_DEBUG = False

if RUN_DEBUG:
    from pathlib import Path
    from delphos.env.environment import evaluate_specification

    debug_path = Path("tutorials/debug_apollo") / proposal.specification_key
    outcome = evaluate_specification(
        task=task,
        apollo_specification=apollo_spec,
        debug_apollo=True,
        debug_path=debug_path,
        raise_on_error=False,
    )
    print("Debug files:", list(debug_path.glob("*")))
    display(outcome)
else:
    print("Skipping debug run.")

```

## 6. Installation checklist

Python:

```bash
pip install -r requirements.txt
```

R:

```bash
Rscript install_r_requirements.R
```

If `rpy2` cannot find R, check that `R_HOME` points to your R installation. The package includes `delphos.env.apollo.r_env.configure_r_environment()` to discover common R locations.

