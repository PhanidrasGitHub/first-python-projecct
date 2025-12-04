# grade_manager.py
import json
from student import Student

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        return student.id

    def find_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def update_scores(self, student_id, subject, score):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found")
        student.add_subject(subject, score)

    def view_report(self, student_id):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found")
        print("\n----- Report Card -----")
        print(student)

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

    def save_to_file(self, filename="grades.json"):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="grades.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(s) for s in data]
        except FileNotFoundError:
            self.students = []
