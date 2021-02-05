from random import randint

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

num = randint(1, 100)

num_guesses = 0

while True:
    try:
        guess = int(input("Your guess?\n"))

        if guess not in range(1, 100):
            print("So you don't know how to count? Try again!")
        elif guess > num:
            print("Too high")
            num_guesses += 1
        elif guess < num:
            print("Too low")
            num_guesses += 1
        elif guess == num:
            num_guesses += 1
            print(f"Congrats, {user_name}! You guessed my number in {num_guesses} tries.")
            break

    except ValueError:
        print("That's not even a number... Try again!")