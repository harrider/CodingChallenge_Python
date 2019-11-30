from io import StringIO
from typing import Union
from CodingChallengeModule.Classes import Employee, Manager


# Class responsible for outputting the employee hierarchy
class SortedEmployeeHierarchyPrinter:

    # Constructor
    def __init__(self):
        self


    # Public method that builds the output string
    #   Input: rootManager : Manager
    #   Output: printString : str
    def PrintString(self, rootManager : Manager):
        
        # Guard clauses to ensure parameters are valid
        if rootManager is None:
            raise ValueError('ERROR :: value for "manager" is NONE!')
        if isinstance(rootManager, Manager) == False:
            raise ValueError('ERROR :: type of "manager" is not "Manager"!')

        # Build the formatted employee hierarchy print string
        printString = self.__PrintStringRecursive(rootManager, 0)
        
        # Return the formatted employee hierarchy print string
        return printString


    # Private method that calculates the sum of employee salaries through recursion
    #   Input: employee : Union[Employee, Manager], hierarchyLevel : int
    #   Output: builder : string
    def __PrintStringRecursive(self, employee : Union[Employee, Manager], hierarchyLevel : int):
        
        # Guard clauses to ensure parameters are valid
        if employee is None:
            raise ValueError('ERROR :: value for "manager" is NONE!')
        if isinstance(employee, Manager) == False and isinstance(employee, Employee) == False:
            raise ValueError('ERROR :: type of "employee" must be "Manager" or "Employee"!')
        if hierarchyLevel < 0:
            raise ValueError('ERROR :: value for "hierarchyLevel" is NEGATIVE!')

        # Create a string builder object
        builder = StringIO()

        # If the 'employee' parameter is a 'Manager'
        if isinstance(employee, Manager):
            
            # Append i number of tab characters depending on 'hierarchyLevel'
            for i in range(0, hierarchyLevel, 1):
                builder.write("\t")

            # Append the Manager's name
            builder.write(employee.manager.name)
            builder.write("\n")

            # Append i number of tab characters depending on 'hierarchyLevel'
            for i in range(0, hierarchyLevel, 1):
                builder.write("\t")

            # Append a line to designate a Manager's list of direct reports
            builder.write(f'Employees of: {employee.manager.name}')
            builder.write("\n")

            # Sort the current manager's list of employees / direct reports
            sortedEmployees = sorted( employee.employees, key = lambda x: x.name )

            # Iterate through a Manager's list of direct reports
            for person in sortedEmployees:

                # If current direct report is a 'Manager'
                if isinstance(person, Manager):

                    # Call method recursively to build the current manager's list of direct reports
                    employeesString = self.__PrintStringRecursive(person, hierarchyLevel + 1)
                    
                    # Append current direct reporting manager's formatted hierarchy string to current manager
                    builder.write(employeesString)

                # Else if current direct report is an 'Employee'
                elif isinstance(person, Employee):

                    # Append i number of tab characters depending on 'hierarchyLevel'
                    for i in range(0, hierarchyLevel + 1, 1):
                        builder.write("\t")

                    # Append current employee's name
                    builder.write(person.name)
                    builder.write("\n")

        # Else if the 'employee' parameter is an 'Employee'
        elif isinstance(employee, Employee):

            # Append i number of tab characters depending on 'hierarchyLevel'
            for i in range(0, hierarchyLevel, 1):
                builder.write("\t")
           
            # Append employee's name
            builder.write(employee.name)
            builder.write("\n")

        # Build string and return the final value
        return builder.getvalue()