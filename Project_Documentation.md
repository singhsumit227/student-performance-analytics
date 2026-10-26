# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project Title:** Student Performance Analytics System  
**Student Name:** [Enter your name]  
**Course:** Python with AI  
**Institute/Training Provider:** EWB Courses  
**Submission Date:** [Enter date]

## 2. Objective
The objective of this project is to analyze student marks and attendance using Python. It calculates each student's total and average marks, assigns a grade, identifies pass/fail status, compares subject performance, and finds top performers. This reduces manual calculation and presents results in a readable format.

## 3. Technologies Used
- Python
- NumPy
- Pandas
- CSV file for storing the dataset

## 4. Dataset Description
The project uses `students.csv`, a sample dataset containing 20 fictional student records. The columns are:
- `Student_ID`: unique student identifier
- `Name`: student name
- `Department`: student's department
- `Python`, `Mathematics`, `Database`, `AI`: marks out of 100
- `Attendance`: attendance percentage

Attendance is used for the pass/fail condition and is not included in the marks total or average.

## 5. Implementation
1. `main.py` locates and loads the CSV dataset with `pandas.read_csv()`.
2. It checks that required columns exist, that the dataset is not empty, and that marks/attendance are numeric and between 0 and 100.
3. `functions.py` defines reusable functions for calculations, grading, pass/fail checks and reporting.
4. Pandas calculates each student's total and average across the four subjects. NumPy is used to round averages to two decimal places.
5. A loop processes each row and applies the grade and pass/fail functions.
6. The report shows student-level results, class statistics, subject averages, department averages, top performer(s) and grade distribution.
7. The analyzed dataset is saved as `student_analysis_output.csv`.

## 6. Key Features and Rules
### Grade rule
- A+: average >= 80
- A: average >= 70 and below 80
- B: average >= 60 and below 70
- C: average >= 50 and below 60
- D: average >= 40 and below 50
- F: average below 40

### Pass/fail rule
A student passes only if every subject mark is at least 40 **and** attendance is at least 75%. Otherwise, the student fails. These are the rules selected for this project and may not match institutional rules.

### Main outputs
- Total and average marks for every student
- Grade and pass/fail result
- Highest and lowest student average
- Overall class average
- Subject-wise average marks
- Top-performing student(s)
- Department-wise average
- Grade distribution

## 7. Output / Screenshots
**Insert screenshots after running `python main.py`:**
1. Terminal output showing class statistics and student-wise summary.
2. Subject-wise average and top performer output.
3. The generated `student_analysis_output.csv` file (optional).

Do not insert screenshots until you have run the program and confirmed the output.

## 8. Final Outcome
The system converts the CSV student dataset into a structured performance report. It demonstrates Python fundamentals, reusable functions, loops, conditions, NumPy numerical operations and Pandas data analysis.

## 9. Challenges and Learning
**Use only what is true for your own work; edit this section after testing.** Possible learning points include:
- Reading CSV data into a DataFrame.
- Selecting subject columns for calculations.
- Writing reusable functions for grades and pass/fail logic.
- Validating data to avoid incorrect calculations.
- Summarizing performance by subject and department.
- Exporting processed results to a new CSV file.

## 10. GitHub Repository
**Repository URL:** [Paste your public GitHub repository URL here]

## How to Run
Install dependencies with `python -m pip install -r requirements.txt`, then run `python main.py`.
