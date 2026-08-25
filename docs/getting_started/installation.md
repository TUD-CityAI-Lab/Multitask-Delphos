# Installation

Delphos combines Python inference code with an R/Apollo estimation backend. Proposal generation can be explored without running Apollo, but model estimation requires both environments.

## Requirements

- Python 3.10 or later;
- R 4.4 or later for estimation;
- Apollo 0.3.7; and
- a working C/C++ toolchain if your platform needs to build Python or R dependencies.

## Install the current pre-release

The source repository is private during release preparation. Collaborators with access can install it as follows:

```bash
git clone https://github.com/gnova3/Delphos.git
cd Delphos
python -m venv .venv
```

Activate the environment:

=== "macOS / Linux"

    ```bash
    source .venv/bin/activate
    ```

=== "Windows PowerShell"

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

Install the package in editable mode:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

After the public release, the final-user installation will be:

```bash
python -m pip install delphos
```

Public users should wait for that release; there is not yet a supported public installation. The documentation is being published early so the interface and examples can be reviewed before packaging.

## Install R and Apollo

From the Delphos repository, run the supplied installer:

```bash
Rscript install_r_requirements.R
```

The script verifies R and installs the Apollo version expected by the package. Apollo users may keep their usual R installation; Delphos connects to it through `rpy2`.

## Verify the installation

Check the Python package and bundled datasets:

```bash
python -c "import delphos as dp; print(len(dp.list_datasets()))"
```

Then check the R environment:

```bash
Rscript -e 'library(apollo); packageVersion("apollo")'
```

## Common setup problems

### Python cannot find R

If `rpy2` cannot discover R, confirm that `R` is available from your terminal:

```bash
R --version
```

On systems with several R installations, set `R_HOME` to the installation you want Delphos to use before activating the Python environment.

### Proposal generation works but estimation fails

This usually means the Python package is installed but Apollo is unavailable or has a different version. Re-run `install_r_requirements.R`, restart the Python session, and use the debugging options described in [Estimate with Apollo](../user-guide/apollo-estimation.md).

### You only want to read the notebooks

Install JupyterLab in the same environment:

```bash
python -m pip install jupyterlab
jupyter lab
```

The documentation site renders every notebook directly, so Jupyter is only required when you want to run or modify the cells yourself.
