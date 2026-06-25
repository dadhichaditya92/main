import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':',
           ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

nr_num = int(input("Enter the number"))
nr_let = int(input("Enter the letters"))
nr_sym = int(input("Enter the Symbols"))

password = []
for char in range(nr_num):
    password.append(random.choice(numbers))

for char in range(nr_let):
    password.append(random.choice(letters))

for char in range(nr_sym):
    password.append(random.choice(symbols))

random.shuffle(password)
print("".join(password))
