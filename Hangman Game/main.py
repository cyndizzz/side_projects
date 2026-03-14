import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder =''
length = len(chosen_word)
for i in range(length):
    placeholder += '_'
print("Word to guess: " + placeholder)

display = placeholder
guessed_letters =[]
game_over = False
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        i=0
        for letter in chosen_word:
            if letter == guess:
                display = display[:i] + letter + display[i+1:]
            else:
                display = display
            i+=1

        print("Word to guess: " + display)
        guessed_letters.append(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            if lives == 0:
                game_over = True
                print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if display == chosen_word:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])



