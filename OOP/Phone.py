class phone:
    def __init__(self, OS, year, RAM, storage):
        self.OS = OS
        self.year = year
        self.RAM = RAM
        self.storage = storage
    
    def watch(self):
        print(f"You watch YouTube on the {self.OS}")
    
    def checkStorage(self):
        print(f"You have {self.storage}GB left")