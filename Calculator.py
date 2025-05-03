# Building a calculator

operator = input("Enter an Operator(+ - * /): ")

# Remember all input is string data, so for a calculator, we have to make it int or float data

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == "+" :
	print (num1 + num2)
elif operator == "-" :
	print (num1 - num2)
elif operator == "*" :
	print (num1 * num2)
elif operator == "/" :
	print (num1 / num2)
else :
	print (f"{operator} is not a valid operator")