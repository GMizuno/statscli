import typer
from rich.console import Console
from rich.table import Table
import polars as pl
from pathlib import Path

from statscli.describer import stats_files
from statscli.reader import df_to_table
from statscli.reader import parquet_reader

main = typer.Typer(name="StatsCli CLI")


@main.command()
def version():
    """Show Polars version used"""
    print(f"Using Polar version {pl.__version__}")


@main.command()
def list_files(path: str):
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
def head(path: str, num_row: int = 5):
    """Print first num_row lines"""
    p = Path(path)
    if p.suffix == '.parquet':
        data = parquet_reader(path, n_rows=num_row)
    else:
        raise ValueError(f'Extension {p.suffix} does not supported')

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    df_to_table(data, table)

    console.print(table)
