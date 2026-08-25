# Transfer and Evaluation

Transfer asks whether modelling knowledge learned across source tasks is useful on a target task. Delphos separates this question into three evaluation settings.

## Evaluation settings

| Setting | Learned parameters updated? | Purpose |
| --- | --- | --- |
| Zero-shot inference | No | Test direct transfer of the pretrained representation and policy |
| Fine-tuning | Yes, selected modules | Measure adaptation with target-task experience |
| From-scratch training | Yes, random initialisation | Provide a target-task learning baseline |

These settings should use the same target-task schema, modelling grammar, estimation environment, search budget, and reporting rules. Otherwise differences cannot be attributed to transfer.

## Zero-shot inference

The target task is mapped into the checkpoint’s global catalogue. The encoder and policy remain frozen while the agent proposes candidates. This is the mode exposed by the final-user package.

Zero-shot evaluation should report more than the best model. Useful measures include:

- valid-action and successful-estimation rates;
- unique specifications and action diversity;
- best and distributional fit statistics under a fixed proposal budget;
- complexity and free-parameter counts;
- runtime and cache-hit rates; and
- behavioural review of the resulting candidates.

## Fine-tuning

The training implementation can update the policy only, the encoder only, or both. These modes answer different questions: policy-only adaptation changes which operations are preferred, whereas encoder adaptation changes how specifications are represented.

Fine-tuning results should state which parameters were trainable and whether the optimiser state was resumed or newly initialised. Target-task Apollo evaluations used for adaptation must not also be treated as unseen evaluation observations.

## From scratch

A randomly initialised target-task agent controls for the amount of target experience. It is not equivalent to manual specification and should not replace behavioural benchmarks such as a documented linear-additive model.

## Avoiding leakage

Dataset splits alone are not sufficient. Repeated Apollo results may be present in a cache, and catalogue construction can expose target concepts. A defensible protocol records:

- which tasks built the catalogue;
- which tasks supplied replay transitions;
- whether target results existed in the estimation cache;
- which checkpoint was selected and using what validation signal; and
- whether the target was used during hyperparameter choice.

See [Papers and Reproducibility](papers.md) for the codebases associated with the two experimental programmes.
