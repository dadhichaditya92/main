import random
guess = random.randint(0, 1)
print(guess)
if guess == 0:
    print("Heads")
else:
    print("Tails")