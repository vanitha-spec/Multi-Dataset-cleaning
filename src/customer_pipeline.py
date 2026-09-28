import pandas as pd

from src.string_cleaner import (
    clean_whitespace,
    clean_name_column,
)

from src.cleaner import (
    copy_dataframe,
    remove_duplicate_rows,
)

from src.transformer import (
    replace_values,
)

from src.validator import (
    validate_required_columns,
    validate_required_values,
    validate_range,
    validate_unique,
    validate_email_format,
)


def clean_customers(df, customer_config):
    """
    Clean and validate a customer DataFrame.

    The function applies customer-specific cleaning rules,
    including whitespace cleanup, name cleanup, gender
    standardization, age conversion, duplicate removal,
    and validation.

    Parameters:
        df (pd.DataFrame):
            Raw customer DataFrame.

        customer_config (dict):
            Customer-specific rules loaded from YAML.

    Returns:
        tuple:
            A tuple containing:

            cleaned_df:
                The cleaned customer DataFrame.

            validation_results:
                Dictionary containing validation results.
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
    # Clean customer names
    # -----------------------------------------------

    cleaned_df = clean_name_column(
        cleaned_df,
        "customer_name"
    )

    # -----------------------------------------------
    # Standardize gender
    # -----------------------------------------------

    gender_mapping = customer_config[
        "gender_mapping"
    ]

    cleaned_df = replace_values(
        cleaned_df,
        "gender",
        gender_mapping
    )

    # -----------------------------------------------
    # Convert age to numeric
    # -----------------------------------------------

    cleaned_df["age"] = pd.to_numeric(
        cleaned_df["age"],
        errors="coerce"
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
        customer_config[
            "required_columns"
        ]
    )

    validation_results[
        "required_values"
    ] = validate_required_values(
        cleaned_df,
        customer_config[
            "required_values"
        ]
    )

    # -----------------------------------------------
    # Age validation
    # -----------------------------------------------

    age_rules = customer_config[
        "age"
    ]

    validation_results[
        "age_range"
    ] = validate_range(
        cleaned_df,
        "age",
        minimum=age_rules[
            "minimum"
        ],
        maximum=age_rules[
            "maximum"
        ]
    )

    # -----------------------------------------------
    # Unique ID validation
    # -----------------------------------------------

    for column in customer_config[
        "unique_columns"
    ]:

        validation_results[
            f"unique_{column}"
        ] = validate_unique(
            cleaned_df,
            column
        )

    # -----------------------------------------------
    # Email validation
    # -----------------------------------------------

    for column in customer_config[
        "email_columns"
    ]:

        validation_results[
            f"{column}_format"
        ] = validate_email_format(
            cleaned_df,
            column
        )

    return (
        cleaned_df,
        validation_results
    )