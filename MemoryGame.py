import random
import time


def generate_sequence(chosen_difficulty):
    random_numbers = []

    for i in range(chosen_difficulty):
        number = random.randint(1, 101)
        random_numbers.append(number)

    return random_numbers


def get_list_from_user(chosen_difficulty):
    # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
    user_numbers = []

    for i in range(chosen_difficulty):
        number = int(input(f"Repeat Computer Number {i + 1}: "))
        user_numbers.append(number)

    print(f"user_numbers={user_numbers}")

    return user_numbers


def is_list_equal(random_numbers, user_numbers):
    # A function to compare two lists if they are equal. The function will return  True / False
    print(f"This is the Random List {random_numbers}")
    if random_numbers == user_numbers:
        print("WIN")
    else:
        print("LOST")


def play(chosen_difficulty):
    # Will call the functions above and play the game. Will return True / False if the user lost or won
    random_numbers = generate_sequence(chosen_difficulty)

    print(f"random_numbers={random_numbers}", end="")
    time.sleep(0.7)
    print("\rx x x")

    user_numbers = get_list_from_user(chosen_difficulty)
    is_list_equal(random_numbers, user_numbers)


    print("End Of Memory Game")
