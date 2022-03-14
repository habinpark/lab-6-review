import string
import tempfile


tempCel = float(input("Please enter a temperature in Celsius: "))
tempFar = (tempCel*1.8) + 32
tempFar = round(tempFar)
print("That is " + str(tempFar) + "°F")