from src.reader import read_dataset

from src.cleaner import (
    copy_dataframe,
    remove_duplicate_rows,
    drop_empty_columns,
    fill_missing_values,
    fill_missing_with_mean,
    drop_rows_with_missing,
    set_display_options,
)


def main():
    """
    Test the general DataFrame cleaning functions.
    """

    # Configure pandas display.
    set_display_options(
        max_rows=100,
        max_columns=50
    )

    # Read customers.
    df = read_dataset(
        "data/raw/customers.csv"
    )

    print("\n===== ORIGINAL CUSTOMERS =====")

    print(df)

    print("\nOriginal row count:")
    print(len(df))

    # Create a safe copy.
    clean_df = copy_dataframe(
        df
    )

    # Remove duplicate rows.
    clean_df = remove_duplicate_rows(
        clean_df
    )

    print("\n===== AFTER DUPLICATE REMOVAL =====")

    print(clean_df)

    print("\nCleaned row count:")
    print(len(clean_df))

    # Fill missing email values.
    clean_df = fill_missing_values(
        clean_df,
        "Email",
        "Not Provided"
    )

    print("\n===== AFTER FILLING EMAIL =====")

    print(
        clean_df[
            [
                "Customer ID",
                "Email"
            ]
        ]
    )

    # Fill missing age values using mean.
    clean_df = fill_missing_with_mean(
        clean_df,
        "Age "
    )

    print("\n===== AFTER FILLING AGE =====")

    print(
        clean_df[
            [
                "Customer ID",
                "Age "
            ]
        ]
    )

    # Demonstrate dropping rows with required data.
    required_df = drop_rows_with_missing(
        clean_df,
        [
            "Customer ID"
        ]
    )

    print("\n===== AFTER REQUIRED-FIELD VALIDATION =====")

    print(required_df)

    print("\nFinal row count:")
    print(len(required_df))


if __name__ == "__main__":
    main()