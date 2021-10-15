from setuptools import find_packages, setup
from package import __version__

setup(
    name="package",
    packages=find_packages(exclude=["tests"]),
    version=__version__,
    description="Test Package",
    author="Test",
    license="MIT",
    install_requires=["pydantic[dotenv]", "httpx", "authlib", "tenacity"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==6.2.2"],
    test_suite="tests",
)
