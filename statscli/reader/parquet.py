from .reader import Readers
import polars as pl


class ParquetReader(Readers):
    """
    A class for reading data.
    """

    def __init__(self,
                 filepath: str,
                 n_rows: int = 5,
                 columns: list[str] | None = None,
                 ):
        super().__init__(filepath, n_rows, columns)

    def read(self) -> pl.DataFrame:
        print(self.filepath, self.column, self.n_rows)
        return pl.read_parquet(self.filepath, columns=None, n_rows=self.n_rows)
