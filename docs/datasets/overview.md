# Datasets

Delphos needs more than a CSV. It needs a transparent description of the choice problem: the choice and individual identifiers, alternatives, availability conditions, attribute mappings, covariates, and the global modelling concepts represented by those variables.

This description is called a **task**.

## Two ways to work with data

### Use a catalogue dataset

Bundled datasets are ready to load and are useful for learning, benchmarking, and reproducing experiments.

```python
import delphos as dp

task = dp.load_dataset("Swissmetro")
```

See [Catalogue Datasets](catalogue.md).

### Use your own dataset

Create a task folder containing:

```text
my_dataset/
├── dataset.csv
└── dataset.yaml
```

The YAML schema maps the columns in your data to the modelling concepts understood by the trained Delphos catalogue. See [Use Your Own Dataset](own-data.md) and the [Schema Reference](dataset_format.md).

## Why global identifiers matter

Column names differ across projects—`TRAIN_TT`, `rail_ivt`, and `time_train` may all describe in-vehicle travel time. Delphos transfers modelling knowledge by mapping those dataset-specific columns to a shared attribute identifier.

This mapping must be substantively correct. Reusing an identifier means that two variables represent the same modelling concept, not merely that they have similar names.

## Data remain under modeller control

Before running Delphos, check:

- one row per choice situation, or the intended panel structure;
- valid choice codes and alternative availability;
- consistent units and scaling across alternatives;
- valid domains for logarithmic or Box–Cox transformations;
- non-empty covariate levels; and
- benchmark likelihoods and observation counts where they are used.

The [Transport Choice Datasets repository](repository.md) is the canonical source for shared training and evaluation data. The final-user package exposes the same collection through `delphos.datasets` in the planned public API, without creating a separate PyPI distribution.
