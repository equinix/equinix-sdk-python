# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "equinix"
VERSION = open('version').read()
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >=2.2.2, <3.0.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Equinix SDK for Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Equinix",
    url="https://github.com/equinix/equinix-sdk-python",
    keywords=["Equinix"],
    install_requires=REQUIRES,
    python_requires=PYTHON_REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    package_data={"equinix.services.metalv1": ["py.typed"]},
)
