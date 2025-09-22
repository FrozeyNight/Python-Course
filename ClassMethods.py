class Student:
    
    count = 0
    totalGPA = 0

    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA
        Student.count += 1
        Student.totalGPA += GPA
    
    def getInfo(self):
        print(f"{self.name} {self.GPA}")

    @classmethod
    def getCount(cls):
        return f"# of students: {cls.count}"
    
    @classmethod
    def getAverageGPA(cls):
        return f"The average GPA is: {cls.totalGPA / cls.count:.2f}"


student1 = Student("John", 3.2)
student2 = Student("Alice", 4.1)
student3 = Student("Jane", 3.8)

print(Student.getCount())
print(Student.getAverageGPA())