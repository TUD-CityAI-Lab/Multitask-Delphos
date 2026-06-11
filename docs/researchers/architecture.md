---
hide:
  - toc
---

## Delphos Architecture

This section provides a technical overview of the Delphos architecture. Unlike the user-oriented documentation, this section focuses on the underlying machine learning framework and how Delphos learns transferable model specification strategies across discrete choice modelling tasks.

At a high level, Delphos formulates model specification as a reinforcement learning problem and combines:

- A structured representation of utility specifications.
- Representation learning through neural encoders.
- Deep Q-Learning for policy optimisation.
- Experience replay across multiple datasets.
- Feasibility-aware action selection.

Together, these components enable Delphos to learn how to construct utility specifications rather than relying on manually defined modelling heuristics.

---

## Delphos as a Reinforcement Learning Problem

Delphos formulates model specification as a Markov Decision Process (MDP).

At any point during the search process, the agent observes a candidate utility specification and decides how to modify it. Actions correspond to modelling operations such as adding a new attribute, changing a transformation, or introducing systematic taste heterogeneity. After the resulting specification is estimated, Delphos receives a reward that reflects the modeller’s objective (e.g., model fit, parsimony, behavioural plausibility).

The objective is not to estimate model parameters directly, but rather to learn a policy capable of generating useful utility specifications.

Formally, the MDP is defined as:

$$
\mathcal{M}

(\mathcal{S},
\mathcal{A},
P,
R)
$$

where:

- $\mathcal{S}$ denotes the space of model specifications.
- $\mathcal{A}$ denotes the set of modelling operations.
- $P$ describes the transition dynamics induced by applying an operation to a specification.
- $R$ measures the quality of the resulting model.

The objective of Delphos is to learn a policy

$$
\pi(a|s)
$$

that maximises the expected cumulative reward over the specification process.

---

## Representation Learning

A fundamental challenge is that utility specifications are variable-sized objects.

For example,

$$
V_1

ASC
+
\beta_{TT}TT
+
\beta_{TC}TC
$$

contains fewer modelling terms than

$$
V_2

ASC
+
\beta_{TT}\log(TT)
+
\beta_{TC}TC
+
\beta_{HW}HW
+
\beta_{TT}^{Income}
(TT \times Income)
$$

Traditional reinforcement learning algorithms require fixed-dimensional state representations. Delphos therefore learns a representation

$$
z=f_\theta(s)
$$

that maps arbitrary specifications into a latent vector space.

The resulting latent representation can then be processed by a standard deep reinforcement learning algorithm regardless of the number of modelling terms contained in the specification.

---

## Term Encoder

The smallest modelling unit in Delphos is a modelling term.

Each term is represented by four discrete identifiers:

$$
t_i=
(a_i,
\tau_i,
\gamma_i,
c_i)
$$

where:

- $a_i$ = attribute
- $\tau_i$ = transformation
- $\gamma_i$ = taste structure
- $c_i$ = interaction covariate

For example:

Attribute Transformation Taste Covariate
Travel Time Linear Generic None
Travel Cost Log Generic Income
Headway Box-Cox Specific Gender

Each identifier is embedded into a continuous vector space:

$$
e_i=
[e_a,
e_\tau,
e_\gamma,
e_c]
$$

where each component is a learnable embedding vector.

The concatenated embedding is then processed through a multilayer perceptron:

$$
h_i

\phi(e_i)
$$

producing a latent representation of the modelling term.

This representation allows semantically similar modelling operations to occupy nearby regions of the latent space.

---

## DeepSet Specification Encoder

A utility specification consists of a collection of modelling terms:

$$
S=
{
t_1,
t_2,
\ldots,
t_n
}
$$

Unlike natural language, utility specifications are naturally sets rather than sequences.

The ordering of terms is irrelevant:

$$
{
A,B,C
}

{
C,B,A
}
$$

Consequently, the encoder must be permutation invariant.

Formally,

$$
f(S)

f(\pi(S))
$$

for any permutation $\pi$.

To satisfy this requirement, Delphos uses a DeepSet architecture.

Each term is first encoded independently:

$$
h_i

\phi(t_i)
$$

and then aggregated using a permutation-invariant pooling operation:

$$
z

\rho
\Bigg(
\frac{1}{n}
\sum_{i=1}^{n}
\phi(t_i)
\Bigg)
$$

where:

- $\phi(\cdot)$ encodes individual modelling terms.
- $\rho(\cdot)$ produces the final specification representation.

The resulting vector

$$
z \in \mathbb{R}^{d}
$$

