"""Testing module for upload/impl_db.py"""
from pathlib import Path
import pytest
import pandas as pd
from sqlalchemy import create_engine
from etl_tools.upload.impl_db import DBUploader


@pytest.fixture(name="mock_db_uploader")
def fixture_mock_db_uploader() -> DBUploader:
    """Fixture providing DBUploader instance."""
    mock_db_uploader = DBUploader(
        host="test_host", username="test_user", password="test_pw", db_name="test_db_name", port=123
    )
    return mock_db_uploader


@pytest.fixture(name="apply_mock_to_sql")
def fixture_apply_mock_to_sql(monkeypatch):
    """Fixture which replaces df.to_sql method with returning the df itself."""

    def mock_to_sql(self, *args, **kwargs) -> pd.DataFrame:  # pylint: disable=unused-argument
        """Mocks the pandas method to return the df itself."""
        return len(self)

    monkeypatch.setattr(pd.DataFrame, "to_sql", mock_to_sql)


def test_get_engine(mock_db_uploader: DBUploader) -> None:
    """Tests DBUploader's creation of the sqlalchemy engine."""
    test_engine = mock_db_uploader.get_engine()
    expected_engine = create_engine("postgresql+psycopg2://test_user:test_pw@test_host:123/test_db_name")
    assert test_engine.driver == expected_engine.driver
    assert test_engine.name == expected_engine.name
    assert test_engine.url == expected_engine.url


def test_upload_parquet(
    tmp_path: Path, mock_db_uploader: DBUploader, apply_mock_to_sql: None  # pylint: disable=unused-argument
) -> None:
    """Tests DBUploader's upload_parquet method."""
    df = pd.DataFrame({"Draw Date": [1, 2, 3], "Winning Numbers": [4, 5, 6], "Multiplier": [7, 8, 9]})
    df.to_parquet(tmp_path / "test.parquet")
    c = mock_db_uploader.upload_parquet(tmp_path / "test.parquet")
    assert c == 3
