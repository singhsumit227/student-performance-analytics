"""Main program for Student Performance Analytics System."""

from pathlib import Path
import pandas as pd
from functions import process_student_records, print_report

DATA_FILE = Path(__file__).parent / "students.csv"
OUTPUT_FILE = Path(__file__).parent / "student_analysis_output.csv"


def main():
    """Load data, validate it, analyze it, and save the result."""
    if not DATA_FILE.exists():
        print(f"Error: Dataset not found at {DATA_FILE}")
        return

    data = pd.read_csv(DATA_FILE)

    required_columns = [
        "Student_ID", "Name", "Department", "Python",
        "Mathematics", "Database", "AI", "Attendance"
    ]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        print("Error: Missing required columns:", ", ".join(missing_columns))
        return

    if data.empty:
        print("Error: Dataset is empty.")
        return

    numeric_columns = ["Python", "Mathematics", "Database", "AI", "Attendance"]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    if data[numeric_columns].isna().any().any():
        print("Error: Marks or attendance contains blank/non-numeric values.")
        return

    if not data[numeric_columns].apply(lambda col: col.between(0, 100).all()).all():
        print("Error: Marks and attendance must be between 0 and 100.")
        return

    analyzed_data = process_student_records(data)
    print_report(analyzed_data)
    analyzed_data.to_csv(OUTPUT_FILE, index=False)
    print(f"\\nDetailed results saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
