# This will be code to validate the criteria of a username
# The rules are:
	# Less than 12 characters
	# No spaces
	# No numbers

username = input("Enter desired Username: ")

if len(username) > 12:
	print ("Too long")
elif not username.find(" ") == -1:
	print ("No spaces")
elif username.isdigit():
	print ("No numbers")
else:
	print ("Welcome")