print("In this game, you will navigate through the airport to help your character reach the correct gate to catch their plane to Berlin. Start by typing your name below, good luck!")

name = input("Please type your characters name: ")
print("Welcome", name, "to your new airport adventure! 🚀")


answer = input(
    "You took a taxi to the airport and the taxi driver dropped you off at terminal 7. You get out of the taxi and walk through one of the revolving door. Congrats, you are now inside terminal 7! Now you need to find how to get to gate number 3, where your plane from the airline 'AirBerlin' will be departing from. Now you have two options, either you go right or you go left. Which direction would you like to take? ").lower()

if answer == "right":
    answer = input("you start walking towards your right and you notice an airport customer service agent. You can ask him for directions or you can try to figure it out yourself. Please type: I need directions or I'll figure it out, to continue.  ")

    if answer == "I need directions":
        print("You asked the airport customer service agent for directions and they imformed you that you must pass through the airport security gates to enter the departures hall, where you will find gate number 3   ")

    elif answer == "I'll figure it out":
        print()

    else:
        print("Not a valid optiom. You missed your plane! 😢")    

elif answer == "left":
    print()

else:
    print("Not a valid optiom. You missed your plane! 😢")

