# Equinix Python SDK

[![Maintained](https://img.shields.io/badge/stability-maintained-green.svg)](https://github.com/equinix-labs/equinix-labs/blob/main/maintained-statement.md)
[![Release](https://img.shields.io/github/v/release/equinix/equinix-sdk-python)](https://github.com/equinix/equinix-sdk-python/releases/latest)
[![GoDoc](https://godoc.org/github.com/equinix/equinix-sdk-go?status.svg)](https://godoc.org/github.com/equinix/equinix-sdk-go)

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
