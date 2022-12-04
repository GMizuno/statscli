from abc import ABC, abstractmethod
import polars as pl


class Readers(ABC):

    def __init__(self,
                 filepath: str,
                 n_rows: int = 5,
                 column: list[str] | None = None
                 ) -> None:
        self.column = column
        self.n_rows = n_rows
        self.filepath = filepath
        

    @abstractmethod
    def read(self) -> pl.DataFrame:
        pass
