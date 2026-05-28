# Reward Functions

The reward function is the core of how Delphos learns. It translates the numerical output of an Apollo model estimation (such as Log-Likelihood or BIC) into a signal that the reinforcement learning agent can use to improve its policy.

## Default Rewards

Delphos comes with several built-in reward functions designed for discrete choice modelling.

### BIC Reward

The Bayesian Information Criterion (BIC) balances Goodness-of-Fit with a penalty for the number of parameters. This is often the preferred metric for finding parsimonious models.

The reward is defined as the relative improvement in BIC over the previous best specification found by the agent.

### Log-Likelihood Reward

A simpler reward based purely on the improvement in Log-Likelihood. This tends to encourage the agent to add more parameters until the model fails to converge.

## Defining Custom Rewards

You can define custom reward functions by subclassing the base `RewardFunction` class in `delphos-core`.

```python
from mdp.reward import RewardFunction

class CustomAICReward(RewardFunction):
    def calculate(self, previous_metrics, new_metrics):
        # Your custom logic here
        aic_improvement = previous_metrics.aic - new_metrics.aic
        return max(0, aic_improvement)
```
