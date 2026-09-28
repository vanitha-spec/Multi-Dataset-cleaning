"""
Streamlit front-end for the Multi-Dataset Data Quality Pipeline.

Put this file in the PROJECT ROOT (same folder as main.py), then run:
    py -m streamlit run app.py
"""

import io
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path

import pandas as pd
import streamlit as st

# Make sure "src" is importable when Streamlit runs this file
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from src.pipeline import run_pipeline  # noqa: E402

st.set_page_config(page_title="Data Quality Pipeline", layout="wide")

# dataset name -> (raw input file, cleaned output file)
DATASETS = {
    "customers": ("data/raw/customers.csv", "data/processed/customers_cleaned.csv"),
    "orders": ("data/raw/orders.csv", "data/processed/orders_cleaned.csv"),
    "products": ("data/raw/products.xlsx", "data/processed/products_cleaned.xlsx"),
    "employees": ("data/raw/employees.csv", "data/processed/employees_cleaned.csv"),
}


def load_file(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".xlsx":
        return pd.read_excel(path)
    return pd.read_csv(path)


st.title("Multi-Dataset Data Quality Pipeline")
st.caption("Read - Profile - Clean - Validate - Report - Export")

dataset = st.selectbox("Pick a dataset", list(DATASETS.keys()))
raw_rel, out_rel = DATASETS[dataset]
raw_path, out_path = ROOT / raw_rel, ROOT / out_rel

if not raw_path.exists():
    st.error(f"Raw file not found: {raw_rel}. Copy your raw data into data/raw/ first.")
    st.stop()

if st.button("Run pipeline", type="primary"):
    console = io.StringIO()
    try:
        # The pipeline prints its quality report with print(); capture it
        # so it can be shown in the browser instead of only the terminal.
        with redirect_stdout(console):
            run_pipeline(
                dataset_name=dataset,
                input_path=str(raw_path),
                output_path=str(out_path),
            )
    except Exception:
        st.error("The pipeline raised an error:")
        st.code(traceback.format_exc())
        st.stop()

    raw_df = load_file(raw_path)
    clean_df = load_file(out_path)

    c1, c2, c3 = st.columns(3)
    c1.metric("Raw rows", len(raw_df))
    c2.metric("Cleaned rows", len(clean_df))
    c3.metric("Rows removed", len(raw_df) - len(clean_df))

    tab_report, tab_clean, tab_raw = st.tabs(["Quality report", "Cleaned data", "Raw data"])

    with tab_report:
        st.code(console.getvalue() or "(no console output captured)")
    with tab_clean:
        st.dataframe(clean_df)
    with tab_raw:
        st.dataframe(raw_df)

    st.download_button(
        "Download cleaned file",
        data=out_path.read_bytes(),
        file_name=out_path.name,
    )