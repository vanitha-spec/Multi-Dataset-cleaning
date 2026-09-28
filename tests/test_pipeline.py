from src.reader import read_dataset

from src.config_loader import (
    load_config,
    get_dataset_config,
)

from src.customer_pipeline import (
    clean_customers,
)

from src.order_pipeline import (
    clean_orders,
)

from src.product_pipeline import (
    clean_products,
)

from src.employee_pipeline import (
    clean_employees,
)


def main():

    config = load_config(
        "config/cleaning_rules.yaml"
    )

    # -----------------------------------------------
    # Customers
    # -----------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING CUSTOMERS")
    print("=" * 60)

    customers = read_dataset(
        "data/raw/customers.csv"
    )

    customers_cleaned, customer_validation = (
        clean_customers(
            customers,
            get_dataset_config(
                config,
                "customers"
            )
        )
    )

    print(
        "Original rows:",
        len(customers)
    )

    print(
        "Cleaned rows:",
        len(customers_cleaned)
    )

    print(
        "Validation:",
        customer_validation
    )

    # -----------------------------------------------
    # Orders
    # -----------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING ORDERS")
    print("=" * 60)

    orders = read_dataset(
        "data/raw/orders.csv"
    )

    orders_cleaned, order_validation = (
        clean_orders(
            orders,
            get_dataset_config(
                config,
                "orders"
            )
        )
    )

    print(
        "Original rows:",
        len(orders)
    )

    print(
        "Cleaned rows:",
        len(orders_cleaned)
    )

    print(
        "Validation:",
        order_validation
    )

    # -----------------------------------------------
    # Products
    # -----------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING PRODUCTS")
    print("=" * 60)

    products = read_dataset(
        "data/raw/products.xlsx"
    )

    products_cleaned, product_validation = (
        clean_products(
            products,
            get_dataset_config(
                config,
                "products"
            )
        )
    )

    print(
        "Original rows:",
        len(products)
    )

    print(
        "Cleaned rows:",
        len(products_cleaned)
    )

    print(
        "Validation:",
        product_validation
    )

    # -----------------------------------------------
    # Employees
    # -----------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING EMPLOYEES")
    print("=" * 60)

    employees = read_dataset(
        "data/raw/employees.csv"
    )

    employees_cleaned, employee_validation = (
        clean_employees(
            employees,
            get_dataset_config(
                config,
                "employees"
            )
        )
    )

    print(
        "Original rows:",
        len(employees)
    )

    print(
        "Cleaned rows:",
        len(employees_cleaned)
    )

    print(
        "Validation:",
        employee_validation
    )


if __name__ == "__main__":
    main()