# Dataset Schema Reference

Every task folder contains `dataset.yaml` and the referenced CSV. The YAML is designed to be readable, reviewable, and version controlled.

## Complete example

```yaml
id: id
choice: choice
panel: false

alternatives:
  CAR:
    id: 1
    avail: av_car
  BUS:
    id: 2
    avail: av_bus

attributes:
  time:
    id: 2
    mapping:
      CAR: tt_car
      BUS: tt_bus
  cost:
    id: 3
    mapping:
      CAR: cost_car
      BUS: cost_bus

covariates:
  income:
    id: 2
    source: income
    type: categorical
    levels: [1, 2, 3, 4]

path_choice_dataset: mode_choice.csv
rewards_path: rewards
ll_null: -1250.4
ll_linear: -980.2
n_obs: 1500
df_name: MyModeChoice
```

## Top-level fields

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | Decision-maker or panel identifier column |
| `choice` | Yes | Observed-choice column |
| `panel` | Yes | Whether observations form panel data |
| `alternatives` | Yes | Choice codes and availability columns |
| `attributes` | Yes | Global attribute concepts and alternative-specific CSV mappings |
| `covariates` | No | Variables available for systematic taste heterogeneity |
| `path_choice_dataset` | Yes | CSV path relative to the YAML file unless absolute |
| `ll_null` | Recommended | Null-model benchmark log-likelihood used by rewards |
| `ll_linear` | Recommended | Linear-additive benchmark log-likelihood |
| `n_obs` | Recommended | Number of observations used by benchmark calculations |
| `df_name` | Yes | Human-readable task name |

## Alternative entries

- `id` must be unique and match the observed choice code.
- `avail` names a binary availability column. Omit it only when the alternative is always available.
- the alternative key must match the keys used in every attribute mapping.

## Attribute entries

- `id` is the global modelling-concept identifier;
- `mapping` connects alternative names to CSV columns; and
- an attribute may be unavailable for some alternatives, in which case omit that alternative from its mapping.

Alternative-specific constants are inserted automatically as `ASC` with global attribute identifier 1.

## Covariate entries

- `id` is the global covariate identifier, or `null` if the variable is retained only as dataset metadata;
- `source` names the CSV column;
- `type` documents the intended coding; and
- `levels` enumerates the categories available for interactions.

## Validation

```python
import yaml
import delphos as dp

with open("dataset.yaml", encoding="utf-8") as stream:
    schema = yaml.safe_load(stream)

dp.validate_dataset_config(schema, "mode_choice.csv")
```

Validation checks that required columns exist and that alternative, attribute, and non-null covariate identifiers are unique. It does not replace substantive data validation.
