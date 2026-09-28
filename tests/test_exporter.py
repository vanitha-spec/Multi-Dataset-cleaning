from src.reader import read_dataset
from src.exporter import export_dataset


def main():
    print("Testing CSV export...")

    customers = read_dataset(
        "data/raw/customers.csv"
    )

    csv_path = export_dataset(
        customers,
        "data/processed/customers_test.csv"
    )

    print(f"CSV exported successfully: {csv_path}")

    print("\nTesting Excel export...")

    products = read_dataset(
        "data/raw/products.xlsx"
    )

    excel_path = export_dataset(
        products,
        "data/processed/products_test.xlsx"
    )

    print(
        f"Excel exported successfully: {excel_path}"
    )


if __name__ == "__main__":
    main()