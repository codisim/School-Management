
class school:
    def __init_(self, name, location):
        self.name = name
        self.location = location
        self.teachers = {}
        self.location = {}
        self.classrooms = {}
        
        
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom 
    
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
        
    def student_admission(self, student):
        pass
    
    
        
    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return "A+"
        elif marks >= 70 and marks < 80:
            return "A"
        elif marks >= 60 and marks < 70:
            return "A-"
        elif marks >= 50 and marks < 60:
            return "B"
        elif marks >= 40 and marks < 50:
            return "C"
        elif marks >= 33 and marks < 40:
            return "D"
        else:
            return "F"
        
        
    
    @staticmethod
    def grade_to_value(grade):
        grade_values = {
            "A+": 4.0,
            "A": 3.7,
            "A-": 3.3,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return grade_values.get(grade, 0.0)   
    
    
    
    @staticmethod
    def value_to_grade(value):
        if value >= 4.5 and value <= 5.00:
            return "A+"
        
          
    
    
    