from src.reader import read_dataset

from src.string_cleaner import (
    standardize_column_names,
    clean_whitespace,
    clean_name_column,
)

from src.transformer import (
    rename_columns,
    replace_values,
    map_values,
    apply_function,
    sort_by_column,
    set_dataframe_index,
    reset_dataframe_index,
    select_columns,
    get_column_names,
)


def classify_age(age):
    """
    Classify a customer into an age group.

    Parameters:
        age:
            Customer age.

    Returns:
        str:
            Age category.
    """

    # Handle missing values.
    if age is None:
        return "Unknown"

    # Handle pandas missing values.
    if hasattr(age, "__class__") and str(age) == "<NA>":
        return "Unknown"

    # Convert age to numeric.
    try:
        age = float(age)
    except (TypeError, ValueError):
        return "Unknown"

    if age < 18:
        return "Minor"

    elif age < 60:
        return "Adult"

    else:
        return "Senior"


def main():
    """
    Test the DataFrame transformation functions.
    """

    # Read customers.
    df = read_dataset(
        "data/raw/customers.csv"
    )

    print("\n===== ORIGINAL COLUMNS =====")

    print(
        get_column_names(df)
    )

    # Standardize raw column names first.
    df = standardize_column_names(df)

    # Clean whitespace.
    df = clean_whitespace(df)

    # Clean customer names.
    df = clean_name_column(
        df,
        "customer_name"
    )

    print("\n===== CLEANED DATA =====")

    print(
        df[
            [
                "customer_id",
                "customer_name",
                "age",
                "gender",
                "city"
            ]
        ].head(10)
    )

    # Standardize gender using replace().
    gender_mapping = {
        "male": "Male",
        "MALE": "Male",
        "M": "Male",
        "m": "Male",
        "female": "Female",
        "FEMALE": "Female",
        "F": "Female",
        "f": "Female",
    }

    df = replace_values(
        df,
        "gender",
        gender_mapping
    )

    print("\n===== AFTER REPLACE =====")

    print(
        df["gender"].value_counts(
            dropna=False
        )
    )

    # Standardize city using map().
    city_mapping = {
        "hyderabad": "Hyderabad",
        "Hyderabad": "Hyderabad",
        "HYDERABAD": "Hyderabad",

        "bengaluru": "Bengaluru",
        "Bengaluru": "Bengaluru",

        "chennai": "Chennai",
        "Chennai": "Chennai",

        "mumbai": "Mumbai",
        "Mumbai": "Mumbai",

        "delhi": "Delhi",
        "Delhi": "Delhi",
    }

    df = map_values(
        df,
        "city",
        city_mapping
    )

    print("\n===== AFTER MAP =====")

    print(
        df[
            [
                "customer_id",
                "city"
            ]
        ]
    )

    # Convert age to numeric.
    df["age"] = __import__(
        "pandas"
    ).to_numeric(
        df["age"],
        errors="coerce"
    )

    # Apply custom business logic.
    df = apply_function(
        df,
        "age",
        classify_age
    )

    print("\n===== AFTER APPLY =====")

    print(
        df[
            [
                "customer_id",
                "age",
            ]
        ]
    )

    # Sort by customer ID.
    df = sort_by_column(
        df,
        "customer_id"
    )

    print("\n===== AFTER SORT =====")

    print(
        df[
            [
                "customer_id",
                "customer_name",
                "city"
            ]
        ]
    )

    # Select only useful columns.
    df = select_columns(
        df,
        [
            "customer_id",
            "customer_name",
            "city",
            "gender",
        ]
    )

    print("\n===== SELECTED COLUMNS =====")

    print(df)

    # Set customer ID as index.
    df = set_dataframe_index(
        df,
        "customer_id"
    )

    print("\n===== AFTER SET_INDEX =====")

    print(df)

    # Reset index.
    df = reset_dataframe_index(
        df
    )

    print("\n===== AFTER RESET_INDEX =====")

    print(df)


if __name__ == "__main__":
    main()