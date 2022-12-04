from rich.table import Table


def df_to_table(
        dataframe,
        rich_table: Table,
) -> Table:
    """Convert a pandas.DataFrame obj into a rich.Table obj.
        Args:
            dataframe (DataFrame): A Pandas DataFrame to be converted to a rich Table.
            rich_table (Table): A rich Table that should be populated by the DataFrame values.
            show_index (bool): Add a column with a row count to the table. Defaults to True.
            index_name (str, optional): The column name to give to the index column. Defaults to None, showing no value.
        Returns:
            Table: The rich Table instance passed, populated with the DataFrame values."""
    for column in dataframe.columns:
        rich_table.add_column(str(column))

    for value_row in dataframe.rows():
        row = [str(x) for x in value_row]
        rich_table.add_row(*row)
    return rich_table
