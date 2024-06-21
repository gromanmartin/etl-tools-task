"""Module with implementation of DBUploader."""
from pathlib import Path
import logging
import pandas as pd
from sqlalchemy import create_engine, URL, Engine
from etl_tools.upload.interface import IUploader


logger = logging.getLogger(__file__)


class DBUploader(IUploader):
    """DBUploader interface."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        host: str,
        username: str,
        password: str,
        db_name: str,
        port: int = 5432,
    ) -> None:
        """DBUploader init for db credentials."""
        self.host = host
        self.username = username
        self.password = password
        self.db_name = db_name
        self.port = port

    def get_engine(self) -> Engine:
        """Creates engine object for connecting to the DB."""
        url_object = URL.create(
            "postgresql+psycopg2",
            database=self.db_name,
            host=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
        )
        engine = create_engine(url_object)
        logger.info("Connection established!")
        return engine

    def upload_parquet(self, file_path: Path) -> int:
        """Uploads a single parquet file from file_path to a database."""
        engine = self.get_engine()
        df = pd.read_parquet(file_path, index=False)
        col_mapper = {"Draw Date": "draw_date", "Winning Numbers": "numbers", "Multiplier": "multiplier"}
        df.rename(col_mapper, axis=1, inplace=True)
        c = df.to_sql(con=engine, name="winning_numbers", if_exists="append", index=False)
        logger.info("Successfully added %s rows to the DB", c)
        return c
