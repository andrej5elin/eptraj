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

## Array backends and acceleration

NumPy is the default array backend and is installed with `eptraj`. To use an
optional backend, install it separately:

```bash
python -m pip install mlx           # MLX, for supported Apple silicon systems
python -m pip install cupy-cuda12x  # CuPy, for CUDA 12.x
python -m pip install numba         # Numba acceleration for NumPy
```

For other CUDA versions or installation options, see the
[CuPy installation guide](https://docs.cupy.dev/en/stable/install.html).

Pass the imported array module (not its name as a string) to `set_backend`:

```python
import eptraj
import mlx.core as mx  # alternatively: import cupy as cp

eptraj.set_backend(mx)  # or eptraj.set_backend(cp)
```

Use `eptraj.set_backend(numpy)` after importing `numpy` to switch back.
Non-NumPy backends require single precision and cannot be used while Numba is
enabled. If `EPSIM_USE_DOUBLE_PRECISION=1` is set before importing `eptraj`,
only NumPy is supported.

Numba can accelerate NumPy computations for large-scale simulations. Install it
before importing `eptraj`; it is disabled by default and can be enabled or
disabled explicitly:

```python
import eptraj

eptraj.enable_numba()
# Run the simulation with the NumPy backend.
eptraj.disable_numba()
```

The Numba implementation does not support `DISABLE_*` simulation flags; it
supports the default flags and `ENABLE_LOW_FREQ_APPROXIMATION`.
