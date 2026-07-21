# 05 - Reward function and model ranking

Delphos was trained with a reward function, and the final-user environment also computes a reward after Apollo estimation.

Important distinction:

- The pretrained agent policy is already fixed.
- Changing the Python reward function does not retrain the policy.
- You can still define custom scores to rank estimated proposals for your project.


## 1. Inspect the built-in reward on a synthetic outcome



```python
import pandas as pd
import delphos as dp
from delphos.env.reward import reward_function

task = dp.load_dataset("Swissmetro")

outcome = pd.DataFrame([
    {
        "successfulEstimation": 1,
        "skipped": 0,
        "LLout": task.ll_linear + 100.0,
        "nFreeParams": task.n_attributes + 2,
    }
])

reward_function(task, outcome)

```

## 2. See what invalid outcomes do

Failed, skipped, or incomplete Apollo runs receive `-1.0`.



```python
failed = pd.DataFrame([
    {"successfulEstimation": 0, "skipped": 0, "LLout": None, "nFreeParams": None}
])

skipped = pd.DataFrame([
    {"successfulEstimation": 0, "skipped": 1, "LLout": None, "nFreeParams": 80}
])

print("failed:", reward_function(task, failed))
print("skipped:", reward_function(task, skipped))

```

## 3. Build your own ranking score

This is useful after `estimate=True`, especially when you care about parsimony, interpretability, or a particular information criterion.



```python
import numpy as np

def custom_choice_model_score(row, task, complexity_penalty=0.02):
    if not bool(row.get("successfulEstimation", 0)):
        return -1.0
    ll_gain = (float(row["LLout"]) - float(task.ll_linear)) / float(task.n_obs)
    complexity = float(row.get("nFreeParams", 0)) / max(float(task.n_attributes), 1.0)
    return float(np.tanh(ll_gain) - complexity_penalty * complexity)

example_row = {
    "successfulEstimation": 1,
    "LLout": task.ll_linear + 150,
    "nFreeParams": 12,
}
custom_choice_model_score(example_row, task)

```

## 4. Apply a custom score to estimated results

Set `RUN_ESTIMATION = True` when you want to call Apollo/R. The default below is false so this notebook stays quick.



```python
RUN_ESTIMATION = False
agent = dp.load_agent()
models = agent.propose(task, n_models=5, strategy="topk", seed=123)

if RUN_ESTIMATION:
    models.estimate(task, max_free_parameters=30)
    df = models.to_dataframe()
    df["custom_score"] = df.apply(lambda row: custom_choice_model_score(row, task), axis=1)
    display(df.sort_values("custom_score", ascending=False))
else:
    print("Skipping Apollo/R estimation. Use models.estimate(...) when ready.")

```

## 5. Reward-design ideas for final users

You can rank estimated models by:

- log-likelihood improvement over linear additive baseline
- BIC or AIC improvement
- number of free parameters
- successful estimation and Hessian quality
- domain constraints such as sign plausibility
- preference for fewer covariate interactions

For final-user inference, use these scores for ranking and filtering. Retraining with a new reward belongs in the training repository, not this final-user package.

