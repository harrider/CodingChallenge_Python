# Class responsible for modeling employee data
class Employee:
    def __init__(self, name : str, salary : int):

        # Guard clauses to ensure only valid 'Employee' is created
        if name is None or name == '':
                raise ValueError('ERROR :: value for "employee" is NONE!')
        if salary < 0:
            raise ValueError('ERROR :: value for "salary" is NEGATIVE!')

        # Assign instance variables
        self.name = name
        self.salary = salary



# Class responsible for modeling manager data; This class uses the 'Decorator' design pattern
#   to decorate 'Employee' type objects in order to extend their functionality.  This extends a
#   normal employee to a manager employee.
class Manager:
    def __init__(self, manager : Employee, employees : []):

        # Guard clauses to ensure only valid 'Manager' is created
        if manager is None:
            raise ValueError('ERROR :: value for "manager" is NONE!')
        if employees is None:
            raise ValueError('ERROR :: value for "employees" is NONE!')

        # Assign instance variables
        self.manager = manager
        self.employees = employees

        self.name = manager.name
        self.salary = manager.salary