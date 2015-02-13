# This is my random number guessing game
import random

def main():
    play = 'y'
    

    while play == 'y' or play == 'Y':

        # Generate a random number

        tries = 0
        mynum = random.randint(1, 1000)
        
        
        # Get a guess from the player and count his try

        guess = int(input('Guess a number between 1 and 1,000 '))
        tries += 1

        # compare the numbers

        while guess != mynum:

            if guess >= mynum + 10:
                guess = int(input('Too high! Try again.'))
                tries += 1

            elif guess > mynum and guess < mynum + 10:
                guess = int(input("A little too high, but you're getting warm."))
                tries += 1

            elif guess <= mynum - 10:
                guess = int(input('Too low! Try again.'))
                tries += 1

            elif guess < mynum and guess > mynum - 10:
                guess = int(input("A little too low, but you're getting warm."))
                tries += 1

        print('Great job! You guessed the number in', tries, 'tries!')
        play = input('Would you like to play again?')
        
main()
