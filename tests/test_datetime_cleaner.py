from src.reader import read_dataset

from src.datetime_cleaner import (
    convert_to_datetime,
    find_invalid_dates,
    extract_date_only,
    extract_year,
)


def main():
    """
    Test datetime cleaning functions
    using the orders dataset.
    """

    # Read the orders dataset.
    df = read_dataset(
        "data/raw/orders.csv"
    )

    print("\n===== ORIGINAL ORDER DATES =====")

    print(
        df[
            [
                " Order ID",
                "Order Date "
            ]
        ]
    )

    # Convert the order date column.
    df = convert_to_datetime(
        df,
        "Order Date "
    )

    print("\n===== CONVERTED ORDER DATES =====")

    print(
        df[
            [
                " Order ID",
                "Order Date "
            ]
        ]
    )

    print("\n===== DATA TYPES =====")

    print(
        df[
            "Order Date "
        ].dtype
    )

    # Find invalid dates.
    invalid_rows = find_invalid_dates(
        df,
        "Order Date "
    )

    print("\n===== INVALID / MISSING DATES =====")

    print(
        invalid_rows[
            [
                " Order ID",
                "Order Date "
            ]
        ]
    )

    # Extract date only.
    df = extract_date_only(
        df,
        "Order Date "
    )

    print("\n===== DATE ONLY =====")

    print(
        df[
            [
                " Order ID",
                "Order Date "
            ]
        ].head(10)
    )

    # Reload the dataset so we can demonstrate
    # year extraction using datetime values.
    df = read_dataset(
        "data/raw/orders.csv"
    )

    df = convert_to_datetime(
        df,
        "Order Date "
    )

    df = extract_year(
        df,
        "Order Date "
    )

    print("\n===== YEAR EXTRACTION =====")

    print(
        df[
            [
                " Order ID",
                "Order Date ",
                "Order Date _year"
            ]
        ].head(10)
    )


if __name__ == "__main__":
    main()