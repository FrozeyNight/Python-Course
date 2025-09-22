class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def getInfo(self):
        print(f"{self.name} {self.position}")
    
    @staticmethod #Python's static keyword, used to allow calling methods without needing an object of that class
    def isValidPosition(position):
        validPositions = ["Manager", "Cook", "Waiter", "Janitor"]
        return position in validPositions

employee = Employee("Patrick", "Manager")
print(employee.getInfo())
print(Employee.isValidPosition("Manager"))
print(Employee.isValidPosition("Accountant"))
        