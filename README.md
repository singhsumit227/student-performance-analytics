# Student Performance Analytics System

A Python data-analysis project using **Python, NumPy and Pandas**. It reads a CSV of 20 students and reports totals, averages, grades, pass/fail status, subject-wise performance, department averages and top performers.

## Features
- Loads `students.csv` into a Pandas DataFrame and shows an overview
- Validates the data before analysis
- NumPy-based total, average and subject statistics
- Reusable functions and loops
- Grades, pass/fail with reasons, top 3 performers
- Exports results to `student_analysis_output.csv`

## Rules used
- Subjects: Python, Mathematics, Database, AI (each out of 100)
- Grade: A+ ≥ 80, A ≥ 70, B ≥ 60, C ≥ 50, D ≥ 40, F < 40 (based on average)
- Pass: at least 40 in every subject and attendance ≥ 75%

## Files
| File | Purpose |
|---|---|
| `main.py` | Entry point: load, validate, analyze, export |
| `functions.py` | Reusable calculation and reporting functions |
| `students.csv` | Dataset (20 records) |
| `Project_Documentation.md` | Full project documentation |
| `requirements.txt` | Dependencies |

## Run
```bash
python -m pip install -r requirements.txt
python main.py
```

## Author
[YOUR NAME] – Python with AI, EWB Courses
