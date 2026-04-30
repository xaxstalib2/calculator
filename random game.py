import random

def get_invalid_guess(lower, upper):
    while True:
        try:
            guess = int(input(f"Enter a number between {lower} and {upper}: "))
            return guess
        except ValueError:
            print("ïnvalid input. Please enter a number.")

def play_game():
    round_number = 1
    lower = 1
    upper = 50

    while True:
        print("\n" + "=" * 40)
        print(f"ROUND {round_number}")
        print(f"Guess the number between {lower} and {upper}")
        print("You have 7 attempts.")
        print("=" * 40)

        secrete_number = random.randint(lower, upper)
        attempts = 0
        guessed_correctly = False

        while attempts < 7:
            guess = get_invalid_guess(lower, upper)

            if guess < lower or guess >upper:
                print(f"Please enter a number from {lower} to {upper}.")
                continue
            attempts += 1

            if guess < secrete_number:
                print(" Too low")
            elif guess > secrete_number:
                print(" Too high")
            else:
                print(f"Correct you guessed it in {attempts} attempt(s).")
                guessed_correctly = True
                break

            if not guessed_correctly:
                print(f"Game Over! The correct number was {secrete_number}.")

            play_again = input("Do you want to play again? (yes/no): ").strip.lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break

            round_number += 1
            upper += 50

play_game()


        