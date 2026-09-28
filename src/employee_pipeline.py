import pandas as pd

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


def clean_employees(df, employee_config):
    """
    Clean and validate an employee DataFrame.

    The function cleans whitespace and employee names,
    processes salaries, converts joining dates, removes
    duplicate rows, and validates employee records.

    Parameters:
        df (pd.DataFrame):
            Raw employee DataFrame.

        employee_config (dict):
            Employee-specific rules loaded from YAML.

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
    # Clean employee names
    # -----------------------------------------------

    cleaned_df = clean_name_column(
        cleaned_df,
        "employee_name"
    )

    # -----------------------------------------------
    # Clean salary
    # -----------------------------------------------

    cleaned_df = clean_currency_column(
        cleaned_df,
        "salary"
    )

    # -----------------------------------------------
    # Convert joining date
    # -----------------------------------------------

    cleaned_df = convert_to_datetime(
        cleaned_df,
        "joining_date"
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
        employee_config[
            "required_columns"
        ]
    )

    validation_results[
        "required_values"
    ] = validate_required_values(
        cleaned_df,
        employee_config[
            "required_values"
        ]
    )

    # -----------------------------------------------
    # Positive salary validation
    # -----------------------------------------------

    for column in employee_config[
        "positive_columns"
    ]:

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
    # Unique employee ID validation
    # -----------------------------------------------

    for column in employee_config[
        "unique_columns"
    ]:

        validation_results[
            f"unique_{column}"
        ] = validate_unique(
            cleaned_df,
            column
        )

    # -----------------------------------------------
    # Joining date validation
    # -----------------------------------------------

    validation_results[
        "joining_date"
    ] = validate_datetime(
        cleaned_df,
        "joining_date"
    )

    return (
        cleaned_df,
        validation_results
    )