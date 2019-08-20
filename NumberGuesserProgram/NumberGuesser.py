import random 

# randomNumber = random.randint(1, 10) # create random number
randomNumber = 3
guessesRemaining = 5

while(guessesRemaining >= 1):
    try:
        guessNumber = int(input('Guess a number 1 through 10\n')) # prompt user to guess number
    except ValueError:
        print('You didn\'t enter an integer. Please, try again.') # validate input
        continue
    if(guessNumber < 1 or guessNumber > 10):
        print('You didn\'t enter an integer between 1 and 10. Please, try again.')
        continue
    elif(guessNumber == randomNumber): # compare guessNumber to randNumber
        print(str(guessNumber) + '! You got it!\nGame Over!') # if correct, return congratulations
        guessNumber = 0
        break
    elif(guessesRemaining > 1):
        guessesRemaining = guessesRemaining - 1 # track number of guesses made
        print('Try again.') 
        continue # else prompt to guess again
    else:
        print('Failure. It was ' + str(randomNumber) + '!')
        break




