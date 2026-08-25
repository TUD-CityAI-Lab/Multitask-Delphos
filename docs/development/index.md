# Development

The umbrella coordinates four independently versioned repositories. Final users should install `delphos`; they do not need the training code or this complete workspace.

Choose the smallest repository that owns your change:

| Change | Repository |
| --- | --- |
| Final-user API, CLI, packaged datasets, or user notebooks | `gnova3/Delphos` |
| Paper 1 single-task code or experiments | `gnova3/delphos-single-task` |
| Multitask training, fine-tuning, checkpoints, or Paper 2 experiments | `gnova3/Delphos-training` |
| Canonical data, preparation, or aggregation schemas | `TUD-CityAI-Lab/transport-choice-datasets` |
| Cross-project navigation, papers, or documentation site | `TUD-CityAI-Lab/Multitask-Delphos` |

The umbrella records approved component commits as Git submodules. It coordinates the ecosystem; it does not replace each component’s issue tracker, tests, or release history.

Continue with [Components](components.md) to clone or update the workspace, [Contribution Workflow](contribution_workflow.md) to make a change, or [Documentation](documentation.md) to work on this site.
