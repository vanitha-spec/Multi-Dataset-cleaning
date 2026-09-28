from src.reader import read_dataset

from src.numeric_cleaner import (
    clean_currency_column,
    convert_numeric_column,
    find_negative_values,
)


def main():
    """
    Test numeric cleaning functions
    using the employees dataset.
    """

    # Read the employees dataset.
    df = read_dataset(
        "data/raw/employees.csv"
    )

    print("\n===== ORIGINAL SALARY DATA =====")

    print(
        df[
            [
                "Employee Name",
                "Salary"
            ]
        ]
    )

    # Clean the salary column.
    df = clean_currency_column(
        df,
        "Salary"
    )

    print("\n===== CLEANED SALARY DATA =====")

    print(
        df[
            [
                "Employee Name",
                "Salary",
                "Salary_currency",
                "Salary_amount"
            ]
        ]
    )

    # Find negative salaries.
    negative_rows = find_negative_values(
        df,
        "Salary_amount"
    )

    print("\n===== NEGATIVE SALARY VALUES =====")

    print(
        negative_rows[
            [
                "Employee Name",
                "Salary",
                "Salary_amount"
            ]
        ]
    )

    # Demonstrate numeric conversion.
    quantity_data = read_dataset(
        "data/raw/orders.csv"
    )

    quantity_data = convert_numeric_column(
        quantity_data,
        "Quantity "
    )

    print("\n===== CLEANED ORDER QUANTITY =====")

    print(
        quantity_data[
            [
                " Order ID",
                "Quantity "
            ]
        ]
    )


if __name__ == "__main__":
    main()