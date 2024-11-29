# Write a Python program that is a number guessing game:
import random

# Move the code in a function called main and split up the code into several function that make sense.

# The user guesses
def user_guess ():

    while True:

        user_input = input("Guess a number between 1 to 20:"). strip()
        # If the user enters "x" any time, exit the program.
        if user_input == 'x':
            print("Thanks for playing!")
            exit()
        elif user_input == 'n':
            return 'new_game'
        elif user_input == 's':
            return 'show_secret'
        
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 to 20, 'x' to exit, 'n' for new game, or 's' to cheat.")

def main ():
    # The computer "thinks" a about a whole number between 1 and 20
    print("Welcome to the Number Guessing Game!")
    print("Commands: 'x' to exit, 'n' for new game, 's' to reveal the number")
    
    while True:
        computer_number= random.randint(1,20)
        Number_of_guess= 0

        while True:
            guess= user_guess()
            
            # If the user enters "n" any time, leave the current game and ask if she wants to play a new game?
            if guess == 'new_game':
                print('Starting new game!')
                break
            # If the user enters "s" any time, show the hidden number (cheating).
            elif guess == 'show_secret':
                print(f"The secret number is {computer_number}\nNext time try not to cheat :)")
                continue

            # The computer tells if the guess was too small, too big or exact.
            # If exact the user wins, the program ends. Otherwise the user can guess again.
            # At the end of the game print out how many guesses the user needed.
            # Allow the user to play several games: once one game ends ask her if she wants to play again, generate a new random number and play again.

            Number_of_guess +=1

            if guess < computer_number:
                print('Number is too small, please guess again')
            elif guess > computer_number:
                print('Number is too big, please guess again')
            else:
                print (f'You are correct! Nunber of guesses:', {Number_of_guess})
                play_again= input('Would you like to play again? please answer yes/no:').strip().lower()
                if play_again.lower() == 'yes':
                    break
                else:
                    print ('Thanks for playing!')
                    exit()

if __name__ == '__main__':
    main()




