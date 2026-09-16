# Tutorial Library

These are real Jupyter notebooks, rendered as notebooks in the documentation and available with their source cells. Use them when you want to learn by running a complete example rather than reading an API reference.

The sequence follows a choice modeller’s workflow: understand the data, define the modelling question, generate candidate utility specifications, estimate them with Apollo, and interpret the results.

## Final-user notebooks

Start here if you normally specify models in Apollo or Biogeme and want Delphos to assist with the search.

| Notebook | Modelling question | Outcome |
| --- | --- | --- |
| [00. Installation](end-user/00_installation.ipynb) | How do I install Delphos? | Verify pip installation, import the package, and test R |
| [01. Getting Started](end-user/01_getting_started.ipynb) | How do I obtain my first candidate specifications? | Load a task and checkpoint, propose candidates, inspect Apollo code |
| [02. Your Own Datasets](end-user/02_your_own_datasets.ipynb) | How does my CSV become a Delphos task? | Inspect a bundled task and build a validated user task |
| [03. Modelling Space](end-user/03_modelling_space.ipynb) | Which modelling decisions should Delphos be allowed to explore? | Restrict transformations, tastes, and covariates |
| [04. Advanced Search](end-user/04_advanced_search.ipynb) | How do I run a broader search? | Configure advanced sampling, run Delphos in a loop, save outputs |
| [05. Reward and Ranking](end-user/05_reward_function.ipynb) | How does Delphos rank candidate models? | Rank outputs by AIC, BIC, and Adjusted Rho-squared |
| [06. Exploring in R](end-user/06_exploring_in_r.ipynb) | How can I explore specifications manually? | Extract R scripts from proposals and use them in RStudio |

The early notebooks include representative saved output where it helps interpretation. Some tutorials intentionally call Apollo so that the resulting diagnostics can be explained; others guard estimation or long searches with flags such as `RUN_ESTIMATION` or `RUN_LONG`. Read the setup cell before using **Run All**.

## Research notebooks

Use this series to inspect the machinery in the multitask training component. It follows the MDP from its data abstraction to the complete estimation environment.

| Notebook | Focus |
| --- | --- |
| [01. Task Representation](research/01_task.ipynb) | Build and inspect a task |
| [02. State Representation](research/02_state.ipynb) | Encode utility specifications as states |
| [03. Action Space](research/03_action.ipynb) | Enumerate and validate modelling actions |
| [04. Apollo Generator](research/04_apollo_generator.ipynb) | Translate a symbolic specification to Apollo inputs |
| [05. Apollo Estimator](research/05_apollo_estimator.ipynb) | Cross the Python–R estimation boundary |
| [06. Results Cache](research/06_results_cache.ipynb) | Store and reuse estimation outcomes |
| [07. Environment](research/07_environment.ipynb) | Evaluate a complete terminal specification |
| [08. Integration Tests](research/08_testing.ipynb) | Exercise the connected pipeline |

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
