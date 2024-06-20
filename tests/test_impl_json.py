"""Module for testing impl_json.py"""
from pathlib import Path
import json
import pytest

import pandas as pd
import responses
from pandas.testing import assert_frame_equal
from etl_tools.download.impl_json import JsonDownloader


TEST_URL = "https://test.url"


@pytest.fixture(name="mock_json_downloader")
def fixture_mock_json_downloader() -> JsonDownloader:
    """Fixture providing MockDownloader instance."""
    mock_downloader = JsonDownloader()
    return mock_downloader


@responses.activate
def test_download_file(mock_json_downloader: JsonDownloader) -> None:
    """Tests JsonDownloader's download_file method."""
    responses.get(TEST_URL, body=b"test")
    content = mock_json_downloader.download_file(TEST_URL)
    assert content == b"test"


def test_save_to_parquet(tmp_path: Path, mock_json_downloader: JsonDownloader) -> None:
    """Tests JsonDownloader's save_to_parquet method."""
    data = {
        "meta": {
            "view": {
                "columns": [
                    {"name": "test"},
                    {"name": "Draw Date"},
                    {"name": "Winning Numbers"},
                    {"name": "Multiplier"},
                ]
            }
        },
        "data": [[0, "18/6 2024", "15 15 12 36", 3]],
    }
    bdata = json.dumps(data).encode("utf-8")
    mock_json_downloader.save_to_parquet(bdata, tmp_path / "test.parquet")
    df = pd.read_parquet(tmp_path / "test.parquet")
    expected_df = pd.DataFrame({"Draw Date": "18/6 2024", "Winning Numbers": "15 15 12 36", "Multiplier": 3}, index=[0])
    assert_frame_equal(df, expected_df)


@responses.activate
def test_download_to_parquet(tmp_path: Path, mock_json_downloader: JsonDownloader) -> None:
    """Tests JsonDownloader's download_to_parquet method."""
    data = {
        "meta": {
            "view": {
                "columns": [
                    {"name": "test"},
                    {"name": "Draw Date"},
                    {"name": "Winning Numbers"},
                    {"name": "Multiplier"},
                ]
            }
        },
        "data": [[0, "18/6 2024", "15 15 12 36", 3]],
    }
    bdata = json.dumps(data).encode("utf-8")
    responses.get(TEST_URL, body=bdata)
    mock_json_downloader.download_to_parquet(TEST_URL, tmp_path / "test.parquet")
    df = pd.read_parquet(tmp_path / "test.parquet")
    expected_df = pd.DataFrame({"Draw Date": "18/6 2024", "Winning Numbers": "15 15 12 36", "Multiplier": 3}, index=[0])
    assert_frame_equal(df, expected_df)
