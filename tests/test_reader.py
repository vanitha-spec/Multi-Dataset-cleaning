from src.reader import read_dataset


def main():
    print("\n===== READING CUSTOMERS =====")

    customers = read_dataset(
        "data/raw/customers.csv"
    )

    print(customers)

    print("\n===== READING ORDERS =====")

    orders = read_dataset(
        "data/raw/orders.csv"
    )

    print(orders)

    print("\n===== READING PRODUCTS =====")

    products = read_dataset(
        "data/raw/products.xlsx"
    )

    print(products)

    print("\n===== READING EMPLOYEES =====")

    employees = read_dataset(
        "data/raw/employees.csv"
    )

    print(employees)


if __name__ == "__main__":
    main()