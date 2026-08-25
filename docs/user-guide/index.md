# User Guide

The user guide follows the decisions a choice modeller makes in practice. It assumes that you can read a utility function and interpret standard Apollo or Biogeme results; no reinforcement-learning knowledge is required.

## Recommended workflow

1. Run the [First Application](../choice_modellers/first_application.md) with a bundled task.
2. Learn how to [understand proposals and estimation results](../choice_modellers/understanding_results.md).
3. [Control the modelling space](modelling-space.md) before running a larger search.
4. Choose an appropriate [search strategy and parameter budget](search-strategies.md).
5. [Estimate a shortlist with Apollo](apollo-estimation.md).
6. [Rank candidates](../choice_modellers/custom_objectives.md) using fit, parsimony, diagnostics, and behavioural criteria.
7. [Export a reproducible shortlist](../choice_modellers/exporting_results.md).

## The three objects you will use most

| Object | Meaning for a choice modeller |
| --- | --- |
| `Task` | The dataset, alternatives, availability, attributes, covariates, and allowed modelling grammar |
| `DelphosModel` | The trained policy and the global catalogue learned during training |
| `ProposalSet` | The candidate utility specifications and, when requested, their Apollo estimation outcomes |

## Keep the search interpretable

Start with a small set of attributes and a proposal-only run. Inspect the generated utilities before estimation. Expand transformations, alternative-specific parameters, and covariate interactions only when they make behavioural sense for the application.

Delphos is most useful when it helps you investigate a defensible modelling space systematically—not when it is asked to search every syntactically possible model.
