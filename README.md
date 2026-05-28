# Multitask Delphos 🏛️

**Reinforcement Learning for Assisted Discrete Choice Model Specification**

Delphos is a system designed to assist in the specification of discrete choice models using Reinforcement Learning. It treats the process of finding the optimal model specification as an exploration problem, suggesting the best functional forms and variable interactions.

This is the **Main Repository** and central hub for the Delphos ecosystem.

## 📦 The Delphos Ecosystem

The project is structured into three main components:

1. **[delphos-core](https://github.com/TUD-CityAI-Lab/delphos-core)**: The main engine and research repository where the heavy lifting (training, reinforcement learning environment, model generation) happens.
2. **delphos (User Library)**: The pip-installable python package intended for end users. It provides a clean API for inference and integrating Delphos with tools like Apollo or Biogeme. 
3. **[delphos-datasets](https://github.com/TUD-CityAI-Lab/transport-choice-datasets)**: A standardized collection of transportation choice datasets used for training and evaluating Delphos.

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
