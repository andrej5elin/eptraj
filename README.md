# eptraj

`eptraj` is a Python 3D particle-tracking simulator for coupled AC
electrophoresis, pressure-driven flow, and Brownian motion in microfluidic
channels.

## Installation

Install the package from PyPI with pip:

```bash
python -m pip install eptraj
```

The PyPI package provides the `eptraj.py` module. Import it in Python with:

```python
import eptraj
```

## Publishing

The GitHub Actions workflow publishes distributions to PyPI when a `v*` tag is
pushed. Configure a PyPI trusted publisher for this repository, using the
`.github/workflows/publish.yml` workflow and the `pypi` environment, then bump
`__version__` in `eptraj.py` and push a matching version tag (for example,
`v0.1.0`).
