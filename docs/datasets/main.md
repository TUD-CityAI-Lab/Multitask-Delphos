# Transport Choice Datasets

Repository of transport-related discrete choice datasets designed to support reproducible research in discrete choice modelling, reinforcement learning, and machine learning workflows.

The repository provides standardized datasets, metadata, preprocessing pipelines, and reproducible formatting scripts for transport choice modelling research.

---

## Objectives

This repository aims to:

1. Collect transport-related discrete choice datasets.
2. Preserve links between datasets, publications, preprocessing decisions, and metadata.
3. Provide reproducible Python pipelines for formatting raw datasets.
4. Support discrete choice modelling workflows in:
   - Apollo,
   - Biogeme,
   - and machine learning environments.
5. Facilitate reproducible benchmarking and multi-task learning experiments.

---

## Dataset Inventory

| Dataset                   | Folder                          |
| ------------------------- | ------------------------------- |
| Netherlands Mode Choice   | `1987_netherlands_modechoice`   |
| UK Value of Time          | `1994_uk_vot`                   |
| Swissmetro                | `2001_swissmetro`               |
| Norway VTT                | `2009_norway_vtt`               |
| Arentze                   | `2013_Arentze`                  |
| Spain Parking Choice      | `2014_spain_parkingchoice`      |
| Netherlands Flight Choice | `2016_netherlands_flightchoice` |
| Apollo Route Choice       | `2018_apollo_routechoice`       |
| London Mode Choice        | `2018_london_modechoice`        |
| OPTIMA Mode Choice        | `2018_optima_modechoice`        |
| Taboo Dataset             | `2018_Taboo`                    |
| Apollo Mode Choice        | `2019_apollo_modechoice`        |
| de Almeida Correia        | `2019_dealmeidacorreia`         |
| Mouter Route Choice B     | `2019_mouter_routechoice_b`     |
| Mouter Route Choice C     | `2019_mouter_routechoice_c`     |
| Mouter Route Choice D     | `2019_mouter_routechoice_d`     |
| van Cranenburgh VOT       | `2019_vancranenburgh_vot`       |
| Death by Automation       | `2020_deathbyautomation`        |
| Decisions Dataset         | `2020_decisions`                |
| Street-Level Conditions   | `2026_cv_dcm`                   |

---

## Repository Structure

Each dataset follows a standardized directory structure.

```text
datasets/
└── <dataset_slug>/
    ├── README.md
    ├── metadata.yaml
    │
    ├── raw/
    │   ├── dataset.yaml
    │   └── <dataset_slug>_original.<ext>
    │
    └── processed/
        ├── <dataset_slug>_formatted.csv
        ├── metadata.yaml
        └── <dataset_slug>_dictionary.csv
```

---

## Dataset Components

### Raw Data

The `raw/` directory contains:

- original dataset files,
- source-specific formatting,
- and the main `dataset.yaml` configuration file describing how the dataset should be processed.

### Processed Data

The `processed/` directory contains:

- formatted datasets,
- metadata summaries,
- and automatically generated variable dictionaries.

### Metadata

Each dataset includes metadata describing:

- source publications,
- authors,
- choice structures,
- alternatives,
- attributes,
- covariates,
- and preprocessing operations.

---

## Processing Pipeline

The repository includes reproducible Python pipelines for:

- loading raw data,
- formatting datasets,
- applying transformations,
- generating metadata,
- validating schemas,
- and exporting standardized outputs.

### Process a Dataset

```bash
python scripts/build_dataset.py datasets/2001_swissmetro/raw/dataset.yaml
```

The pipeline:

1. Loads raw data files.
2. Applies preprocessing operations.
3. Normalizes column names.
4. Generates metadata summaries.
5. Exports formatted datasets and dictionaries.

---

## Dataset YAML Configuration

Each dataset contains a `dataset.yaml` configuration file describing:

- dataset metadata,
- source information,
- parsing rules,
- data structure,
- alternatives,
- attributes,
- covariates,
- and preprocessing transformations.

The configuration system enables reproducible and transparent dataset formatting.

---

## Supported Transformations

The preprocessing pipeline supports:

- row filtering,
- column scaling,
- recoding,
- derived variables,
- attribute aggregation,
- binning,
- quantile segmentation,
- one-hot encoding conversion,
- missing-value filtering,
- and custom preprocessing operations.

---

## Example Workflow

A complete end-to-end example is available using the Swissmetro dataset.

```bash
examples/swissmetro_example.ipynb
```

The notebook demonstrates:

- dataset loading,
- preprocessing,
- metadata generation,
- and formatted dataset creation.
