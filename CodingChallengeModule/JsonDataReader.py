import json
from typing import Union 
from CodingChallengeModule.Classes import Employee, Manager

class JsonDataReader:

    # Constructor
    def __init__(self, hierarchyFileName : str):

        # Guard clauses to ensure parameters are valid
        if hierarchyFileName is None:
            raise ValueError('ERROR :: value for "hierarchyFileName" is NONE!')
        if hierarchyFileName == '':
            raise ValueError('ERROR :: value for "hierarchyFileName" is empty!')
        if hierarchyFileName.lower().endswith('.json') == False:
            raise ValueError('ERROR :: "hierarchyFileName" must be a .JSON file!')

        # Assign instance variables
        self.hierarchyFileName = hierarchyFileName


    # Public method that builds the python represenation of the employee hierarchy
    #   Input: N/A
    #   Output: rootManager : Manager
    def Read(self):

        # Load Employee Hierarchy Data from JSON file
        with open(self.hierarchyFileName, 'r') as jsonFile:
            jsonData = json.load(jsonFile)

            # Build root 'Manager' object from JSON data
            rootManager = self.__ReadRecursive(jsonData)

        # return root manager object
        return rootManager



    # Public method that builds the python represenation of the employee hierarchy
    #   Input: jsonData - Python object representing json data read from employee hierarchy json file
    #   Output: employee : Union[Employee, Manager]
    def __ReadRecursive(self, jsonData):

        # Check the employee type for the current employee
        employeeType = jsonData['EmployeeType']

        # if the current employee is a 'Manager'
        if employeeType == 'Manager':

            managerData = jsonData['EmployeeData']      # Get employee data
            directReports = []                          # create a list to add their direct reports to

            # Iterate through the Manager's list of employees / direct reports
            for person in jsonData['DirectReports']:
                
                # if the current direct reporting employee is a 'Manager'
                if person['EmployeeType'] == 'Manager':

                    # Call this method recursively
                    newManagerEmployee = self.__ReadRecursive(person)

                    # Add the new manager employee to the current manager's list of direct reports
                    directReports.append(newManagerEmployee)

                # else if the current direct employee is an 'Employee'
                elif person['EmployeeType'] == 'Employee':

                    # Create a new 'Employee' object
                    newEmployee = Employee(
                        person['EmployeeData']['Name'],
                        person['EmployeeData']['Salary'],
                    )

                    # Add the new employee to the current manager's list of direct reports
                    directReports.append(newEmployee)

            # Create a new 'Employee' object to store the current manager's employee data
            managerEmployee = Employee(
                managerData['Name'],
                managerData['Salary']
            )

            # Create a new 'Manager' object to decorate the managerEmployee object and store
            #   list of current manager's employees / direct reports
            newManager = Manager(
                managerEmployee,
                directReports
            )

            # return the 'Manager' object
            return newManager

        # Else if the current employee is an 'Employee
        elif employeeType == 'Employee':

            # Create a new 'Employee' object to store the employee's data
            newEmployee = Employee(
                jsonData['EmployeeData']['Name'],
                jsonData['EmployeeData']['Salary'],
            )

            # return the 'Employee' object
            return newEmployee

        # Else, dealing with an unhandled type
        else:
            raise ValueError(f'ERROR :: type "{employeeType}" is not supported!')