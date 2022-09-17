import string
from random import choices, shuffle

n_letters = int(input("letters: "))
n_symbols = int(input("symbols: "))
n_numbers = int(input("numbers: "))

# letters - string.ascii_letters
# numbers - string.digits
# symbols - string.punctuation

password = []
l = choices(string.ascii_letters, k=n_letters)
s = choices(string.digits, k=n_symbols)
n = choices(string.punctuation, k=n_numbers)
password = l + s + n
shuffle(password)
password = "".join(password)

print(f"Here is your password: {password}")
