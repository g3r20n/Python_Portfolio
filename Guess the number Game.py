#importing a built-in module on python 
import random

print("This game will let you input any number to create a range which starts with 0 and ends with your input number for example(0 to 10, 0 to 50, 0 to 100, etc.). Then you try to guess the random number the python program selected for you to guess! 😊")

userNumber = input("Type a number: ")

if userNumber.isdigit():
    userNumber = int(userNumber)

    if userNumber <= 0:
        print("Please type a numbeeer larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()        

randomNumber = random.randrange(0, userNumber)
guesses = 0

while True:
    guesses += 1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number next time.")
        continue

    if userGuess == randomNumber:
        print("Winner Winner Chicken Dinner! 🍗")
        break
    elif userGuess > randomNumber:
        print("Too hot! You were above the number! 🥵🥵🥵")
    else:
        print("Too cold! You were below the number! 🥶🥶🥶")    
             
print("You got it in", guesses, "guesses")