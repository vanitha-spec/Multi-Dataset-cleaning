import pandas as pd


def copy_dataframe(df):
    """
    Create an independent copy of a pandas DataFrame.

    This prevents modifications to the original DataFrame
    from affecting the source data.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        pd.DataFrame:
            Independent copy of the DataFrame.

    Raises:
        TypeError:
            If the input is not a pandas DataFrame.
    """

    # Validate the input type.
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    # Create and return a copy.
    return df.copy()


def remove_duplicate_rows(df):
    """
    Remove completely duplicated rows from a DataFrame.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        pd.DataFrame:
            A new DataFrame with duplicate rows removed.
    """

    # Create a copy.
    result = df.copy()

    # Remove duplicate rows.
    result = result.drop_duplicates()

    # Reset the index after removing rows.
    result = result.reset_index(
        drop=True
    )

    return result


def drop_empty_columns(df):
    """
    Remove columns that contain only missing values.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        pd.DataFrame:
            A new DataFrame without completely empty columns.
    """

    # Create a copy.
    result = df.copy()

    # Drop columns where every value is missing.
    result = result.dropna(
        axis=1,
        how="all"
    )

    return result


def drop_empty_rows(df):
    """
    Remove rows where every value is missing.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        pd.DataFrame:
            A new DataFrame without completely empty rows.
    """

    # Create a copy.
    result = df.copy()

    # Drop rows where every value is missing.
    result = result.dropna(
        axis=0,
        how="all"
    )

    # Reset the index.
    result = result.reset_index(
        drop=True
    )

    return result


def fill_missing_values(
    df,
    column,
    value
):
    """
    Fill missing values in a specific column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Column whose missing values should be filled.

        value:
            Value used to replace missing values.

    Returns:
        pd.DataFrame:
            A new DataFrame with missing values filled.
    """

    # Create a copy.
    result = df.copy()

    # Fill missing values.
    result[column] = result[column].fillna(
        value
    )

    return result


def fill_missing_with_mean(
    df,
    column
):
    """
    Fill missing numeric values using the column mean.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Numeric column.

    Returns:
        pd.DataFrame:
            A new DataFrame with missing numeric values
            replaced by the column mean.
    """

    # Create a copy.
    result = df.copy()

    # Convert the column to numeric.
    numeric_values = pd.to_numeric(
        result[column],
        errors="coerce"
    )

    # Calculate the mean.
    mean_value = numeric_values.mean()

    # Fill missing values with the mean.
    result[column] = numeric_values.fillna(
        mean_value
    )

    return result


def drop_rows_with_missing(
    df,
    columns
):
    """
    Remove rows containing missing values in required columns.

    This is useful when certain columns are mandatory.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        columns (list):
            Columns that must contain values.

    Returns:
        pd.DataFrame:
            A new DataFrame containing only rows where
            all required columns are present.
    """

    # Create a copy.
    result = df.copy()

    # Drop rows with missing values in the required columns.
    result = result.dropna(
        subset=columns
    )

    # Reset the index.
    result = result.reset_index(
        drop=True
    )

    return result


def set_display_options(
    max_rows=100,
    max_columns=50
):
    """
    Configure pandas display options.

    Parameters:
        max_rows (int):
            Maximum number of rows displayed.

        max_columns (int):
            Maximum number of columns displayed.

    Returns:
        None
    """

    # Configure maximum displayed rows.
    pd.set_option(
        "display.max_rows",
        max_rows
    )

    # Configure maximum displayed columns.
    pd.set_option(
        "display.max_columns",
        max_columns
    )