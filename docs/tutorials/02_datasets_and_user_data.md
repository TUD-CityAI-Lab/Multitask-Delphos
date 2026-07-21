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

