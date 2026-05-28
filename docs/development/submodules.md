# Managing Submodules

The `Multitask-Delphos` repository is the "hub" repository. The actual code lives in submodules (`delphos-core`, `delphos` (user), and `delphos-datasets`).

This structure allows each component to be versioned and installed independently while keeping the ecosystem logically grouped.

## Cloning the Repository

When cloning the main repository, you must initialize the submodules:

```bash
# Clone and initialize submodules in one command
git clone --recurse-submodules https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
```

If you already cloned it without submodules:
```bash
git submodule update --init --recursive
```

## Updating Submodules

To update all submodules to the latest commits on their respective remote tracking branches:

```bash
git submodule update --remote --merge
```

## Making Changes to Submodules

If you want to contribute code to `delphos-core`, you must commit those changes within the `submodules/delphos-core` directory. 

1. `cd submodules/delphos-core`
2. Make your branch, commit, and push *from within that directory*.
3. Once the submodule is updated on GitHub, go back to the main repository root.
4. Commit the new submodule pointer in the main repository:
   ```bash
   cd ../.. # Back to Multitask-Delphos root
   git add submodules/delphos-core
   git commit -m "Update delphos-core submodule pointer"
   git push
   ```
