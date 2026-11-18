""" "Implementation of customed errors."""

from pathlib import Path


class EmptyDirectoryError(ValueError):
    """Raised when the directory is empty."""

    def __init__(self, path: Path):
        self.path = path
        super().__init__(self.path)
