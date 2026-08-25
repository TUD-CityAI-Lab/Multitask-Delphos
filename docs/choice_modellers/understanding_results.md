# Understand Proposals and Results

Delphos returns a `ProposalSet`. Before estimation, it describes what the agent proposed. After estimation, the same object also contains Apollo outcomes. Keeping these two stages separate makes large searches easier to control.

## Proposal-stage information

```python
proposal_table = proposals.to_dataframe()
print(proposal_table.columns.tolist())
```

Before Apollo is called, the table contains:

| Column | Interpretation |
| --- | --- |
| `specification_key` | Stable encoded identifier used for deduplication and caching |
| `n_terms` | Number of modelling terms in the utility specification |
| `episode_length` | Number of sequential actions used to construct the proposal |
| `search_strategy` | Greedy, top-k, stochastic, or Boltzmann action selection |
| `attempt_found` | Attempt on which the unique specification was found |
| `action_indices` | Internal sequence of modelling actions |
| `estimated` | Whether Apollo has evaluated this proposal |
| `reward` | Built-in estimation reward, or `None` before estimation |

Use this table to check diversity and complexity before committing resources to estimation.

```python
print(proposal_table[
    ["specification_key", "n_terms", "episode_length", "attempt_found"]
].sort_values("n_terms"))
```

## Read the model, not only its key

The encoded key is useful to the software, but the generated modelling terms and Apollo code are what the modeller should review.

```python
proposal = proposals.proposals[0]

for term in proposal.terms:
    print(term)

print(proposal.apollo_specification.utility_code)
```

Check that:

- the included attributes have a clear behavioural role;
- generic and alternative-specific parameters are sensible;
- transformations are valid for the observed variable range;
- interactions have a meaningful reference level; and
- the resulting model is identified.

## Estimation-stage information

After calling `proposals.estimate(task, ...)`, `to_dataframe()` adds the Apollo summary columns.

```python
results = proposals.to_dataframe()

successful = results[
    (results["successfulEstimation"] == 1)
    & (results["skipped"] == 0)
].copy()
```

The most useful fields are:

| Field | What to check |
| --- | --- |
| `LLout` | Final log-likelihood; larger values are better for the same data |
| `nFreeParams` | Number of freely estimated parameters |
| `AIC`, `BIC` | Fit–complexity measures; smaller values are preferred |
| `rho2_0`, `adjRho2_0` | Fit relative to the null model |
| `successfulEstimation` | Apollo convergence indicator |
| `vcHessianConditionNumber` | Large values may indicate weak identification or numerical instability |
| `eigValue` | Values close to zero may indicate a near-singular Hessian |
| `timeTaken` | Apollo estimation time |
| `skipped` | Delphos did not estimate the model because it exceeded the configured parameter limit |

Rank a first statistical shortlist with BIC:

```python
shortlist = successful.sort_values(["BIC", "nFreeParams"]).head(10)
print(shortlist[
    ["specification_key", "LLout", "nFreeParams", "AIC", "BIC"]
])
```

## Why the lowest BIC is not automatically the final model

Information criteria do not establish behavioural plausibility, policy relevance, or stability. For each shortlisted model, inspect:

1. parameter signs and magnitudes;
2. standard errors and robust standard errors;
3. identification and Hessian diagnostics;
4. sensitivity to starting values and data exclusions;
5. performance on held-out data where appropriate; and
6. whether the specification answers the research question.

Apollo parameter tables are written when you estimate with `save=True`. The compact Delphos dataframe is intended for screening; it does not replace the full Apollo output.

## Cached outcomes

Estimated specifications are cached by task name and specification key. This avoids repeating the same Apollo estimation.

```python
from delphos.env.result_cache import ResultCache

cache = ResultCache(task.rewards_path)
cached_results = cache.load(task.name)
```

The cache is part of the computational record. Keep it with the task when you need resumable searches, but export a clean shortlist for publication and sharing.

Continue to [Control the Modelling Space](../user-guide/modelling-space.md).
