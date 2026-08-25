# Multitask Delphos

**Assisted discrete choice model specification with multitask reinforcement learning**

Delphos helps choice modellers explore utility specifications. A pretrained agent proposes modelling operations, while R Apollo estimates the resulting candidate models. The modeller remains responsible for the data, modelling space, diagnostics, behavioural interpretation, and final model choice.

This repository is the umbrella for documentation, papers, and coordination across four independently versioned components.

## Start as a choice modeller

The final-user package is `gnova3/Delphos`. It contains the public Python API, command-line interface, catalogue datasets, and final-user notebooks. Training machinery is deliberately excluded. The repository remains private during release preparation.

Package publication is still being prepared. Until the `delphos` distribution is released on PyPI, follow the [installation guide](https://tud-cityai-lab.github.io/Multitask-Delphos/getting_started/installation/) for a source install.

- [What Delphos does](https://tud-cityai-lab.github.io/Multitask-Delphos/getting_started/overview/)
- [Quickstart](https://tud-cityai-lab.github.io/Multitask-Delphos/getting_started/quickstart/)
- [First application](https://tud-cityai-lab.github.io/Multitask-Delphos/choice_modellers/first_application/)
- [Jupyter tutorials](https://tud-cityai-lab.github.io/Multitask-Delphos/tutorials/)

## Components

1. `gnova3/Delphos`: final-user inference package and sole source of the future `delphos` PyPI distribution; private until package release.
2. [`gnova3/delphos-single-task`](https://github.com/gnova3/delphos-single-task): Paper 1 single-task machinery and experiments.
3. `gnova3/Delphos-training`: multitask training, fine-tuning, and Paper 2 reproduction; private until Paper 2 release.
4. `TUD-CityAI-Lab/transport-choice-datasets`: canonical training and evaluation datasets; private during release preparation.

The umbrella pins an approved commit of every component under `components/`. Each repository remains independently cloneable and developable.

```bash
git clone --recurse-submodules https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
```

See the [component guide](https://tud-cityai-lab.github.io/Multitask-Delphos/development/components/) before updating a pinned version.

## Documentation and research

The [documentation site](https://tud-cityai-lab.github.io/Multitask-Delphos/) separates final-user guidance, data, research, development, and runnable notebooks. Publication links and exact reproduction repositories are maintained under [Papers and Reproducibility](https://tud-cityai-lab.github.io/Multitask-Delphos/research/papers/).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and the complete [development guide](https://tud-cityai-lab.github.io/Multitask-Delphos/development/).
