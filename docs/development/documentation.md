# Documentation Development

The documentation site is built from Markdown and Jupyter notebooks with MkDocs Material. Generated HTML under `site/` is ignored and must not be committed.

## Local setup

Install the pinned documentation dependencies:

```bash
python -m pip install --requirement requirements-docs.txt
```

Preview changes:

```bash
mkdocs serve
```

Before committing, run the same checks used by continuous integration:

```bash
python scripts/check_tutorial_sync.py
python scripts/check_documentation_links.py
mkdocs build --strict
```

## Information architecture

Place each page according to its primary reader and purpose:

- **Start Here** answers what Delphos does and gets a new user to a first proposal;
- **User Guide** explains final-user decisions and outputs;
- **Datasets** covers catalogue data, user schemas, and data responsibility;
- **Research & Papers** explains the MDP, learning architecture, evaluation, and reproducibility;
- **Development** covers repository coordination and contribution; and
- **Tutorials** contains runnable notebook sequences for final users and researchers.

Do not create a second navigation path to the same concept. Link to the canonical page instead.

## Writing for choice modellers

Use a modelling decision as the unit of explanation. A strong page normally follows this order:

1. state what the reader will obtain;
2. explain why the decision matters;
3. show the smallest complete example;
4. show or describe the important output;
5. explain how to interpret it; and
6. identify the next decision or common failure.

Prefer the language used by Apollo and Biogeme users: alternatives, availability, utility functions, parameters, transformations, log-likelihood, convergence, and model comparison. Introduce reinforcement-learning terms only when they change what the reader must decide.

Code must use the current public `delphos` API. Avoid placeholder output that looks real, and distinguish proposal generation from Apollo estimation. Never imply that the highest numerical score replaces behavioural judgement.

## Notebook policy

The source notebooks live in their owning components:

- `components/delphos/tutorials` for final-user notebooks; and
- `components/delphos-training/tutorials` for research notebooks.

The copies under `docs/tutorials/` are published byte for byte by the umbrella. `scripts/check_tutorial_sync.py` prevents silent drift. Edit a notebook in its component first, review and commit it there, update the umbrella component pin, and then refresh the published copy.

Notebooks should:

- have a clear title and learning outcomes;
- run from top to bottom in the documented environment;
- keep quick, deterministic cells early;
- guard Apollo estimations and long searches with explicit flags;
- explain results immediately after the output they concern;
- avoid machine-specific absolute paths; and
- end with saved artefacts or a clear next tutorial.

The documentation renderer does not execute notebooks. This avoids hidden network, R, dataset, and runtime dependencies during deployment. Commit only outputs that are stable, useful, and safe to publish.

## Automated deployment

Pull requests and pushes that affect documentation run a strict build. After an approved change reaches `main`, GitHub Actions builds the site and deploys its artifact to GitHub Pages. Generated HTML never enters Git history.
