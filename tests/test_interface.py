"""Testing module for interface.py."""
import pytest

from etl_tools.download.interface import IDownloader


class MockDownloader(IDownloader):
    """Mocks an implementation of IDownloader."""

    def download_file(self) -> bytes:
        """Downloads a single file and stores it into memory."""
        return b"test"

    def save_to_parquet(self, content: bytes) -> None:
        """Save in-memory stored file to parquet."""
        return

    def download_to_parquet(self) -> None:
        """Downloads a single file into memory, converts it to parquet and stores locally."""
        return


@pytest.fixture(name="mock_downloader")
def fixture_mock_downloader() -> MockDownloader:
    """Fixture providing MockDownloader instance."""
    mock_downloader = MockDownloader("random.url")
    return mock_downloader


def test_init_url(mock_downloader: MockDownloader) -> None:
    """Tests if the url is correctly initiliazed."""
    assert mock_downloader.url == "random.url"


def test_isinstance(mock_downloader: MockDownloader) -> None:
    """Tests if mock_downloader is instance of IDownloader."""
    assert isinstance(mock_downloader, IDownloader)


def test_methods(mock_downloader: MockDownloader) -> None:
    """Tests if all required methods are implemented."""
    assert mock_downloader.download_file() == b"test"
    assert mock_downloader.save_to_parquet(b"test") is None  # type: ignore[func-returns-value]
    assert mock_downloader.download_to_parquet() is None  # type: ignore[func-returns-value]
