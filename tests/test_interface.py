"""Testing module for interface.py."""
from pathlib import Path
import pytest

from etl_tools.download.interface import IDownloader


class MockDownloader(IDownloader):
    """Mocks an implementation of IDownloader."""

    def download_file(self, url: str) -> bytes:
        """Downloads a single file and stores it into memory."""
        return b"test"

    def save_to_parquet(self, content: bytes, file_path: Path) -> None:
        """Save in-memory stored file to parquet."""
        return

    def download_to_parquet(self, url: str, file_path: Path) -> None:
        """Downloads a single file into memory, converts it to parquet and stores locally."""
        return


@pytest.fixture(name="mock_downloader")
def fixture_mock_downloader() -> MockDownloader:
    """Fixture providing MockDownloader instance."""
    mock_downloader = MockDownloader()
    return mock_downloader


def test_isinstance(mock_downloader: MockDownloader) -> None:
    """Tests if mock_downloader is instance of IDownloader."""
    assert isinstance(mock_downloader, IDownloader)


def test_methods(mock_downloader: MockDownloader) -> None:
    """Tests if all required methods are implemented."""
    assert mock_downloader.download_file("test.url") == b"test"
    assert (
        mock_downloader.save_to_parquet(b"test", Path("test_path.parquet")) is None  # type: ignore[func-returns-value]
    )
    assert (
        mock_downloader.download_to_parquet("test.url", Path("test_path.parquet"))  # type: ignore[func-returns-value]
        is None
    )
