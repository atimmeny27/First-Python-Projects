import time

my_time = int(input("Enter the time in seconds: "))

# Time.sleep(seconds) is from the time module we imported
# It will delay a response by that many seconds

for x in range(my_time, 0, -1):
	seconds = x % 60
	minutes = int(x/60) % 60
	print (f"00:{minutes:02}:{seconds:02}")
	time.sleep(.8)

print ("Done")