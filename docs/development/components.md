# Managing Components

`Multitask-Delphos` is the umbrella repository for the Delphos ecosystem. Its implementation and research code lives in four independently versioned component repositories:

- `components/delphos`: end-user inference package;
- `components/delphos-single-task`: Paper 1 single-task implementation;
- `components/delphos-training`: multitask training and Paper 2 reproduction; and
- `components/transport-choice-datasets`: canonical dataset collection.

The `components/` directories are Git submodules. The umbrella records an exact approved commit for each component, while every component remains independently cloneable and developable.

## Cloning the Repository

Clone the umbrella and initialise all components with:

```bash
git clone --recurse-submodules https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
```

If the umbrella was cloned without its components, run:

```bash
git submodule update --init --recursive
```

## Working on One Component

Enter the component directory, create a branch there, and commit changes in that component repository:

```bash
cd components/delphos-training
git switch -c my-change
```

The umbrella should continue to point to the last approved component commit until the component change has been reviewed and pushed.

## Updating an Umbrella Pin

After an approved component commit has been pushed, check out that exact commit inside `components/` and commit the changed pointer in the umbrella:

```bash
cd components/delphos-training
git fetch origin
git checkout <approved-commit>
cd ../..
git add components/delphos-training
git commit -m "Update delphos-training component"
```

Do not use `git submodule update --remote --merge` as the normal umbrella workflow. It follows moving branches and can update several components without an explicit review of their new pins.
