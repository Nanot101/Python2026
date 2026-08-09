# **Number Guessing Game** — Computer picks a random number 1-100, user guesses in a `while` loop, program says "higher"/"lower" until correct; count the number of guesses.

import random

num = random.randrange(1, 101, 1)
print(num)

counter = 0

guess = int(input("Enter a whole number between 1 & 100: "))

# # testing randrange
# for i in range(5):
#     num = random.randrange(1, 101, 1)
#     print(num)

while guess != num:
    if guess < num:
        print("Higher")
        counter += 1
        guess = int(input("Guess again: "))
    else:
        print("Lower")
        counter += 1
        guess = int(input("Guess again: "))

print(f"You did it! It took you {counter} tries to get the correct number which was {num}!!")