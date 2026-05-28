# Contribution Workflow

We welcome contributions to Delphos! Whether you are adding new features, fixing bugs, or improving documentation, please follow this workflow.

## 1. Open an Issue
Before writing any code, check the issue tracker to see if your idea is already being worked on. If not, open a new issue describing the bug you found or the feature you want to add.

## 2. Setup your Development Environment
Clone the repository and its submodules. Create a virtual environment and install the development requirements.

## 3. Create a Branch
Following our [Branching Strategy](branches.md), create a new branch for your work.
```bash
git checkout -b feature/my-awesome-contribution develop
```

## 4. Make Changes
Write your code, ensuring you follow existing style conventions. Write tests for your new features.

## 5. Commit and Push
Commit your changes with clear, descriptive commit messages.
```bash
git commit -m "Add new reward function for convergence speed"
git push origin feature/my-awesome-contribution
```

## 6. Open a Pull Request
Open a Pull Request (PR) against the `develop` branch. Link the PR to the issue you opened in Step 1. A maintainer will review your code.
