from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom



school = School("ABC", "Tala")


eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")


school.add_classroom(eight)
school.add_classroom(eight)
school.add_classroom(eight)



rahim = Student("Rahim", eight)
habib = Student("Habib", nine)
karin = Student("Karin", nine)
ratan = Student("Ratan", ten)
kamal = Student("Kamal", ten)
manik = Student("Manik", eight)


