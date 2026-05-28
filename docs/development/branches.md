# Branching Strategy

The Delphos repositories follow a standardized branching strategy to ensure stable releases while allowing active research and development.

## Main Branches

- **`main`**: The primary, stable branch. Contains code that has been tested and is considered stable. This branch corresponds to the current release versions.
- **`develop`**: The integration branch for new features and research experiments. All feature branches merge into `develop` before eventually being merged into `main` for a release.

## Supporting Branches

- **`feature/<feature-name>`**: Used for developing new features or conducting new experiments. Branched from `develop` and merged back into `develop`.
- **`bugfix/<bug-name>`**: Used to fix non-critical bugs found in `develop`.
- **`hotfix/<bug-name>`**: Used to quickly patch critical issues in `main`. Merged into both `main` and `develop`.
- **`docs/<doc-updates>`**: For updates that strictly modify documentation.

## Example Workflow

```bash
# Create a new feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/new-reward-function

# ... Make changes and commit ...

# Push and create a Pull Request to develop
git push origin feature/new-reward-function
```
