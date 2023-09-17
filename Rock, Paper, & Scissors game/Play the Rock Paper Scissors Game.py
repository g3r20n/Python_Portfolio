import random

userWins = 0
computerWins = 0

playersOptions = ["rock", "paper", "scissors"]

while True:
    userInput = input("Please type Rock, Paper, or Scissors or Q to quit and see results: ").lower()
    if userInput == "q":
        break

    if userInput not in playersOptions:
        continue

    randonNumber = random.randint(0,2)
    # Rock: 0, Paper: 1, Scissors: 2
    computerSelect = playersOptions[randonNumber]
    print("Computer picked", computerSelect + ".")

    if userInput == "rock" and computerSelect == "scissors":
        print("You won! 🎉")
        userWins += 1
    elif userInput == "paper" and computerSelect == "rock":
            print("You won! 🎉")
            userWins += 1
    elif userInput == "scissors" and computerSelect == "paper":
            print("You won! 🎉")
            userWins += 1
    else:
         print("You lost! 😢")
         computerWins += 1

print("You won", userWins, "times. 😎")  
print("The computer won", computerWins, "times. 😢") 
      

print("See you soon!")


