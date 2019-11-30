import unittest
from io import StringIO
from CodingChallengeModule.Classes import Employee, Manager
from CodingChallengeModule.JsonDataReader import JsonDataReader


# 'JsonDataReader' object tests
class JsonDataReaderUnitTests(unittest.TestCase):

    # Test to ensure guard clause raises error when 'hierarchyFileName' parameter is NULL
    def test_JsonDataReaderNullEmployeeHierarchyJsonFileName(self):
        with self.assertRaises(ValueError):
            dataReader = JsonDataReader(None)

    # Test to ensure guard clause raises error when 'hierarchyFileName' parameter is empty
    def test_JsonDataReaderEmptyEmployeeHierarchyJsonFileName(self):
        with self.assertRaises(ValueError):
            dataReader = JsonDataReader('')

    # Test to ensure guard clause raises error when 'hierarchyFileName' file extension is not '.json'
    def test_JsonDataReaderEmployeeHierarchyJsonFileNameWrongFileExtension(self):
        with self.assertRaises(ValueError):
            dataReader = JsonDataReader('./Hierarchy.txt')

    # Test to ensure valid creation of object is as expected
    def test_JsonDataReaderValidCreation(self):
        dataReader = JsonDataReader('./Hierarchy.json')

        self.assertIsInstance(dataReader, JsonDataReader)


    # Test to ensure 'Read()' method returns expected object type and value
    def test_JsonDataReaderReadMethod(self):
        dataReader = JsonDataReader('./Hierarchy.json')
        result = dataReader.Read()

        self.assertIsInstance(result, Manager)
        self.assertEqual(result.name, 'Jeff')
        self.assertEqual(result.salary, 100000)
        self.assertEqual(len(result.employees), 2)

#-----------------------------------------------------------------------------

# Main
if __name__ == '__main__':
    unittest.main()