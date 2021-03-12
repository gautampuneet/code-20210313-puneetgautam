**Introduction**

This is a Body mass Index Calculator, which will have following features inside it.

  1. You can provide a json file which will have a list of dicts in it and dict would have the Gender, HeightCm, WeightKg in it.
  2. It will get the HeightCm and WeightKg from each dict and will calculate its BMI using BMI(kg/m ) = mass(kg) / height(m) Formula.
  3. It will also get BMI Category and Health risk for each person and at the end it will add these three values in the same list. 
  4. It also have the feature to return count of Overweight People in that list. 

For Running any of this functionality you have to do run the following command:-
Command:- python3 bmi_calculator.py 

We have also created Some automated Test cases using unitTest Module so for running them you just have to run test.py file.
Command:- python -m unittest test.BMICalculatorTestCase

