import unittest
from io import StringIO
from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.SalaryRequirementPrinter import SalaryRequirementPrinter


# 'SalaryRequirementPrinter' object tests
class SalaryRequirementPrinterUnitTests(unittest.TestCase):

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
            employeeAndy,
            employeeDan
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

    def tearDown(self):
        self

#--------------------------------------------------------------------------------------------------
    
    # Test to ensure valid creation of object is as expected
    def test_SalaryRequirementPrinterValidCreation(self):
        salaryRequirementPrinter = SalaryRequirementPrinter()

        self.assertIsInstance(salaryRequirementPrinter, SalaryRequirementPrinter)

    # Test to ensure guard clause raises error when 'rootManager' parameter is NULL
    def test_SalaryRequirementPrinterPrintStringRootManagerNull(self):
        with self.assertRaises(ValueError):
            salaryRequirementPrinter = SalaryRequirementPrinter()

            result = salaryRequirementPrinter.PrintString(None)

    # Test to ensure guard clause raises error when 'rootManager' parameter is not of type 'Manager'
    def test_SalaryRequirementPrinterPrintStringRootManagerNotManagerType(self):
        with self.assertRaises(ValueError):
            salaryRequirementPrinter = SalaryRequirementPrinter()
            testRootManager = Employee('TestEmployee', 1)

            result = salaryRequirementPrinter.PrintString(testRootManager)

    # Test to ensure 'PrintString()' method returns expected string and string format
    def test_SalaryRequirementPrinterPrintString(self):
        salaryRequirementPrinter = SalaryRequirementPrinter()

        builder = StringIO()
        builder.write('Total salary: $375,000.00')

        expectedSalaryRequirementString = builder.getvalue()
        resultSalaryRequirementString = salaryRequirementPrinter.PrintString(self.rootManager)

        self.assertEqual(expectedSalaryRequirementString, resultSalaryRequirementString)

#-----------------------------------------------------------------------------

# Main
if __name__ == '__main__':
    unittest.main()