# Dataset Usage

To use the datasets in `delphos-datasets` with the `delphos` Python package, you can use the built-in dataset loaders.

These loaders automatically fetch the dataset and its corresponding schema, returning them in a format ready for the Delphos agent.

## Available Loaders

```python
from delphos.datasets import (
    load_swissmetro,
    load_apollo_modechoice,
    load_optima
)

# Example: Loading Swissmetro
dataset_df, schema = load_swissmetro()

print(dataset_df.head())
print(schema.get_variables())
```

These loaders ensure that the data types and column names match exactly what the agent expects based on the schema.
