"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Database", "AI"]
PASS_MARK = 40
MIN_ATTENDANCE = 75


def calculate_total_and_average(df):
    """Add total and average marks columns."""
    df = df.copy()
    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    df["Average_Marks"] = np.round(df[SUBJECTS].mean(axis=1), 2)
    return df


def assign_grade(average):
    """Assign a grade using the project's stated grading rule."""
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def assign_result(row):
    """Pass only if every subject mark is at least 40 and attendance is at least 75%."""
    marks_pass = all(row[subject] >= PASS_MARK for subject in SUBJECTS)
    attendance_pass = row["Attendance"] >= MIN_ATTENDANCE
    return "Pass" if marks_pass and attendance_pass else "Fail"


def process_student_records(df):
    """Calculate derived columns for every student."""
    df = calculate_total_and_average(df)
    grades = []
    results = []

    # A loop is used to demonstrate iteration over student records.
    for _, row in df.iterrows():
        grades.append(assign_grade(row["Average_Marks"]))
        results.append(assign_result(row))

    df["Grade"] = grades
    df["Result"] = results
    return df


def print_report(df):
    """Print student summaries and class-level analysis."""
    subjects = SUBJECTS
    print("\n" + "=" * 72)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print(f"Total students: {len(df)}")
    print(f"Students passed: {(df['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(df['Result'] == 'Fail').sum()}")
    print(f"Overall class average: {df['Average_Marks'].mean():.2f}/100")
    print(f"Highest student average: {df['Average_Marks'].max():.2f}/100")
    print(f"Lowest student average: {df['Average_Marks'].min():.2f}/100")

    print("\\nSTUDENT-WISE SUMMARY")
    columns = ["Student_ID", "Name", "Department", "Total_Marks",
               "Average_Marks", "Grade", "Result", "Attendance"]
    print(df[columns].to_string(index=False))

    print("\\nSUBJECT-WISE AVERAGE")
    for subject in subjects:
        print(f"{subject}: {df[subject].mean():.2f}/100")

    top_average = df["Average_Marks"].max()
    top_students = df[df["Average_Marks"] == top_average]
    print("\\nTOP PERFORMER(S)")
    print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))

    print("\\nDEPARTMENT-WISE AVERAGE")
    department_summary = df.groupby("Department")["Average_Marks"].mean().round(2)
    print(department_summary.to_string())

    print("\\nGrade distribution")
    print(df["Grade"].value_counts().sort_index().to_string())
    print("=" * 72)
