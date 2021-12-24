
# guessnumber:

while(1):
    from random import randint

    guessNumber = int(input("\n\nEnter the guess between 1 to 5 : "))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("...YOU HAVE WON...")

    else:
        print("...YOU HAVE LOST...")
        print"Random number was : ", randomNumber
