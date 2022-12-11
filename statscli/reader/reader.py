from abc import ABC, abstractmethod

import polars as pl


class Readers(ABC):

    def __init__(self,
                 filepath: str,
                 n_rows: int = 5,
                 columns: list[str] | None = None,
                 sep: str | None = ','
                 ) -> None:
        self.filepath = filepath
        self.n_rows = n_rows
        self.columns = columns
        self.sep = sep

    @abstractmethod
    def read(self) ->  pl.DataFrame:
        pass

    def schema(self):
        return self.read().schema
