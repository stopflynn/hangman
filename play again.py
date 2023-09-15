import random
from easy import easy_list
from medium import medium_list
from hard import hard_list

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


def main():
    play_again = "yes"
    while play_again == "yes" or "y":

        # Ask user if they would like to read the instructions before they play
        want_instructions = yes_no("Would you like to read the instructions? (Y/N)")
        if want_instructions == "yes":
            print("Test instructions")
        play_again = input("Do you want to play again? (Y/N)")
    print("End of the game")


if __name__ == "__main__":
    main()
