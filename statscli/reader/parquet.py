import polars as pl

from .reader import Readers


class ParquetReader(Readers):
    """
    A class for reading data.
    """

    def __init__(self,
                 filepath: str,
                 n_rows: int | None = 5,
                 columns: list[str] | None = None,
                 sep: None = None
                 ):
        super().__init__(filepath, n_rows, columns, sep)

    def read(self) -> pl.DataFrame:
        return pl.read_parquet(self.filepath, columns=self.columns, n_rows=self.n_rows)
