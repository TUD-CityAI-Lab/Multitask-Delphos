# Zero-Shot Inference

Zero-shot inference is the process of taking a Delphos agent that was trained on a set of source datasets and applying it directly to a completely new, unseen dataset.

Because Delphos learns abstract modelling strategies (e.g., "try adding a non-linear transform to continuous variables") rather than dataset-specific heuristics, it can generalize well to new data.

## Running Zero-Shot Inference

```python
from delphos import DelphosAgent, DatasetSchema

# Load a generic multitask agent
agent = DelphosAgent.load_pretrained("multitask_base")

# Load your new dataset
schema = DatasetSchema.from_json("my_dataset_schema.json")

# The agent explores the new dataset without any parameter updates
pareto_front = agent.explore(
    dataset_path="my_dataset.csv",
    schema=schema,
    steps=100
)

print(pareto_front.get_best_by_metric("BIC"))
```

In zero-shot mode, the neural network weights of the agent are frozen. It simply uses its learned policy to navigate the specification space for the new dataset.
