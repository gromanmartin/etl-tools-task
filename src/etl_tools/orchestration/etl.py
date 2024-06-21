"""Module with the ETL pipeline design."""
from pathlib import Path
from etl_tools.download.interface import IDownloader
from etl_tools.upload.interface import IUploader


class ETL:
    """Class describing an ETL pipeline."""

    def __init__(self, name: str, downloader: IDownloader, uploader: IUploader) -> None:
        """Init of the ETL pipeline."""
        self.name = name
        self.downloader = downloader
        self.uploader = uploader

    def extract(self, url: str, file_path: Path) -> None:
        """Extract part of the pipeline."""
        self.downloader.download_to_parquet(url, file_path)

    def transform(self) -> None:
        """Transform part of the pipeline."""
        # pylint: disable=W0511
        # TODO: Implement transformator
        return

    def load(self, file_path: Path) -> None:
        """Load part of the pipeline."""
        self.uploader.upload_parquet(file_path)

    def run(self, url: str, file_path: Path) -> None:
        """Method to run the whole ETL pipeline."""
        self.extract(url, file_path)
        self.transform()
        self.load(file_path)
