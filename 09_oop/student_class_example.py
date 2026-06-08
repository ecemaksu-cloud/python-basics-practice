# Student class example

class Student:

    surname = "ALP"

    def __init__(self, name="Undefined", student_id=0):
        self.name = name
        self.student_id = student_id


print("Student surname:", Student.surname)

student1 = Student()
print("Student 1:", student1.name)

student2 = Student()
student2.name = "Yasin"

student1.name = "Ali"

student3 = Student("Ahmet", 400)

print(student1.name)
print(student2.name)
print(student3.name, student3.student_id)

print("Student 1 ID:", student1.student_id)
print("Student 2 ID:", student2.student_id)
print("Student 3 ID:", student3.student_id)
