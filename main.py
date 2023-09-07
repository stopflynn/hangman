import random
from easy import easy_list
from medium import medium_list
from hard import hard_list

# checks user has enters yes / no to a question, can be used throughout for multiple purposes


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

# gets users to select a difficulty


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


# game begins, loop starts


def get_word(wording):
    difficulty = random.choice(wording)
    return difficulty.upper()


def play(word, name, wins):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print("Let's play Hang-person, "+name+"!")
    print(display_hangman(attempts))
    print(word_completion)
    while not guessed and attempts > 0:
        # forces players to input a letter or a word
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                # tells players that they've already put in that letter, and they need to choose another. No lives lost.
                print("\033[1;31;10m You have already guessed the letter", guess)
            elif guess not in word:
                # tells players that their guess is not in the word. They lose a life
                print(f"\033[1;31;10m {guess} is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                # tells users their guessed letter is in the word and lives remain the same
                print(f"\033[1;32;10m Good job, {guess} is in the word! \n")
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
                # tells players that they've already put in that word, and they need to choose another. No lives lost.
                print("\033[1;31;10m You already guessed the word", guess)
            elif guess != word:
                # tells players that their guess is not the word. They lose a life
                print(f"\033[1;31;10m {guess} is not the word.", display_hangman(attempts))
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\033[1;31;10m Not a valid guess.")
        print(display_hangman(attempts))
        print(word_completion)
        # tells players which letters and words they've guessed as well as how many lives they have per attempt
        print(f"You've guessed: {guessed_letters, guessed_words} You have, {attempts} lives left")
        print("\n")
    if guessed:
        wins += 1
        print("\033[1;32;10m Congratulations on finding the word, you win!")
        return wins
    else:
        print(f"\033[1;31;10m Sorry, you ran out of lives. The word was {word}. Better luck next time!")


# images


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
    # wins
    wins = 0
    print("Welcome to Hang-person, it's like Hangman but more inclusive.")
    name = input("Please enter your name: ")
    play_again = "yes"
    while play_again == "yes":

        difficulty = levels("What difficulty would you like, " + name + "? Easy (e), medium (m), or hard (h)? ")
        # Ask user if they would like to read the instructions before they play
        want_instructions = yes_no("Would you like to read the instructions? (Yes/No) ")
        if want_instructions == "yes":
            print("To play Hang-person, you must guess one letter at a time. "
                  "If the letter is correct, it will enter one ore more of the blank spaces, ")
            print("which will help you to find the word. "
                  "You have seven lives, so if guess wrong seven times, you will lose and the person will be hanged. ")
            print("As each difficulty progresses, the words get longer but your number of lives remain the same.")
        word = get_word(difficulty)
        games_1 = play(word, name, wins)
        play_again = yes_no("Do you want to play again? (Yes/No)")
    print(f"End of the game. You won {games_1} games.")


if __name__ == "__main__":
    main()
