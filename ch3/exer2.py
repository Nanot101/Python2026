# Rock Paper Scissors (single round) — Ask user for their choice, generate a 
# random computer choice (import random), determine and print the winner.
import random

rps = ['rock', 'paper', 'scissors']
playerRPS = str(input("Enter RPS: "))
print(f"Player chose: {playerRPS}")
compRPS = random.choice(rps)
print(f"Computer chose: {compRPS}")
# method 2:
# check for tie, check when player beats, else comp beats


if compRPS == playerRPS:
  print("Tie")
elif playerRPS == "rock" and compRPS == "scissors":
  print("Player wins")
elif playerRPS == "scissors" and compRPS == "paper":
  print("Player wins")
elif playerRPS == "paper" and compRPS == "rock":
  print("Player wins")
else:
  print("Computer wins")