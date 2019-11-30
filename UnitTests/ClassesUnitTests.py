import unittest
from CodingChallengeModule.Classes import Employee, Manager


# 'Employee' object tests
class EmployeeClassUnitTests(unittest.TestCase):

    # Test to ensure guard clause raises error when 'name' parameter is NULL
    def test_EmployeeNameNullValueError(self):
        with self.assertRaises(ValueError):
            testEmployee = Employee(None, 1)

    # Test to ensure guard clause raises error when 'name' parameter is empty string
    def test_EmployeeNameEmptyValueError(self):
        with self.assertRaises(ValueError):
            testEmployee = Employee('', 1)

    # Test to ensure guard clause raises error when 'salary' parameter is negative number
    def test_EmployeeSalaryNegativeValueError(self):
        with self.assertRaises(ValueError):
            testEmployee = Employee('TestEmployee', -1)

    # Test to ensure valid creation of object is as expected
    def test_EmployeeValidCreation(self):
        testEmployee = Employee('TestEmployee', 1)
        self.assertIsInstance(testEmployee, Employee)

#-----------------------------------------------------------------------------

# 'Manager' object tests
class ManagerClassUnitTests(unittest.TestCase):

    # Test to ensure guard clause raises error when 'employee' parameter is NULL
    def test_ManagerDecoratedEmployeeNullValueError(self):
        with self.assertRaises(ValueError):
            testManagerEmployee = Employee('TestManagerEmployee', 1)
            testEmployee = Employee('TestEmployee', 1)

            testManager = Manager(None, [testEmployee])

    # Test to ensure guard clause raises error when 'employees' parameter is NULL
    def test_ManagerEmployeesListNullValueError(self):
        with self.assertRaises(ValueError):
            testManagerEmployee = Employee('TestManagerEmployee', 1)

            testManager = Manager(testManagerEmployee, None)

    # Test to ensure valid creation of object when 'employees' list is empty
    def test_ManagerEmployeesListEmptyValidCreation(self):
            testManagerEmployee = Employee('TestManagerEmployee', 1)
            testEmployee = Employee('TestEmployee', 1)
            testManager = Manager(testManagerEmployee, [])

            self.assertIsInstance(testManager, Manager)

    # Test to ensure valid creation of object is as expected
    def test_ManagerValidCreation(self):
        testManagerEmployee = Employee('TestManagerEmployee', 1)
        testEmployee = Employee('TestEmployee', 1)
        testEmployees = [
            testEmployee
        ]

        testManager = Manager(testManagerEmployee, testEmployees)

        self.assertIsInstance(testManager, Manager)


#-----------------------------------------------------------------------------

# Main
if __name__ == '__main__':
    unittest.main()