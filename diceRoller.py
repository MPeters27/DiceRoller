import random

def rNumberGenerator():

    minimum = 1
    maximum = 6

    number = random.randint(minimum, maximum)

    return number


num = rNumberGenerator()
print(num)
print("Would you like to play again?")