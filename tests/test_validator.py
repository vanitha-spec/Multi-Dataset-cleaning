import pandas as pd

from src.reader import read_dataset

from src.string_cleaner import (
    standardize_column_names,
    clean_whitespace,
    clean_name_column,
)

from src.validator import (
    validate_required_columns,
    validate_required_values,
    validate_range,
    validate_unique,
    validate_email_format,
    create_validation_summary,
)


def main():
    """
    Test customer data validation rules.
    """

    # Read the raw customer data.
    df = read_dataset(
        "data/raw/customers.csv"
    )

    # Standardize column names.
    df = standardize_column_names(
        df
    )

    # Clean whitespace.
    df = clean_whitespace(
        df
    )

    # Clean customer names.
    df = clean_name_column(
        df,
        "customer_name"
    )

    # Convert age to numeric.
    df["age"] = pd.to_numeric(
        df["age"],
        errors="coerce"
    )

    print("\n===== DATA BEING VALIDATED =====")

    print(df)

    # --------------------------------
    # Rule 1: Required columns
    # --------------------------------

    required_columns_result = (
        validate_required_columns(
            df,
            [
                "customer_id",
                "customer_name",
                "age",
                "gender",
                "city",
                "email",
            ]
        )
    )

    # --------------------------------
    # Rule 2: Required values
    # --------------------------------

    required_values_result = (
        validate_required_values(
            df,
            [
                "customer_id",
                "customer_name",
            ]
        )
    )

    # --------------------------------
    # Rule 3: Age range
    # --------------------------------

    age_result = validate_range(
        df,
        "age",
        minimum=18,
        maximum=100
    )

    # --------------------------------
    # Rule 4: Unique Customer IDs
    # --------------------------------

    unique_result = validate_unique(
        df,
        "customer_id"
    )

    # --------------------------------
    # Rule 5: Email format
    # --------------------------------

    email_result = validate_email_format(
        df,
        "email"
    )

    # Put all rules together.
    validation_results = {
        "required_columns": required_columns_result,
        "required_values": required_values_result,
        "age_range": age_result,
        "unique_customer_id": unique_result,
        "email_format": email_result,
    }

    # --------------------------------
    # Print each validation result
    # --------------------------------

    print("\n===== VALIDATION RESULTS =====")

    for rule_name, result in validation_results.items():

        status = (
            "PASS"
            if result["valid"]
            else "FAIL"
        )

        print(
            f"\n{rule_name}: {status}"
        )

        print(
            result["message"]
        )

    # --------------------------------
    # Show invalid age rows
    # --------------------------------

    print("\n===== INVALID AGE ROWS =====")

    print(
        age_result[
            "invalid_rows"
        ]
    )

    # --------------------------------
    # Show duplicate IDs
    # --------------------------------

    print("\n===== DUPLICATE CUSTOMER IDs =====")

    print(
        unique_result[
            "duplicate_rows"
        ]
    )

    # --------------------------------
    # Show invalid emails
    # --------------------------------

    print("\n===== INVALID EMAILS =====")

    print(
        email_result[
            "invalid_rows"
        ]
    )

    # --------------------------------
    # Overall summary
    # --------------------------------

    summary = create_validation_summary(
        validation_results
    )

    print("\n===== OVERALL VALIDATION =====")

    print(
        f"Overall valid: "
        f"{summary['valid']}"
    )

    print(
        f"Total rules: "
        f"{summary['total_rules']}"
    )

    print(
        f"Passed rules: "
        f"{summary['passed_rules']}"
    )

    print(
        f"Failed rules: "
        f"{summary['failed_rules']}"
    )

    print(
        "Failed rule names:"
    )

    print(
        summary["failed_rule_names"]
    )


if __name__ == "__main__":
    main()