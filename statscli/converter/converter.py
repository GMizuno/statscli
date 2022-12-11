from abc import ABC, abstractmethod
from pathlib import Path

from statscli.reader import Readers


class Convert(ABC):

    def __init__(self, file: Readers):
        self.file = file

    @abstractmethod
    def convert(self, new_filename: str, sep) -> None:
        pass


class ParquetConvert(Convert):

    def __init__(self, file: Readers):
        super().__init__(file)
        self.filepath = file.filepath
        self.n_rows = file.n_rows
        self.columns = file.columns
        self.sep = file.sep

    def convert(self, new_filename: str, sep=None) -> None:
        data = self.file.read()
        if new_filename is not None:
            data.write_parquet(new_filename)
        else:
            new_filename = str(Path(self.filepath).with_suffix(".parquet"))
            data.write_parquet(new_filename)

        print(f"File {self.filepath} converted to Parquet format")


class CSVConvert(Convert):

    def __init__(self, file: Readers):
        super().__init__(file)
        self.filepath = file.filepath
        self.n_rows = file.n_rows
        self.columns = file.columns
        self.sep = file.sep

    def convert(self, new_filename: str, sep: str = None) -> None:
        data = self.file.read()
        if new_filename is not None:
            data.write_csv(new_filename, sep=sep)
        else:
            new_filename = str(Path(self.filepath).with_suffix(".csv"))
            data.write_parquet(new_filename)
        print(f"File {self.filepath} converted to CSV format")


class AvroConvert(Convert):

    def __init__(self, file: Readers):
        super().__init__(file)
        self.filepath = file.filepath
        self.n_rows = file.n_rows
        self.columns = file.columns
        self.sep = file.sep

    def convert(self, new_filename: str, sep: str = None) -> None:
        data = self.file.read()
        if new_filename is not None:
            data.write_avro(new_filename)
        else:
            new_filename = str(Path(self.filepath).with_suffix(".avro"))
            data.write_avro(new_filename)
        print(f"File {self.filepath} converted to Avro format")
