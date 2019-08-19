while True:
    # Validation
    try:
        numCats = int(input("How many cats do you have?"))
    except ValueError:
        print('You did not enter a number.')
        continue
    
    if(numCats < 0):
        print('Number can\'t be less than zero')
        continue
    
    # Response
    if(numCats >= 4):
        print('That\'s a lot of cats.')
        break
    else:
        print('That is not a lot of cats.')
        break