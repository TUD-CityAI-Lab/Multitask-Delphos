# Adding a custom dataset

You can easily use Delphos with your own datasets. You do not need to add them to `delphos-datasets` unless you want to contribute them to the project.

To use a custom dataset:

1. Prepare your data as a CSV file.
2. Write a JSON schema following the format described in [Dataset Format](dataset_format.md).
3. Load them into Delphos.

```python
import pandas as pd
from delphos import DatasetSchema, DelphosAgent

# Load your custom data
my_data = pd.read_csv("path/to/my_data.csv")

# Load your custom schema
my_schema = DatasetSchema.from_json("path/to/my_schema.json")

# Run inference
agent = DelphosAgent.load_pretrained("multitask_base")
pareto = agent.explore(my_data, my_schema)
```
