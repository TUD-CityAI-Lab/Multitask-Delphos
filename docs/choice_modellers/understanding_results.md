---
hide:
  - toc
---

# Understanding Results

After generating candidate specifications, Delphos stores the estimated models and their modelling results in a database. During inference, Delphos iteratively proposes candidate specifications and updates the database with the estimation outcomes. This page explains how to load the results generated during inference and inspect the candidate specifications proposed by Delphos.

!!! example "Step 1: Access the modelling results"

Delphos stores all estimated specifications and their modelling outcomes in a SQLite database. The easiest way to access the results is through the `ResultCache` class.

```python
from delphos.env.result_cache import ResultCache
```

!!! example "Step 2: Connect to the results database"

Create a `ResultCache` object with the path to the results database. If you do not specify a path, it will default to `results/rewards.sqlite`.

```python
modelling_results = ResultCache(db_path="results/rewards.sqlite")

```

!!! example "Step 3: Load the estimated specifications"

Load all specifications currently stored in the database.

```python

results = modelling_results.load()
print(results.head())

```

Example output:

```text
 task_name   specification        adjRho2_0  AIC     BIC
 swissmetro  1000_2110_3000_4210  0.245      5234.1  5298.2
 swissmetro  1110_2110_3000_4210  0.252      5201.3  5274.8
 swissmetro  1110_2310_3000_4210  0.258      5178.4  5261.2
 ...         ...                  ...        ...     ...
```

Each row corresponds to a candidate specification evaluated by Delphos.

!!! example "Step 4: Inspect the available modelling results"

The results table contains information about model performance, complexity, estimation success, and computation time.

You can inspect the available columns using:

```python
print(results.columns.tolist())
```

| Modelling Result           | Description                                                                                                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `task_name`                | Name of the modelling task or dataset on which the specification was estimated.                                                                                                                                     |
| `specification`            | Encoded representation of the utility specification explored by Delphos. Each block corresponds to a modelling decision such as attribute inclusion, transformation, taste heterogeneity, or covariate interaction. |
| `successfulEstimation`     | Indicates whether the choice model converged successfully during estimation (`1 = success`, `0 = failure`).                                                                                                         |
| `numParams`                | Total number of estimated parameters in the model.                                                                                                                                                                  |
| `LL0`                      | Log-likelihood of the null model.                                                                                                                                                                                   |
| `LLC`                      | Log-likelihood at the model with alternative-specific constants.                                                                                                                                                    |
| `LLout`                    | Log-likelihood of the final model.                                                                                                                                                                                  |
| `rho2_0`                   | McFadden's pseudo-R², computed relative to the null model.                                                                                                                                                          |
| `adjRho2_0`                | Adjusted McFadden's pseudo-R². Penalises models with a large number of parameters.                                                                                                                                  |
| `rho2_C`                   | McFadden's pseudo-R² relative to a constant-only model.                                                                                                                                                             |
| `adjRho2_C`                | Adjusted McFadden's pseudo-R² relative to a constant-only model.                                                                                                                                                    |
| `AIC`                      | Akaike Information Criterion. Balances model fit and complexity, with lower values indicating preferred models.                                                                                                     |
| `BIC`                      | Bayesian Information Criterion. Similar to AIC but imposes a stronger penalty for additional parameters.                                                                                                            |
| `vcHessianConditionNumber` | Condition number of the variance-covariance matrix or Hessian approximation. Large values may indicate numerical instability or identification issues.                                                              |
| `eigValue`                 | Smallest eigenvalue of the Hessian matrix. Values close to zero may indicate poorly identified parameters.                                                                                                          |
| `numResids`                | Number of residuals or observations used in the estimation process.                                                                                                                                                 |
| `timeTaken`                | Total computational time required to estimate the specification, measured in seconds.                                                                                                                               |
| `skipped`                  | Indicates whether the specification was skipped without estimation due to a large number of parameters. (`1 = skipped`, `0 = estimated`).                                                                           |

!!! example "Step 5: Keep only successfully estimated models"

Some specifications may fail to estimate or be skipped.

Filter the results as follows:

```python
successful = results[ (results["successfulEstimation"] == 1) & (results["skipped"] == 0) ]
print(f"Successful models: {len(successful)}")
```

!!! example "Step 6: Rank specifications by model fit"

For example, to identify the specifications with the highest Log-Likelihood:

```python
best_models = successful.sort_values("LLout", ascending=False)
print( best_models[ ["specification", "LLout", "numParams"] ].head(10) )
```

Example output:

```text
specification	LLout	numParams
0	1110_2310_4210	-7252.17	10
1	1110_2311_4210	-7251.83	11
2	1110_2311_4220	-7251.10	12
```

!!! example "Step 7: Inspect a specific specification"

You can retrieve the results associated with a particular specification.

```python
specification = "1110_2310_4210"
model = results[results["specification"] == specification]
print(model.T)
```

Example output:

```text
task_name                             swissmetro
specification                     1110_2310_4210
successfulEstimation                           1
numParams                                     10
LL0                                   -7902.36
LLC                                   -7449.17
LLout                                 -7252.17
rho2_0                                    0.1077
adjRho2_0                                 0.0990
rho2_C                                    0.0274
adjRho2_C                                -0.0062
AIC                                    7272.17
BIC                                    7312.11
vcHessianConditionNumber                6599.57
eigValue                                5.77e-06
numResids                             103936.0000
timeTaken                              135.1641
skipped                                        0
```

## What Happened?

During inference, Delphos estimated multiple candidate utility specifications and stored their outcomes in the results database.

The rewards table contains:

- The generated specification.
- Modelling results.
- Estimation diagnostics.

By analysing this table, you can identify promising candidate specifications and decide which models deserve further investigation.
