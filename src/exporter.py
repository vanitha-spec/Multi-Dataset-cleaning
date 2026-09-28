from pathlib import Path
import pandas as pd


def ensure_output_directory(file_path):
    """
    Create the parent directory for an output file if it does not exist.

    Parameters:
        file_path (str or Path):
            Path where the output file will be saved.

    Returns:
        Path:
            The normalized output file path.
    """
    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    return path


def export_to_csv(df, file_path, index=False):
    """
    Export a pandas DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame):
            The DataFrame to export.

        file_path (str or Path):
            Destination path for the CSV file.

        index (bool):
            Whether to include the DataFrame index in the CSV file.

    Returns:
        Path:
            Path of the exported CSV file.

    Raises:
        TypeError:
            If the input is not a pandas DataFrame.

        ValueError:
            If the output file does not have a .csv extension.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    path = ensure_output_directory(file_path)

    if path.suffix.lower() != ".csv":
        raise ValueError(
            "CSV export requires a .csv file extension."
        )

    df.to_csv(
        path,
        index=index
    )

    return path


def export_to_excel(df, file_path, index=False):
    """
    Export a pandas DataFrame to an Excel file.

    Parameters:
        df (pd.DataFrame):
            The DataFrame to export.

        file_path (str or Path):
            Destination path for the Excel file.

        index (bool):
            Whether to include the DataFrame index in the Excel file.

    Returns:
        Path:
            Path of the exported Excel file.

    Raises:
        TypeError:
            If the input is not a pandas DataFrame.

        ValueError:
            If the output file does not have an Excel extension.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    path = ensure_output_directory(file_path)

    if path.suffix.lower() not in [".xlsx", ".xls"]:
        raise ValueError(
            "Excel export requires a .xlsx or .xls extension."
        )

    df.to_excel(
        path,
        index=index
    )

    return path


def export_dataset(df, file_path, index=False):
    """
    Export a pandas DataFrame based on the file extension.

    CSV files are exported using to_csv().
    Excel files are exported using to_excel().

    Parameters:
        df (pd.DataFrame):
            The DataFrame to export.

        file_path (str or Path):
            Destination path for the output file.

        index (bool):
            Whether to include the DataFrame index in the output.

    Returns:
        Path:
            Path of the exported file.

    Raises:
        TypeError:
            If the input is not a pandas DataFrame.

        ValueError:
            If the file format is unsupported.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    path = Path(file_path)

    extension = path.suffix.lower()

    if extension == ".csv":
        return export_to_csv(
            df,
            path,
            index=index
        )

    elif extension in [".xlsx", ".xls"]:
        return export_to_excel(
            df,
            path,
            index=index
        )

    else:
        raise ValueError(
            f"Unsupported export format: {extension}"
        )