# Quickstart

If you just want to see Delphos in action as quickly as possible, here is the minimal code required to load a pre-trained agent and generate specifications for a dataset.

## The Minimal Example

```python
import pandas as pd
from delphos import DelphosAgent, DatasetSchema

# 1. Load your dataset and schema
dataset = pd.read_csv("my_transport_data.csv")
schema = DatasetSchema.from_json("schema.json")

# 2. Load the pre-trained agent
agent = DelphosAgent.load_pretrained("multitask_v1")

# 3. Generate specifications
pareto_front = agent.generate_specifications(
    dataset=dataset,
    schema=schema,
    n_specs=10
)

# 4. View results
print(pareto_front.summary())
```
