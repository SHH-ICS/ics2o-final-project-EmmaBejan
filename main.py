import random

options = ("rock", "paper", "scissor")
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Please choose (rock, paper, scissors): ")

  print(f"Player: {player}")
  print(f"Computer: {computer}")

  if player == computer:
    print("It's a tie!")
  elif player == "scissors" and computer == "paper":
    print("You win!")
  elif player == "paper" and computer == "rock":
    print("You win!")
  elif player == "rock" and computer == "scissors":
    print("You win!")
  else:
    print("Computer wins! You Lose, haha!")
  if not input("Want to play again? (y/n): ").lower() == "y":
    break
print("Thank you for playing :)")