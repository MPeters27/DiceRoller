import random

def rNumberGenerator():
    minimum = 1
    maximum = 6
    number = random.randint(minimum, maximum)
    return number


def diceRollText():
    print("Would you like to roll again?")
    print("Y == roll again")
    print("N == quit")


answer = "Y"
while answer.upper() == "Y":
    num = rNumberGenerator()
    print("You rolled a " + str(num))
    diceRollText()
    answer = input()
    while answer.upper() != "Y" and answer.upper() != "N":
        print("Invalid entry")
        diceRollText()
        answer = input()

