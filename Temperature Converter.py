# Building a temperature converter

temp = float(input("Please enter the degree: "))
unit = input("Please enter the unit (C or F): ")

if unit == "C":
	temp = temp * 9/5 + 32
	unit = "F"
	print (f"The temperature is {round(temp, 1)} {unit}")
elif unit == "F":
	temp = (temp - 32) * (5/9)
	unit = "C"
	print (f"The temperature is {round(temp, 1)} {unit}")
else :
	print (f"{unit} is not an accepted unit")