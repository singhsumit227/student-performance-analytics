"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Database", "AI"]
PASS_MARK = 40          # minimum marks needed in every subject
MIN_ATTENDANCE = 75     # minimum attendance percentage


def show_data_overview(df):
    """Step 2: display the loaded data and its basic information."""
    print("\n" + "=" * 72)
    print("DATASET OVERVIEW")
    print("=" * 72)
    print(f"Number of records : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")
    print(f"Columns           : {', '.join(df.columns)}")
    print("\nFirst 5 records:")
    print(df.head().to_string(index=False))
    print("\nData types and non-null counts:")
    df.info()


def calculate_total_and_average(df):
    """Add Total_Marks and Average_Marks columns using NumPy."""
    df = df.copy()
    marks = df[SUBJECTS].to_numpy()                       # NumPy 2D array
    df["Total_Marks"] = np.sum(marks, axis=1)             # row-wise total
    df["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)
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
    """Pass only if every subject mark is >= 40 and attendance is >= 75%."""
    marks_pass = all(row[subject] >= PASS_MARK for subject in SUBJECTS)
    attendance_pass = row["Attendance"] >= MIN_ATTENDANCE
    return "Pass" if marks_pass and attendance_pass else "Fail"


def process_student_records(df):
    """Calculate total, average, grade and result for every student."""
    df = calculate_total_and_average(df)
    grades = []
    results = []

    # Loop over every student record and apply the grade/result rules.
    for _, row in df.iterrows():
        grades.append(assign_grade(row["Average_Marks"]))
        results.append(assign_result(row))

    df["Grade"] = grades
    df["Result"] = results
    return df


def subject_analysis(df):
    """Return a table with average, highest, lowest and topper for each subject."""
    rows = []
    for subject in SUBJECTS:                              # loop over subjects
        values = df[subject].to_numpy()
        topper = df.loc[df[subject].idxmax(), "Name"]
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(values)), 2),
            "Highest": int(np.max(values)),
            "Lowest": int(np.min(values)),
            "Std_Dev": round(float(np.std(values)), 2),
            "Subject_Topper": topper,
        })
    return pd.DataFrame(rows)


def get_top_students(df, n=3):
    """Return the top n students ranked by average marks."""
    ranked = df.sort_values("Average_Marks", ascending=False).head(n).copy()
    ranked.insert(0, "Rank", range(1, len(ranked) + 1))
    return ranked[["Rank", "Student_ID", "Name", "Department",
                   "Average_Marks", "Grade"]]


def print_report(df):
    """Print student summaries and class-level analysis."""
    subjects = subject_analysis(df)
    best = subjects.loc[subjects["Average"].idxmax()]
    weakest = subjects.loc[subjects["Average"].idxmin()]
    highest = df.loc[df["Average_Marks"].idxmax()]
    lowest = df.loc[df["Average_Marks"].idxmin()]
    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()

    print("\n" + "=" * 72)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print(f"Total students        : {len(df)}")
    print(f"Students passed       : {passed} ({passed / len(df) * 100:.1f}%)")
    print(f"Students failed       : {failed} ({failed / len(df) * 100:.1f}%)")
    print(f"Overall class average : {df['Average_Marks'].mean():.2f}/100")
    print(f"Highest average       : {highest['Average_Marks']:.2f} ({highest['Name']})")
    print(f"Lowest average        : {lowest['Average_Marks']:.2f} ({lowest['Name']})")

    print("\nSTUDENT-WISE SUMMARY")
    columns = ["Student_ID", "Name", "Department", "Total_Marks",
               "Average_Marks", "Grade", "Result", "Attendance"]
    print(df[columns].to_string(index=False))

    print("\nSUBJECT-WISE ANALYSIS")
    print(subjects.to_string(index=False))
    print(f"\nBest subject   : {best['Subject']} (average {best['Average']:.2f})")
    print(f"Weakest subject: {weakest['Subject']} (average {weakest['Average']:.2f})")

    print("\nTOP 3 PERFORMERS")
    print(get_top_students(df, 3).to_string(index=False))

    print("\nFAILED STUDENTS (with reason)")
    for _, row in df[df["Result"] == "Fail"].iterrows():
        reasons = [f"{s} < {PASS_MARK}" for s in SUBJECTS if row[s] < PASS_MARK]
        if row["Attendance"] < MIN_ATTENDANCE:
            reasons.append(f"attendance {row['Attendance']}% < {MIN_ATTENDANCE}%")
        print(f"  {row['Student_ID']} {row['Name']}: {', '.join(reasons)}")

    print("\nDEPARTMENT-WISE AVERAGE")
    print(df.groupby("Department")["Average_Marks"].mean().round(2).to_string())

    print("\nGRADE DISTRIBUTION")
    print(df["Grade"].value_counts().sort_index().to_string())
    print("=" * 72)
