
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