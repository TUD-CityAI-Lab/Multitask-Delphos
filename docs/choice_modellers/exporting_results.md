# Export Results

A reproducible Delphos run should preserve the candidate table, the generated utility specifications, and the settings used to produce them.

## Export the comparison table

```python
from pathlib import Path

output_dir = Path("delphos_run")
output_dir.mkdir(exist_ok=True)

results = proposals.to_dataframe()
results.to_csv(output_dir / "candidates.csv", index=False)
results.to_json(output_dir / "candidates.json", orient="records", indent=2)
```

## Export generated Apollo code

```python
for proposal in proposals:
    model_dir = output_dir / proposal.specification_key
    model_dir.mkdir(exist_ok=True)

    apollo_spec = proposal.apollo_specification
    (model_dir / "utilities.R").write_text(
        apollo_spec.utility_code,
        encoding="utf-8",
    )
    (model_dir / "apollo_probabilities.R").write_text(
        apollo_spec.probability_code,
        encoding="utf-8",
    )
```

These files make the generated model readable without decoding the specification key.

## Export a complete Apollo script

For an independently runnable R representation:

```python
from delphos.env.apollo.estimator import generate_apollo_r_script

proposal = proposals.proposals[0]
script = generate_apollo_r_script(
    task=task,
    apollo_specification=proposal.apollo_specification,
    output_directory=output_dir / "apollo_output",
    summary_file=output_dir / "apollo_summary.csv",
)

(output_dir / "selected_model.R").write_text(script, encoding="utf-8")
```

Review the generated script before using it as a final analysis file. Add project-specific validation, reporting, and post-estimation calculations in the same way you would for a manually written Apollo model.

## Record the run configuration

```python
import json

manifest = {
    "checkpoint": str(model.checkpoint_path),
    "dataset": task.name,
    "dataset_schema": str(task.yaml_path),
    "n_models": 25,
    "max_attempts": 250,
    "strategy": "topk",
    "top_k": 5,
    "seed": 123,
}

(output_dir / "run_manifest.json").write_text(
    json.dumps(manifest, indent=2),
    encoding="utf-8",
)
```

For an archival result, also record the Delphos release or Git commit, Apollo version, R version, Python environment, dataset version, and any manual filtering decisions.
