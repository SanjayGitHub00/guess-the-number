import math
import random


# The code is prompting the user to enter the lower and upper bounds of a range. The input function is
# used to take user input, and the int function is used to convert the input into an integer data
# type. The lower bound is stored in the variable `lowerBound` and the upper bound is stored in the
# variable `upperBound`.
lowerBound = int(input("Enter the lower Range: \n"))
upperBound = int(input("Enter the upper Range: \n"))

# `randomInt = random.randint(lowerBound,upperBound)` is generating a random integer between the
# lowerBound and upperBound (inclusive). The `random.randint()` function is part of the `random`
# module in Python and is used to generate random integers. In this case, it is generating a random
# integer that the user needs to guess in the subsequent code.
randomInt = random.randint(lowerBound, upperBound)

print(
    "\n\tYou have only ",
    round(math.log(upperBound - lowerBound + 1, 2)),
    " chances to guess the integer!\n",
)

count = 0

while count < math.log(upperBound - lowerBound + 1, 2):
    count += 1

    guess = int(input("Enter your number "))

    if randomInt == guess:
        print("Congratulation you won by ", count, " try.")
        break
    elif randomInt > guess:
        print("You guessed to small!")
    elif randomInt < guess:
        print("You guessed to high!")

if count > math.log(upperBound - lowerBound + 1, 2):
    print("\nThe number is {}".format(randomInt))
    print("\tBetter luck next time!")
