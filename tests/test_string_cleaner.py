from src.reader import read_dataset

from src.string_cleaner import (
    clean_whitespace,
    standardize_categories,
    clean_name_column,
    standardize_column_names,
)


def main():
    """
    Test the string cleaning functions
    using the customers dataset.
    """

    # ---------------------------------------------------------
    # Read the customers dataset
    # ---------------------------------------------------------

    df = read_dataset(
        "data/raw/customers.csv"
    )

    print("\n===== ORIGINAL DATA =====")

    print(df.head(10))

    # ---------------------------------------------------------
    # Standardize column names
    # ---------------------------------------------------------

    df = standardize_column_names(df)

    print("\n===== AFTER COLUMN NAME CLEANING =====")

    print(df.columns.tolist())

    # ---------------------------------------------------------
    # Clean whitespace
    # ---------------------------------------------------------

    df = clean_whitespace(df)

    print("\n===== AFTER WHITESPACE CLEANING =====")

    print(
        df[
            [
                "customer_id",
                "customer_name",
                "city"
            ]
        ].head(10)
    )

    # ---------------------------------------------------------
    # Clean names
    # ---------------------------------------------------------

    df = clean_name_column(
        df,
        "customer_name"
    )

    print("\n===== AFTER NAME CLEANING =====")

    print(
        df[
            [
                "customer_id",
                "customer_name"
            ]
        ].head(10)
    )

    # ---------------------------------------------------------
    # Standardize gender
    # ---------------------------------------------------------

    gender_mapping = {
        "Male": "Male",
        "male": "Male",
        "MALE": "Male",
        "M": "Male",
        "m": "Male",

        "Female": "Female",
        "female": "Female",
        "FEMALE": "Female",
        "F": "Female",
        "f": "Female",
    }

    df = standardize_categories(
        df,
        "gender",
        gender_mapping
    )

    print("\n===== AFTER GENDER STANDARDIZATION =====")

    print(
        df["gender"].value_counts(
            dropna=False
        )
    )

    # ---------------------------------------------------------
    # Final result
    # ---------------------------------------------------------

    print("\n===== FINAL CLEANED DATA =====")

    print(df)


if __name__ == "__main__":
    main()