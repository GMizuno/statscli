from statscli.reader import ParquetReader


class Parquet(ParquetReader):

    def __init__(self, filepath, columns, n_rows=None):
        super().__init__(filepath=filepath, n_rows=n_rows, columns=columns)

    def to_csv(self, new_filename: str, sep: str):
        data = self.read()
        return data.write_csv(new_filename, sep=sep)
