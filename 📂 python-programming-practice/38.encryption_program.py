import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + string.hexdigits + string.whitespace


chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"CHARS: {chars}")
# print(f"KEYS: {key}")

#ENCRYPT:
input_txt = input("Enter a message: ")
cypher_txt = ""

for letter in input_txt:
    index = chars.index(letter)
    cypher_txt += key[index]

print(f"Original Message: {input_txt}")
print(f"Encrypted message: {cypher_txt}")

#DECRYPT:
cypher_txt = input("Enter a message: ")
input_txt = ""

for letter in cypher_txt:
    index = key.index(letter)
    input_txt += chars[index]

print(f"Original Message: {cypher_txt}")
print(f"Decrypted message: {input_txt}")
