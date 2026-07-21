# 07 - Robust and best results over a long run

This notebook gives a 24-hour style recipe. It is designed to be resumable: every batch writes a CSV, and duplicate specification keys are removed at the end.

By default, `RUN_LONG = False` so running the notebook will not start a long experiment accidentally.


## 1. Configure the long run



```python
from pathlib import Path
from time import monotonic
import pandas as pd
import delphos as dp

RUN_LONG = False
HOURS = 24
RUN_DIR = Path("tutorials/robust_run")
RUN_DIR.mkdir(parents=True, exist_ok=True)

agent = dp.load_agent()
task = dp.load_dataset("Swissmetro")

```

## 2. Use a broader but still interpretable space

Add a few covariates only after the quick run behaves well.



```python
robust_task = dp.configure_modelling_space(
    task,
    transformations=["linear", "log", "box_cox"],
    tastes=["generic", "specific"],
    covariates=["income", "purpose", "age"],
)

# Optionally collapse levels to keep parameter counts manageable.
robust_task = dp.set_covariate_levels(
    robust_task,
    income=[1, 2, 3, 4],
    purpose=[1, 2],
)

print("Covariates:", [(cov.name, cov.levels) for cov in robust_task.modelling_covariates])

```

## 3. Define a strategy schedule

A robust run should mix high-confidence search with exploratory search.



```python
strategy_schedule = [
    {"strategy": "greedy", "n_models": 1, "max_attempts": 1},
    {"strategy": "topk", "n_models": 50, "max_attempts": 500, "top_k": 5, "temperature": 0.8},
    {"strategy": "topk", "n_models": 50, "max_attempts": 500, "top_k": 10, "temperature": 1.0},
    {"strategy": "boltzmann", "n_models": 50, "max_attempts": 500, "temperature": 1.2},
    {"strategy": "stochastic", "n_models": 50, "max_attempts": 500, "epsilon": 0.15},
]
strategy_schedule

```

## 4. Long-running loop

This loop estimates as it goes. If you prefer to inspect before estimating, set `estimate=False`, save proposals, then estimate selected proposals later.



```python
def run_batch(batch_id, settings):
    models = agent.propose(
        robust_task,
        horizon_kappa=2.5,
        seed=10_000 + batch_id,
        estimate=True,
        estimate_kwargs={
            "max_free_parameters": 40,
            "info": False,
            "save": False,
        },
        **settings,
    )
    df = models.to_dataframe()
    df["batch_id"] = batch_id
    df.to_csv(RUN_DIR / f"batch_{batch_id:04d}.csv", index=False)
    return df

if RUN_LONG:
    deadline = monotonic() + HOURS * 60 * 60
    batch_id = 0
    while monotonic() < deadline:
        settings = strategy_schedule[batch_id % len(strategy_schedule)]
        print(f"Running batch {batch_id}: {settings}")
        run_batch(batch_id, settings)
        batch_id += 1
else:
    print("RUN_LONG is False. Set it to True to start the long run.")

```

## 5. Resume and aggregate results

Run this cell any time to combine completed batches.



```python
batch_files = sorted(RUN_DIR.glob("batch_*.csv"))
if batch_files:
    combined = pd.concat([pd.read_csv(path) for path in batch_files], ignore_index=True)
    combined = combined.drop_duplicates("specification_key")
    combined = combined.sort_values(["reward", "LLout"], ascending=[False, False], na_position="last")
    combined.to_csv(RUN_DIR / "combined_results.csv", index=False)
    display(combined.head(20))
else:
    print("No batch files yet.")

```

## 6. Best-practice checklist

- Keep all batch CSVs.
- Use multiple strategies, not only greedy.
- Cap free parameters early, then relax later.
- Deduplicate by `specification_key`.
- Inspect estimation failures separately.
- Re-estimate the best few models with saved Apollo output enabled.
- Keep a written record of modelling-space restrictions used for the run.

