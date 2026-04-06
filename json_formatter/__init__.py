"""
json-formatter - Format and pretty-print JSON with validation

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import JsonFormatter, format, process, main

__all__ = ["JsonFormatter", "format", "process", "main"]
