# Apollo Estimation Environment

Apollo is the econometric engine in the Delphos MDP. Delphos generates a symbolic specification, translates it into Apollo inputs, runs estimation in R, normalises the result, and stores it for later reuse.

## Evaluation boundary

```text
Delphos specification
        ↓
ApolloSpecification
  - parameter names and starts
  - fixed parameters
  - utility code
  - probability function
        ↓
R / Apollo estimation
        ↓
normalised result row
        ↓
SQLite result cache + optional output files
```

The generated code is intentionally inspectable. This gives an Apollo modeller a familiar audit point before trusting a proposed model.

## What is cached

Every specification has a deterministic key. Before invoking R, the environment looks up the task and key in the result cache. Successful, skipped, and ordinarily failed results can therefore be reused instead of repeating an expensive estimation.

The stored outcome includes the estimation status and available model diagnostics. Debug mode can bypass a cached failure so the underlying Apollo error can be reproduced and captured.

## Guardrails

The environment:

- verifies that R and Apollo are available;
- limits the number of free parameters when requested;
- records oversized specifications as skipped;
- converts estimation exceptions into a failed outcome unless re-raising is requested;
- writes generated and diagnostic files only when enabled; and
- upserts the normalised outcome into the task cache.

These guardrails protect a large search from one malformed specification, but they do not establish behavioural validity.

## Reproducible estimation

Report the exact R and Apollo versions, task schema, generated specification key, estimation settings, and cache state. Preserve debug artefacts for failures that affect reported success rates. When a candidate becomes part of a paper or application, export and archive the complete Apollo script rather than relying only on a cached row.

Final users can follow [Estimate with Apollo](../user-guide/apollo-estimation.md). Researchers can inspect the [Apollo generator](../tutorials/research/04_apollo_generator.ipynb), [estimator](../tutorials/research/05_apollo_estimator.ipynb), and [result cache](../tutorials/research/06_results_cache.ipynb) notebooks.
