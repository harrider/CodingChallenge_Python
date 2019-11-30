import argparse
from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.DataReader import DataReader
from CodingChallengeModule.EmployeeHierarchyPrinter import EmployeeHierarchyPrinter
from CodingChallengeModule.SortedEmployeeHierarchyPrinter import SortedEmployeeHierarchyPrinter
from CodingChallengeModule.SalaryRequirementPrinter import SalaryRequirementPrinter


# Main
if __name__ == "__main__":
    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='flag to determine whether to sort the employee hierarchy output')
    parser.add_argument('-s', '--sort',
                        dest='sortOutput',
                        type=bool,
                        default=False,
                        help='flag to determine whether to sort the employee hierarchy output')

    # Parse for any command line arguments
    args = parser.parse_args()

    # Create a DataReader object and read employee hierarchy data
    dataReader = DataReader()
    rootManager = dataReader.Read()

    # Create the data printers that deal with the formatting of the output
    # if command line argument '-s' or '--sort' used, create a SortedEmployeeHieararchyPrinter
    if args.sortOutput:
        hierarchyPrinter = SortedEmployeeHierarchyPrinter()
    # else, create an unsorted EmployeeHieararchyPrinter
    else:
        hierarchyPrinter = EmployeeHierarchyPrinter()

    # Create a salary requirement printer
    salaryRequirementPrinter = SalaryRequirementPrinter()

    # Call the data printers' 'PrintString' methods to get the formatted output strings
    employeeHierarchyString = hierarchyPrinter.PrintString(rootManager)
    salaryRequirementString = salaryRequirementPrinter.PrintString(rootManager)

    # Print each formatted output string
    print(employeeHierarchyString)
    print(salaryRequirementString)