import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    welcome_message = f"hello {name} and welcome to the World of Games.\nHere you can find many cool games to play"
    return welcome_message


def load_game():
    announce01 = "Please choose a game to play:" \
               "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back" \
               "\n2. Guess Game - guess a number and see if you chose like the computer" \
               "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
    print(announce01)
    chosen_game = input("1, 2, 3 ? ")
    chosen_difficulty = int(input("Please choose game difficulty from 1 to 5:"))

    if chosen_game == "1":
        MemoryGame.play(chosen_difficulty)
    if chosen_game == "2":
        GuessGame.play(chosen_difficulty)
    if chosen_game == "3":
        CurrencyRouletteGame.play(chosen_difficulty)

    print("End Load Game")

