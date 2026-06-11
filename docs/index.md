---
hide:
  - navigation
---

# Assisting Choice Model Specification with Reinforcement Learning

Specifying discrete choice models is often an iterative and time-consuming process. Modellers typically evaluate many alternative utility specifications while balancing model fit, parsimony, behavioural plausibility, and theoretical consistency. As model complexity and the number of modelling decisions increase, exploring the specification space becomes increasingly challenging.

To support this process, we introduce **Delphos**, a reinforcement learning agent that learns to specify discrete choice models from previous modelling tasks and transfer this modelling knowledge across transport choice datasets.

The project supports:

1. Practical model specification assistance through pre-trained agents;
2. Methodological research on reinforcement learning for automated choice model specification;
3. Choice datasets hub for benchmarking and reproducibility.

## Why Delphos?

- **Learning from previous modelling tasks**: Delphos learns modelling strategies from previous choice modelling specification tasks and transfers this knowledge to new modelling problems.

- **Automated specification process**: Delphos can efficiently navigate large modelling spaces to propose utility specifications that balance model fit, parsimony, and behavioural plausibility.

- **Flexible objective**: Delphos supports customisable reward functions, allowing modellers to incorporate their own criteria into the specification process.

- **Collaborative**: Researchers and practitioners can contribute by:
  1. Adding new datasets to the catalogue,
  2. Developing new reward functions,
  3. Extending estimation environments,
  4. Implementing alternative reinforcement learning algorithms,
  5. Reporting issues and suggestions.

---

### [Delphos](delphos/overview.md)

A Python package that allows choice modellers to apply pre-trained Delphos to their own discrete choice datasets without requiring reinforcement learning expertise. It supports zero-shot inference and few-shot fine-tuning on the new dataset. It includes:

- Loading pre-trained agents
- Loading discrete choice datasets from the catalgoue
- Automated utility specification generation
- Pareto-front exploration
- Reproducible modelling workflows
- Tutorials and examples

### [Choice datasets](transport-choice-datasets/overview.md)

A collection of transport choice datasets used for training, benchmarking, teaching, and reproducible research. It includes:

- Dataset files
- Data processing and validation pipelines
- Metadata and documentation

### [Delphos-core](delphos-core/overview.md)

The research framework used to train, evaluate, and extend Delphos agents. It includes:

- Markov Decision Process formulation
- State and action space
- Reward function design
- Reinforcement learning algorithms
- Apollo integration
- Training and evaluation pipeline
- Experiment configurations

---

## Getting Started

Choose the guide that best matches your profile.

- **Choice Modellers**: Learn how to use pretrained Delphos agents for model specification.

1. [Getting Started](./choice_modellers/getting_started.md)
2. [First application](./choice_modellers/first_application.md)
3. [Understanding results](./choice_modellers/understanding_results.md)
4. [Using catalogue datasets](./choice_modellers/using_catalogue_datasets.md)
5. [Using your own datasets](./choice_modellers/using_your_own_datasets.md)
6. [Custom objectives](./choice_modellers/custom_objectives.md)
7. [Exporting results](./choice_modellers/exporting_results.md)

- **Researchers and ML Practitioners**: Learn how Delphos is trained, evaluated, and extended.

1. [Installation](./researchers/installation.md)
2. [Delphos architecture](./researchers/delphos_architecture.md)
3. [Task and Catalogue](./researchers/task_and_catalogue.md)
4. [State representations](./researchers/state_representations.md)
5. [Action space](./researchers/action_space.md)
6. [Reward functions](./researchers/reward_functions.md)
7. [Apollo integration](./researchers/apollo_integration.md)
8. [Training pipeline](./researchers/training_pipeline.md)
9. [Inference and transfer](./researchers/inference_and_transfer.md)
10. [Adding new datasets](./researchers/adding_new_datasets.md)
11. [Adding new rewards](./researchers/adding_new_rewards.md)
12. [Extending the framework](./researchers/extending_the_framework.md)

---

## Citation

If you use Delphos, please cite the corresponding repositories and associated publications.

### Publications

```bibtex
@techreport{nova2025delphos,
  title={Delphos: A reinforcement learning framework for assisting discrete choice model specification},
  author={Nova, Gabriel and Hess, Stephane and van Cranenburgh, Sander},
  year={2025},
  institution={TU Delft},
  url={https://arxiv.org/abs/2506.06410}
}

@techreport{nova2026sharing,
  title={Sharing modelling decisions across assisted choice model specification tasks},
  author={Nova, Gabriel and Hess, Stephane and van Cranenburgh, Sander},
  year={2026},
  institution={TU Delft},
  note={Working paper}
}
```
