from src.config_loader import (
    load_config,
    get_dataset_config,
)


def main():

    config = load_config(
        "config/cleaning_rules.yaml"
    )

    print("=" * 60)
    print("CONFIGURATION LOADED")
    print("=" * 60)

    print("\nConfigured datasets:")

    for dataset_name in config:
        print("-", dataset_name)

    print("\nCustomer configuration:")

    customer_config = get_dataset_config(
        config,
        "customers"
    )

    print(customer_config)

    print("\nCustomer age rules:")

    print(
        customer_config["age"]
    )

    print("\nCustomer gender mapping:")

    print(
        customer_config["gender_mapping"]
    )


if __name__ == "__main__":
    main()