from setuptools import setup, find_packages

setup(
    name="pyffmpeg",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyffmpeg = pyffmpeg.main:main",
        ],
    },
)
