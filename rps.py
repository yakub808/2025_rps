import sys
import random

def main():
    while True:
        print()
        print("ROCK, PAPER, SCISSORS")
        print()
        main_menu()
        print()

        try:
            choice = int(input("Choice: "))

            if choice == 1:
                play_game()
            elif choice == 2:
                display_rules()
            elif choice == 3:
                sys.exit()
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, try again.")


def main_menu():
    print("Main Menu")
    print()
    print("1. Play")
    print("2. Rules")
    print("3. Quit")
    print()


def play_game():
    print()
    print("Choose your weapon.")
    print()
    print("1. Rrock")
    print("2. Paper")
    print("3. Scissors")
    print()
    print("4. Back")
    print()

    pawns = ["rock", "paper", "scissors"]

    while True:
        try:
            weapon = int(input("Weapon: "))

            if weapon == 1:
                player = "rock"
            elif weapon == 2:
                player = "paper"
            elif weapon == 3:
                player = "scissors"
            elif weapon == 4:
                return
            else:
                print("Invalid input, try again.")
      
            
            pc = random.choice(pawns)
            print(f"PC: {pc}")

            if player == pc:
                print("Tie!")
            elif player == "rock" and pc == "scissors":
                print("Rock crushed scissors! You win!")
            elif player == "scissors" and pc == "paper":
                print("Scissors cut paper! You win!")
            elif player == "paper" and pc == "rock":
                print("Paper covered rock! You win!")
            elif player == "rock" and pc == "paper":
                print("Rock was covered by paper! You lose!")
            elif player == "scissors" and pc == "rock":
                print("Scissors were crushed by rock! You lose!")
            elif player == "paper" and pc == "scissors":
                print("Paper was cut by scissors! You lose!")
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, try again.")


def display_rules():
    print()
    print("Rules")
    print()
    print("Rock crushes scissors")
    print("Scissors cuts paper")
    print("Paper covers rock")
    print()
    print("1. Back")
    print()

    while True:
        try:
            back = int(input("Choice:"))
            if back == 1:
                return
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()