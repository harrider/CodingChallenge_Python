# Class responsible for modeling employee data
class Employee:
    def __init__(self, name : str, salary : int):
        self.name = name
        self.salary = salary


# Class responsible for modeling manager data
class Manager:
    def __init__(self, manager : Employee, employees : []):
        self.manager = manager
        self.employees = employees