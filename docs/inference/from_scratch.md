# Training From Scratch

If zero-shot or few-shot inference does not yield satisfactory results, or if your dataset is highly unusual, you can train a Delphos agent entirely from scratch on your specific dataset.

This essentially treats your single dataset as the entire environment, and the agent will learn a policy specifically optimized for it.

## Running From Scratch

Training from scratch is done via the `delphos-core` repository.

```python
from delphos_core import RLTrainer, DelphosAgent

# Initialize a new, untrained agent
agent = DelphosAgent(config="default_config.yaml")

trainer = RLTrainer(
    agent=agent,
    dataset="my_dataset.csv",
    schema="my_dataset_schema.json"
)

# Train for a larger number of episodes to learn the policy
trainer.train(episodes=100)

# Generate specifications using the fully trained agent
pareto_front = agent.explore(steps=100)
```

**Note:** Training from scratch can be computationally expensive, as every step in every episode requires estimating a discrete choice model using Apollo.
