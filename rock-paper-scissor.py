import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"The computer chose {computer_choice}.\n")

        result = check_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
play_game()
