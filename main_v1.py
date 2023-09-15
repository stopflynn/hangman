import random
from easy import easy_list
from medium import medium_list
from hard import hard_list

# checks user has enters yes / no to a question


def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes":
            return "yes"

        elif response == "no":
            return "no"

        else:
            print("Please enter yes or no"
                  "")


def levels(question):

    error = "Please enter a difficulty "

    while True:
        response = input(question).lower()

        if response == "easy":
            return easy_list
        elif response == "medium":
            return medium_list
        elif response == "hard":
            return hard_list
        else:
            print(error)


# hangman begins
def get_word(wording):
    difficulty = random.choice(wording)
    return difficulty.upper()


def play(word, name):
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
                print("You have already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word! You have", attempts, " attempts left.")
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
                print(guess, "is not the word.", display_hangman(attempts))
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(word_completion)
        print("You've guessed:", guessed_letters, guessed_words, ". You have", attempts, "attempts left.")
        print("\n")
    if guessed:
        print("Congratulations on finding the word, you win!")
    else:
        print("Sorry, you ran out of attempts. The word was " + word + ". Maybe next time!")


def display_hangman(attempts):
    stages = [  # hanged
        """
           ---------
           |       |
           0       |
          /|\      |
          / \      |
                   |
            _______^
        """,
        # head body both arms and a leg hanging

        """
           ---------
           |       |
           0       |
          /|\      |
          /        |
                   |
            _______^
        """,
        # head body and both arms hanging

        """
           ---------
           |       |
           0       |
          /|\      |
                   |
                   |
            _______^
        """,
        # head body and an arm hanging

        """
           ---------
           |       |
           0       |
           |\      |
                   |
                   |
            _______^
        """,
        # head and body hanging
        """                
           ---------
           |       |
           0       |
           |       |
                   |
                   |
            _______^
        """,
        # head hanging
        """                      
           ---------
           |       |
           0       |
                   |
                   |
                   |
            _______^
        """,
        # rope hanging
        """
           ---------
           |       |
                   |
                   |
                   |
                   |
            _______^
        """,
        # empty state

        """ 
           ---------
                   |
                   |
                   |
                   |
                   |
            _______^
        """

    ]
    return stages[attempts]


def main():
    print("Welcome to Hangman")
    name = input("Please enter your name: ")
    play_again = "yes"
    while play_again == "yes":

        difficulty = levels("What difficulty would you like, " + name + "? Easy (e), medium (m), or hard (h)? ")
        # Ask user if they would like to read the instructions before they play
        want_instructions = yes_no("Would you like to read the instructions? (Y/N)")
        if want_instructions == "yes":
            print("To play Hangman, you must guess one letter at a time. "
                  "If the letter is correct, it will enter one ore more of the blank spaces, ")
            print("which will help you to find the word. "
                  "If you guess wrong seven times,you will lose and the man will be hanged. ")
        word = get_word(difficulty)
        play(word, name)
        play_again = input("Do you want to play again? (Y/N)")
    print("End of the game")


if __name__ == "__main__":
    main()
