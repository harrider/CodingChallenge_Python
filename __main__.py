import json
import os
from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.DataReader import DataReader
from CodingChallengeModule.JsonDataReader import JsonDataReader
from CodingChallengeModule.EmployeeHierarchyPrinter import EmployeeHierarchyPrinter
from CodingChallengeModule.SortedEmployeeHierarchyPrinter import SortedEmployeeHierarchyPrinter
from CodingChallengeModule.SalaryRequirementPrinter import SalaryRequirementPrinter


# Main
if __name__ == "__main__":

    # Load app settings from settings file
    with open('appsettings.json', 'r') as settingsFile:
        settings = json.load(settingsFile)

        # Guard clause to check for an empty 'settings' variable
        if settings == None:
            raise TypeError('ERROR :: Problem reading "appsettings.json"!')
        if type(settings['EmployeeHierarchyFileName']) != str:
            raise TypeError('ERROR :: Value for settings parameter "EmployeeHierarchyFileName" must be a string!')
        if type(settings['SortEmployeeHierarchyOutput']) != bool:
            raise TypeError('ERROR :: Value for settings parameter "SortEmployeeHierarchyOutput" must be a bool!')

    # Get the app settings values for the specified keys
    employeeHierarchyFileName = settings['EmployeeHierarchyFileName']
    sortEmployeeHierarchyOutputFlag = settings['SortEmployeeHierarchyOutput']

    # Create the filepath to the employee hierarchy json file
    hierarchyFilePath = os.path.join(os.getcwd(), employeeHierarchyFileName)
    
    # Create a DataReader object
    dataReader = JsonDataReader(hierarchyFilePath)

    # Create the data printers that deal with the formatting of the output
    # if 'SortEmployeeHierarchyOutput' is true, create a SortedEmployeeHierarchyPrinter:
    if sortEmployeeHierarchyOutputFlag:
        hierarchyPrinter = SortedEmployeeHierarchyPrinter()
    # else, create an unsorted EmployeeHieararchyPrinter
    else:
        hierarchyPrinter = EmployeeHierarchyPrinter()

    # Create a salary requirement printer
    salaryRequirementPrinter = SalaryRequirementPrinter()

    # Read Employee Data from Data Source
    rootManager = dataReader.Read()

    # Call the data printers' 'PrintString' methods to get the formatted output strings
    employeeHierarchyString = hierarchyPrinter.PrintString(rootManager)
    salaryRequirementString = salaryRequirementPrinter.PrintString(rootManager)

    # Print each formatted output string
    print(employeeHierarchyString)
    print(salaryRequirementString)