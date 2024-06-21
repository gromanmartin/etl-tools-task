"""Module containing the pipeline run."""
from pathlib import Path
from etl_tools.orchestration.etl import ETL
from etl_tools.download.impl_csv import CSVDownloader
from etl_tools.upload.impl_db import DBUploader

URL_TO_DOWNLOAD = "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD"
local_file_to_save = Path("demo_run.parquet")
downloader = CSVDownloader()
uploader = DBUploader(host="localhost", username="test_user", password="test_user", db_name="lottery", port=5000)
etl_pipeline = ETL(name="demo_run", downloader=downloader, uploader=uploader)


if __name__ == "__main__":
    etl_pipeline.run(URL_TO_DOWNLOAD, local_file_to_save)
