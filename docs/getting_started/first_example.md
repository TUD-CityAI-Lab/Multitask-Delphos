# First Example: End-to-End Walkthrough

In this guide, we'll walk through a complete example of using Delphos to assist in specifying a discrete choice model.

## 1. Preparation

First, ensure you have the `delphos` library installed and an R installation with Apollo configured. 
We will use one of the standard datasets from `delphos-datasets` (e.g., Swissmetro).

## 2. Initialize the Agent

We start by loading a pre-trained agent.

```python
from delphos import DelphosAgent
from delphos.datasets import load_swissmetro

agent = DelphosAgent.load_pretrained("multitask_base")
data, schema = load_swissmetro()
```

## 3. Run Inference

We ask Delphos to explore the specification space. It will propose utility functions, estimate them using the Apollo backend, and observe the rewards (AIC/BIC improvements).

```python
results = agent.explore(
    dataset=data,
    schema=schema,
    steps=50 # Number of exploration steps
)
```

## 4. Inspecting the Pareto Front

Delphos maintains a Pareto front of the best models found during exploration, balancing model complexity and Goodness-of-Fit.

```python
pareto = results.get_pareto_front()
best_model = pareto.get_best_by_metric("BIC")

print(best_model.utility_equations)
```

## 5. Export to Apollo

Once you find a specification you like, you can easily export it to an Apollo R script for final reporting and analysis.

```python
best_model.export_to_apollo("swissmetro_final.R")
```

You can now run `Rscript swissmetro_final.R` to get the full Apollo output!
