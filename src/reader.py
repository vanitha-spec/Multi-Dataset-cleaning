from pathlib import Path

import pandas as pd


def read_dataset(file_path):
    """
    Read a CSV or Excel dataset into a pandas DataFrame.

    Parameters:
        file_path (str or Path):
            Path to the input CSV or Excel file.

    Returns:
        pd.DataFrame:
            The loaded dataset.

    Raises:
        FileNotFoundError:
            If the specified file does not exist.

        ValueError:
            If the file format is not supported.
    """

    # Convert the given path into a Path object.
    path = Path(file_path)

    # Check whether the file actually exists.
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    # Get the file extension.
    extension = path.suffix.lower()

    # Read CSV files.
    if extension == ".csv":
        return pd.read_csv(path)

    # Read Excel files.
    elif extension in [".xlsx", ".xls"]:
        return pd.read_excel(path)

    # Reject unsupported file formats.
    else:
        raise ValueError(
            f"Unsupported file format: {extension}"
        )