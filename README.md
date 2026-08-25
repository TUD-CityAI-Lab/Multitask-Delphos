# Multitask Delphos

**Reinforcement Learning for Assisted Discrete Choice Model Specification**

Delphos is a system designed to assist in the specification of discrete choice models using Reinforcement Learning. It treats the process of finding the optimal model specification as an exploration problem, suggesting the best functional forms and variable interactions.

This is the **Main Repository** and central hub for the Delphos ecosystem.

## 📦 The Delphos Ecosystem

The project is structured into four independently versioned components:

1. **[Delphos](https://github.com/gnova3/Delphos)**: The end-user Python package for loading trained agents, searching for model specifications, and estimating models through Apollo.
2. **[Delphos single-task](https://github.com/gnova3/delphos-single-task)**: The reference implementation and experiments for the first Delphos paper.
3. **[Delphos training](https://github.com/gnova3/Delphos-training)**: The multitask reinforcement-learning, fine-tuning, evaluation, and Paper 2 reproduction repository.
4. **[Transport choice datasets](https://github.com/TUD-CityAI-Lab/transport-choice-datasets)**: The canonical collection of training and evaluation datasets and their standardised schemas.

The umbrella pins an approved commit of each repository under [`components/`](components/). Each component can also be cloned and developed independently.

## 🚀 Getting Started

The easiest way to get started with Delphos is to install the user library. 

*(Note: Package deployment is WIP. For now, see the docs for local installation).*

```bash
pip install delphos
```

For full documentation, tutorials, and advanced usage, please visit our **[Documentation Site](https://tud-cityai-lab.github.io/Multitask-Delphos/)**.

## 📖 Documentation Quick Links

- [Installation & Quickstart](https://tud-cityai-lab.github.io/Multitask-Delphos/getting_started/quickstart/)
- [First Example](https://tud-cityai-lab.github.io/Multitask-Delphos/getting_started/first_example/)
- [Inference Modes](https://tud-cityai-lab.github.io/Multitask-Delphos/inference/overview/)
- [Available Datasets](https://tud-cityai-lab.github.io/Multitask-Delphos/datasets/overview/)

## 🤝 Contributing

If you wish to contribute to the core development of Delphos, please refer to the [Contributing Guidelines](CONTRIBUTING.md) and the [Development Documentation](https://tud-cityai-lab.github.io/Multitask-Delphos/development/contribution_workflow/).
