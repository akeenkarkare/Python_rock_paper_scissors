from random import randint

choice = ["rock", "paper", "scissors"]

computer = choice[randint(0,2)]

print("Welcome to the rock paper and scissors game!")
player = input("Your choice: ").lower()
print("Computer chose: " + computer)

if player == computer:
    print("Its a draw!")
elif player == "rock" and computer == "paper":
    print("Computer wins!")
elif player == "paper" and computer == "rock":
    print("Player wins!")    
elif player == "scissors" and computer == "rock":
     print("Computer wins!")
elif player == "rock" and computer == "scissors":
     print("Player wins!")
elif player == "paper" and computer == "scissors":
     print("Computer wins!") 
elif player == "scissors" and computer == "paper":
     print("Player wins!")       