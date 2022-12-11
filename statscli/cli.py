import typer
from rich.console import Console
from rich.table import Table
import polars as pl
from pathlib import Path
from typing import List

from statscli.converter import CSV, Parquet
from statscli.describer import stats_files
from statscli.describer import df_to_table

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
def head(path: str, num_row: int = 5, columns = None, sep: str = ','):
    """Print first num_row lines"""
    p = Path(path)
    if p.suffix == '.parquet':
        data = Parquet(path, n_rows=num_row, columns=columns)
    elif p.suffix == '.csv':
        data = CSV(path, n_rows=num_row, columns=columns, sep=sep)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')
    
    data = data.read()

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    console.print(df_to_table(data, table))


@main.command()
def to_parquet(path: str = typer.Option(..., help="Path to the file"),
               new_filename: str = typer.Option(None, help="Path where the file should be written"),
               columns: list[str] = typer.Option(None, help="List of columns to be read"),
               sep: str = typer.Option(',', help="Separator to be used")):
    """Convert a file to ParquetReader format"""
    p = Path(path)
    if p.suffix == '.csv':
        file = CSV(str(path), columns=columns, sep=sep)
        if new_filename is not None:
            file.to_parquet(str(path), new_filename=new_filename, columns=columns)
        else:
            new_filename = str(p.with_suffix(".parquet"))
            file.to_parquet(str(path), new_filename=new_filename, columns=columns)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')


@main.command()
def to_csv(path: str = typer.Option(..., help="Path to the file"),
           new_filename: str = typer.Option(None, help="Path where the file should be written"),
           columns: list[str] = typer.Option(None, help="List of columns to be read"),
           sep: str = typer.Option(',', help="Separator to be used")):
    """Convert a file to ParquetReader format"""
    p = Path(path)
    if p.suffix == '.parquet':
        file = Parquet(str(path), columns=columns)
        if new_filename is not None:
            file.to_csv(new_filename=new_filename, sep=sep)
        else:
            new_filename = str(p.with_suffix(".csv"))
            file.to_csv(new_filename=new_filename, sep=sep)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')
