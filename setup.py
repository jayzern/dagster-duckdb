from setuptools import find_packages, setup

setup(
    name="dagster_duckdb",
    packages=find_packages(exclude=["dagster_duckdb_tests"]),
    install_requires=[
        "dagster",
        "duckdb",
        "pandas",
        "sqlescapy",
        "lxml",
        "html5lib"
    ],
    extras_require={"dev": [
        "dagit",
        "dagster-webserver",
        "pytest",
        "localstack",
        "awscli",
        "awscli-local"
    ]},
)
