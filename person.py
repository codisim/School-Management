import random

class Person:
    def __init__(self, name):
        self.name = name
        


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def evaluate_result(self):
        return random.randint(1, 100)
        
        
        
        
class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self._id = random.randint(1000, 9999)
        self.marks = {}
        self.subject_grades = {}
        self.grade = None
    
    