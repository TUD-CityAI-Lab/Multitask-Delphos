# Dataset Format

To use your own dataset with Delphos, you need to provide a dataset in the correct format, as well as its dataset schema in a .yaml file.

## Dataset schema

A valid schema must define:

1. **`alternatives`**: The names of the alternatives in the choice set.
2. **`choice_var`**: The column name representing the chosen alternative.
3. **`availabilities`**: A mapping from alternative names to their availability columns.
4. **`variables`**: A list of attributes, their types (e.g., continuous, categorical), and which alternatives they apply to.

## Example JSON Schema

```json
{
  "name": "simple_mode_choice",
  "choice_var": "choice",
  "alternatives": ["car", "bus"],
  "availabilities": {
    "car": "av_car",
    "bus": "av_bus"
  },
  "variables": [
    {
      "name": "time",
      "type": "continuous",
      "applies_to": ["car", "bus"],
      "columns": { "car": "time_car", "bus": "time_bus" }
    },
    {
      "name": "cost",
      "type": "continuous",
      "applies_to": ["car", "bus"],
      "columns": { "car": "cost_car", "bus": "cost_bus" }
    },
    {
      "name": "income",
      "type": "continuous",
      "applies_to": ["all"],
      "columns": { "all": "income" }
    }
  ]
}
```
