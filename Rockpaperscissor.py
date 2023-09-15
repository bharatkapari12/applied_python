import random

class RockPaperScissor:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor"]
        self.winning_combinations = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper"
        }
        
    def play(self):
        print("Welcome to Rock Paper Scissor!")
        user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
        
        while user_choice not in self.choices:
            print("Invalid choice! Please choose rock, paper, or scissor.")
            user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
        
        computer_choice = random.choice(self.choices)
        print(f"Computer chooses: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif self.winning_combinations[user_choice] == computer_choice:
            print("You win!")
        else:
            print("Computer wins!")

# Create an instance of the game and play
game = RockPaperScissor()
game.play()
