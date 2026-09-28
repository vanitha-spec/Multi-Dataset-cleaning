import pandas as pd


def profile_dataset(df):
    """
    Analyze a pandas DataFrame and generate a basic data-quality profile.

    The profile contains:
        - Number of rows
        - Number of columns
        - Column names
        - Data types
        - Missing values
        - Duplicate rows
        - Descriptive statistics
        - Number of unique values
        - Frequency of values

    Parameters:
        df (pd.DataFrame):
            The DataFrame that needs to be analyzed.

    Returns:
        dict:
            A dictionary containing the profiling information.

    Raises:
        TypeError:
            If the input is not a pandas DataFrame.
    """

    # ---------------------------------------------------------
    # 1. Validate the input
    # ---------------------------------------------------------

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    # ---------------------------------------------------------
    # 2. Basic dataset information
    # ---------------------------------------------------------

    rows = len(df)

    columns = len(df.columns)

    column_names = list(df.columns)

    # ---------------------------------------------------------
    # 3. Data types
    # ---------------------------------------------------------

    dtypes = df.dtypes.astype(str).to_dict()

    # ---------------------------------------------------------
    # 4. Missing values
    # ---------------------------------------------------------

    missing_values = df.isna().sum().to_dict()

    # ---------------------------------------------------------
    # 5. Duplicate rows
    # ---------------------------------------------------------

    duplicate_rows = int(
        df.duplicated().sum()
    )

    # ---------------------------------------------------------
    # 6. Descriptive statistics
    # ---------------------------------------------------------

    statistics = df.describe(
        include="all"
    ).to_dict()

    # ---------------------------------------------------------
    # 7. Unique values
    # ---------------------------------------------------------

    unique_values = {}

    for column in df.columns:

        unique_values[column] = int(
            df[column].nunique(
                dropna=False
            )
        )

    # ---------------------------------------------------------
    # 8. Value counts
    # ---------------------------------------------------------

    value_counts = {}

    for column in df.columns:

        value_counts[column] = (
            df[column]
            .value_counts(
                dropna=False
            )
            .to_dict()
        )

    # ---------------------------------------------------------
    # 9. Create the final profile
    # ---------------------------------------------------------

    profile = {
        "rows": rows,
        "columns": columns,
        "column_names": column_names,
        "dtypes": dtypes,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "statistics": statistics,
        "unique_values": unique_values,
        "value_counts": value_counts,
    }

    return profile