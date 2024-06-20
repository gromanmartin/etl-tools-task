"""Module describing implementation of JsonDownloader"""
from pathlib import Path
import logging
import json
import requests
import pandas as pd
from etl_tools.download.interface import IDownloader


logger = logging.getLogger(__file__)


class JsonDownloader(IDownloader):
    """JsonDownloader interface."""

    def __init__(self) -> None:
        self.column_names = ["Draw Date", "Winning Numbers", "Multiplier"]

    def download_file(self, url: str) -> bytes:
        """Downloads a single file and stores it into memory."""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error("There was an HTTP error - %s", err)
            raise
        logger.info("File successfully downloaded!")
        return response.content

    def save_to_parquet(self, content: bytes, file_path: Path) -> None:
        """Save in-memory stored file to parquet."""
        data = json.loads(content.decode("utf-8"))
        col_map = self.find_columns(data["meta"])
        df = pd.DataFrame(data["data"])
        df = df.iloc[:, list(col_map.keys())].rename(col_map, axis=1)
        df.to_parquet(file_path)
        logger.info("Content successfully saved to %s", file_path)

    def download_to_parquet(self, url: str, file_path: Path) -> None:
        """Downloads a single file into memory, converts it to parquet and stores locally."""
        data = self.download_file(url)
        self.save_to_parquet(data, file_path)

    def find_columns(self, metadata: dict) -> dict[int, str]:
        """Creates a mapping with indexes of columns which we are interested in based on self.column_names"""
        col_list = metadata["view"]["columns"]
        col_map = {key: val["name"] for key, val in enumerate(col_list) if val["name"] in self.column_names}
        return col_map
