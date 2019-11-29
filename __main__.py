from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.DataReader import DataReader
from CodingChallengeModule.EmployeeHierarchyPrinter import EmployeeHierarchyPrinter
from CodingChallengeModule.SalaryRequirementPrinter import SalaryRequirementPrinter


# Main
if __name__ == "__main__":
    # Create a DataReader object and read employee hierarchy data
    dataReader = DataReader()
    rootManager = dataReader.Read()

    # Create the data printers that deal with the formatting of the output
    hierarchyPrinter = EmployeeHierarchyPrinter()
    salaryRequirementPrinter = SalaryRequirementPrinter()

    # Call the data printers' 'PrintString' methods to get the formatted output strings
    employeeHierarchyString = hierarchyPrinter.PrintString(rootManager)
    salaryRequirementString = salaryRequirementPrinter.PrintString(rootManager)

    # Print each formatted output string
    print(employeeHierarchyString)
    print(salaryRequirementString)