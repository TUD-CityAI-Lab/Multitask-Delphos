# Delphos: Reinforcement Learning for Automated Discrete Choice Model Specification

**Delphos** is a Reinforcement learning agent to assist the choice model specification process. The framework formulates model specification as a sequential decision-making problem in which Delphos progressively proposes utility specifications and receives feedback from an estimation environment (e.g. Log-Likelihood, AIC, BIC, convergence metrics).

Delphos is designed to support both methodological research in reinforcement learning for choice modelling and the practical application of trained agents for assisted model specification.

The codebase is organised into three interconnected repositories:

---

<div class="grid cards" markdown>

- ## Delphos Core

  The main research and development repository containing the reinforcement learning framework for automated discrete choice model specification. It provides the code for extending the methodology, implementing new algorithms, designing reward functions, and reproducing experiments.

  This repository includes:
  - Markov Decision Process (State space, Action space, Reward function, and task manager)
  - Agent
  - Environment (Apollo integration)
  - Training
  - Inference
  - configs

  [:octicons-arrow-right-24: Explore Delphos Core](researchers/architecture.md)

- ## Delphos User

  Repository for applying trained Delphos agents in inference mode to unseen or similar discrete choice modelling contexts without requiring further training.

  This repository focuses exclusively on inference and application workflows, including:
  - Loading pre-trained weights
  - Loading new dataset schema
  - Proposing utility specifications
  - Generating Pareto front based on user-defined metrics
  - Reproducible application tutorials

  [:octicons-arrow-right-24: Explore Delphos User](choice_modellers/inference.md)

- ## Transport Choice Datasets

  Repository of transport choice datasets used for training, inference, and reproducibility.

  [:octicons-arrow-right-24: Explore Transport Datasets](datasets/structure.md)

</div>

---

## Overview

This repository separates the methodological development of Delphos from its application in inference mode.

### Delphos core

Contains the complete reinforcement learning framework required to train, evaluate, and extend Delphos. It includes the MDP formulation, environments, agents, training pipelines, reward functions, benchmarking utilities, and inference modules.

### Delphos user

Contains only the components required to apply trained Delphos agents in inference mode. It provides a lightweight interface for loading pre-trained models and generating utility specifications for new datasets without retraining the agent.

### Transport choice datasets

Provides standardized transport choice datasets and metadata used for training, evaluation, benchmarking, and reproducibility.

---

## Main Features

### Reinforcement Learning for Model Specification

Delphos formulates utility specification as a sequential decision-making problem in which an agent progressively modifies and evaluates model specifications.

### Automated Utility Specification

The framework can propose utility specifications for discrete choice models based on learned modelling strategies from previous datasets and experiments.

### Multi-Task Learning

Delphos supports training across multiple transport choice datasets to learn transferable modelling strategies rather than dataset-specific heuristics.

### Reward Functions

Reward functions may incorporate:

- goodness-of-fit,
- model complexity,
- convergence quality,
- parameter significance,
- and behavioural plausibility constraints.

### Apollo Integration

The framework integrates with the Apollo R package for model estimation and evaluation.

### Reproducibility and Benchmarking

This repo includes standardized datasets, benchmark tasks, and reproducible workflows for evaluating reinforcement learning approaches for choice model specification.

---

## Repository Structure

```text
Multitask-Delphos/
│
├── docs/
├── tutorials/
├── examples/
├── papers/
│
├── submodules/
│   ├── delphos-core/
│   ├── delphos-user/
│   └── transport-choice-datasets/
│
├── mkdocs.yml
├── README.md
└── CONTRIBUTING.md
```

---

## Citation

If you use Delphos, please cite the corresponding repositories and associated publications.

### Working Paper

```
@techreport{nova2025delphos,
  title={Delphos: A reinforcement learning framework for assisting discrete choice model specification},
  author={Nova, Gabriel and Hess, Stephane and van Cranenburgh, Sander},
  year={2025},
  month={dec},
  institution={TU Delft},
  url={https://arxiv.org/abs/2506.06410}
}

@techreport{nova2026sharing,
  title={Sharing modelling decisions across assisted choice model specification tasks},
  author={Nova, Gabriel and Hess, Stephane and van Cranenburgh, Sander},
  year={2026},
  month={may},
  institution={TU Delft},
  note={Working paper}
}
```
