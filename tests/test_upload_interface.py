"""Testing module for upload/interface.py."""
from pathlib import Path
import pytest

from etl_tools.upload.interface import IUploader


class MockUploader(IUploader):  # pylint: disable=too-few-public-methods
    """Mocks an implementation of IDownloader."""

    def upload_parquet(self, file_path: Path) -> int:
        """Uploads a single parquet file to final destination"""
        return 1


@pytest.fixture(name="mock_uploader")
def fixture_mock_uploader() -> MockUploader:
    """Fixture providing MockDownloader instance."""
    mock_uploader = MockUploader()
    return mock_uploader


def test_isinstance(mock_uploader: MockUploader) -> None:
    """Tests if mock_downloader is instance of IDownloader."""
    assert isinstance(mock_uploader, IUploader)


def test_methods(mock_uploader: MockUploader) -> None:
    """Tests if all required methods are implemented."""
    assert mock_uploader.upload_parquet(Path("test.parquet")) == 1
