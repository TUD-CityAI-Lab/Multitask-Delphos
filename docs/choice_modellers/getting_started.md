---
hide:
  - toc
---

# Getting Started

## What is Delphos?

Delphos is a Python library that assists the specification of discrete choice models.

Rather than manually exploring large numbers of candidate utility specifications, Delphos uses reinforcement learning to learn modelling strategies from previous choice modelling specification tasks, and uses these strategies to propose candidate specifications on new datasets.

The goal is not to replace the human-modeller, but to assist the specification process by reducing the effort required to identify useful model structures.

---

## Installing Delphos

Install Python 3.11 or later. Delphos is an open-source Python package that uses Python 3.11. Ensure Python is installed in your computer, if not, follow the instructions on the [official Python website](https://www.python.org/downloads/).

It is recommended to use a virtual environment to avoid conflicts with other Python packages. You may run the following commands to create a virtual environment:

!!! example "Step 1 — Create a virtual environment"

```bash
python -m venv .venv
```

!!! example "Step 2 — Activate the environment"

=== "macOS / Linux"

    ```bash
    source .venv/bin/activate

    ```

=== "Windows"

    ```bash
    .venv\Scripts\activate

    ```

Having an environment configured, you can install the required dependencies for Delphos using pip:

!!! example "Step 3 — Install Delphos requirements"

```bash
pip install -r requirements.txt
```

!!! example "Step 4 — Verify the installation"

```python
import delphos

print(delphos.__version__)
```

If no errors are produced, Delphos has been successfully installed. The installed version should be `0.1.0`.

## Next Steps

Continue to the [First Application](./first_application.md) tutorial to run Delphos on a discrete choice dataset and generate your first utility specifications.

## Interactive Tutorials

The latest end-to-end Delphos tutorials from the submodule notebooks are available here:

- [01. Getting Started](../tutorials/01_getting_started.md)
- [02. Datasets and User Data](../tutorials/02_datasets_and_user_data.md)
- [02. Your Own Datasets](../tutorials/02_your_own_datasets.md)
- [03. Modelling Space](../tutorials/03_modelling_space.md)
- [04. Delphos Parameters](../tutorials/04_delphos_parameters.md)
- [05. Reward Function](../tutorials/05_reward_function.md)
- [06. Quick Results](../tutorials/06_quick_results.md)
- [07. Robust Results](../tutorials/07_robust_results.md)
- [08. Environment and Outputs](../tutorials/08_environment_and_outputs.md)
