from setuptools import setup, find_packages
from glob import glob
from pybind11.setup_helpers import Pybind11Extension, build_ext

so_files = glob("linalg/python/linalg_core*.so")

ext_modules = [
    Pybind11Extension(
        "linalg_core",
        ["linalg/src/LinearAlgebra.cpp",
         'linalg/python/bindings.cpp'],
        include_dirs=["linalg/src"],
    ),
]

setup(
    name="linalg",
    version="0.1.0",
    description="Linear Algebra Python Bindings using Pybind11",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    packages=find_packages(),
    package_data={
        "linalg": ["python/*.so", "src/*.h"],
    },
    package_dir={"linalg": "linalg"},
    python_requires=">=3.6",
)
