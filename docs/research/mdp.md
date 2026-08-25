# MDP Formulation

Delphos treats model specification as a finite sequence of modelling decisions. The agent does not estimate taste parameters; it constructs the systematic utility specification that Apollo will estimate.

## Markov Decision Process

For a task $\tau$, the process is

$$
\mathcal M_\tau=(\mathcal S_\tau,\mathcal A, P_\tau,R_\tau,\gamma).
$$

| Element | Delphos interpretation |
| --- | --- |
| State $s_t$ | Current set of utility terms, with optional task context |
| Action $a_t$ | Add or modify a modelling term, or terminate |
| Transition $P_\tau$ | Deterministic application of a valid modelling operation |
| Reward $R_\tau$ | Quality of the Apollo-estimated terminal specification |
| Discount $\gamma$ | Credit assigned backwards through the construction sequence |

## State

A state is a valid specification represented as a set of tuples:

$$
s_t=\{(a_i,\tau_i,g_i,c_i)\}_{i=1}^{L_t}.
$$

It is kept symbolic for validation and Apollo generation, then encoded into a fixed-length vector for the Q-network. The empty specification is a valid initial state.

## Action

An action selects a modelling operation in the global catalogue. The runtime keeps only actions compatible with the task and current state. This action mask prevents duplicate terms, unavailable concepts, invalid transformations, and loops through already visited specifications.

The episode also contains an explicit termination decision. A maximum horizon provides a second stopping condition when no termination action is selected.

## Transition

Applying a valid action produces the next symbolic specification. The transition itself does not call Apollo. Estimation occurs when the terminal specification is evaluated, keeping a trajectory cheap until its outcome is needed.

## Reward and credit assignment

The default estimation reward compares the converged model log-likelihood, $LL(s)$, with the task’s null-model likelihood and scales it by the number of observations:

$$
r(s)=\tanh\!\left(\frac{LL(s)-LL_{\mathrm{null}}}{N}\right).
$$

Invalid or failed estimations receive the failure reward. The terminal reward is distributed backwards across the episode using $\gamma$, producing one replay transition per modelling decision.

This reward is a training objective, not a claim that the highest-reward model is automatically the preferred behavioural model. Final candidate selection still considers convergence, identification, plausibility, parsimony, and the intended application.

## Objective

The learned action-value function approximates

$$
Q^*(s,a)=\max_\pi\;\mathbb E_\pi\!\left[\sum_{k=0}^{H-t}\gamma^k r_{t+k}\mid s_t=s,a_t=a\right].
$$

At inference time, the pretrained policy uses these values to navigate the specification space without another reinforcement-learning update.

The research notebooks [Task](../tutorials/research/01_task.ipynb), [State](../tutorials/research/02_state.ipynb), and [Action](../tutorials/research/03_action.ipynb) expose these objects directly.
