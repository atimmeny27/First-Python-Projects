# Exercise with grocery prices

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many are you buying?: "))

total = price * quantity
print (f"The total price of {quantity} {item} is ${total}")