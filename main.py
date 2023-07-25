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


# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
    print("To play Hangman, you must guess one letter at a time. "
          "If the letter is correct, it will enter one ore more of the blank spaces, ")
    print("which will help you to find the word. "
          "If you guess wrong seven times,you will lose and the man will be hanged. ")


print()

name = input("Please enter your name: ")


# hangman begins
def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Let's play Hangman, "+name+"!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
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
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations on finding the word, you win!3")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [    # hanged
        """
           --------^
           |       |
          x_x      |
          /|\      |
          / \      |
                   |
            -------o
        """,
        # head body both arms and a leg hanging
        """
           --------^
           |       |
           0       |
          /|\      |
          /        |
                   |
            -------o
        """,
        # head body and both arms hanging

        """
           --------^
           |       |
           0       |
          /|\      |
                   |
                   |
            -------o
        """,
        # head body and an arm hanging

        """
           --------^
           |       |
           0       |
           |\      |
                   |
                   |
            -------o
        """,
        # head and body hanging
        """                
           --------^
           |       |
           0       |
           |       |
                   |
                   |
            -------o
        """,
        # head hanging
        """                      
           --------^
           |       |
           0       |
                   |
                   |
                   |
            -------o
        """,
        # rope hanging
        """
           --------^
           |       |
                   |
                   |
                   |
                   |
            -------o
        """,
        # empty state

        """ 
           --------^
                   |
                   |
                   |
                   |
                   |
            -------o            
        """

    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
