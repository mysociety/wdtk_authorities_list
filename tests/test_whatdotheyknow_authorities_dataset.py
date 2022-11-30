import pandas as pd
from pathlib import Path

top_level = Path(__file__).parent.parent
package_dir = top_level / "data" / "packages" / "whatdotheyknow_authorities_dataset"


def all_csvs() -> list[Path]:
    """
    Return a list of all csv files in the package directory.
    """
    return [p for p in package_dir.glob("**/*.csv") if p.is_file()]


def df_columns_are_kebab_case(df: pd.DataFrame) -> bool:
    """
    Check that all columns are in kebab-case.
    """
    columns = list(df.columns)
    for column in columns:
        if "_" in column:
            return False
        if " " in column:
            return False
        if column.lower() != column:
            return False
    return True


def test_correct_columns():
    """
    We want kebab case columns.
    """
    assert package_dir.exists()
    for file in all_csvs():
        df = pd.read_csv(file)
        is_kebab = df_columns_are_kebab_case(df)
        assert is_kebab == True, f"Columns are not in kebab-case in {file.stem}"
