# Equinix Python SDK

[![Release](https://img.shields.io/github/v/release/equinix/equinix-sdk-python)](https://github.com/equinix/equinix-sdk-python/releases/latest)
[![PyPi](https://img.shields.io/pypi/v/equinix)](https://pypi.org/project/equinix)

This is the official Python SDK for Equinix services.  This SDK is currently provided with a major version of `v0`. We aim to avoid breaking changes to this library, but they will certainly happen as we work towards a stable `v1` library.

Each Equinix service supported by this SDK is maintained as a separate submodule that is generated from the OpenAPI specification for that service.  If any Equinix service is not supported by this SDK and you would like to see it added, please [submit a change request](CONTRIBUTING.md)

## Installation

To import this library into your Python project:

```sh
pip install equinix
```

In a given Python file, you can then import all available services: 

```python
import equinix
```

Or you can import individual services:

```python
from equinix.services import metalv1
```

## Usage

You can see usage of the generated code in the [`examples` directory](https://github.com/equinix/equinix-sdk-python/tree/main/examples).
