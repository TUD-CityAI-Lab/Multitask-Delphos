# First Application

This walkthrough uses a trained Delphos agent to propose utility specifications for the bundled Swissmetro task. You will generate candidates first, inspect the Apollo representation, and then decide whether to estimate them.

## 1. Import Delphos

```python
import delphos as dp
```

The final-user API is available directly from the `delphos` package. Internal training classes are deliberately kept out of this workflow.

## 2. See the available datasets

```python
for dataset in dp.list_datasets():
    print(dataset.id, dataset.name)
```

Load Swissmetro by name:

```python
task = dp.load_dataset("Swissmetro")

print(task.name)
print([alternative.name for alternative in task.alternatives])
print([attribute.name for attribute in task.attributes])
```

For an Apollo user, `task` contains the information normally used to build `apollo_control`, the availability list, and utility-variable mappings. For a Biogeme user, it plays a role similar to the database description plus the catalogue of expressions that may enter the utilities.

## 3. Load the trained agent

```python
model = dp.load_agent(device="cpu")
```

`model` combines the trained policy with the global catalogue used during training. A custom checkpoint can be supplied with `dp.load_agent(checkpoint="path/to/checkpoint.pt")`.

## 4. Generate a small candidate set

```python
proposals = model.propose(
    task,
    n_models=10,
    max_attempts=100,
    strategy="topk",
    top_k=5,
    seed=123,
)

proposal_table = proposals.to_dataframe()
print(proposal_table.head())
```

The proposal-only workflow is the recommended starting point. It lets you review what the policy generated without paying the cost of ten Apollo estimations.

## 5. Read a proposed specification

```python
proposal = proposals.proposals[0]

print("Specification key:", proposal.specification_key)
print("Number of terms:", len(proposal.terms))
print("Actions taken:", proposal.action_indices)
```

Inspect the generated Apollo object:

```python
apollo_spec = proposal.apollo_specification

print(apollo_spec.summary())
print(apollo_spec.utility_code)
print(apollo_spec.probability_code)
```

The specification key is a stable encoded representation used by Delphos for caching and comparison. The generated R code is the modeller-facing representation: read it as you would read an Apollo model file.

## 6. Estimate only when ready

If R and Apollo are installed, estimate the candidate set:

```python
proposals.estimate(
    task,
    info=True,
    save=False,
    max_free_parameters=30,
)

estimated = proposals.to_dataframe()
print(estimated[["specification_key", "LLout", "AIC", "BIC", "reward"]])
```

`max_free_parameters` prevents unexpectedly large models from reaching Apollo. Start with a conservative value and raise it deliberately.

!!! warning "Estimation can be expensive"

    Each uncached proposal is a separate Apollo estimation. Test one or two proposals before launching a larger run, particularly when Box–Cox terms or many interactions are allowed.

## 7. Save a first shortlist

```python
estimated.to_csv("swissmetro_delphos_candidates.csv", index=False)
```

The CSV records the search metadata and the available Apollo results. The next step is not simply to choose the highest likelihood: inspect convergence, parameter count, signs, uncertainty, identification, and the purpose of the model.

Continue to [Understand Proposals and Results](understanding_results.md).
