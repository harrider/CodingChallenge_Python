import unittest
from io import StringIO
from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.DataReader import DataReader


# 'DataReader' object tests
class DataReaderUnitTests(unittest.TestCase):

    # Test to ensure valid creation of object is as expected
    def test_DataReaderValidCreation(self):
        testDataReader = DataReader()

        self.assertIsInstance(testDataReader, DataReader)


    # Test to ensure 'Read()' method returns expected object type and value
    def test_DataReaderReadMethod(self):
        testDataReader = DataReader()
        result = testDataReader.Read()

        self.assertIsInstance(result, Manager)
        self.assertEqual(result.name, 'Jeff')
        self.assertEqual(result.salary, 100000)
        self.assertEqual(len(result.employees), 2)

#-----------------------------------------------------------------------------

# Main
if __name__ == '__main__':
    unittest.main()