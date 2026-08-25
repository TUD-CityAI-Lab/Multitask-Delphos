# Multitask Training

Multitask Delphos learns one specification policy from episodes generated across several choice modelling tasks. Shared catalogue identifiers make transitions from different datasets compatible with one replay buffer and one Q-network.

## One training round

A normal round performs the following operations:

1. shuffle the registered tasks;
2. generate one episode for each task using the current exploration setting;
3. estimate the terminal specification through the task’s Apollo environment;
4. distribute the terminal reward across the trajectory;
5. add the transitions to replay memory;
6. sample a mini-batch spanning tasks;
7. update the encoder and policy network; and
8. softly update the target network and write diagnostics/checkpoints.

This schedule prevents one dataset from silently defining the whole learning signal. Alternative experiments can sample tasks or episodes differently, but the task distribution must always be reported.

## Shared representation

The default multitask agent embeds each modelling term and uses a DeepSet encoder to produce a permutation-invariant state vector. An optional context vector can append dataset-level information. The interaction-aware encoder is an experimental alternative that allows terms to attend to one another before pooling.

## Double DQN update

The policy network selects the best valid next action and the target network evaluates it. The update uses a smooth L1 loss, optional importance weights supplied by the replay buffer, gradient clipping, and a Polyak target update.

Only task-valid next actions enter the target. Without that mask, the network could learn value from transitions that cannot be executed for the task.

## Exploration and reproducibility

The training implementation supports epsilon-greedy and Boltzmann exploration. Reproducible experiments should record at least:

- the task set and exact dataset versions;
- catalogue and action-space definitions;
- encoder architecture and context configuration;
- random seeds and task-sampling schedule;
- exploration, discount, horizon, and optimisation settings;
- Apollo and R versions;
- checkpoint and software commit identifiers; and
- episode, update, per-task, diversity, and estimation diagnostics.

## Where to run experiments

Training does not belong in the `delphos` final-user package. Use `gnova3/Delphos-training` for multitask training, fine-tuning, evaluation, and Paper 2 reproduction. The repository remains private until the Paper 2 release; its pinned copy under `components/delphos-training` records the version coordinated by this umbrella.

The [research notebook series](../tutorials/index.md#research-notebooks) provides small, inspectable examples of the runtime and estimation boundary before a full experiment is launched.
