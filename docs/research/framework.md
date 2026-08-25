# Framework Architecture

Delphos separates the choice model from the mechanism that searches for it. Apollo remains responsible for estimating each discrete choice model; Delphos learns which modelling decision to try next.

## From a dataset to a proposed model

```text
dataset + schema
      ↓
Task ──→ task-valid modelling space
      ↓
Catalogue ──→ shared identifiers and actions
      ↓
Specification ──→ set of modelling terms
      ↓
Encoder ──→ fixed-length latent state
      ↓
Q-network ──→ values for valid actions
      ↓
Apollo environment ──→ estimates and diagnostics
      ↓
Reward + replay buffer ──→ policy update
```

The end-user package starts near the bottom of this diagram: it loads a trained encoder and policy and uses them to propose specifications. Dataset preparation, catalogue construction, reinforcement-learning updates, and paper experiments remain in the training components.

## Four layers

| Layer | Responsibility | Principal objects |
| --- | --- | --- |
| Choice problem | Describe variables, alternatives, and data | `Task`, dataset schema |
| Modelling grammar | Give shared meaning to modelling operations | `Catalogue`, specification, action space |
| Learning | Represent states and value possible actions | term encoder, DeepSet encoder, Q-networks |
| Estimation | Translate and evaluate a specification | Apollo generator, estimator, result cache |

This separation is deliberate. A task never needs to know how a neural network is trained, and the agent never needs to reason about local names such as `TRAIN_TT` or `rail_ivt`.

## A specification is a set

The elementary unit is a modelling term

$$
t_i=(a_i,\tau_i,g_i,c_i),
$$

where $a_i$ is an attribute, $\tau_i$ a transformation, $g_i$ a taste structure, and $c_i$ an optional interaction covariate. A specification is the set

$$
s=\{t_1,t_2,\ldots,t_L\}.
$$

The order of utility terms does not change the choice model. The main encoder therefore uses a permutation-invariant DeepSet representation:

$$
z_s=\rho\!\left(\operatorname{pool}_{t_i\in s}\phi(t_i)\right).
$$

`TermEncoder` embeds the four identifiers and maps each term through a shared multilayer perceptron. `DeepSetEncoder` then mean- or sum-pools the term embeddings. The implementation also provides an interaction-aware encoder for experiments where relations among terms should be modelled before pooling.

## A policy over modelling operations

The policy network estimates $Q(z_s,a)$ for every action in the global catalogue. The runtime masks actions that are invalid for the current task or state—for example a duplicate term, an unavailable attribute, or a transition to an already visited specification.

During inference, Delphos can select the best valid action or sample among promising actions to produce a diverse set of candidates. During training, exploration, Apollo evaluation, experience replay, and Double DQN updates teach the shared policy.

## Exact responsibilities of the repositories

- `gnova3/Delphos` contains the stable inference surface: load a checkpoint, propose models, estimate them, and export results.
- [`delphos-single-task`](https://github.com/gnova3/delphos-single-task) preserves the Paper 1 agent and experiments.
- `gnova3/Delphos-training` contains the multitask encoders, trainer, fine-tuning modes, diagnostics, and Paper 2 experiments.
- `TUD-CityAI-Lab/transport-choice-datasets` defines the canonical data and cross-dataset mappings.

The three unlinked components above remain private during release preparation. Their public links will be added when the corresponding package, paper, or dataset release is ready.

Continue with the [MDP formulation](mdp.md), or open the [research notebooks](../tutorials/index.md#research-notebooks) to inspect each layer interactively.
