# Python HW 2 - part 2b

# Guess the number game  (inspired by the binary search from HCI 574 lecture 14)

### version 2 - implement any (or all) of these features:
# on wrong guess, add info if guess was too high or too low
# keep track of number of guesses and print out the guess number before the user's input and, on success, the number of guesses that were required
# Optional: set a round limit (e.g. 5 rounds to guess correctly) and print out the number of remaining guesses instead of then guess number. Quit after limit has been reached.

import random


winner = 0
print("How many trys do you want?")
max_rounds = int(input())
print("How many numbers do you want?")
max_number = int(input())
print("Guess a number any number!")

my_secret_number = random.randint(1, max_number)
round = 1

while not(winner) and round <= max_rounds:

    guess = input()
    guess = int(guess)

    if guess == my_secret_number:
        print("You Got it!  It was:",my_secret_number,"Guess #:",round,"Guesses Remaining:",(max_rounds-round))
        winner = 1
    else:
        if guess > my_secret_number:
            print(guess,"is too high. Guess #:",round,"Guesses Remaining:",(max_rounds-round))
            round += 1

        if guess < my_secret_number:
            print(guess,"is too low Guess #:",round,"Guesses Remaining:",(max_rounds-round))
            round += 1

if not(winner):
    print("You ran out of lives!  Try again?")