"""Module describing the Uploader interface."""

from abc import ABC, abstractmethod
from pathlib import Path


class IUploader(ABC):  # pylint: disable=too-few-public-methods
    """Uploader interface."""

    @abstractmethod
    def upload_parquet(self, file_path: Path) -> int:
        """Uploads a single parquet file to final destination"""
        raise NotImplementedError("Subclass hasn't implemented method 'download_file'.")
