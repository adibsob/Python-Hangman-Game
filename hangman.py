import random
from words import words
from visuals import lives_visual
import string


def hangman():

    word = random.choice(words).upper()
    # Saving letters of the random word in this set
    random_word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()  # what the user has guessed are saved in this set
    tries = 7
    print("\nThey are about to hang an innocent man in town.\nThe only way to save him is to guess the random word that the executioner has in mind.\nGood Luck!")
    # getting user input
    while len(random_word_letters) > 0 and tries > 0:
        print('You have', tries, 'chances left and you have used these letters: ',
              ' '.join(guessed_letters))
        word_list = [
            letter if letter in guessed_letters else '-' for letter in word]
        print(lives_visual[tries])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in random_word_letters:
                random_word_letters.remove(user_letter)
                print('')

            else:
                tries = tries - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in guessed_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when tries == 0
    if tries == 0:
        print(lives_visual[tries])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


hangman()


def playagain():
    while True:
        play_again = input("Play Again? Y/N ").upper()
        if play_again == "Y":
            hangman()
        else:
            break


playagain()
