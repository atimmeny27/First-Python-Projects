import random

player_hand = [random.randint(1, 11), random.randint(1, 11)]
dealer_hand = [random.randint(1, 11), random.randint(1, 11)]

player_total = sum(player_hand)
dealer_total = sum(dealer_hand)

print(f"Your hand: {player_hand} (Total: {player_total})")
print(f"Dealer's first card: {dealer_hand[0]}")

while player_total < 21:
	hit_stand = input("would you like to hit or stand (h/s): ").lower()
	if hit_stand == "h":
		new_card = random.randint(2, 11)
		player_hand.append(new_card)
		player_total = sum(player_hand)
		print(f"Your hand: {player_hand} (Total: {player_total})")
	elif hit_stand == "s":
		break
	else:
		print ("Invalid response, please hit (h) or stand (s)")
		hit_stand = input("would you like to hit or stand (h/s): ").lower()

if player_total > 21:
	print("You busted! Dealer wins.")
else:
	print(f"Dealer's hand: {dealer_hand} (Total: {dealer_total})")
	while dealer_total < 17:
		new_card = random.randint(1, 11)
		dealer_hand.append(new_card)
		dealer_total = sum(dealer_hand)


if player_total > dealer_total and player_total <=21:
	print ("You win!")
else:
	print("You lose")