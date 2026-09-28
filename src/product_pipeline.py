from src.string_cleaner import (
    clean_whitespace,
    clean_name_column,
)

from src.cleaner import (
    copy_dataframe,
    remove_duplicate_rows,
)

from src.numeric_cleaner import (
    clean_currency_column,
)

from src.validator import (
    validate_required_columns,
    validate_required_values,
    validate_positive,
    validate_unique,
)


def clean_products(df, product_config):
    """
    Clean and validate a product DataFrame.

    The function cleans whitespace and product names,
    processes product prices, removes duplicates,
    and validates product records.

    Parameters:
        df (pd.DataFrame):
            Raw product DataFrame.

        product_config (dict):
            Product-specific rules loaded from YAML.

    Returns:
        tuple:
            Cleaned DataFrame and validation results.
    """

    cleaned_df = copy_dataframe(
        df
    )

    # -----------------------------------------------
    # Clean whitespace
    # -----------------------------------------------

    cleaned_df = clean_whitespace(
        cleaned_df
    )

    # -----------------------------------------------
    # Clean product names
    # -----------------------------------------------

    cleaned_df = clean_name_column(
        cleaned_df,
        "product_name"
    )

    # -----------------------------------------------
    # Clean price
    # -----------------------------------------------

    cleaned_df = clean_currency_column(
        cleaned_df,
        "price"
    )

    # -----------------------------------------------
    # Remove duplicates
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
        product_config[
            "required_columns"
        ]
    )

    validation_results[
        "required_values"
    ] = validate_required_values(
        cleaned_df,
        product_config[
            "required_values"
        ]
    )

    # -----------------------------------------------
    # Positive price validation
    # -----------------------------------------------

    for column in product_config[
        "positive_columns"
    ]:

        # Price becomes price_amount after
        # currency cleaning.

        amount_column = (
            f"{column}_amount"
        )

        validation_results[
            f"positive_{column}"
        ] = validate_positive(
            cleaned_df,
            amount_column
        )

    # -----------------------------------------------
    # Unique product ID validation
    # -----------------------------------------------

    for column in product_config[
        "unique_columns"
    ]:

        validation_results[
            f"unique_{column}"
        ] = validate_unique(
            cleaned_df,
            column
        )

    return (
        cleaned_df,
        validation_results
    )