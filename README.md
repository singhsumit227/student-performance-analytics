# Student Performance Analytics System

A beginner-friendly Python data-analysis mini project using **Python, NumPy and Pandas**. It analyzes a CSV dataset of 20 students and reports marks, averages, grades, pass/fail status, subject performance and top performers.

## Features
- Reads student records from `students.csv` into a Pandas DataFrame.
- Uses NumPy/Pandas operations to calculate total and average marks.
- Uses reusable functions, loops and conditions.
- Assigns grades from the student's average.
- Checks pass/fail using subject marks and attendance.
- Shows class statistics, subject-wise averages, department averages and grade distribution.
- Saves the detailed result to `student_analysis_output.csv`.

## Rules used
- Subjects: Python, Mathematics, Database and AI; each is marked out of 100.
- Grade: A+ = 80–100, A = 70–79.99, B = 60–69.99, C = 50–59.99, D = 40–49.99, F = below 40.
- Pass: at least 40 marks in **every subject** and attendance of at least 75%.
- Attendance is not included in total or average marks.

These are project rules, not official college grading rules.

## Files
- `main.py` — entry point; loads, validates, analyzes and exports data.
- `functions.py` — reusable calculation and reporting functions.
- `students.csv` — sample dataset with 20 fictional student records.
- `Project_Documentation.md` — project report template/details.
- `requirements.txt` — required Python libraries.

## Run the project
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
5. The report is printed in the terminal and `student_analysis_output.csv` is created.


## Before submitting
- Run the program yourself and inspect the results.
- Replace or personalize the student details if your trainer expects your own dataset.
- Add your name, course/batch and screenshots to the documentation.
- Make sure you understand the grade and pass/fail rules because the assessment focuses on understanding, not only output.
