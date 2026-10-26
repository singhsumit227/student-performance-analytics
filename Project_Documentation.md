# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project Title:** Student Performance Analytics System  
**Student Name:** [Sumit Singh]  
**Course:** Python with AI  
**Institute/Training Provider:** EWB Courses  
**Submission Date:** [26/10/2026]

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
   ![Dataset overview](screenshots/01_overview.png)
   ![Student summary](screenshots/02_summary.png)
   ![Subject analysis and top performers](screenshots/03_subjects_top.png)
   ![Failed students and departments](screenshots/04_failed_dept.png)

Do not insert screenshots until you have run the program and confirmed the output.

## 8. Final Outcome
For the 20-student dataset the system found:
- **16 passed, 4 failed** (80% pass rate)
- Overall class average: **71.95**
- Highest average: **Isha Mishra (94.00)**; lowest: **Arjun Yadav (39.25)**
- Best subject: **AI (74.30)**; weakest: **Python (69.50)**
- Top 3: Isha Mishra, Myra Kapoor, Rohan Singh
- Department averages: Data Science 76.89, CSE 74.11, IT 63.67

## 9. Challenges and Learning
- Reading CSV data into a DataFrame.
- Selecting subject columns for calculations.
- Writing reusable functions for grades and pass/fail logic.
- Validating data to avoid incorrect calculations.
- Summarizing performance by subject and department.
- Exporting processed results to a new CSV file.

## 10. GitHub Repository
**Repository URL:** [https://github.com/singhsumit227/student-performance-analytics]

## How to Run
Install dependencies with `python -m pip install -r requirements.txt`, then run `python main.py`.
