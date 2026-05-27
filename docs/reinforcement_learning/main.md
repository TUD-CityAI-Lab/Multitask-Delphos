---
hide:
  - navigation
---
# Delphos Core

Welcome to the `delphos-core` repository, the heart of Multitask Delphos framework. This repository contains the complete reinforcement learning infrastructure required to:

- formulate discrete choice model specification as a Markov Decision Process (MDP),
- train reinforcement learning agents,
- evaluate modelling strategies,
- benchmark transferability across datasets,
- and automate utility specification workflows.

---

# Structure

The framework is organized into modular components.

# `configs/`

It defines the set of tasks to be used in the training process. Each discrete choice dataset can be defined as a task by creating a `dataset.yaml` file in `dataset/` and registering it using `task_registry.py`.

Example:

```python
from mdp.task import Task

TASKS: list[Task] = [
    Task.from_yaml(0, PROJECT_ROOT.parent / "dataset/dataset_1/dataset.yaml"),
    Task.from_yaml(1, PROJECT_ROOT.parent / "dataset/dataset_2/dataset.yaml"),
    Task.from_yaml(2, PROJECT_ROOT.parent / "dataset/dataset_3/dataset.yaml"),
    #...
    Task.from_yaml(N, PROJECT_ROOT.parent / "dataset/dataset_N/dataset.yaml"),
]

INFERENCE_TASKS: list[Task] = [
    Task.from_yaml(0, PROJECT_ROOT.parent / "dataset/dataset_N+1/dataset.yaml")
]
```

---

# `mdp/`

It defines defines all the core Markov Decision Process (MDP) components of Delphos. The specification process is formulated as a sequential decision-making problem in which:

- states represent utility specifications,
- actions represent modelling decisions,
- and rewards evaluate the resulting estimated models.

### `task.py`

Defines the `Task` object, which acts as the central representation of a dataset and modelling environment. Responsible for:

- parsing `dataset.yaml` files,
- constructing attribute and covariate spaces,
- generating structural tensors and masks,
- and exposing environment configurations to the RL agent.

### `state_manager.py`

Defines the state space of all feasible model specification space given the attributes and covariates in the task object. It is responsible for:

- encoding utility terms into symbolic states,
- decoding specifications from symbolic states to utility structures,
- generating fixed-length state representations.

### `action_manager.py`

Defines the modelling action grammar and valid actions available to the agent. It is responsible for:

- adding utility terms,
- modifying transformations,
- changing taste structures,
- adding covariate interactions,
- and terminating specifications.

### `task_runtime.py`

Encapsulates task instances, state managers, and action managers into a single environment instance.

### `reward.py`

Defines the reward functions used during training. Reward signals may incorporate:

- AIC,
- BIC,
- Log-Likelihood,
- adjusted rho-square,
- behavioural plausibility,
- convergence quality,
- etc.

# `env/`

It connects Delphos with Apollo estimation software and is responsible for:

- executing model estimations,
- retrieving metrics,
- caching results,
- and coordinating communication between Python and the estimation backend.

### `environment.py`

Coordinates:

- estimation requests,
- reward retrieval,
- caching,
- and interaction between Delphos and the estimation environment.

### `apollo_runner.py`

Generates and executes Apollo estimation scripts dynamically. Responsible for:

- Generating Apollo syntax to be ran using R,
- launching estimation routines,
- extracting estimation results,
- and returning model metrics to the reinforcement learning environment.

### `result_cache_sqlite.py`

Implements SQLite-based caching to avoid redundant model estimations.

# `agent/`

It contains the reinforcement learning architectures and neural networks used by Delphos.

### `delphos_agent.py`

Includes:

- policy network (a DQN),
- modelling term embedding (a DeepSet encorder),
- action masking,
- exploration strategies,
- multitask learning integration,
- and state encoding pipelines.

### `dqn.py`

Implements the Double Deep Q-Network (Double DQN) architecture used for training.

### `z_state_encoder.py`

Contains permutation-invariant state encoders used to create a fixed-length state of model specifications.

# `training/`

It contains the training algorithm, where `trainer.py`:

Coordinates:

- multitask training,
- exploration,
- replay buffer updates,
- target network synchronization,
- checkpointing,
- and logging.

# `transfer/`

It contains benchmarking and evaluation workflows for unseen datasets. It supports:

- zero-shot transfer,
- few-shot adaptation.

# `scripts/`

Contains executable entry points for:

- training (e.g., run_small_full_pipeline.py),
- evaluation (e.g., run_evaluation.py),
- benchmarking (e.g., run_transfer_benchmark.py).

Example:

```bash
python scripts/run_small_full_pipeline.py
```
