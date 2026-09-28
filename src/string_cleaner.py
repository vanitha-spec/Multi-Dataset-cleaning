import re

import pandas as pd


def clean_whitespace(df, columns=None):
    """
    Remove unnecessary whitespace from string columns.

    The function:
        - Removes leading spaces.
        - Removes trailing spaces.
        - Replaces multiple spaces with a single space.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        columns (list, optional):
            List of columns to clean.
            If None, all object/string columns are cleaned.

    Returns:
        pd.DataFrame:
            A new DataFrame with cleaned whitespace.
    """

    # Create a copy so the original DataFrame is not modified.
    result = df.copy()

    # If no columns were provided, find all string columns.
    if columns is None:
        columns = result.select_dtypes(
            include=["object", "string"]
        ).columns

    # Clean each selected column.
    for column in columns:

        # Convert values to pandas string type.
        result[column] = result[column].astype("string")

        # Remove spaces at the beginning and end.
        result[column] = result[column].str.strip()

        # Replace multiple spaces with one space.
        result[column] = result[column].str.replace(
            r"\s+",
            " ",
            regex=True
        )

    return result


def standardize_categories(df, column, mapping):
    """
    Standardize inconsistent categorical values.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Name of the categorical column.

        mapping (dict):
            Dictionary containing old values and their standardized values.

    Returns:
        pd.DataFrame:
            A new DataFrame with standardized category values.
    """

    # Create a copy.
    result = df.copy()

    # Apply the mapping to the selected column.
    result[column] = result[column].replace(mapping)

    return result


def clean_name(value):
    """
    Clean a person's name using basic string rules.

    The function:
        - Handles missing values.
        - Removes leading and trailing spaces.
        - Removes characters that are not letters, spaces,
          apostrophes, or hyphens.
        - Replaces multiple spaces with one space.

    Parameters:
        value:
            Name value to clean.

    Returns:
        str or pd.NA:
            Cleaned name.
    """

    # Preserve missing values.
    if pd.isna(value):
        return pd.NA

    # Convert the value to a string.
    value = str(value)

    # Remove leading and trailing spaces.
    value = value.strip()

    # Keep letters, spaces, apostrophes, and hyphens.
    value = re.sub(
        r"[^A-Za-z\s'-]",
        "",
        value
    )

    # Replace multiple spaces with one space.
    value = re.sub(
        r"\s+",
        " ",
        value
    )

    # Remove spaces left at the beginning/end.
    value = value.strip()

    return value


def clean_name_column(df, column):
    """
    Apply the clean_name function to an entire name column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Name of the name column.

    Returns:
        pd.DataFrame:
            A new DataFrame with cleaned names.
    """

    # Create a copy.
    result = df.copy()

    # Apply the name-cleaning rule to every value.
    result[column] = result[column].apply(
        clean_name
    )

    return result


def standardize_column_names(df):
    """
    Standardize DataFrame column names.

    The function:
        - Removes leading/trailing spaces.
        - Converts names to lowercase.
        - Replaces spaces and hyphens with underscores.
        - Removes other unnecessary characters.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

    Returns:
        pd.DataFrame:
            A new DataFrame with standardized column names.
    """

    # Create a copy.
    result = df.copy()

    new_columns = []

    for column in result.columns:

        # Convert the column name to string.
        column = str(column)

        # Remove leading/trailing whitespace.
        column = column.strip()

        # Convert to lowercase.
        column = column.lower()

        # Replace spaces and hyphens with underscores.
        column = re.sub(
            r"[\s-]+",
            "_",
            column
        )

        # Remove unwanted characters.
        column = re.sub(
            r"[^a-z0-9_]",
            "",
            column
        )

        # Remove repeated underscores.
        column = re.sub(
            r"_+",
            "_",
            column
        )

        # Remove underscores from beginning/end.
        column = column.strip("_")

        new_columns.append(column)

    result.columns = new_columns

    return result