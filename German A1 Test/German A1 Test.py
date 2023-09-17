print("Welcome to Gerson's German A1 Languague Quiz")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Schöne! Let the games beging! 😎")

score = 0

answer = input("How would you say 'I am' in German? ")
if answer.lower() == "ich bin":
    print ("Correct!")
    score += 1
else:
    print ("😢 incorrect")

answer = input("How would you say 'You are' in German? ")
if answer.lower() == "du bist":
    print ("Correct! 2 in a row!")
    score += 1
else:
    print ("😢 incorrect")

answer = input("How would you say 'She is' in German? ")
if answer.lower() == "sie ist":
    print ("Correct! 3 in a row, you are a rockstar! 🔥")
    score += 1
else:
    print ("😢 incorrect")

answer = input("How would you say 'He is' in German? ")
if answer.lower() == "er ist":
    print ("Correct! Wow 🔥")
    score += 1
else:
    print ("😢 incorrect")         

print("You got " + str(score) + " questions correct! 🤯🤩")  
print("You got " + str((score / 4) * 100) + "%.")         