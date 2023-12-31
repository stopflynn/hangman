import random
from easy import easy_list
from medium import medium_list
from hard import hard_list

# checks user has enters yes / no to getting instructions


def levels(question):

    error = "Please enter a difficulty "

    while True:
        response = input(question).lower()

        if response == "easy" or response == "e":
            return easy_list
        elif response == "medium" or response == "m":
            return medium_list
        elif response == "hard" or response == "h":
            return hard_list
        else:
            print(error)


print()

name = input("Please enter your name: ")
print()
difficulty = levels("What difficulty would you like, " + name + "? Easy, medium, or hard? ")
print(difficulty)


# hangman begins
def get_word(wording):
    difficulty = random.choice(wording)

    return difficulty.upper()


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
                print("You have already guessed the letter", guess)
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
        print("\n")
    if guessed:
        print("Congratulations on finding the word, you win!")
    else:
        print("Sorry, you ran out of attempts. The word was " + word + ". Maybe next time!")


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
    word = get_word(difficulty)
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word(difficulty)
        play(word)


if __name__ == "__main__":
    main()
