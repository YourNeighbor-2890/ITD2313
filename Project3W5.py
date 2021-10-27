import random
guesses = int(0)
highBound = int(input("What is the higher boundry "))
lowBound = int(input("What is the lower boundry "))
numToGuess = int(input("Pick a number between those bounds "))

if numToGuess > highBound or numToGuess < lowBound:
    numToGuess = int(input("Please pick a number in between your boundries: "))
for guesses in range(1, 6):
    computerGuess = random.randint(lowBound, highBound)
    if computerGuess > numToGuess:
        print("Almost, too low")
    elif computerGuess < numToGuess:
        print("Too high")
    else:
        print("The computer got it in ", guesses, "tries")
        break
    guesses += 1

    

    
            
