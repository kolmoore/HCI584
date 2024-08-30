# Python HW 2 - part 2a

# Guess the number game  (inspired by the binary search from HCI 574 lecture 14)

#### Version 1
# make a game to guess a number between 1 and 10 (including both)
# secretly using random.randint(1, 10) to create a secret_number to guess (int)
# ask the user to guess a number: use input() and use int() to convert its string into an int
# (you can assume that that conversion always works, no need to wrap try/except around int()!)
# set up a while loop
# compare the user's input (int) with your int
# if guess was correct, jump out of the loop
# otherwise repeat user input and comparison until guess is correct

# Note: the tricky part is jumping out of the loop. You could use a while True: loop
# and break out once the guess was correct. Or you could use a bool flag variable to stay in the 
# loop while it is True (i.e. guess was not correct). On a correct guess change this
# variable to True so that the while condition is also wrong and thus exited.

# I strongly suggest that you practice using a debugger for this so you can run your code 
# line by line, see where it jumps to and what variable values are. See HCI 574 lecture 14 for info
# or look at the HCI 54 lecture 1 addendum pdf.
#guess_is_wrong = True  # bool flag you can use loop other your while block as long as it's True

import random

winner = 0
my_secret_number = random.randint(1, 10)
print("Guess a number! (1-10)")

while not(winner):

    guess = input()
    guess = int(guess)

    if guess == my_secret_number:
        print("You Got it!  It was:",my_secret_number)
        winner = 1
    else:
        print(guess,"isn't right.")


