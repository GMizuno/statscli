import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="StatsCli",
    version="0.1.0",
    description="CLI to extract some statistics from files",
    url="pamps.io",
    python_requires=">=3.10",
    long_description="CLI to extract some statistics from Parquet, ORC, Avro and .... This CLI uses Typer and Polars",
    long_description_content_type="text/markdown",
    author="Gabriel Mizuno",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["stats = statscli.cli:main"]
    }
)