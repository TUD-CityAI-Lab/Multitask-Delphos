---
hide:
  - toc
---

```python
import sys
from pathlib import Path
import pandas as pd

ROOT = Path.cwd().parent
sys.path.insert(0, str(ROOT / "code"))

from mdp.task import Task
from mdp.catalogue import Catalogue
from mdp.state import Specification, Term
from mdp.action import *
from env.apollo.generator import ApolloGenerator

from env.result_cache import ResultCache
```

## Test rewards

1. Create a temporary rewards database

```python
cache_path = Path("./test_rewards.sqlite")

if cache_path.exists():
    cache_path.unlink()

cache = ResultCache(cache_path)

cache
```

    ResultCache(db_path=PosixPath('test_rewards.sqlite'))

2. Create a failed outcome

```python
failed = cache.failed(task_name="apollo_mode_choice", specification="spec_1")
failed
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apollo_mode_choice</td>
      <td>spec_1</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>0</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

3. Create a skipped outcome

```python
skipped = cache.skipped(task_name="apollo_mode_choice", specification="spec_2", n_free_parameters=60)
skipped
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apollo_mode_choice</td>
      <td>spec_2</td>
      <td>60</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>0</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>60</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

4. Add failed and skipped outcomes

```python
cache.upsert(failed)
cache.upsert(skipped)
```

5. Check if a specification has already estimated

```python
cache.exists(task_name="apollo_mode_choice", specification="spec_1")
```

    True

6. Retrieve modelling outcomes of a estimated model

```python
cache.lookup(task_name="apollo_mode_choice", specification="spec_1")
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apollo_mode_choice</td>
      <td>spec_1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

7. Load all the model outcomes

```python
cache.load()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apollo_mode_choice</td>
      <td>spec_1</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>apollo_mode_choice</td>
      <td>spec_2</td>
      <td>60.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>60.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

8. update a model estimation outcome

```python
updated = failed.copy()
updated["LLout"] = -1234
cache.upsert(updated)

cache.lookup(task_name="apollo_mode_choice", specification="spec_1")
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apollo_mode_choice</td>
      <td>spec_1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>-1234.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

## Emprical rewards

```python
cache_path = Path("../dataset/dataset_1/rewards.sqlite")
cache = ResultCache(cache_path)

