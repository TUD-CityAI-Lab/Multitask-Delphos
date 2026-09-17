# Tutorial Library

These are real Jupyter notebooks, rendered as notebooks in the documentation and available with their source cells. Use them when you want to learn by running a complete example rather than reading an API reference.

The sequence follows a choice modeller’s workflow: understand the data, define the modelling question, generate candidate utility specifications, estimate them with Apollo, and interpret the results.

## Final-user notebooks

Start here if you normally specify models in Apollo or Biogeme and want Delphos to assist with the search.

| Notebook | Modelling question | Outcome | Source |
| --- | --- | --- | :---: |
| [00. Installation](end-user/00_installation.ipynb) | How do I install Delphos? | Verify pip installation, import the package, and test R | <a href="end-user/00_installation/00_installation.ipynb" download>⬇️</a> |
| [01. Getting Started](end-user/01_getting_started.ipynb) | How do I obtain my first candidate specifications? | Load a task and checkpoint, propose candidates, inspect Apollo code | <a href="end-user/01_getting_started/01_getting_started.ipynb" download>⬇️</a> |
| [02. Modelling Space](end-user/02_modelling_space.ipynb) | Which modelling decisions should Delphos be allowed to explore? | Restrict transformations, tastes, and covariates | <a href="end-user/02_modelling_space/02_modelling_space.ipynb" download>⬇️</a> |
| [03. Your Own Datasets](end-user/03_your_own_datasets.ipynb) | How does my CSV become a Delphos task? | Inspect a bundled task and build a validated user task | <a href="end-user/03_your_own_datasets/03_your_own_datasets.ipynb" download>⬇️</a> |
| [04. Advanced Search](end-user/04_advanced_search.ipynb) | How do I run a broader search? | Configure advanced sampling, run Delphos in a loop, save outputs | <a href="end-user/04_advanced_search/04_advanced_search.ipynb" download>⬇️</a> |
| [05. Reward and Ranking](end-user/05_reward_function.ipynb) | How does Delphos rank candidate models? | Rank outputs by AIC, BIC, and Adjusted Rho-squared | <a href="end-user/05_reward_function/05_reward_function.ipynb" download>⬇️</a> |
| [06. Exploring in R](end-user/06_exploring_in_r.ipynb) | How can I explore specifications manually? | Extract R scripts from proposals and use them in RStudio | <a href="end-user/06_exploring_in_r/06_exploring_in_r.ipynb" download>⬇️</a> |

The early notebooks include representative saved output where it helps interpretation. Some tutorials intentionally call Apollo so that the resulting diagnostics can be explained; others guard estimation or long searches with flags such as `RUN_ESTIMATION` or `RUN_LONG`. Read the setup cell before using **Run All**.

## Research notebooks

Use this series to inspect the machinery in the multitask training component. It follows the MDP from its data abstraction to the complete estimation environment.

| Notebook | Focus | Source |
| --- | --- | :---: |
| [01. Task Representation](research/01_task.ipynb) | Build and inspect a task | <a href="research/01_task/01_task.ipynb" download>⬇️</a> |
| [02. State Representation](research/02_state.ipynb) | Encode utility specifications as states | <a href="research/02_state/02_state.ipynb" download>⬇️</a> |
| [03. Action Space](research/03_action.ipynb) | Enumerate and validate modelling actions | <a href="research/03_action/03_action.ipynb" download>⬇️</a> |
| [04. Apollo Generator](research/04_apollo_generator.ipynb) | Translate a symbolic specification to Apollo inputs | <a href="research/04_apollo_generator/04_apollo_generator.ipynb" download>⬇️</a> |
| [05. Apollo Estimator](research/05_apollo_estimator.ipynb) | Cross the Python–R estimation boundary | <a href="research/05_apollo_estimator/05_apollo_estimator.ipynb" download>⬇️</a> |
| [06. Results Cache](research/06_results_cache.ipynb) | Store and reuse estimation outcomes | <a href="research/06_results_cache/06_results_cache.ipynb" download>⬇️</a> |
| [07. Environment](research/07_environment.ipynb) | Evaluate a complete terminal specification | <a href="research/07_environment/07_environment.ipynb" download>⬇️</a> |
| [08. Integration Tests](research/08_testing.ipynb) | Exercise the connected pipeline | <a href="research/08_testing/08_testing.ipynb" download>⬇️</a> |

These notebooks expose research internals and are tied to `Delphos-training`; they are not required to use the `delphos` final-user package.

## Run a notebook locally

The component repositories remain private during release preparation. The commands below are for collaborators with access; public users will receive the same notebooks with the package release.

For final-user tutorials, clone and install the end-user component:

```bash
git clone https://github.com/gnova3/Delphos.git
cd Delphos
python -m pip install -e .
python -m pip install jupyterlab
jupyter lab tutorials
```

For research tutorials, use the training repository and its environment instead:

```bash
git clone --recurse-submodules https://github.com/gnova3/Delphos-training.git
cd Delphos-training
python -m pip install --requirement requirements.txt
jupyter lab tutorials
```

R and Apollo are needed only for cells that perform estimation. Proposal generation and most inspection steps can be explored without launching R.

## How the notebook documentation is maintained

The component repositories are the canonical notebook sources. The umbrella publishes byte-for-byte copies so the notebook rendered here is the same file a user runs from the component. Continuous integration checks that the copies have not drifted.

This mirrors the useful pattern in established choice-modelling documentation: a short beginner route, examples grouped by modelling task, visible code and results, and downloadable sources—while keeping Delphos-specific decisions and interpretation explicit.
