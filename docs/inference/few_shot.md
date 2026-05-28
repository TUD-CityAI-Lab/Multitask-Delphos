# Few-Shot Inference

Few-shot inference (also related to Transfer Learning) involves taking a pre-trained agent and allowing it to train for a small number of episodes on the new dataset before generating the final specifications.

This is useful when the new dataset has characteristics that are slightly different from the agent's training distribution, and you want to give the agent a chance to adapt its policy.

## Running Few-Shot Inference

Currently, few-shot inference is managed via the `delphos-core` repository, as it requires the training loop to be active.

```python
# Pseudo-code for few-shot adaptation
from delphos_core import RLTrainer, DelphosAgent

agent = DelphosAgent.load_pretrained("multitask_base")

trainer = RLTrainer(
    agent=agent,
    dataset="my_dataset.csv",
    schema="my_dataset_schema.json"
)

# Train for a very small number of episodes (e.g., 5-10)
trainer.train(episodes=10)

# Now use the adapted agent to generate the Pareto front
pareto_front = agent.explore(steps=100)
```
