import re

import pandas as pd


def extract_currency(value):
    """
    Extract the currency code from a currency-formatted value.

    Supported currencies:
        - INR
        - USD

    Supported formats include:
        - ₹50,000
        - ₹ 50,000
        - Rs. 50,000
        - Rs 50,000
        - INR 50000
        - $1,200
        - $ 1,200
        - USD 1200

    Parameters:
        value:
            Currency value that needs to be analyzed.

    Returns:
        str or pd.NA:
            Currency code such as "INR" or "USD".
            Returns "UNKNOWN" when no supported currency
            can be identified.
    """

    # Preserve missing values.
    if pd.isna(value):
        return pd.NA

    # Convert the value to uppercase string.
    value = str(value).strip().upper()

    # Check for Indian Rupee symbol.
    if "₹" in value:
        return "INR"

    # Check for Rs or Rs. notation.
    if re.search(r"\bRS\.?\b", value):
        return "INR"

    # Check for INR text.
    if "INR" in value:
        return "INR"

    # Check for dollar symbol.
    if "$" in value:
        return "USD"

    # Check for USD text.
    if "USD" in value:
        return "USD"

    # No supported currency was found.
    return "UNKNOWN"


def clean_numeric_string(value):
    """
    Remove currency symbols and formatting characters
    from a numeric value and convert it to a number.

    Supported examples:
        ₹50,000  -> 50000
        Rs. 50,000 -> 50000
        INR 50000 -> 50000
        $1,200 -> 1200
        USD 1500 -> 1500
        75,000 -> 75000
        unknown -> NaN

    Parameters:
        value:
            Numeric or string value.

    Returns:
        float or pd.NA:
            Clean numeric value.
    """

    # Preserve missing values.
    if pd.isna(value):
        return pd.NA

    # Convert value to string.
    value = str(value).strip()

    # Treat common missing-value text as missing.
    if value.lower() in {
        "",
        "unknown",
        "n/a",
        "na",
        "null",
        "none",
    }:
        return pd.NA

    # Remove currency symbols and currency names.
    value = re.sub(
        r"₹|Rs\.?|INR|USD|\$",
        "",
        value,
        flags=re.IGNORECASE
    )

    # Remove commas used as thousands separators.
    value = value.replace(",", "")

    # Remove unnecessary spaces.
    value = value.strip()

    # Convert the cleaned string into a numeric value.
    numeric_value = pd.to_numeric(
        value,
        errors="coerce"
    )

    return numeric_value


def clean_currency_column(df, column):
    """
    Clean a currency column while preserving currency information.

    Two new columns are created:
        - <column>_currency
        - <column>_amount

    Example:

        salary
        ----------------
        ₹50,000

    becomes:

        salary_currency    salary_amount
        ---------------------------------
        INR                50000

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Name of the currency column.

    Returns:
        pd.DataFrame:
            A new DataFrame containing cleaned currency
            and numeric amount columns.
    """

    # Create a copy so the original DataFrame is not modified.
    result = df.copy()

    # Extract currency information.
    result[f"{column}_currency"] = result[column].apply(
        extract_currency
    )

    # Clean the numeric amount.
    result[f"{column}_amount"] = result[column].apply(
        clean_numeric_string
    )

    return result


def convert_numeric_column(df, column):
    """
    Convert a column into numeric values.

    Invalid numeric values are converted to missing values.

    Examples:
        "10"      -> 10
        "25.5"    -> 25.5
        "unknown" -> NaN

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Name of the column to convert.

    Returns:
        pd.DataFrame:
            A new DataFrame with the selected column
            converted to numeric values.
    """

    # Create a copy.
    result = df.copy()

    # Convert values to numeric.
    result[column] = pd.to_numeric(
        result[column],
        errors="coerce"
    )

    return result


def find_negative_values(df, column):
    """
    Find negative values in a numeric column.

    Parameters:
        df (pd.DataFrame):
            Input DataFrame.

        column (str):
            Numeric column to check.

    Returns:
        pd.DataFrame:
            Rows containing negative values.
    """

    # Convert the column to numeric temporarily.
    numeric_values = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    # Return rows where the value is negative.
    return df[numeric_values < 0]