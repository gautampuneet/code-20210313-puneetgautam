**Introduction**

This is a Body mass Index Calculator, which will have following features inside it.

  1. You can provide a json file which will have a list of dicts in it and dict would have the Gender, HeightCm, WeightKg in it.
  2. It will get the HeightCm and WeightKg from each dict and will calculate its BMI using 2BMI(kg/m ) = mass(kg) / height(m) Formula.
  3. It will also get BMI Category and Health risk for each person and at the end it will add these three values in the same list. 
  4. It also have the feature to return count of Overweight People in that list. 

For Running any of this functionality you have to do the following steps:-
  1. For only Creating a new File with BMI, BMI Category, Health Risk we have to call execute method in main.py file
  2. For Creating the file as well as counting the overweight people in Output file we have to call execute method but with count_overweight_people=True Variable.
  3. For Only counting overweight people we have to call get_overweight_people_count method in main.py file with output file name as variable. 

We have also created Some automated Test cases using unitTest Module so for running them you just have to run test.py file.
Command:- python -m unittest test.BMICalculatorTestCase

