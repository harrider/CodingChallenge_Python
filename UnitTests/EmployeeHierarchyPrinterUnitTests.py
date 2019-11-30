import unittest
from io import StringIO
from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.EmployeeHierarchyPrinter import EmployeeHierarchyPrinter


# 'EmployeeHierarchyPrinter' object tests
class EmployeeHierarchyPrinterUnitTests(unittest.TestCase):

    # Unit Test Setup
    def setUp(self):
        # Create 'Employee' objects for all employees
        employeeJeff = Employee('Jeff', 100000)
        employeeDave = Employee('Dave', 85000)
        employeeCory = Employee('Cory', 65000)
        employeeAndy = Employee('Andy', 65000)
        employeeDan = Employee('Dan', 60000)

        # Build manager Dave's list of direct reports
        managerDaveEmployees = [
            employeeDan,
            employeeAndy
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

        # Assign 'rootManager' attribute the setup value
        self.rootManager = managerJeff

#--------------------------------------------------------------------------------------------------

    # Unit Test Tear Down
    def tearDown(self):
        self

#--------------------------------------------------------------------------------------------------

    # Test to ensure valid creation of object is as expected
    def test_EmployeeHierarchyPrinterValidCreation(self):
        hierarchyPrinter = EmployeeHierarchyPrinter()

        self.assertIsInstance(hierarchyPrinter, EmployeeHierarchyPrinter)

    # Test to ensure guard clause raises error when 'rootManager' parameter is NULL
    def test_EmployeeHierarchyPrinterPrintStringRootManagerNull(self):
        with self.assertRaises(ValueError):
            hierarchyPrinter = EmployeeHierarchyPrinter()

            result = hierarchyPrinter.PrintString(None)

    # Test to ensure guard clause raises error when 'rootManager' parameter is not of type 'Manager'
    def test_EmployeeHierarchyPrinterPrintStringRootManagerNotManagerType(self):
        with self.assertRaises(ValueError):
            hierarchyPrinter = EmployeeHierarchyPrinter()
            testRootManager = Employee('TestEmployee', 1)

            result = hierarchyPrinter.PrintString(testRootManager)

    # Test to ensure 'PrintString()' method returns expected string and string format
    def test_EmployeeHierarchyPrinterPrintString(self):
        hierarchyPrinter = EmployeeHierarchyPrinter()

        builder = StringIO()
        builder.write('Jeff\n')
        builder.write('Employees of: Jeff\n')
        builder.write('\tDave\n')
        builder.write('\tEmployees of: Dave\n')
        builder.write('\t\tDan\n')
        builder.write('\t\tAndy\n')
        builder.write('\tCory\n')

        expectedEmployeeHierarchyString = builder.getvalue()
        resultEmployeeHierarchyString = hierarchyPrinter.PrintString(self.rootManager)

        self.assertEqual(expectedEmployeeHierarchyString, resultEmployeeHierarchyString)

#-----------------------------------------------------------------------------

# Main
if __name__ == '__main__':
    unittest.main()