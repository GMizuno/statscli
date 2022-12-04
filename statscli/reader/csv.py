from .reader import Readers
import polars as pl


class CSVReader(Readers):
    """
    A class for reading data.
    """

    def __init__(self,
                 filepath: str,
                 n_rows: int = 5,
                 column: list[str] | None = None,
                 sep: str = ','):
        super().__init__(filepath)
        self.sep = sep
        self.n_rows = n_rows
        self.column = column


    def read(self) -> pl.DataFrame:
        return pl.read_csv(self.filepath, n_rows=self.n_rows, columns=self.column, sep=self.sep)
