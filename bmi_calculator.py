import json
import datetime
import math


class BMICalculator:

    def __init__(self, data_directory):
        self.directory = data_directory
        self.bmi_dict = {'18.5-24.9': ['Normal weight', 'Low risk'],
                         '25-29.9': ['Overweight', 'Enhanced risk'],
                         '30-34.9': ['Moderately obese', 'Medium risk'],
                         '35-39.9': ['Severely obese', 'High risk'],
                         '40-inf': ['Very severely obese', 'Very high risk'],
                         '0-18.4': ['Underweight', 'Malnutrition risk']}

    def execute(self, count_overweight_people=False):
        json_data = self.file_read()
        output_file_name = self.create_file_with_bmi_data(json_data)
        if count_overweight_people:
            count = self.get_overweight_people_count(output_file_name)
            return count, output_file_name
        return output_file_name

    def get_overweight_people_count(self, directory_name=None):
        if directory_name:
            self.directory = directory_name
        output_data = self.file_read()
        overweight_people = list(filter(self.overweight_condition, output_data))
        return len(overweight_people)

    @staticmethod
    def overweight_condition(data):
        if data.get("BMI Category") == "Overweight":
            return data

    def file_read(self):
        with open(self.directory) as file:
            json_data = file.read()
        json_data = json.loads(json_data)
        return json_data

    def create_file_with_bmi_data(self, json_data):
        try:
            current_time = datetime.datetime.now()
            updated_json_data = list(map(self.bmi_calculate, json_data))
            output_file_name = "Output_" + str(current_time) + ".json"
            with open(output_file_name, "w") as output_file:
                json.dump(updated_json_data, output_file)
            return output_file_name
        except Exception as ex:
            print("Exception Occurred: ", ex)
            return "File Creation Failed"

    def bmi_calculate(self, value):
        height = value.get("HeightCm")
        weight = value.get("WeightKg")
        if not weight or not height:
            print("Height or weight does not exist")
        calculated_bmi = round(weight / (height / 100), 1)
        value["BMI"] = calculated_bmi
        for i, j in self.bmi_dict.items():
            age_range = i.split("-")
            starting_range = age_range[0]
            ending_range = age_range[1]
            if age_range[1] == "inf":
                ending_range = math.inf
            if float(ending_range) > float(calculated_bmi) > float(starting_range):
                value["BMI Category"] = j[0]
                value["Health risk"] = j[1]
                continue
        return value


if __name__ == "__main__":
    print("BMI Calculator\n 1. Create file with calculated bmi\n 2. Create File with calculated bmi and"
          "give overweight count\n 3. Count the overweight people")
    user_choice = int(input("Please Provide Your Choice: "))
    if user_choice == 1:
        # Case 1 - Will Create a file with BMI, BMI Category, Health Risk
        bmi = BMICalculator("data.json").execute()
        print(bmi)
    elif user_choice == 2:
        # Case 2 - Will Create a file with BMI, BMI Category, Health Risk and also return the count of overweight people
        bm2 = BMICalculator("data.json").execute(True)
        print(bm2)
    elif user_choice == 3:
        # Case 3 - Will return the count of overweight people in file
        bm3 = BMICalculator("Output_2021-03-12 01:36:37.028884.json").get_overweight_people_count()
        print(bm3)
    else:
        print("Wrong Choice")
