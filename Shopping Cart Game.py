foods = []
prices = []
total = 0

while True:
	food = input("Enter the food name (q to quit): ")
	if food == "q":
		break
	else:
		price = float(input(f"Enter the price of {food}: $" ))
		foods.append(food)
		prices.append(price)

print()
print("-----Your Cart-----")

for food in foods:
	print(food)

for price in prices:
	total = (total + price) * 1.06

print (f"Your total after tax is ${total:.2f}")