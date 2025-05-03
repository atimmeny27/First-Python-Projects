principle = 0
rate = 0
time = 0

while principle <= 0:
	principle = int(input("What is the initial investment?: "))
	if principle <=0:
		print ("Principle cannot be less than $1")

while rate <= 0:
	rate = int(input("What is the expected return rate per year?: "))
	if rate <=0:
		print ("Rate cannot be less than 1%")

while time <= 0:
	time = int(input("What is the investment period in years?: "))
	if time <=0:
		print ("Time cannot be less than 1 month")

total = principle * pow((1 + rate / 100), time)

print (f"The expected final amount after {time} years is ${total:,.2f}")