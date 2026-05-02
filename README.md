# zuzu-diagrams

Architecture diagrams generated with [mingrammer/diagrams](https://github.com/mingrammer/diagrams) and published automatically to GitHub Pages via GitHub Actions.

## Live site

GitHub Pages URL is published after the first workflow run:  
`https://teamzuzu.github.io/zuzu-diagrams/`

## How it works

1. **Write** a Python diagram script in the `diagrams/` directory.
2. **Push** to `main` — the [GitHub Actions workflow](.github/workflows/diagrams.yml) automatically:
   - Installs Graphviz and the `diagrams` Python library.
   - Runs every `*.py` file in `diagrams/` to produce PNG images.
   - Generates an `index.html` gallery page.
   - Deploys everything to GitHub Pages.

## Adding a new diagram

Create a new `.py` file inside `diagrams/`. The file should use `show=False` and
specify an explicit `filename` so the image lands in the right place:

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("My Diagram", filename="my_diagram", show=False):
    EC2("server")
```

Commit and push — the workflow takes care of the rest.

## Local development

```bash
# Install system dependency
brew install graphviz          # macOS
sudo apt-get install graphviz  # Debian/Ubuntu

# Install Python library
pip install diagrams

# Run a diagram script
python diagrams/web_service.py
```

## Diagram library reference

See the full provider catalogue at <https://diagrams.mingrammer.com/docs/nodes/aws>.