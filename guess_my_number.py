from random import randrange

'''
A computer will randomly generate a number and the user has to guess it
'''

print('Guess a number game?')
computerNumber = randrange(10) # Randomly generates a number b/w 1 - 10

userNumber = int(input("Pick a number between 1-10: "))

if(userNumber == computerNumber):
    print("You guessed correctly")
    print(f"The computer number is: " + computerNumber)
else:
    print("You guessed incorrectly")
