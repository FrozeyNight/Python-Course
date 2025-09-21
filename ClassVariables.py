class Student:
    
    classYear = 2025
    numberOfStudents = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.numberOfStudents += 1
    
student1 = Student("Patrick", 18)
student2 = Student("John", 19)
student3 = Student("Alice", 18)
student4 = Student("Bob", 18)

print(f"There are {Student.numberOfStudents} students in the {Student.classYear} class")