provides a fixed-dimensional representation of the specification regardless of its complexity.

---

## Deep Q-Network Policy

Given a latent specification representation $z$, Delphos must decide which modelling action should be executed next.

To achieve this, Delphos uses a Deep Q-Network (DQN).

The policy network estimates:

$$
Q(z,a)
$$

for every modelling action.

The Q-value represents the expected future reward obtained by executing action $a$ in specification state $z$.

The network therefore learns the mapping:

$$
Q_\theta :
\mathbb{R}^{d}
\rightarrow
\mathbb{R}^{|\mathcal A|}
$$

where:

- Input dimension $d$ is determined by the specification encoder.
- Output dimension equals the size of the action space.

The selected action is

$$
a^*

\arg\max_a
Q(z,a)
$$

subject to feasibility constraints.

The Q-network therefore learns which modelling operations are most likely to improve future model quality.

---

## Double DQN Learning

Standard DQN algorithms tend to overestimate action values.

To reduce this bias, Delphos uses Double DQN.

Two networks are maintained:

Policy Network

Used to select actions.

$$
Q_{\theta}
$$

Target Network

Used to compute learning targets.

$$
Q_{\theta^-}
$$

The target network is updated gradually using Polyak averaging:

$$
\theta^-
\leftarrow
\tau \theta
+
(1-\tau)\theta^-
$$

where $\tau$ controls the update rate.

This significantly improves training stability and prevents oscillatory learning behaviour.

## Action Masking

Unlike many reinforcement learning environments, not all actions are valid.

For example:

- Adding an attribute already present in the specification.
- Applying the same transformation twice.
- Introducing unavailable interactions.
- Creating duplicate modelling terms.

Consequently, Delphos uses action masking.

Let

$$
A_{valid}
\subseteq
A
$$

denote the set of valid actions for the current specification.

The modified Q-values become:

$$
Q’(a)

\begin{cases}
Q(a),
&
a \in A_{valid}
\
-\infty,
&
otherwise
\end{cases}
$$

The agent then selects actions using

$$
a^*

\arg\max_a
Q’(a)
$$

This guarantees that only feasible specifications can be generated.

Action masking dramatically reduces the effective search space and substantially improves sample efficiency.

---

## Experience Replay

After each modelling episode, Delphos stores transitions in a replay buffer.

Each transition consists of:

$$
(s_t,
a_t,
r_t,
s_{t+1},
d_t)
$$

where:

- $s_t$ is the current specification.
- $a_t$ is the selected modelling action.
- $r_t$ is the observed reward.
- $s_{t+1}$ is the resulting specification.
- $d_t$ indicates whether the episode terminated.

During training, mini-batches are sampled randomly from the replay buffer.

This breaks temporal correlations and improves learning stability.

---

## Multitask Learning and Transfer

The key innovation of Delphos is not merely the use of experience replay, but the fact that experiences originate from multiple discrete choice modelling tasks.

Let

$$
D_\tau
$$

denote the experience collected from task $\tau$.

The replay buffer contains:

$$
D

\bigcup_{\tau=1}^{N_{tasks}}
D_\tau
$$

Consequently, the agent learns from modelling experiences generated across multiple datasets simultaneously.

This creates a shared repository of modelling knowledge.

For example:

- Travel time transformations may be useful across many transport datasets.
- Cost variables may consistently benefit from generic specifications.
- Certain interaction structures may repeatedly improve model fit.

Rather than learning dataset-specific heuristics, Delphos learns transferable modelling strategies that can generalise to previously unseen datasets.

---

## Inference on Unseen Tasks

Once training is complete, only the encoder and policy network are required.

Given a new dataset:

1. The task is converted into the global modelling grammar.
2. Candidate specifications are encoded into latent vectors.
3. The policy network proposes modelling actions.
4. Utility specifications are generated sequentially.
5. Estimated models are evaluated according to the chosen objective.

No additional training is required.

The resulting workflow enables Delphos to act as an intelligent specification assistant capable of transferring modelling knowledge across discrete choice modelling tasks.

---

## Summary

Delphos combines representation learning and reinforcement learning to automate model specification.

Its core components are:

| Component                | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| Global Modelling Grammar | Common representation across datasets     |
| Term Encoder             | Learns representations of modelling terms |
| DeepSet Encoder          | Produces specification embeddings         |
| Deep Q-Network           | Learns modelling policies                 |
| Double DQN               | Stabilises learning                       |
| Action Masking           | Ensures feasibility                       |
| Replay Buffer            | Stores modelling experience               |
| Multitask Learning       | Enables transfer across datasets          |
