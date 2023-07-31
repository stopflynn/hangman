import random
from easy import easy_list
from medium import medium_list
from hard import hard_list


# hangman begins
def get_word(wording):

    easy = random.choice(wording)

    return easy.upper()


print()

name = input("Please enter your name: ")
print()
difficulty = input("What difficulty would you like, " + name + "? Easy, medium, or hard? ")
if difficulty == "easy":
    words = easy_list
elif difficulty == "medium":
    words = medium_list
else:
    words = hard_list

secret_word = get_word(words)
print(secret_word)
guess = input("Please guess a letter or word: ").upper()

if secret_word == guess:
    print("Correct word")
else:
    print("Incorrect word")
