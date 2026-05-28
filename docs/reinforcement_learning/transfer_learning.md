# Transfer Learning

Transfer learning is the ability of Delphos to apply knowledge gained from one set of transport choice datasets to a completely new one.

Instead of starting from a blank slate (random initialization), the agent starts with the neural network weights from a pre-trained `multitask` agent.

## Why Transfer Learning?

When a choice modeler looks at a new dataset, they don't test variables randomly. They use prior knowledge (e.g., "cost should probably be divided by income"). Delphos learns similar structural priors.

Transfer learning allows Delphos to:
1. Find good specifications much faster.
2. Avoid common specification traps (like severe multicollinearity).
3. Be useful in **zero-shot** or **few-shot** scenarios.

## Executing Transfer

To execute transfer learning, use the `run_transfer_benchmark.py` script provided in `delphos-core`.

```bash
python scripts/run_transfer_benchmark.py --agent pretrained_multitask.pt --target my_new_dataset.yaml
```
