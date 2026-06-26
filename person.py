import random
from school import School 

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
    
    def final_grade(self):
        sum = 0
        for grade in self.subject_grades.values():
            point = School.grade_to_value(grade)
            sum += point
            gpa = sum / len(self.subject_grades)
            self.grade = School.value_to_grade(gpa)
            
            
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
        