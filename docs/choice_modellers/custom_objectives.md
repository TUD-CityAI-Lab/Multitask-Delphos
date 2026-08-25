# Rank Candidate Models

The trained agent uses the reward defined during training. Final users normally do not change that training reward. Instead, define a transparent ranking rule after Apollo estimation and use it to create a shortlist.

## Start from valid estimations

```python
results = proposals.to_dataframe()

valid = results[
    (results["successfulEstimation"] == 1)
    & (results["skipped"] == 0)
].copy()
```

## A simple statistical ranking

```python
valid["delta_bic_from_best"] = valid["BIC"] - valid["BIC"].min()

ranked = valid.sort_values(
    ["BIC", "nFreeParams", "vcHessianConditionNumber"]
)
```

This gives priority to BIC, then to parsimony and numerical stability. It is a screening rule, not a behavioural decision rule.

## Add modeller-defined checks

Create explicit columns for the judgements that matter in your application:

```python
ranked["expected_signs"] = False
ranked["parameters_identified"] = False
ranked["policy_interpretable"] = False
ranked["validated_out_of_sample"] = False
ranked["modeller_notes"] = ""
```

Populate these columns after reading the full Apollo outputs. A candidate should not become a preferred model only because it performs well on an automated scalar score.

## Example composite score

If a scalar score is useful for sorting, make its assumptions visible:

```python
import numpy as np

ranked["selection_score"] = (
    -ranked["BIC"]
    - 2.0 * ranked["nFreeParams"]
    - np.log1p(ranked["vcHessianConditionNumber"].clip(lower=0))
    + 25.0 * ranked["expected_signs"].astype(int)
    + 25.0 * ranked["parameters_identified"].astype(int)
)

ranked = ranked.sort_values("selection_score", ascending=False)
```

The weights above are illustrative. Report and justify any weights used in your own analysis.

## Training rewards belong in the research package

Changing the reward that teaches the policy is a different operation: it requires training or fine-tuning machinery from `delphos-training`. Use the [Research & Papers](../research/index.md) section if your objective is to study alternative RL rewards rather than rank final-user results.

Continue to [Export Results](exporting_results.md).
