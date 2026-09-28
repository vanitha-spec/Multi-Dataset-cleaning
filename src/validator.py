import re

import pandas as pd


def validate_required_columns(
    df,
    required_columns
):
    """
    Check whether all required columns exist in a DataFrame.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        required_columns (list):
            Columns that must exist.

    Returns:
        dict:
            Validation result containing:
                - valid
                - missing_columns
                - message
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    valid = len(missing_columns) == 0

    if valid:
        message = "All required columns are present."

    else:
        message = (
            f"Missing required columns: "
            f"{missing_columns}"
        )

    return {
        "valid": valid,
        "missing_columns": missing_columns,
        "message": message,
    }


def validate_required_values(
    df,
    columns
):
    """
    Find rows where required columns contain missing values.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        columns (list):
            Columns that must contain values.

    Returns:
        dict:
            Validation result containing:
                - valid
                - invalid_rows
                - invalid_count
    """

    # Check whether all requested columns exist.
    missing_columns = [
        column
        for column in columns
        if column not in df.columns
    ]

    if missing_columns:
        return {
            "valid": False,
            "invalid_rows": pd.DataFrame(),
            "invalid_count": 0,
            "message": (
                f"Columns not found: "
                f"{missing_columns}"
            ),
        }

    # Identify rows with missing required values.
    invalid_mask = df[
        columns
    ].isna().any(axis=1)

    invalid_rows = df[
        invalid_mask
    ].copy()

    return {
        "valid": len(invalid_rows) == 0,
        "invalid_rows": invalid_rows,
        "invalid_count": len(invalid_rows),
        "message": (
            "All required values are present."
            if len(invalid_rows) == 0
            else (
                f"{len(invalid_rows)} rows "
                f"have missing required values."
            )
        ),
    }


def validate_range(
    df,
    column,
    minimum=None,
    maximum=None
):
    """
    Validate that numeric values fall within a specified range.

    Missing values are not considered range violations;
    required-field validation should handle missing values separately.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        column (str):
            Numeric column to validate.

        minimum:
            Minimum allowed value.

        maximum:
            Maximum allowed value.

    Returns:
        dict:
            Validation result containing invalid rows.
    """

    if column not in df.columns:
        return {
            "valid": False,
            "invalid_rows": pd.DataFrame(),
            "invalid_count": 0,
            "message": f"Column not found: {column}",
        }

    # Convert values to numeric for validation.
    values = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    invalid_mask = pd.Series(
        False,
        index=df.index
    )

    # Apply minimum rule.
    if minimum is not None:
        invalid_mask = invalid_mask | (
            values < minimum
        )

    # Apply maximum rule.
    if maximum is not None:
        invalid_mask = invalid_mask | (
            values > maximum
        )

    invalid_rows = df[
        invalid_mask
    ].copy()

    return {
        "valid": len(invalid_rows) == 0,
        "invalid_rows": invalid_rows,
        "invalid_count": len(invalid_rows),
        "message": (
            "All values are within the allowed range."
            if len(invalid_rows) == 0
            else (
                f"{len(invalid_rows)} rows "
                f"are outside the allowed range."
            )
        ),
    }


def validate_positive(
    df,
    column
):
    """
    Validate that numeric values are greater than zero.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        column (str):
            Numeric column to validate.

    Returns:
        dict:
            Validation result containing invalid rows.
    """

    if column not in df.columns:
        return {
            "valid": False,
            "invalid_rows": pd.DataFrame(),
            "invalid_count": 0,
            "message": f"Column not found: {column}",
        }

    # Convert to numeric.
    values = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    # Zero and negative values are invalid.
    invalid_mask = values <= 0

    # Missing values are handled separately.
    invalid_mask = invalid_mask.fillna(False)

    invalid_rows = df[
        invalid_mask
    ].copy()

    return {
        "valid": len(invalid_rows) == 0,
        "invalid_rows": invalid_rows,
        "invalid_count": len(invalid_rows),
        "message": (
            "All values are positive."
            if len(invalid_rows) == 0
            else (
                f"{len(invalid_rows)} rows "
                f"contain zero or negative values."
            )
        ),
    }


def validate_non_negative(
    df,
    column
):
    """
    Validate that numeric values are zero or greater.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        column (str):
            Numeric column to validate.

    Returns:
        dict:
            Validation result containing invalid rows.
    """

    if column not in df.columns:
        return {
            "valid": False,
            "invalid_rows": pd.DataFrame(),
            "invalid_count": 0,
            "message": f"Column not found: {column}",
        }

    values = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    invalid_mask = (
        values < 0
    )

    invalid_rows = df[
        invalid_mask
    ].copy()

    return {
        "valid": len(invalid_rows) == 0,
        "invalid_rows": invalid_rows,
        "invalid_count": len(invalid_rows),
        "message": (
            "All values are non-negative."
            if len(invalid_rows) == 0
            else (
                f"{len(invalid_rows)} rows "
                f"contain negative values."
            )
        ),
    }


def validate_unique(
    df,
    column
):
    """
    Validate that values in a column are unique.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        column (str):
            Column that should contain unique values.

    Returns:
        dict:
            Validation result containing duplicate rows.
    """

    if column not in df.columns:
        return {
            "valid": False,
            "duplicate_rows": pd.DataFrame(),
            "duplicate_count": 0,
            "message": f"Column not found: {column}",
        }

    duplicate_mask = df[
        column
    ].duplicated(
        keep=False
    )

    duplicate_rows = df[
        duplicate_mask
    ].copy()

    return {
        "valid": len(duplicate_rows) == 0,
        "duplicate_rows": duplicate_rows,
        "duplicate_count": len(duplicate_rows),
        "message": (
            f"All values in {column} are unique."
            if len(duplicate_rows) == 0
            else (
                f"{len(duplicate_rows)} rows "
                f"contain duplicate {column} values."
            )
        ),
    }


def validate_email_format(
    df,
    column
):
    """
    Validate email addresses using a basic email pattern.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        column (str):
            Column containing email addresses.

    Returns:
        dict:
            Validation result containing invalid email rows.
    """

    if column not in df.columns:
        return {
            "valid": False,
            "invalid_rows": pd.DataFrame(),
            "invalid_count": 0,
            "message": f"Column not found: {column}",
        }

    # Basic email validation pattern.
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    def is_valid_email(value):
        """
        Check one email value.
        """

        if pd.isna(value):
            return False

        return bool(
            re.match(
                pattern,
                str(value)
            )
        )

    valid_mask = df[
        column
    ].apply(
        is_valid_email
    )

    invalid_rows = df[
        ~valid_mask
    ].copy()

    return {
        "valid": len(invalid_rows) == 0,
        "invalid_rows": invalid_rows,
        "invalid_count": len(invalid_rows),
        "message": (
            "All email addresses are valid."
            if len(invalid_rows) == 0
            else (
                f"{len(invalid_rows)} rows "
                f"contain invalid email addresses."
            )
        ),
    }


def validate_datetime(
    df,
    column
):
    """
    Validate that values in a column can be interpreted as dates.

    Parameters:
        df (pd.DataFrame):
            DataFrame being validated.

        column (str):
            Date column to validate.

    Returns:
        dict:
            Validation result containing invalid rows.
    """

    if column not in df.columns:
        return {
            "valid": False,
            "invalid_rows": pd.DataFrame(),
            "invalid_count": 0,
            "message": f"Column not found: {column}",
        }

    parsed_dates = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    invalid_mask = (
        parsed_dates.isna()
    )

    invalid_rows = df[
        invalid_mask
    ].copy()

    return {
        "valid": len(invalid_rows) == 0,
        "invalid_rows": invalid_rows,
        "invalid_count": len(invalid_rows),
        "message": (
            "All dates are valid."
            if len(invalid_rows) == 0
            else (
                f"{len(invalid_rows)} rows "
                f"contain invalid or missing dates."
            )
        ),
    }


def create_validation_summary(
    validation_results
):
    """
    Create a compact summary from multiple validation results.

    Parameters:
        validation_results (dict):
            Dictionary containing named validation results.

    Returns:
        dict:
            Overall validation summary.
    """

    total_rules = len(
        validation_results
    )

    failed_rules = [
        name
        for name, result
        in validation_results.items()
        if not result["valid"]
    ]

    passed_rules = (
        total_rules - len(failed_rules)
    )

    overall_valid = (
        len(failed_rules) == 0
    )

    return {
        "valid": overall_valid,
        "total_rules": total_rules,
        "passed_rules": passed_rules,
        "failed_rules": len(failed_rules),
        "failed_rule_names": failed_rules,
    }