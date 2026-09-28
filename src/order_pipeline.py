import pandas as pd

from src.string_cleaner import (
    clean_whitespace,
)

from src.cleaner import (
    copy_dataframe,
    remove_duplicate_rows,
)

from src.numeric_cleaner import (
    clean_currency_column,
)

from src.datetime_cleaner import (
    convert_to_datetime,
)

from src.validator import (
    validate_required_columns,
    validate_required_values,
    validate_positive,
    validate_unique,
    validate_datetime,
)


def clean_orders(df, order_config):
    """
    Clean and validate an order DataFrame.

    The function cleans whitespace, converts quantities,
    processes currency values, converts order dates,
    removes duplicate rows, and validates order data.

    Parameters:
        df (pd.DataFrame):
            Raw order DataFrame.

        order_config (dict):
            Order-specific rules loaded from YAML.

    Returns:
        tuple:
            Cleaned DataFrame and validation results.
    """

    # -----------------------------------------------
    # Create working copy
    # -----------------------------------------------

    cleaned_df = copy_dataframe(df)

    # -----------------------------------------------
    # Clean whitespace
    # -----------------------------------------------

    cleaned_df = clean_whitespace(
        cleaned_df
    )

    # -----------------------------------------------
    # Convert quantity
    # -----------------------------------------------

    cleaned_df["quantity"] = pd.to_numeric(
        cleaned_df["quantity"],
        errors="coerce"
    )

    # -----------------------------------------------
    # Clean unit price
    # -----------------------------------------------

    cleaned_df = clean_currency_column(
        cleaned_df,
        "unit_price"
    )

    # -----------------------------------------------
    # Convert order date
    # -----------------------------------------------

    cleaned_df = convert_to_datetime(
        cleaned_df,
        "order_date"
    )

    # -----------------------------------------------
    # Remove duplicate rows
    # -----------------------------------------------

    cleaned_df = remove_duplicate_rows(
        cleaned_df
    )

    # -----------------------------------------------
    # Validation
    # -----------------------------------------------

    validation_results = {}

    validation_results[
        "required_columns"
    ] = validate_required_columns(
        cleaned_df,
        order_config[
            "required_columns"
        ]
    )

    validation_results[
        "required_values"
    ] = validate_required_values(
        cleaned_df,
        order_config[
            "required_values"
        ]
    )

    # -----------------------------------------------
    # Positive-value validation
    # -----------------------------------------------

    for column in order_config[
        "positive_columns"
    ]:

        validation_results[
            f"positive_{column}"
        ] = validate_positive(
            cleaned_df,
            column
        )

    # -----------------------------------------------
    # Unique ID validation
    # -----------------------------------------------

    for column in order_config[
        "unique_columns"
    ]:

        validation_results[
            f"unique_{column}"
        ] = validate_unique(
            cleaned_df,
            column
        )

    # -----------------------------------------------
    # Date validation
    # -----------------------------------------------

    validation_results[
        "order_date"
    ] = validate_datetime(
        cleaned_df,
        "order_date"
    )

    return (
        cleaned_df,
        validation_results
    )