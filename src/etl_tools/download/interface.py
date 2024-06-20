"""Module describing the Downloader interface."""

from abc import ABC, abstractmethod
from pathlib import Path


class IDownloader(ABC):
    """Downloader interface."""

    @abstractmethod
    def download_file(self, url: str) -> bytes:
        """Downloads a single file and stores it into memory."""
        raise NotImplementedError("Subclass hasn't implemented method 'download_file'.")

    @abstractmethod
    def save_to_parquet(self, content: bytes, file_path: Path) -> None:
        """Save in-memory stored file to parquet."""
        raise NotImplementedError("Subclass hasn't implemented method 'save_to_parquet'.")

    @abstractmethod
    def download_to_parquet(self, url: str, file_path: Path) -> None:
        """Downloads a single file into memory, converts it to parquet and stores locally."""
        raise NotImplementedError("Subclass hasn't implemented method 'download_to_parquet'.")
