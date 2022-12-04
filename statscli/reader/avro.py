from .reader import Readers
import polars as pl


class Avro(Readers):
    """
    A class for reading data.
    """

    def __init__(self,
                 filepath: str,
                 n_rows: int = 5,
                 column: list[str]|None = None):
        super().__init__(filepath,  n_rows, column)


    def read(self) -> pl.DataFrame:
        return pl.read_avro(self.filepath, n_rows=self.n_rows, columns=self.column)
