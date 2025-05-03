import random
import string

chars = "" + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

# ENCRYPTION

plain_text = input("Enter text to encrypt: ")
cypher = ""

for letter in plain_text:
	if letter in chars:
		index = chars.index(letter)
		cypher += key[index]
	else:
		cypher += letter

print(f"Original Message: {plain_text}")
print(f"Cypher Message: {cypher}")


# DECRYPTION

cypher = input("Enter text to decrypt: ")
plain_text = ""

for letter in cypher:
	index = key.index(letter)
	plain_text += chars[index]

print(f"Cypher Message: {cypher}")
print(f"Original Message: {plain_text}")
