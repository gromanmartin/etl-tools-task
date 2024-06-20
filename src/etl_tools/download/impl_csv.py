"""Module with implementation of CSVDownloader."""
from pathlib import Path
from io import BytesIO
import logging

import requests
import pandas as pd
from etl_tools.download.interface import IDownloader


logger = logging.getLogger(__file__)


class CSVDownloader(IDownloader):
    """Implementation of CSV specific IDownloader."""

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
        df = pd.read_csv(BytesIO(content))
        df.to_parquet(file_path)
        logger.info("Content successfully saved to %s", file_path)

    def download_to_parquet(self, url: str, file_path: Path) -> None:
        """Downloads a single file into memory, converts it to parquet and stores locally."""
        data = self.download_file(url)
        self.save_to_parquet(data, file_path)
