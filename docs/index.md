---
hide:
  - navigation
---

# Delphos: assisted specification of discrete choice models

Delphos helps choice modellers explore utility specifications with a trained reinforcement-learning agent. The agent proposes modelling decisions; Apollo estimates the resulting discrete choice models; you decide which specifications are behaviourally meaningful and worth carrying forward.

Delphos is an assistant, not an automatic model-selection authority. It reduces repetitive search while keeping the modeller responsible for data preparation, identification, interpretation, validation, and reporting.

## Choose your route

<div class="grid cards" markdown>

-   **New to Delphos**

    Understand the workflow, install the package, and generate a small set of proposals.

    [Start here](getting_started/overview.md)

-   **Choice modeller**

    Control the modelling space, estimate proposals with Apollo, compare results, and export a shortlist.

    [Open the user guide](user-guide/index.md)

-   **Working with data**

    Use a catalogue dataset or describe your own CSV with a transparent Delphos schema.

    [Open the datasets guide](datasets/overview.md)

-   **Researcher or developer**

    Study the MDP, multitask architecture, training machinery, paper repositories, and contribution workflow.

    [Research and papers](research/index.md) · [Development](development/index.md)

-   **Learn by running code**

    Follow complete Jupyter notebooks for final users and for the internal training machinery.

    [Open the tutorial library](tutorials/index.md)

</div>

## From Apollo or Biogeme?

If you use **Apollo**, the generated objects will look familiar: Delphos constructs parameter definitions, utility functions, availability conditions, and an `apollo_probabilities` function before calling Apollo through R.

If you use **Biogeme**, think of Delphos as a learned assisted-specification search over a catalogue of utility terms. The main difference is the estimation backend: the current Delphos package generates and estimates models with Apollo.

In both cases, the modelling logic is unchanged:

1. define alternatives, attributes, availability, and covariates;
2. define the modelling space that may be explored;
3. generate candidate utility specifications;
4. estimate and diagnose a manageable shortlist; and
5. use behavioural judgement and validation to select models for further work.

## Project components

| Component | Purpose | Availability |
| --- | --- | --- |
| `gnova3/Delphos` | Final-user inference and Apollo estimation package | Private until the first package release |
| [Delphos single-task](https://github.com/gnova3/delphos-single-task) | Paper 1 implementation and experiments | Public |
| `gnova3/Delphos-training` | Multitask training, transfer, and Paper 2 experiments | Private until Paper 2 release |
| `TUD-CityAI-Lab/transport-choice-datasets` | Canonical data and aggregation schemas | Private during release preparation |

See [Papers and Reproducibility](research/papers.md) for citations and the repository associated with each paper.
