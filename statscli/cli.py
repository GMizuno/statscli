from pathlib import Path

import polars as pl
import typer
from rich.console import Console
from rich.table import Table

from statscli.converter import ParquetConvert, CSVConvert, AvroConvert
from statscli.describer import df_to_table
from statscli.describer import stats_files, print_schemas
from statscli.reader import AvroReader, ParquetReader, CSVReader

main = typer.Typer(name="StatsCli CLI")


@main.command()
def version():
    """Show Polars version used"""
    print(f"Using Polar version {pl.__version__}")


@main.command()
def list_files(path: str = typer.Option(..., help="Path to the file")):
    """Show all files in a path"""
    files = [file for file in Path(path).glob('*') if file.is_file()]

    table = Table(title=f"Files in {path}")

    table.add_column("Path", justify="left", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Size (in MB)", justify="right", style="green")

    stats_files(files, table)
    console = Console()
    console.print(table)


@main.command()
def head(path: str = typer.Option(..., help="Path to the file"),
         num_row: int = typer.Option(5, help="Stop reading from file after reading n_rows"),
         columns: list[str] = typer.Option(None, help="List of columns to be read"),
         sep: str = typer.Option(',', help="Separator to be used, if necessary")):
    """Print first num_row lines"""
    p = Path(path)
    if columns == []: columns = None
    if p.suffix == '.parquet':
        data = ParquetReader(path, n_rows=num_row, columns=columns)
    elif p.suffix == '.csv':
        data = CSVReader(path, n_rows=num_row, columns=columns, sep=sep)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')

    data = data.read()
    print(data)

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    console.print(df_to_table(data, table))


@main.command()
def to_parquet(path: str = typer.Option(..., help="Path to the file"),
               new_filename: str = typer.Option(None, help="Path where the file should be written"),
               columns: list[str] = typer.Option(None, help="List of columns to be read"),
               sep: str = typer.Option(',', help="Separator to be used, if necessary")):
    """Convert a file to Parquet format"""
    p = Path(path)
    if columns == []: columns = None
    if p.suffix == '.csv':
        reader = CSVReader(str(path), n_rows=None, columns=columns, sep=sep)
        ParquetConvert(reader).convert(new_filename)
    elif p.suffix == '.avro':
        reader = AvroReader(str(path), n_rows=None, columns=columns, sep=None)
        ParquetConvert(reader).convert(new_filename)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')


@main.command()
def to_csv(path: str = typer.Option(..., help="Path to the file"),
           new_filename: str = typer.Option(None, help="Path where the file should be written"),
           columns: list[str] = typer.Option(None, help="List of columns to be read"),
           sep: str = typer.Option(',', help="Separator to be used, if necessary")):
    """Convert a file to CSV format"""
    p = Path(path)
    if columns == []: columns = None
    if p.suffix == '.parquet':
        reader = ParquetReader(str(path), columns=columns)
        CSVConvert(reader).convert(new_filename, sep=sep)
    elif p.suffix == '.avro':
        reader = AvroReader(str(path))
        CSVConvert(reader).convert(new_filename, sep=sep)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')

@main.command()
def to_avro(path: str = typer.Option(..., help="Path to the file"),
           new_filename: str = typer.Option(None, help="Path where the file should be written"),
           columns: list[str] = typer.Option(None, help="List of columns to be read"),
           sep: str = typer.Option(',', help="Separator to be used, if necessary")):
    """Convert a file to CSV format"""
    p = Path(path)
    if columns == []: columns = None
    if p.suffix == '.parquet':
        reader = ParquetReader(str(path), columns=columns)
        AvroConvert(reader).convert(new_filename)
    elif p.suffix == '.csv':
        reader = CSVReader(str(path), n_rows=None, columns=columns, sep=sep)
        AvroConvert(reader).convert(new_filename)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')

@main.command()
def schema(path: str = typer.Option(..., help="Path to the file"),
           sep: str = typer.Option(',', help="Separator to be used, if necessary")):
    """Print Schema information

    :param path: Path to the file
    :param sep: Separato if necessary
    """
    p = Path(path)
    if p.suffix == '.parquet':
        data = ParquetReader(path, n_rows=None, columns=None)
    elif p.suffix == '.csv':
        data = CSVReader(path, n_rows=None, columns=None, sep=sep)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')

    table = Table(title=f"Schema of {p.name}")

    table.add_column("Column", justify="left", style="cyan", no_wrap=True)
    table.add_column("Type", style="magenta")

    print_schemas(data.schema(), table)
    console = Console()
    console.print(table)


@main.command()
def describer(path: str = typer.Option(..., help="Path to the file"),
              sep: str = typer.Option(',', help="Separator to be used, if necessary")):
    """Print Schema information

    :param path: Path to the file
    :param sep: Separato if necessary
    """
    p = Path(path)
    if p.suffix == '.parquet':
        data = ParquetReader(path, n_rows=None, columns=None).read()
    elif p.suffix == '.csv':
        data = CSVReader(path, n_rows=None, columns=None, sep=sep).read()
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')

    stats = data.describe()

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    console.print(df_to_table(stats, table))
