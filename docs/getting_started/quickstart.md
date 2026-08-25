# Quickstart

This example loads the bundled Swissmetro task and generates five utility specifications. It does **not** run Apollo estimation.

```python
import delphos as dp

model = dp.load_agent()
task = dp.load_dataset("Swissmetro")

proposals = model.propose(
    task,
    n_models=5,
    max_attempts=50,
    strategy="topk",
    seed=123,
)

summary = proposals.to_dataframe()
print(summary[
    ["specification_key", "n_terms", "episode_length", "search_strategy"]
])
```

Inspect the first generated Apollo specification:

```python
proposal = proposals.proposals[0]

print(proposal.apollo_specification.summary())
print(proposal.apollo_specification.utility_code)
```

At this stage:

- `proposal.terms` contains the structured modelling terms;
- `utility_code` contains the generated Apollo utility definitions;
- `probability_code` contains the generated `apollo_probabilities` function; and
- `summary` contains one row per unique proposal.

!!! tip "Start without estimation"

    Proposal-only runs are fast and make it easier to understand the grammar. Enable Apollo estimation only after the task and generated utility code look correct.

Continue to the [First Application](../choice_modellers/first_application.md) for a complete modeller-facing workflow.
