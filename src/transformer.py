import pandas as pd


def rename_columns(df, mapping):
    """
    Rename DataFrame columns using a mapping dictionary.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        mapping (dict):
            Dictionary where keys are existing column names
            and values are the new column names.

    Returns:
        pd.DataFrame:
            A new DataFrame with renamed columns.
    """

    # Create a copy so the original DataFrame is not modified.
    result = df.copy()

    # Rename the requested columns.
    result = result.rename(
        columns=mapping
    )

    return result


def replace_values(df, column, mapping):
    """
    Replace specific values in a DataFrame column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Column where values should be replaced.

        mapping (dict):
            Dictionary containing old and new values.

    Returns:
        pd.DataFrame:
            A new DataFrame with replaced values.
    """

    # Create a copy.
    result = df.copy()

    # Replace values using the mapping.
    result[column] = result[column].replace(
        mapping
    )

    return result


def map_values(df, column, mapping):
    """
    Map values in a DataFrame column to standardized values.

    Unlike replace(), map() converts values according to
    the supplied mapping.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Column to transform.

        mapping (dict):
            Dictionary containing input and output values.

    Returns:
        pd.DataFrame:
            A new DataFrame with mapped values.
    """

    # Create a copy.
    result = df.copy()

    # Apply the mapping.
    result[column] = result[column].map(
        mapping
    )

    return result


def apply_function(df, column, function):
    """
    Apply a custom Python function to every value
    in a DataFrame column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Column to transform.

        function:
            Function that will be applied to every value.

    Returns:
        pd.DataFrame:
            A new DataFrame with the transformed column.
    """

    # Create a copy.
    result = df.copy()

    # Apply the supplied function.
    result[column] = result[column].apply(
        function
    )

    return result


def sort_by_column(
    df,
    column,
    ascending=True
):
    """
    Sort a DataFrame using a selected column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Column used for sorting.

        ascending (bool):
            True for ascending order.
            False for descending order.

    Returns:
        pd.DataFrame:
            A new sorted DataFrame.
    """

    # Create a copy.
    result = df.copy()

    # Sort the DataFrame.
    result = result.sort_values(
        by=column,
        ascending=ascending
    )

    # Reset the index after sorting.
    result = result.reset_index(
        drop=True
    )

    return result


def set_dataframe_index(df, column):
    """
    Set a DataFrame column as its index.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Column that should become the index.

    Returns:
        pd.DataFrame:
            A new DataFrame with the selected column
            used as the index.
    """

    # Create a copy.
    result = df.copy()

    # Set the selected column as the index.
    result = result.set_index(
        column
    )

    return result


def reset_dataframe_index(df):
    """
    Reset a DataFrame index back to the default integer index.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        pd.DataFrame:
            A new DataFrame with a standard integer index.
    """

    # Create a copy.
    result = df.copy()

    # Reset the index.
    result = result.reset_index()

    return result


def select_columns(df, columns):
    """
    Select a specific set of columns from a DataFrame.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        columns (list):
            Columns that should be retained.

    Returns:
        pd.DataFrame:
            A new DataFrame containing only the requested columns.
    """

    # Create a copy containing the requested columns.
    result = df[columns].copy()

    return result


def get_column_names(df):
    """
    Return the column names of a DataFrame.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        list:
            List containing the DataFrame column names.
    """

    return df.columns.tolist()