cache.load()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>task_name</th>
      <th>specification</th>
      <th>numParams</th>
      <th>numResids</th>
      <th>maximum</th>
      <th>vcHessianConditionNumber</th>
      <th>successfulEstimation</th>
      <th>LL0</th>
      <th>LLC</th>
      <th>LLout</th>
      <th>rho2_0</th>
      <th>adjRho2_0</th>
      <th>rho2_C</th>
      <th>adjRho2_C</th>
      <th>AIC</th>
      <th>BIC</th>
      <th>eigValue</th>
      <th>timeTaken</th>
      <th>nFreeParams</th>
      <th>skipped</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ApolloModeChoice</td>
      <td>1110_2110_3110_4110_5000_6110_7000_8000</td>
      <td>7.0</td>
      <td>5600.0</td>
      <td>-4670.988194</td>
      <td>5.802145e-07</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4670.988194</td>
      <td>0.293034</td>
      <td>0.291975</td>
      <td>0.139922</td>
      <td>0.139185</td>
      <td>9355.976387</td>
      <td>9402.390040</td>
      <td>-25.901553</td>
      <td>0.592869</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ApolloModeChoice</td>
      <td>1110_2110_3110_4110_5000_6120_7000_8000</td>
      <td>8.0</td>
      <td>5600.0</td>
      <td>-4670.221880</td>
      <td>6.592906e-07</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4670.221880</td>
      <td>0.293150</td>
      <td>0.291940</td>
      <td>0.140063</td>
      <td>0.139142</td>
      <td>9356.443760</td>
      <td>9409.487935</td>
      <td>-20.973439</td>
      <td>0.538391</td>
      <td>8.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ApolloModeChoice</td>
      <td>1110_2110_3110_4110_5000_6210_7000_8000</td>
      <td>7.0</td>
      <td>5600.0</td>
      <td>-4660.531979</td>
      <td>4.405313e-07</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4660.531979</td>
      <td>0.294617</td>
      <td>0.293557</td>
      <td>0.141847</td>
      <td>0.141110</td>
      <td>9335.063957</td>
      <td>9381.477610</td>
      <td>-20.114351</td>
      <td>0.502049</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ApolloModeChoice</td>
      <td>1110_2110_3110_4110_5000_6220_7000_8000</td>
      <td>8.0</td>
      <td>5600.0</td>
      <td>-4659.639354</td>
      <td>2.441837e-07</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4659.639354</td>
      <td>0.294752</td>
      <td>0.293541</td>
      <td>0.142011</td>
      <td>0.141091</td>
      <td>9335.278709</td>
      <td>9388.322884</td>
      <td>-10.116044</td>
      <td>0.483173</td>
      <td>8.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ApolloModeChoice</td>
      <td>1110_2110_3110_4110_5000_6310_7000_8000</td>
      <td>8.0</td>
      <td>5600.0</td>
      <td>-4603.567575</td>
      <td>1.183897e-36</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4603.567575</td>
      <td>0.303239</td>
      <td>0.302028</td>
      <td>0.152336</td>
      <td>0.151415</td>
      <td>9223.135150</td>
      <td>9276.179325</td>
      <td>NaN</td>
      <td>0.367627</td>
      <td>8.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>26385</th>
      <td>ApolloModeChoice</td>
      <td>1110_2310_3112_4000_5120_6000_7000_8000</td>
      <td>9.0</td>
      <td>5600.0</td>
      <td>-4563.285215</td>
      <td>2.534571e-06</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4563.285215</td>
      <td>0.309335</td>
      <td>0.307973</td>
      <td>0.159753</td>
      <td>0.158648</td>
      <td>9144.570430</td>
      <td>9204.245127</td>
      <td>-24.059556</td>
      <td>0.715114</td>
      <td>9.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26386</th>
      <td>ApolloModeChoice</td>
      <td>1116_2110_3216_4000_5120_6000_7000_8000</td>
      <td>19.0</td>
      <td>5600.0</td>
      <td>-4698.099622</td>
      <td>6.077046e-06</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4698.099622</td>
      <td>0.288931</td>
      <td>0.286055</td>
      <td>0.134930</td>
      <td>0.131983</td>
      <td>9434.199244</td>
      <td>9560.179160</td>
      <td>-7.391760</td>
      <td>1.554350</td>
      <td>19.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26387</th>
      <td>ApolloModeChoice</td>
      <td>1112_2110_3216_4000_5216_6000_7000_8000</td>
      <td>15.0</td>
      <td>5600.0</td>
      <td>-4346.970751</td>
      <td>6.479791e-06</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4346.970751</td>
      <td>0.342075</td>
      <td>0.339805</td>
      <td>0.199584</td>
      <td>0.197374</td>
      <td>8723.941502</td>
      <td>8823.399330</td>
      <td>-6.136886</td>
      <td>1.213176</td>
      <td>15.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26388</th>
      <td>ApolloModeChoice</td>
      <td>1110_2316_3216_4000_5210_6000_7000_8000</td>
      <td>13.0</td>
      <td>5600.0</td>
      <td>-4667.061211</td>
      <td>1.074200e-05</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4667.061211</td>
      <td>0.293629</td>
      <td>0.291661</td>
      <td>0.140645</td>
      <td>0.138803</td>
      <td>9360.122422</td>
      <td>9446.319206</td>
      <td>-25.088253</td>
      <td>1.692919</td>
      <td>13.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26389</th>
      <td>ApolloModeChoice</td>
      <td>1110_2326_3216_4000_5120_6000_7000_8000</td>
      <td>26.0</td>
      <td>5600.0</td>
      <td>-4590.831492</td>
      <td>7.305856e-09</td>
      <td>1</td>
      <td>-6607.093673</td>
      <td>-5430.886635</td>
      <td>-4590.831492</td>
      <td>0.305166</td>
      <td>0.301231</td>
      <td>0.154681</td>
      <td>0.150446</td>
      <td>9233.662985</td>
      <td>9406.056553</td>
      <td>-0.007338</td>
      <td>4.265082</td>
      <td>26.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>26390 rows × 20 columns</p>
</div>
