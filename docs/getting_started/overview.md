# What Delphos Does

Delphos treats utility specification as a sequence of modelling decisions. Starting from a simple specification, a trained agent chooses actions such as adding an attribute, changing its functional form, using generic or alternative-specific taste parameters, or interacting a parameter with a covariate.

The final-user workflow has four stages:

1. **Describe the choice problem.** Load a catalogue task or create a task for your own CSV.
2. **Constrain the modelling space.** Decide which attributes, transformations, taste structures, and covariates may be considered.
3. **Generate proposals.** Ask the trained agent for a diverse set of utility specifications.
4. **Estimate and review.** Send selected proposals to Apollo, inspect diagnostics and behavioural signs, and retain a defensible shortlist.

## What Delphos automates

Delphos automates the repetitive construction and exploration of candidate utility specifications. It can:

- reuse modelling strategies learned across transport choice datasets;
- generate valid utility structures from a task-specific grammar;
- produce Apollo parameter, utility, availability, and probability definitions;
- estimate proposals through Apollo when requested; and
- return proposal metadata and modelling results in tabular form.

## What remains the modeller's responsibility

Delphos does not decide whether a variable is causally meaningful, whether the data are appropriate, or whether a model is suitable for policy analysis. You remain responsible for:

- checking coding, scaling, availability, and missing values;
- defining a scientifically defensible modelling space;
- checking identification, convergence, parameter signs, and uncertainty;
- comparing models out of sample where appropriate; and
- documenting why a final specification was selected.

!!! note "A familiar mental model"

    Apollo users can think of Delphos as a specification layer placed before `apollo_estimate()`. Biogeme users can think of it as a learned search over a catalogue of expressions, with Apollo used as the current estimation engine.

## Recommended first session

1. Complete [Installation](installation.md).
2. Run the proposal-only [Quickstart](quickstart.md); it does not estimate models.
3. Follow the [First Application](../choice_modellers/first_application.md) to inspect generated Apollo code and optionally estimate a small shortlist.
4. Continue with the [User Guide](../user-guide/index.md) or work through the [Jupyter tutorials](../tutorials/index.md).
