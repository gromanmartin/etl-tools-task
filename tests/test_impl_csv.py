"""Module for testing impl_csv.py"""
from pathlib import Path
import pytest
import pandas as pd
import responses
from pandas.testing import assert_frame_equal
from etl_tools.download.impl_csv import CSVDownloader


TEST_URL = "https://test.url"


@pytest.fixture(name="mock_csv_downloader")
def fixture_mock_csv_downloader() -> CSVDownloader:
    """Fixture providing MockDownloader instance."""
    mock_downloader = CSVDownloader()
    return mock_downloader


@responses.activate
def test_download_file(mock_csv_downloader: CSVDownloader) -> None:
    """Tests CSVDownloader's download_file method."""
    responses.get(TEST_URL, body=b"test")
    content = mock_csv_downloader.download_file(TEST_URL)
    assert content == b"test"


def test_save_to_parquet(tmp_path: Path, mock_csv_downloader: CSVDownloader) -> None:
    """Tests CSVDownloader's save_to_parquet method."""
    data = b"test\r\n1\r\n"
    mock_csv_downloader.save_to_parquet(data, tmp_path / "test.parquet")
    df = pd.read_parquet(tmp_path / "test.parquet")
    expected_df = pd.DataFrame({"test": 1}, index=[0])
    assert_frame_equal(df, expected_df)


@responses.activate
def test_download_to_parquet(tmp_path: Path, mock_csv_downloader: CSVDownloader) -> None:
    """Tests CSVDownloader's download_to_parquet method."""
    responses.get(TEST_URL, body=b"test\r\n1\r\n")
    mock_csv_downloader.download_to_parquet(TEST_URL, tmp_path / "test.parquet")
    df = pd.read_parquet(tmp_path / "test.parquet")
    expected_df = pd.DataFrame({"test": 1}, index=[0])
    assert_frame_equal(df, expected_df)
