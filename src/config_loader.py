from pathlib import Path

import yaml


def load_config(file_path):
    """
    Load a YAML configuration file.

    Parameters:
        file_path (str or Path):
            Path to the YAML configuration file.

    Returns:
        dict:
            Configuration data loaded from the YAML file.

    Raises:
        FileNotFoundError:
            If the configuration file does not exist.

        ValueError:
            If the YAML file does not contain a dictionary.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {path}"
        )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError(
            "Configuration must contain a YAML dictionary."
        )

    return config


def get_dataset_config(config, dataset_name):
    """
    Retrieve configuration rules for a specific dataset.

    Parameters:
        config (dict):
            Complete configuration dictionary.

        dataset_name (str):
            Name of the dataset whose rules are required.

    Returns:
        dict:
            Dataset-specific configuration.

    Raises:
        KeyError:
            If the requested dataset is not configured.
    """
    if dataset_name not in config:
        raise KeyError(
            f"Dataset configuration not found: "
            f"{dataset_name}"
        )

    return config[dataset_name]