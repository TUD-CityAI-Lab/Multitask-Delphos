# Branching Strategy

Delphos uses a simple GitHub flow in each repository.

## Permanent branch

`main` is the protected integration and release branch. It should remain buildable and should receive changes through reviewed pull requests once branch protection is enabled.

## Short-lived branches

- `feature/<topic>` for user-facing or architectural additions;
- `fix/<topic>` for defects;
- `docs/<topic>` for documentation and notebooks; and
- `research/<topic>` for bounded experimental work intended for a research component.

Branch from the current `main`, keep the branch focused, and delete it after merge. Release tags—not long-lived release branches—identify immutable versions used by papers and packages.

## Component and umbrella branches are independent

A branch inside `components/delphos-training` belongs to the training repository. A branch at the umbrella root belongs to `Multitask-Delphos`. They do not share commits.

When work changes a component and its umbrella pin:

1. merge and push the component change;
2. check out the approved component commit in the umbrella;
3. create an umbrella branch;
4. commit the changed submodule pointer; and
5. open a separate umbrella pull request.

Never point the umbrella at an unpublished local component commit: collaborators and automation cannot retrieve it.
