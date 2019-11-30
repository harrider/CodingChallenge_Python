from typing import Union
from CodingChallengeModule.Classes import Employee, Manager


# Class responsible for outputting the salary requirements for the company
class SalaryRequirementPrinter:

    # Constructor
    def __init__(self):
        self

    
    # Public method that builds the output string
    #   Input: rootManager : Manager
    #   Output: formattedPrintString : str
    def PrintString(self, rootManager : Manager):

        # Guard clauses to ensure parameters are valid
        if rootManager is None:
            raise ValueError('ERROR :: value for "manager" is NONE!')
        if isinstance(rootManager, Manager) == False:
            raise ValueError('ERROR :: type of "manager" is not "Manager"!')

        # Calculate the sum of the salary requirement
        sum = self.__PrintStringRecursive(rootManager)

        # Format the sum in US dollars
        formattedSum = '${:,.2f}'.format(sum)
        
        # Build the formatted print string
        formattedPrintString = f'Total salary: {formattedSum}'

        # Return the formatted print string
        return formattedPrintString


    # Private method that calculates the sum of employee salaries through recursion
    #   Input: employee : Union[Employee, Manager]
    #   Output: sum : float
    def __PrintStringRecursive(self, employee : Union[Employee, Manager]):

        # Guard clauses to ensure parameters are valid
        if employee is None:
            raise ValueError('ERROR :: value for "manager" is NONE!')
        if isinstance(employee, Manager) == False and isinstance(employee, Employee) == False:
            raise ValueError('ERROR :: type of "employee" must be "Manager" or "Employee"!')

        # Initialize current sum to '0'
        sum = 0.0

        # If current employee is of type 'Manager'
        if isinstance(employee, Manager):

            # Add current manager's salary to running sum
            sum += employee.manager.salary

            # Iterate through current manager's list of employees / direct reports
            for person in employee.employees:

                # If current manager's employee is a manager themself, call this method recursively
                if isinstance(person, Manager):
                    sum += self.__PrintStringRecursive(person)      # add the result sum to the running sum

                # Else if current manager's employee is just an employee
                elif isinstance(person, Employee):
                    sum += person.salary                            # add the employee's salary to running sum
        
        # Else if current employee is of 'Employee'
        elif isinstance(employee, Employee):

            # Add current employee's salary to running sum
            sum += employee.salary

        # return the calculated sum
        return float(sum)