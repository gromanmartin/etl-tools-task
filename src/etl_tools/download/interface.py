"""Module describing the Downloader interface."""

from abc import ABC, abstractmethod


class IDownloader(ABC):
    """Downloader interface."""

    def __init__(self, url) -> None:
        self.url = url

    @abstractmethod
    def download_file(self) -> bytes:
        """Downloads a single file and stores it into memory."""
        raise NotImplementedError("Subclass hasn't implemented method 'download_file'.")

    @abstractmethod
    def save_to_parquet(self, content: bytes) -> None:
        """Save in-memory stored file to parquet."""
        raise NotImplementedError("Subclass hasn't implemented method 'convert_to_parquet'.")

    @abstractmethod
    def download_to_parquet(self) -> None:
        """Downloads a single file into memory, converts it to parquet and stores locally."""
        raise NotImplementedError("Subclass hasn't implemented method 'save_to_parquet'.")
