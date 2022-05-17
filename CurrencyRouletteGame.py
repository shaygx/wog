from currency_converter import CurrencyConverter
import random


def play(chosen_difficulty):
    # 1. welcome
    print("Welcome ,The computer will choose for you A Random Number Between 1-100...")
    # 2. random value in USD
    random_number = random.randint(1, 100)
    # 3. covert USD to ILS
    currency = CurrencyConverter().convert(random_number, 'USD', 'ILS')
    # print(f"for debug! ILS: {currency}")

    # 4. find boundaries for the guess
    low_value, high_value = get_money_interval(chosen_difficulty, currency)
    # 5. ask user to guess ILS according to USD
    money_guess = get_guess_from_user(random_number)

    # 6. compare actual ILS to user's guess ILS
    if low_value <= money_guess <= high_value:
        print(f'The actual value of {random_number} USD in ILS is {currency}', end='')
        print("\nNice , you are correct.\n")
    else:
        print(f'The actual value of {random_number} USD in ILS is {currency}', end='')
        print("\nSo you LOST , feel free to try again .\n")
    print("Game over Currency.")


def get_money_interval(chosen_difficulty, currency):
    low_value = (currency - (5 - chosen_difficulty))
    high_value = (currency + (5 - chosen_difficulty))
    return low_value, high_value


def get_guess_from_user(random_number):
    money_guess = int(input(f'Now,what is your Guess ILS value according to that chosen number of {random_number}USD? '))
    return money_guess
