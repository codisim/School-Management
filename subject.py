from person import Teacher
from school import school

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher  # teacher ar obj
        self.max_marks = 100
        self.pass_marks = 33
        
    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_result() # 1 - 100
            student.marks[self.name] = mark
            student.subject_grades[self.name] = school.calculate_grade(mark)