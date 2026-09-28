from src.reader import read_dataset

from src.string_cleaner import (
    standardize_column_names,
)

from src.report_generator import (
    generate_data_quality_report,
    print_data_quality_report,
)

from src.exporter import (
    export_dataset,
)

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


def get_dataset_processor(dataset_name):
    """
    Return the cleaning function associated with a dataset.

    Parameters:
        dataset_name (str):
            Name of the dataset.

    Returns:
        function:
            Dataset-specific cleaning function.

    Raises:
        ValueError:
            If the dataset is not supported.
    """

    processors = {
        "customers": clean_customers,
        "orders": clean_orders,
        "products": clean_products,
        "employees": clean_employees,
    }

    if dataset_name not in processors:
        raise ValueError(
            f"Unsupported dataset: {dataset_name}"
        )

    return processors[dataset_name]


def run_pipeline(
    dataset_name,
    input_path,
    output_path,
    config_path="config/cleaning_rules.yaml"
):
    """
    Run the complete data-cleaning pipeline for a dataset.

    The pipeline performs the following steps:

        1. Load configuration.
        2. Read the raw dataset.
        3. Standardize column names.
        4. Select the dataset-specific processor.
        5. Clean and validate the dataset.
        6. Generate a data-quality report.
        7. Export the cleaned dataset.

    Parameters:
        dataset_name (str):
            Dataset identifier configured in YAML.

        input_path (str):
            Path to the raw dataset.

        output_path (str):
            Path where the cleaned dataset will be saved.

        config_path (str):
            Path to the YAML configuration file.

    Returns:
        dict:
            Pipeline execution results.
    """

    print("\n" + "=" * 70)
    print(
        f"DATA CLEANING PIPELINE: "
        f"{dataset_name.upper()}"
    )
    print("=" * 70)

    # ------------------------------------------------
    # STEP 1: LOAD CONFIGURATION
    # ------------------------------------------------

    print("\n[1/7] Loading configuration...")

    config = load_config(
        config_path
    )

    dataset_config = get_dataset_config(
        config,
        dataset_name
    )

    print(
        f"Configuration loaded for: "
        f"{dataset_name}"
    )

    # ------------------------------------------------
    # STEP 2: READ DATASET
    # ------------------------------------------------

    print("\n[2/7] Reading dataset...")

    raw_df = read_dataset(
        input_path
    )

    print(
        f"Loaded {len(raw_df)} rows "
        f"and {len(raw_df.columns)} columns."
    )

    # ------------------------------------------------
    # STEP 3: STANDARDIZE COLUMN NAMES
    # ------------------------------------------------

    print("\n[3/7] Standardizing column names...")

    raw_df = standardize_column_names(
        raw_df
    )

    print(
        "Columns:",
        raw_df.columns.tolist()
    )

    # ------------------------------------------------
    # STEP 4: SELECT DATASET PROCESSOR
    # ------------------------------------------------

    print("\n[4/7] Selecting dataset processor...")

    processor = get_dataset_processor(
        dataset_name
    )

    print(
        f"Selected processor: "
        f"{processor.__name__}"
    )

    # ------------------------------------------------
    # STEP 5: CLEAN AND VALIDATE
    # ------------------------------------------------

    print("\n[5/7] Cleaning and validating...")

    cleaned_df, validation_results = (
        processor(
            raw_df,
            dataset_config
        )
    )

    print(
        f"Cleaning completed. "
        f"Rows after cleaning: "
        f"{len(cleaned_df)}"
    )

    # ------------------------------------------------
    # STEP 6: GENERATE REPORT
    # ------------------------------------------------

    print("\n[6/7] Generating quality report...")

    report = generate_data_quality_report(
        raw_df,
        cleaned_df,
        validation_results
    )

    print_data_quality_report(
        report
    )

    # ------------------------------------------------
    # STEP 7: EXPORT
    # ------------------------------------------------

    print("\n[7/7] Exporting cleaned dataset...")

    exported_path = export_dataset(
        cleaned_df,
        output_path,
        index=False
    )

    print(
        f"Cleaned dataset saved to: "
        f"{exported_path}"
    )

    print(
        "\nPipeline completed successfully."
    )

    return {
        "dataset_name": dataset_name,
        "cleaned_df": cleaned_df,
        "validation_results": validation_results,
        "report": report,
        "output_path": exported_path,
    }