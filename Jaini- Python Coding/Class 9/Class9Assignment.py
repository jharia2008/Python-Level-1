import random
NUMBER=random.randint(1, 100)
print(NUMBER)
guess1=int(input("Guess a number within 1 to 100"))
previousGuess=int(input("Guess another number within 1-100"))
if guess1 > 100 or guess1 < 1:
    print("Out of bounds")
elif guess1 == NUMBER:
    print("you guessed it first try!!!")
elif guess1 == NUMBER < 10 or guess1 == NUMBER > 10:
    print("WARM")
elif guess1== NUMBER > guess1:
    print("COLD")
elif previousGuess < guess1:
    print("WARMER")
elif previousGuess== NUMBER :
    print("you guess the number second try!")