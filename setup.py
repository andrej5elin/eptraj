from pathlib import Path
import re

from setuptools import setup


root = Path(__file__).parent
source = (root / "eptraj.py").read_text(encoding="utf-8")
version = re.search(r'^__version__ = "([^"]+)"$', source, re.MULTILINE).group(1)

setup(
    name="eptraj",
    version=version,
    description="3D particle-tracking simulator for microfluidic channels",
    long_description=(root / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    py_modules=["eptraj"],
    python_requires=">=3.9",
    install_requires=["numpy"],
    license="MIT",
)
