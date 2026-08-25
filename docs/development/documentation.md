# Documentation Development

The Markdown sources under `docs/` are the only documentation files edited by hand. The generated `site/` directory is ignored and must not be committed.

## Local Setup

Install the pinned documentation dependencies:

```bash
python -m pip install --requirement requirements-docs.txt
```

Preview the site locally:

```bash
mkdocs serve
```

Run the same strict build used in continuous integration:

```bash
mkdocs build --strict
```

## Automated Checks and Deployment

Pull requests that change documentation run a strict MkDocs build. Broken navigation entries, missing local links, and MkDocs warnings therefore prevent the documentation change from being merged.

After an approved documentation change reaches `main`, GitHub Actions builds the site and deploys the generated artifact to GitHub Pages. Generated HTML is never committed to the repository.
