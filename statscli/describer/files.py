from rich.table import Table

def stats_files(files: list, table: Table) -> None:
    for file in files:
        path = file.absolute().parent.__str__()
        name = file.name.__str__()
        size = round(file.stat().st_size / (1024.0 * 1024.0), 3)
        table.add_row(path, name, f"{size}")

def print_schemas(schema: dict, table: Table):
    for column, type in schema.items():
        table.add_row(column, type.string_repr())
