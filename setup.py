from pathlib import Path
import re

from setuptools import setup
from setuptools.command.build_py import build_py


root = Path(__file__).parent
source = (root / "eptraj.py").read_text(encoding="utf-8")
version = re.search(r'^__version__ = "([^"]+)"$', source, re.MULTILINE).group(1)
csv_files = sorted((root / "csv").glob("*.csv"))


class BuildPyWithCsv(build_py):
    def run(self):
        super().run()
        destination = Path(self.build_lib) / "csv"
        self.mkpath(str(destination))
        for csv_file in csv_files:
            self.copy_file(str(csv_file), str(destination / csv_file.name))

    def get_outputs(self, include_bytecode=1):
        outputs = super().get_outputs(include_bytecode)
        outputs.extend(
            str(Path(self.build_lib) / "csv" / csv_file.name)
            for csv_file in csv_files
        )
        return outputs

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
    cmdclass={"build_py": BuildPyWithCsv},
)
