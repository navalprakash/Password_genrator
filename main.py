import random
import string

word1 = string.ascii_lowercase
word2 = string.ascii_uppercase
word3 = string.digits
word4 = string.punctuation

def generate_password(length):
    alphabet = word1 + word2 + word3 + word4
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

password = generate_password(10)
print(password)