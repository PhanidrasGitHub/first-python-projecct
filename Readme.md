# Student Report Card Manager

## Project Overview

The **Student Report Card Manager** is a console-based Python application that allows users to manage student grades using **Object-Oriented Programming (OOP) principles**.  
It enables adding students, recording subject-wise marks, calculating averages and grades, updating/deleting records, and storing/retrieving data from a JSON file (`grades.json`).

---

## Key Features

- Add student records with multiple subjects and scores
- Update subject marks or add new subjects
- View grade reports including average and grade
- Delete student records
- Save and load student data to/from `grades.json`
- Fully encapsulated and modular OOP design

---

## Technologies Used

- Python 3.12
- JSON for data persistence
- OOP Concepts: Encapsulation, Inheritance, Polymorphism, Abstraction

---

## Project Structure

pythonproject/
│
├─ main.py # Main console program (menu & user input)
├─ student.py # Student class (attributes & methods)
├─ grade_manager.py # GradeManager class (CRUD operations & file I/O)
├─ grades.json # Data storage file (created automatically)
└─ README.md # Project documentation

yaml
Copy code

---

## How to Run

1. Make sure Python 3.12 is installed. Check with:

```bash
python --version
Navigate to the project folder in terminal:

bash
Copy code
cd path/to/student_report_card
Run the program:

bash
Copy code
python main.py
Follow the menu:

markdown
Copy code
===== Student Grade Manager =====
1. Add Student
2. Update Scores
3. View Report
4. Delete Student
5. Save & Exit
Add Student: Enter student name, subjects, and scores.

Update Scores: Enter student ID, subject, and new score.

View Report: Enter student ID to see grades.

Delete Student: Enter student ID to remove a record.

Save & Exit: Saves all data to grades.json and exits.

Notes
Student IDs are auto-generated (first 8 characters of a UUID).

Make sure to note the ID when adding a student; it is used for all updates and deletions.

grades.json is automatically created and updated when saving.

Future Enhancements
Add a feature to list all students and their IDs

Add ranking or top scorer report

Add login/authentication for multiple users

Export reports to CSV or PDF

Author
Phanindra Gullapudi

yaml
Copy code

---

If you want, I can also make a **shorter “Interview-friendly” README** version that looks very professional and can be **shown in your portfolio or GitHub** — easy to impress.

Do you want me to do that?







```
