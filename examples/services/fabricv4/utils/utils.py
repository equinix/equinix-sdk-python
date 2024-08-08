# Utility functions.

from datetime import datetime
from enum import Enum


def pr_cyan(skk):
    """Prints the given string in cyan color."""
    print("\033[96m {}\033[00m".format(skk))


def pr_yellow(skk):
    """Prints the given string in yellow color."""
    print("\033[93m {}\033[00m".format(skk))


def pr_purple(skk):
    """Prints the given string in purple color."""
    print("\033[95m {}\033[00m".format(skk))


def custom_serializer(obj):
    """
        Custom JSON serializer to handle various object types.
        - Handles Enums by returning their value.
        - Converts datetime objects to ISO format.
        - Converts objects with `__dict__` attribute to dictionary representation.
    """
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, datetime):
        return obj.isoformat()
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return str(obj)