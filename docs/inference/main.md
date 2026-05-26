# Inference and transfer learning

Delphos supports inference workflows in which a previously trained reinforcement learning agent is applied to unseen discrete choice modelling tasks without additional training or few adaptation steps.

The objective of inference is to evaluate whether the agent has learned transferable modelling strategies that generalize across datasets and modelling contexts.

---

# Frozen-Agent Transfer

The transfer workflow evaluates a frozen reinforcement learning policy on unseen tasks.

In this setting:

- network weights remain fixed,
- gradients are disabled,
- replay buffers are not updated,
- and no additional learning occurs.

The trained agent only performs sequential specification actions using the modelling strategies acquired during training.

---

# Inference Pipeline

The inference phase follows four main stages:

1. Load the trained agent.
2. Switch the trainer to inference mode.
3. Register an unseen dataset runtime.
4. Execute inference episodes under multiple decision policies.

---

# Main Transfer Function

```python
def transfer(loaded_agent):

    loaded_agent.inference()

    unseen_runtime = loaded_agent.register_runtime(INFERENCE_TASKS[0])

    transfer_df = compare_inference_modes(
        trainer=loaded_agent,
        runtime=unseen_runtime,
        modes=["greedy", "stochastic", "boltzmann"],
        n_episodes=N_TRANSFER_EPISODES,
    )
```

---

To evaluate whether the trained agent can generalize to unseen tasks, Delphos uses different inference protocols.

## Greedy inference

The agent always selects the action with the highest predicted Q-value.

Characteristics:

- deterministic,
- exploitative,
- low exploration,
- stable specifications.

## Stochastic inference

Actions are sampled probabilistically from the policy distribution.

Characteristics:

- moderate exploration,
- increased specification diversity,
- stochastic trajectories.

## Boltzmann inference

Actions are sampled using a temperature-controlled softmax over Q-values.

Characteristics:

- exploration-exploitation balance,
- controlled stochasticity,
- sensitivity to Q-value magnitudes.

# Inference Diagnostics

The inference workflow logs diagnostics during transfer evaluation.

```python
inf_logger = DiagnosticsLogger(cap=50_000)
```

Diagnostics are used to evaluate:

- transferability,
- exploration behaviour,
- specification diversity,
- trajectory stability,
- and policy uncertainty.

The output of the transfer phase is a dataframe which stores:

- rewards,
- model specifications,
- number of terms,
- number of steps,
- and estimation outcomes.
