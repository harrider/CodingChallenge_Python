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
        sum = 0.0

        if isinstance(employee, Manager):
            sum += employee.manager.salary

            for person in employee.employees:

                if isinstance(person, Manager):
                    sum += self.__PrintStringRecursive(person)

                elif isinstance(person, Employee):
                    sum += person.salary
        
        elif isinstance(employee, Employee):
            sum += employee.salary

        return float(sum)