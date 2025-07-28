"""Main entry point for running nk2dl as a module.

This allows running the package with 'python -m nk2dl_cli'.
"""

from .cli.commands import main

if __name__ == "__main__":
    main() 