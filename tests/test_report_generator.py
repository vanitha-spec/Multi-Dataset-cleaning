import pandas as pd

from src.reader import read_dataset

from src.cleaner import (
    remove_duplicate_rows,
)

from src.string_cleaner import (
    standardize_column_names,
)

from src.validator import (
    validate_required_columns,
    validate_required_values,
    validate_range,
    validate_unique,
    validate_email_format,
)

from src.report_generator import (
    generate_data_quality_report,
    print_data_quality_report,
)


def main():
    """
    Test the data-quality report generator.
    """

    # ----------------------------
    # Read original data
    # ----------------------------

    original_df = read_dataset(
        "data/raw/customers.csv"
    )

    # ----------------------------
    # Create cleaned copy
    # ----------------------------

    cleaned_df = original_df.copy()

    # Standardize column names.
    cleaned_df = (
        standardize_column_names(
            cleaned_df
        )
    )

    # Convert age to numeric.
    cleaned_df["age"] = pd.to_numeric(
        cleaned_df["age"],
        errors="coerce"
    )

    # Remove completely duplicated rows.
    cleaned_df = (
        remove_duplicate_rows(
            cleaned_df
        )
    )

    # ----------------------------
    # Run validation
    # ----------------------------

    validation_results = {}

    validation_results[
        "required_columns"
    ] = validate_required_columns(
        cleaned_df,
        [
            "customer_id",
            "customer_name",
            "age",
            "gender",
            "city",
            "email",
        ]
    )

    validation_results[
        "required_values"
    ] = validate_required_values(
        cleaned_df,
        [
            "customer_id",
            "customer_name",
        ]
    )

    validation_results[
        "age_range"
    ] = validate_range(
        cleaned_df,
        "age",
        minimum=18,
        maximum=100
    )

    validation_results[
        "unique_customer_id"
    ] = validate_unique(
        cleaned_df,
        "customer_id"
    )

    validation_results[
        "email_format"
    ] = validate_email_format(
        cleaned_df,
        "email"
    )

    # ----------------------------
    # Generate report
    # ----------------------------

    report = (
        generate_data_quality_report(
            original_df,
            cleaned_df,
            validation_results
        )
    )

    # ----------------------------
    # Print report
    # ----------------------------

    print_data_quality_report(
        report
    )


if __name__ == "__main__":
    main()