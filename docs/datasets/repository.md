# Transport Choice Datasets Repository

`TUD-CityAI-Lab/transport-choice-datasets` is the canonical source for transport datasets and variable-aggregation schemas used across the Delphos ecosystem. It remains private during release preparation; its public link will be activated when licences, provenance, and release artefacts are ready.

## What belongs there

- source and processed transport choice data, subject to their licences;
- reproducible preparation and validation code;
- dataset-level metadata and provenance;
- standardised mappings from local variables to shared modelling concepts; and
- benchmark artefacts used in training and evaluation.

## What belongs in the final-user package

The `delphos` distribution exposes the datasets needed by final users through the same package and the planned `delphos.datasets` API. There is no separate `delphos-datasets` PyPI distribution in the initial release.

## Adding a shared dataset

Before proposing a new canonical dataset:

1. confirm that redistribution is permitted;
2. preserve the original source and document every transformation;
3. define alternatives, choice codes, and availability explicitly;
4. map attributes and covariates to existing global concepts where substantively valid;
5. introduce new concepts only with a clear cross-task definition;
6. validate the schema against the processed CSV; and
7. provide a small smoke test or example task.

Project-specific or restricted data should remain in the user's own workspace. A task can still use such data without contributing the underlying CSV to the canonical repository.
