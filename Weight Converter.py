# Building a weight converter

weight = float(input("Please enter weight: "))
label = input("Please enter a unit (kg or lbs): ")

if label == "kg":
	weight = weight * 2.2
	label = "lbs"
elif label == "lbs":
	weight = weight / 2.2
	label = "kg"

print (f"The weight is : {round(weight, 1)} {label}")