import polars as pl


def parquet_reader(path: str, n_rows: int) -> pl.DataFrame:
    return pl.read_parquet(path, n_rows=n_rows)
