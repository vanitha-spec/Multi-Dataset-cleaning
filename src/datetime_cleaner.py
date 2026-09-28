import pandas as pd


def convert_to_datetime(
    df,
    column,
    dayfirst=False
):
    """
    Convert a DataFrame column into pandas datetime values.

    Invalid or unparseable dates are converted to NaT.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Name of the date column.

        dayfirst (bool):
            Whether dates should be interpreted with the
            day appearing before the month.

    Returns:
        pd.DataFrame:
            A new DataFrame with the selected column
            converted to datetime.

    Example:
        "2026-01-15" -> Timestamp("2026-01-15")
        "invalid-date" -> NaT
    """

    # Create a copy so the original DataFrame
    # is not modified.
    result = df.copy()

    # Convert the column to datetime.
    result[column] = pd.to_datetime(
        result[column],
        errors="coerce",
        dayfirst=dayfirst
    )

    return result


def find_invalid_dates(
    df,
    column
):
    """
    Find rows containing missing or invalid dates.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Name of the datetime column.

    Returns:
        pd.DataFrame:
            Rows where the date is missing or invalid.
    """

    # Create a copy.
    result = df.copy()

    # Convert values to datetime temporarily.
    parsed_dates = pd.to_datetime(
        result[column],
        errors="coerce"
    )

    # Return rows where parsing failed or
    # the original value was missing.
    return result[parsed_dates.isna()]


def extract_date_only(
    df,
    column
):
    """
    Extract only the calendar date from a datetime column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Datetime column.

    Returns:
        pd.DataFrame:
            A new DataFrame where the selected column
            contains date-only values.
    """

    # Create a copy.
    result = df.copy()

    # Make sure the column is datetime.
    result[column] = pd.to_datetime(
        result[column],
        errors="coerce"
    )

    # Extract only the date portion.
    result[column] = result[column].dt.date

    return result


def extract_year(
    df,
    column
):
    """
    Extract the year from a datetime column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Datetime column.

    Returns:
        pd.DataFrame:
            A new DataFrame containing a new
            '<column>_year' column.
    """

    # Create a copy.
    result = df.copy()

    # Convert the column to datetime.
    result[column] = pd.to_datetime(
        result[column],
        errors="coerce"
    )

    # Extract the year.
    result[f"{column}_year"] = result[column].dt.year

    return result


def find_future_dates(
    df,
    column,
    reference_date=None
):
    """
    Find dates that occur after a specified reference date.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Datetime column.

        reference_date:
            Date used as the comparison point.
            If None, today's date is used.

    Returns:
        pd.DataFrame:
            Rows containing dates after the reference date.
    """

    # Create a copy.
    result = df.copy()

    # Convert the column to datetime.
    result[column] = pd.to_datetime(
        result[column],
        errors="coerce"
    )

    # Use today's date if no reference date was provided.
    if reference_date is None:
        reference_date = pd.Timestamp.today()

    else:
        reference_date = pd.Timestamp(
            reference_date
        )

    # Return future dates.
    return result[
        result[column] > reference_date
    ]