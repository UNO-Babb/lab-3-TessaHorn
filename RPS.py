#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
 while True:
  # Show scoreboard before each game
  print("\nWins\tDraws\tLosses")
  print(wins, "\t", ties, "\t", losses)

  # Computer chooses
  computer = random.choice(["R", "P", "S"])

  # Player input
  player = input("Pick your weapon (R, P, S): ")

  # Show what computer picked
  if computer == "R":
     print("Computer picked Rock")
  elif computer == "P":
     print("Computer picked Paper")
  else:
     print("Computer picked Scissors")

  # Show what player picked
  if player == "R":
      print("Player chose Rock")
  elif player == "P":
      print("Player chose Paper")
  elif player == "S":
      print("Player chose Scissors")
  else:
      print("Invalid choice.")
      continue  # restart loop if input is invalid

  # Determine winner
  if player == computer:
     print("It's a draw!")
     ties += 1
  elif (player == "R" and computer == "S") or \
       (player == "P" and computer == "R") or \
       (player == "S" and computer == "P"):
        print("You win!")
        wins += 1
  else:
        print("You lose...")
        losses += 1

  # Show scoreboard after round
  print("Wins\tDraws\tLosses")
  print(wins, "\t", ties, "\t", losses)

  # Ask if player wants to play again
  again = input("Do you want to play again? (Y/N): ").upper()
  if again != "Y":
    print("\nFinal Scoreboard:")
    print("Wins\tDraws\tLosses")
    print(wins, "\t", ties, "\t", losses)
    print("Thanks for playing!")
    break


if __name__ == '__main__':
  main()
