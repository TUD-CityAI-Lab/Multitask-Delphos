# Catalogue Datasets

The bundled catalogue provides standardised transport choice tasks used for learning, examples, and evaluation.

## List available tasks

```python
import delphos as dp

for dataset in dp.list_datasets():
    print(
        f"{dataset.id:>2}  {dataset.name:<24} "
        f"{dataset.folder}"
    )
```

Each `DatasetInfo` records the dataset identifier, human-readable name, folder, and local path.

## Load by name or identifier

```python
swissmetro = dp.load_dataset("Swissmetro")
same_task = dp.load_dataset(4)
```

The returned `Task` is a modelling problem, not only a dataframe.

```python
print(swissmetro)
print("CSV:", swissmetro.dataset_path)
print("Choice column:", swissmetro.choice_column)
print("Panel data:", swissmetro.is_panel)
```

## Inspect alternatives and availability

```python
for alternative in swissmetro.alternatives:
    print(
        alternative.id,
        alternative.name,
        alternative.availability,
    )
```

Alternative identifiers correspond to the values used in the choice column. Availability names refer to columns in the CSV.

## Inspect attributes

```python
for attribute in swissmetro.attributes:
    print(attribute.id, attribute.name, attribute.alternative)
```

The `alternative` mapping connects a global modelling concept to the dataset column for each alternative. `ASC` is added automatically as attribute identifier 1.

## Inspect covariates

```python
for covariate in swissmetro.covariates:
    print(covariate.id, covariate.name, covariate.levels)
```

Covariates with a global identifier may enter the Delphos modelling grammar. Dataset variables without a trained global identifier can remain useful for filtering, validation, or later manual analysis, but the current policy cannot transfer a learned action for an unseen concept.

## Inspect the trained global catalogue

The loaded model contains the catalogue used to interpret checkpoint inputs:

```python
model = dp.load_agent()

print(model.catalogue.summary())
print(model.catalogue.global_attribute_ids)
print(model.catalogue.global_covariate_ids)
```

Your own task must use attribute, covariate, transformation, and taste identifiers that exist in this trained catalogue. Delphos validates this before generating proposals.

## Do not edit bundled data in place

Bundled tasks are shared reference artefacts. For a project-specific recoding, filtering decision, or additional variable, create a new task folder and record the provenance of the source data.

Continue to [Use Your Own Dataset](own-data.md).
