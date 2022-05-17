import random


def generate_number(chosen_difficulty):
    print(f"Inside GuessGame.generate_number. difficulty={chosen_difficulty}")
    max_range = chosen_difficulty*20
    print(f"max range={max_range}")
    secret_number = random.randint(1, max_range)
    print(f"secret_number={secret_number}")
    return secret_number


def get_guess_from_user():
    print("Inside GussGame.get_guess_from_user")
    user_number = int(input("guess my number: "))
    return user_number


def compare_results(secret_number, user_number):
    print("Inside GuessGame.compare_result")
    if secret_number == user_number:
        return True
    else:
        return False


def play(chosen_difficulty):
    print("Inside GussGame.play")
    secret_number = generate_number(chosen_difficulty)
    print(f"secret_number inside play {secret_number}")
    user_number = get_guess_from_user()
    print(f"user number is:{user_number}")
    user_win = compare_results(secret_number, user_number)
    if user_win == True:
        print("User WIN")
    else:
        print("User LOST")
