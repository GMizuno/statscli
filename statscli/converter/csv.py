from statscli.reader import CSVReader


class CSV(CSVReader):

    def __init__(self, filepath, columns, sep, n_rows=None):
        super().__init__(filepath, n_rows, columns, sep)

    def to_parquet(self, filename, columns, new_filename: str, **kwargs):
        data = self.read()
        return data.write_parquet(new_filename)
