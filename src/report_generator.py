import pandas as pd


def count_missing_values(df):
    """
    Count missing values in every column.

    Parameters:
        df (pd.DataFrame):
            DataFrame to analyze.

    Returns:
        dict:
            Dictionary containing missing-value counts
            for each column.
    """

    return df.isna().sum().to_dict()


def count_total_missing_values(df):
    """
    Count the total number of missing values in a DataFrame.

    Parameters:
        df (pd.DataFrame):
            DataFrame to analyze.

    Returns:
        int:
            Total number of missing values.
    """

    return int(
        df.isna().sum().sum()
    )


def count_duplicate_rows(df):
    """
    Count duplicate rows in a DataFrame.

    Parameters:
        df (pd.DataFrame):
            DataFrame to analyze.

    Returns:
        int:
            Number of duplicate rows.
    """

    return int(
        df.duplicated().sum()
    )


def compare_row_counts(
    original_df,
    cleaned_df
):
    """
    Compare row counts between original and cleaned DataFrames.

    Parameters:
        original_df (pd.DataFrame):
            Original DataFrame.

        cleaned_df (pd.DataFrame):
            Cleaned DataFrame.

    Returns:
        dict:
            Row-count comparison information.
    """

    original_rows = len(
        original_df
    )

    cleaned_rows = len(
        cleaned_df
    )

    rows_removed = (
        original_rows - cleaned_rows
    )

    return {
        "original_rows": original_rows,
        "cleaned_rows": cleaned_rows,
        "rows_removed": rows_removed,
    }


def compare_columns(
    original_df,
    cleaned_df
):
    """
    Compare column names between original and cleaned DataFrames.

    Parameters:
        original_df (pd.DataFrame):
            Original DataFrame.

        cleaned_df (pd.DataFrame):
            Cleaned DataFrame.

    Returns:
        dict:
            Information about added and removed columns.
    """

    original_columns = set(
        original_df.columns
    )

    cleaned_columns = set(
        cleaned_df.columns
    )

    added_columns = sorted(
        cleaned_columns - original_columns
    )

    removed_columns = sorted(
        original_columns - cleaned_columns
    )

    return {
        "original_columns": list(
            original_df.columns
        ),
        "cleaned_columns": list(
            cleaned_df.columns
        ),
        "added_columns": added_columns,
        "removed_columns": removed_columns,
    }


def summarize_validation_results(
    validation_results
):
    """
    Summarize validation results.

    Parameters:
        validation_results (dict):
            Dictionary containing validation results.

    Returns:
        dict:
            Validation summary.
    """

    total_rules = len(
        validation_results
    )

    passed_rules = 0
    failed_rules = 0
    failed_rule_names = []

    for rule_name, result in validation_results.items():

        if result["valid"]:
            passed_rules += 1

        else:
            failed_rules += 1

            failed_rule_names.append(
                rule_name
            )

    return {
        "total_rules": total_rules,
        "passed_rules": passed_rules,
        "failed_rules": failed_rules,
        "failed_rule_names": failed_rule_names,
        "overall_valid": (
            failed_rules == 0
        ),
    }


def generate_data_quality_report(
    original_df,
    cleaned_df,
    validation_results=None
):
    """
    Generate a complete data-quality report.

    The report compares the original and cleaned DataFrames
    and optionally includes validation results.

    Parameters:
        original_df (pd.DataFrame):
            DataFrame before cleaning.

        cleaned_df (pd.DataFrame):
            DataFrame after cleaning.

        validation_results (dict, optional):
            Validation results produced by validator.py.

    Returns:
        dict:
            Complete data-quality report.
    """

    # Compare row counts.
    row_comparison = compare_row_counts(
        original_df,
        cleaned_df
    )

    # Compare columns.
    column_comparison = compare_columns(
        original_df,
        cleaned_df
    )

    # Count missing values.
    original_missing = (
        count_total_missing_values(
            original_df
        )
    )

    cleaned_missing = (
        count_total_missing_values(
            cleaned_df
        )
    )

    # Count duplicate rows.
    original_duplicates = (
        count_duplicate_rows(
            original_df
        )
    )

    cleaned_duplicates = (
        count_duplicate_rows(
            cleaned_df
        )
    )

    # Build the base report.
    report = {
        "rows": row_comparison,

        "columns": column_comparison,

        "missing_values": {
            "original": original_missing,
            "cleaned": cleaned_missing,
            "difference": (
                original_missing
                - cleaned_missing
            ),
        },

        "duplicates": {
            "original": original_duplicates,
            "cleaned": cleaned_duplicates,
            "removed": (
                original_duplicates
                - cleaned_duplicates
            ),
        },
    }

    # Add validation information if available.
    if validation_results is not None:

        report["validation"] = (
            summarize_validation_results(
                validation_results
            )
        )

    return report


def print_data_quality_report(
    report
):
    """
    Print a human-readable data-quality report.

    Parameters:
        report (dict):
            Report generated by
            generate_data_quality_report().

    Returns:
        None
    """

    print("\n")
    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)

    # ----------------------------
    # Rows
    # ----------------------------

    print("\nROWS")

    print(
        f"Original rows : "
        f"{report['rows']['original_rows']}"
    )

    print(
        f"Cleaned rows  : "
        f"{report['rows']['cleaned_rows']}"
    )

    print(
        f"Rows removed  : "
        f"{report['rows']['rows_removed']}"
    )

    # ----------------------------
    # Columns
    # ----------------------------

    print("\nCOLUMNS")

    print(
        f"Added columns   : "
        f"{report['columns']['added_columns']}"
    )

    print(
        f"Removed columns : "
        f"{report['columns']['removed_columns']}"
    )

    # ----------------------------
    # Missing values
    # ----------------------------

    print("\nMISSING VALUES")

    print(
        f"Original : "
        f"{report['missing_values']['original']}"
    )

    print(
        f"Cleaned  : "
        f"{report['missing_values']['cleaned']}"
    )

    print(
        f"Difference : "
        f"{report['missing_values']['difference']}"
    )

    # ----------------------------
    # Duplicates
    # ----------------------------

    print("\nDUPLICATES")

    print(
        f"Original : "
        f"{report['duplicates']['original']}"
    )

    print(
        f"Cleaned  : "
        f"{report['duplicates']['cleaned']}"
    )

    print(
        f"Removed  : "
        f"{report['duplicates']['removed']}"
    )

    # ----------------------------
    # Validation
    # ----------------------------

    if "validation" in report:

        validation = report[
            "validation"
        ]

        print("\nVALIDATION")

        print(
            f"Total rules  : "
            f"{validation['total_rules']}"
        )

        print(
            f"Passed rules : "
            f"{validation['passed_rules']}"
        )

        print(
            f"Failed rules : "
            f"{validation['failed_rules']}"
        )

        print(
            f"Overall valid: "
            f"{validation['overall_valid']}"
        )

        print(
            f"Failed rule names: "
            f"{validation['failed_rule_names']}"
        )

    print("\n" + "=" * 60)