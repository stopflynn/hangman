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
