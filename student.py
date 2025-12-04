# student.py
import uuid

class Student:
    def __init__(self, name):
        self.id = str(uuid.uuid4())[:8]  # auto-generated short ID
        self.name = name
        self.subjects = {}  # { "Math": 90, "Science": 80 }

    def add_subject(self, subject, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.subjects[subject] = score

    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 90: return "A"
        if avg >= 75: return "B"
        if avg >= 60: return "C"
        return "Fail"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "subjects": self.subjects
        }

    @staticmethod
    def from_dict(data):
        s = Student(data["name"])
        s.id = data["id"]
        s.subjects = data["subjects"]
        return s

    def __str__(self):
        report = f"{self.name} (ID: {self.id})\n"
        for sub, marks in self.subjects.items():
            report += f"  {sub}: {marks}\n"
        report += f"Average: {self.calculate_average():.2f} | Grade: {self.get_grade()}\n"
        return report
