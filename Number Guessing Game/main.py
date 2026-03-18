import random
import art

def check_answer(number, guess_number, attempt):
    if guess_number > number:
        print("Too high!\nGuess again!")
        return attempt - 1
    elif guess_number < number:
        print("Too low!\nGuess again!")
        return attempt - 1
    else:
        print(f"You got it! The answer was {number}.")

def guessing_game():
    print(art.logo)
    print("I'm thinking a number between 1 and 100.")
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty level (easy, hard): ")

    attempts = {
        'easy': 10,
        'hard': 5
    }
    attempt = attempts[difficulty]

    guess_number = 0
    while number != guess_number:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        if attempt > 0:
            attempt = check_answer(number, guess_number, attempt)
        else:
            print("You've run out of guesses. You lose!")
            print("The number was: " + str(number))
            return

    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        guessing_game()
    else:
        print("Thanks for playing!")

guessing_game()
