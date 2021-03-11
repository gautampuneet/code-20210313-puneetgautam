import unittest
import json
import pathlib as pl
from main import BMICalculator
import constants


class BMICalculatorTestCase(unittest.TestCase):

    def test_bmi_calculator(self):
        directory_name = "data.json"
        output_file_name = BMICalculator(directory_name).execute()
        path = pl.Path(output_file_name)
        self.assertEqual((str(path), path.is_file()), (str(path), True))
        with open(output_file_name) as file:
            output = json.loads(file.read())
        self.assertListEqual(output, constants.FIRST_TESTCASE_CORRECT_RESULT)

    def test_overweight_count_with_file_creation(self):
        directory_name = "data.json"
        overweight_count, output_file_name = BMICalculator(directory_name).execute(True)
        path = pl.Path(output_file_name)
        self.assertEqual((str(path), path.is_file()), (str(path), True))
        with open(output_file_name) as file:
            output = json.loads(file.read())
        self.assertListEqual(output, constants.FIRST_TESTCASE_CORRECT_RESULT)
        self.assertEqual(overweight_count, constants.SECOND_TESTCASE_COUNT_RESULT)

    def test_overweight_count(self):
        directory_name = "Output_2021-03-12 01:36:37.028884.json"
        overweight_count = BMICalculator(directory_name).get_overweight_people_count()
        self.assertEqual(overweight_count, constants.THIRD_TESTCASE_RESULT)


if __name__ == "__main__":
    unittest.main()




