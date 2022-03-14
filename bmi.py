import sys

w = float(input("Enter weight in pounds: "))
h = float(input("Enter height in inches: "))

bmi = (703*w)/pow(h,2)

print("Your body mass index (BMI) is " + str(bmi))
