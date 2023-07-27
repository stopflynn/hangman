import random
from words import word_list

# checks user has enters yes / no to a question


def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no"
                  "")


# Ask user if they would like to read the instructions before they play
want_instructions = yes_no("Would you like to read the instructions? ")

if want_instructions == "yes":
    print("To play Hangman, you must guess one letter at a time. "
          "If the letter is correct, it will enter one ore more of the blank spaces, ")
    print("which will help you to find the word. "
          "If you guess wrong seven times,you will lose and the man will be hanged. ")


print()

name = input("Please enter your name: ")


# easy = random word from words_list with letters (<5)
# medium = random word from words_list with letters (>5, <8)
# medium = random word from words_list with letters (>10)


difficulty = input("What difficulty would you like, " + name + "? Easy, medium, or hard? ")
if difficulty == "easy":
    word = easy
if difficulty == "medium":
    word = medium
if difficulty == "hard":
    word = hard


# hangman begins
def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print("Let's play Hangman, "+name+"!")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations on finding the word, you win!3")
    else:
        print("Sorry, you ran out of attemps. The word was " + word + ". Maybe next time!")


def display_hangman(attempts):
    stages = [  # hanged
        """
           --------^
           |       |
          x_x      |
          /|\      |
          / \      |
                   |
            _______o
        """,
        # head body both arms and a leg hanging
        """
           --------^
           |       |
           0       |
          /|\      |
          /        |
                   |
            _______o
        """,
        # head body and both arms hanging

        """
           --------^
           |       |
           0       |
          /|\      |
                   |
                   |
            _______o
        """,
        # head body and an arm hanging

        """
           --------^
           |       |
           0       |
           |\      |
                   |
                   |
            _______o
        """,
        # head and body hanging
        """                
           --------^
           |       |
           0       |
           |       |
                   |
                   |
            _______o
        """,
        # head hanging
        """                      
           --------^
           |       |
           0       |
                   |
                   |
                   |
            _______o
        """,
        # rope hanging
        """
           --------^
           |       |
                   |
                   |
                   |
                   |
            _______o
        """,
        # empty state

        """ 
           --------^
                   |
                   |
                   |
                   |
                   |
            _______o
        """

    ]
    return stages[attempts]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

import random
easy = random.randint (1,20)
medium = random.randint (1,50)
hard = random.randint (1,100)

guessesTaken = 0
my_name = input("Hello, What is your name? ")
difficulty = input("Well, "+ my_name + ". What dificulty would you like ? easy medium or hard? ")
if difficulty == "easy":
    number = easy
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 20")
if difficulty == "medium":
    number = medium
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 50")
if difficulty == "hard":
    number = hard

    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 100")


while guessesTaken < 6:
    guess = int(input('Take a guess. '))
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str (guessesTaken)
    print('Good job, ' + my_name + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str (number)
    print('Nope. The number I was thinking of was ' + number)
