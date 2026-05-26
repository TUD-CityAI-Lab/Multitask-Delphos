# Delphos: Reinforcement Learning for Automated Discrete Choice Model Specification

**Delphos** is a reinforcement learning framework designed to automate the specification of discrete choice models. It learns how to specify models by iteratively building configurations and receiving feedback (e.g., Log-Likelihood, AIC, BIC) from the resulting estimations.

The project consists of three interconnected repositories:

<div class="grid cards" markdown>

- **Delphos Core**

  ***

  The primary research and development framework for RL-assisted specification. It handles agent training, environments, and core RL logic.

  [Go to Core](researchers/architecture.md)

- **Delphos User**

  ***

  A lightweight inference framework tailored for applying pre-trained agents in production or applied projects.

  [Go to User](choice_modellers/inference.md)

- **Transport Datasets**

  ***

  A collection of transport choice datasets, utilized for both training the agent and benchmarking performance.

  [Explore Datasets](datasets/structure.md)

</div>

## Target Audience

### Choice Modellers

Leverage pre-trained Delphos agents to automatically build discrete choice model specifications. Delphos can even provide ready-to-use **Apollo** code suggestions for your datasets.

[Getting Started for Modellers](choice_modellers/overview.md){ .md-button .md-button--primary }

### Researchers

Dive deep into the mechanics. Develop novel RL algorithms, design innovative reward functions, build advanced encoders, and run comprehensive benchmark experiments.

[Documentation for Researchers](researchers/architecture.md){ .md-button }
