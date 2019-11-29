from CodingChallengeModule.Classes import Employee, Manager


# Class responsible for outputting the employee hierarchy
class DataReader:

    # Constructor
    def __init__(self):
        self


    # Public method that builds the python represenation of the employee hierarchy
    #   Input: N/A
    #   Output: managerJeff : Manager
    def Read(self):

        # Create 'Employee' objects for all employees
        employeeJeff = Employee('Jeff', 100000)
        employeeDave = Employee('Dave', 85000)
        employeeCory = Employee('Cory', 65000)
        employeeAndy = Employee('Andy', 65000)
        employeeDan = Employee('Dan', 60000)
        employeeJason = Employee('Jason', 60000)
        employeeRick = Employee('Rick', 56000)
        employeeSuzanne = Employee('Suzanne', 61000)

        # Build manager Dave's list of direct reports
        managerDaveEmployees = [
            employeeAndy,
            employeeDan,
            employeeJason,
            employeeRick,
            employeeSuzanne
        ]

        # Create 'Manager' object for Dave
        managerDave = Manager(employeeDave, managerDaveEmployees)

        # Build manager Jeff's list of direct reports
        managerJeffEmployees = [
            managerDave,
            employeeCory
        ]

        # Create 'Manager' object for Jeff
        managerJeff = Manager(employeeJeff, managerJeffEmployees)

        # return rootManager object (CEO of the company 'managerJeff')
        return managerJeff