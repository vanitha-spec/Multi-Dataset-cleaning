from src.pipeline import run_pipeline


def main():
    """
    Start the multi-dataset data-cleaning application.
    """

    # -----------------------------------------------
    # CUSTOMERS
    # -----------------------------------------------

    run_pipeline(
        dataset_name="customers",
        input_path="data/raw/customers.csv",
        output_path=(
            "data/processed/"
            "customers_cleaned.csv"
        )
    )

    # -----------------------------------------------
    # ORDERS
    # -----------------------------------------------

    run_pipeline(
        dataset_name="orders",
        input_path="data/raw/orders.csv",
        output_path=(
            "data/processed/"
            "orders_cleaned.csv"
        )
    )

    # -----------------------------------------------
    # PRODUCTS
    # -----------------------------------------------

    run_pipeline(
        dataset_name="products",
        input_path="data/raw/products.xlsx",
        output_path=(
            "data/processed/"
            "products_cleaned.xlsx"
        )
    )

    # -----------------------------------------------
    # EMPLOYEES
    # -----------------------------------------------

    run_pipeline(
        dataset_name="employees",
        input_path="data/raw/employees.csv",
        output_path=(
            "data/processed/"
            "employees_cleaned.csv"
        )
    )


if __name__ == "__main__":
    main()