import random
import string

chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)

key=chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"keys: {key}")

# encryption 

plain_text=input("Enter the message to encrypt \n")
cipher_text=""

for letter in plain_text:
    if letter in chars:
        index=chars.index(letter)
        cipher_text+=key[index]
    else:
        cipher_text+=letter

print(f"Original Message : {plain_text}")

print(f"Encrypted Message:{cipher_text}")
# decrypting 
cipher_text=input("Enter the message to decrypt\n")
plain_text=""

for letter in cipher_text:
    if letter in key:
        index=key.index(letter)
        plain_text+=chars[index]
    else:
        plain_text+=letter


print(f"Encrypted Message:{cipher_text}")
print(f"Original Message : {plain_text}")


