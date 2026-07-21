# 02 - Datasets and user data

Delphos expects each choice dataset to have:

- a CSV file
- a `dataset.yaml` schema
- alternatives with choice codes and optional availability columns
- attributes mapped by alternative
- covariates and their discrete levels

This notebook shows how to inspect bundled datasets and how to prepare your own.


## 1. Load a bundled dataset



```python
from pathlib import Path
import pandas as pd
import yaml
import delphos as dp

info = dp.list_datasets()[3]
dataset = dp.load_dataset(info.id)
print(info)
print(dataset)

```

    DatasetInfo(id=4, folder='dataset_4', name='Swissmetro', path=PosixPath('/Users/gnova/Developer/Delphos/dataset/dataset_4'))
    Task(name='Swissmetro', alternatives=3, attributes=5, covariates=11)


## 2. Inspect the schema and CSV columns



```python
schema_path = dataset.yaml_path
csv_path = dataset.dataset_path

schema = yaml.safe_load(schema_path.read_text())
print("Schema:", schema_path)
print("CSV:", csv_path)
print("Schema keys:", list(schema.keys()))

columns = pd.read_csv(csv_path, nrows=0).columns.tolist()
print("First CSV columns:", columns[:20])

```

    Schema: /Users/gnova/Developer/Delphos/dataset/dataset_4/dataset.yaml
    CSV: /Users/gnova/Developer/Delphos/dataset/dataset_4/2001_swissmetro_formatted.csv
    Schema keys: ['id', 'choice', 'panel', 'alternatives', 'attributes', 'covariates', 'path_choice_dataset', 'rewards_path', 'll_null', 'll_linear', 'n_obs', 'df_name']
    First CSV columns: ['id', 'obs_id', 'choice', 'chosen_alt', 'train_av', 'sm_av', 'car_av', 'train_tt_scaled', 'sm_tt_scaled', 'car_tt_scaled', 'train_cost_scaled', 'sm_cost_scaled', 'car_co_scaled', 'train_he_scaled', 'sm_he_scaled', 'sm_seats_scaled', 'purpose', 'first', 'ticket', 'who']


## 3. Inspect alternatives, attributes, and covariates



```python
print("Alternatives")
for alt in dataset.alternatives:
    print(alt)

print("\nAttributes")
for attr in dataset.attributes:
    print(attr)

print("\nModelled covariates")
for cov in dataset.modelling_covariates:
    print(cov)

```

    Alternatives
    Alternative(id=1, name='TRAIN', choice=1, availability='train_av')
    Alternative(id=2, name='SM', choice=2, availability='sm_av')
    Alternative(id=3, name='CAR', choice=3, availability='car_av')
    
    Attributes
    Attribute(id=1, name='ASC', alternative={})
    Attribute(id=2, name='time', alternative={1: 'train_tt_scaled', 2: 'sm_tt_scaled', 3: 'car_tt_scaled'})
    Attribute(id=3, name='cost', alternative={1: 'train_cost_scaled', 2: 'sm_cost_scaled', 3: 'car_co_scaled'})
    Attribute(id=4, name='headway', alternative={1: 'train_he_scaled', 2: 'sm_he_scaled'})
    Attribute(id=6, name='seat', alternative={2: 'sm_seats_scaled'})
    
    Modelled covariates
    Covariate(id=4, name='purpose', levels=(1, 2))
    Covariate(id=6, name='first', levels=(0, 1))
    Covariate(id=3, name='age', levels=(1, 2, 3, 4, 5))
    Covariate(id=1, name='male', levels=(0, 1))
    Covariate(id=2, name='income', levels=(1, 2, 3, 4))


## 4. Understand the trained global catalogue

User datasets must use the trained Delphos ids. The bundled catalogue helps you map common transport-choice variables to those ids.



```python
catalogue_path = Path("dataset/catalogue/catalogue.json")
catalogue = yaml.safe_load(catalogue_path.read_text())

print("Attribute ids")
for item in catalogue["attributes"]:
    print(item["id"], item["name"], "-", item["description"])

print("\nCovariate ids")
for item in catalogue["covariates"]:
    print(item["id"], item["name"], "-", item["description"])

```

## 5. Validate a schema against a CSV

`validate_dataset_config` checks required columns before creating a task.



```python
from delphos.data.validation import validate_dataset_config

validate_dataset_config(schema, csv_path)
print("Bundled schema and CSV are consistent")

```

    Bundled schema and CSV are consistent


## 6. Create a user dataset folder

The example below uses the bundled Swissmetro CSV as if it were user data. In your own work, replace `source_csv` and the schema dictionaries.



```python
from pathlib import Path
import delphos as dp

source_csv = dataset.dataset_path
user_folder = Path("tutorials/my_swissmetro_dataset")

alternatives = schema["alternatives"]
attributes = schema["attributes"]
covariates = schema["covariates"]

# Uncomment to create the folder when you are ready.
# user_task = dp.create_dataset(
#     user_folder,
#     name="MySwissmetro",
#     csv_path=source_csv,
#     choice_column=schema["choice"],
#     id_column=schema["id"],
#     panel=schema["panel"],
#     alternatives=alternatives,
#     attributes=attributes,
#     covariates=covariates,
#     ll_null=schema["ll_null"],
#     ll_linear=schema["ll_linear"],
#     n_obs=schema["n_obs"],
#     dataset_id=100,
# )
# print(user_task)

```

## 7. Practical schema tips

- Keep `id` and `choice` column names explicit.
- Every availability column used by an alternative must exist in the CSV.
- Every attribute mapping column must exist in the CSV.
- Covariate levels should match the values in your CSV.
- Attribute and covariate ids should follow `dataset/catalogue/catalogue.json`.
- Use `id: null` for covariates you want documented but not included in Delphos search.

