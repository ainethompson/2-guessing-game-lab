
"""A number-guessing game."""

#Pseudocode:

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

user_name = input("Howdy, what's your name?\n")

print(f"{user_name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.")


