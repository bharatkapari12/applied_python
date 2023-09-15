import random

def ComputerRandomNumberGen():
    return random.randint(1, 3)

def displayComputerChoice(computer_choice):
    if computer_choice == 1:
        return "Computer chose Rock"
    elif computer_choice == 2:
        return "Computer chose Paper"
    else:
        return "Computer chose Scissors"

def displayUserChoice():
    choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
    if choice == 1:
        return "You chose Rock", choice
    elif choice == 2:
        return "You chose Paper", choice
    elif choice == 3:
        return "You chose Scissors", choice
    else:
        return "Invalid choice", 0

def DetermineWinnerOfRPS(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if user_choice == 1:
        if computer_choice == 3:
            return "You win!"
        else:
            return "Computer wins!"

    if user_choice == 2:
        if computer_choice == 1:
            return "You win!"
        else:
            return "Computer wins!"

    if user_choice == 3:
        if computer_choice == 2:
            return "You win!"
        else:
            return "Computer wins!"


def display_static_Info(user_info, result):
    with open("result.txt", "w") as file:
        file.write("User Information:\n")
        file.write(user_info)
        file.write("\nResult of the RPS Game:\n")
        file.write(result)

def main():
    user_name = input("Enter your name: ")
    user_address = input("Enter your address: ")
    user_phone = input("Enter your phone number: ")

    user_info = f"Name: {user_name}\nAddress: {user_address}\nPhone: {user_phone}"

    while True:
        user_choice, u_choice = displayUserChoice()
        computer_choice = ComputerRandomNumberGen()
        computer_display = displayComputerChoice(computer_choice)
        result = DetermineWinnerOfRPS(u_choice, computer_choice)

        print(user_choice)
        print(computer_display)
        print(result)

        with open("inputData.txt", "a") as input_file:
            if "You win!" in result:
                input_file.write(user_info + "\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    display_static_Info(user_info, result)

main()







