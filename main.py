from statscli.converter import Parquet

file = Parquet('tests/KwhConsumptionBlower78_1.parquet', n_rows=5, columns=None)
file.schema()