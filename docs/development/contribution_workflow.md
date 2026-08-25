# Contribution Workflow

## 1. Identify the owner

Use the [component table](index.md) to choose the repository that owns the change. Open a component independently for focused work, or clone the umbrella when a change must be coordinated across repositories.

Check existing issues before starting a substantial feature. Open an issue when the intended behaviour or repository ownership needs discussion.

## 2. Start from an up-to-date `main`

Create a short-lived branch in the owning repository:

```bash
git switch main
git pull --ff-only
git switch -c docs/clearer-dataset-guide
```

Use a descriptive prefix such as `feature/`, `fix/`, `docs/`, or `research/`. A permanent `develop` branch is not required.

## 3. Make and verify the change

Keep changes focused. Run the component’s documented tests and any checks specific to the files you touched. For user-facing behaviour, update the relevant example or notebook in the same component.

Documentation changes should pass:

```bash
python scripts/check_tutorial_sync.py
python scripts/check_documentation_links.py
mkdocs build --strict
```

## 4. Commit and open a pull request

Write a commit message that describes the outcome, push the branch, and open a pull request into `main`:

```bash
git add <changed-files>
git commit -m "Clarify custom dataset validation"
git push --set-upstream origin docs/clearer-dataset-guide
```

The pull request should explain the modelling or software problem, the chosen change, verification performed, and any effect on APIs, data, checkpoints, or reproduction results.

## 5. Update the umbrella only after approval

When a component pull request is merged, the umbrella still points to the previous approved commit. Update its submodule pointer in a separate umbrella change and confirm that the documentation and cross-component checks pass.

This creates two reviewable facts: the component change itself, and the decision that the umbrella now coordinates that version.
