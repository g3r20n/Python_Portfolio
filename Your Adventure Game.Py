print("In this game, you will navigate through the airport to help your character reach the correct gate to catch their plane to Berlin. Start by typing your name below, good luck!")

characterName = input("Please type your character's name: ")
print("Welcome", characterName, "to your new airport adventure! 🚀")


answer = input(
    "You took a taxi to the airport and the taxi driver dropped you off at terminal 7. You get out of the taxi and walk through one of the revolving doors. Congrats, you are now inside terminal 7! All you need to do is find how to get to gate number 3, where your plane from the airline Airberlin will be departing from. Now you have two options, either you go right or you go left. Which direction would you like to take? Please type: Right or Left, to continue. ").lower()

if answer == "right":
    answer = input("You start walking towards your right and you notice an airport customer service agent. You can ask him for directions or you can try to figure it out yourself. Please type: I need directions or I'll figure it out, to continue. ").lower()

    if answer.lower() == "i need directions":
       answer = input("You asked the airport customer service agent for directions and they imformed you that you must pass through the airport security gates to enter the departures hall, where you will find gate number 3. That's when you remembered about your luggage, should you carry it on the plane or get it checked-in at the counter? Please type: Cabin or Check-in, to continue. ")

    if answer.lower() == "cabin":
            print("You take your carry-on luggage through TSA and pass the security check point and finally arrive at departure hall where you quickly locate gate number 3, which happen to be right in front of you! Congrats, you made it to Airberlin! Right on time, as they just started calling you group A to board the plane. Enjoy your time in Berlin, tschuss! ")

    elif answer.lower() == "check-in":
            print("You look around and try to find the Airbeerlin check-in counter, after a few minutes you finally find it. There are 4 people head of you which is not bad. You patiently wait for your turn and right before it's your time, the airberlin computers stop working. You decide to head back to all gates entrance for departure, but now the line is 5 times as long. It takes you 50 minutes to pass through TSA and you end up missing your flight. Sorry, you lost! ")


    elif answer.lower() == "i'll figure it out":
        answer =  input("You take your time to find the way to your gate as you have a lot of time and previous experience nativating in previous airport. Like, let's be honest. How diferent could they be!? Your start to look around and you see a sign that says 'All gates entrance for departure.' At that exact moment, you realized you have a decision to make about your luggage, should you carry it on the plane or get it checked-in at the counter? Please type: Cabin or Check-in, to continue. ")

    if answer.lower() == "cabin":
            print("You take your carry-on luggage through TSA and pass the security check point and finally arrive at departure hall where you quickly locate gate number 3, which happen to be right in front of you! Congrats, you made it to Airberlin! Right on time, as they just started calling you group A to board the plane. Enjoy your time in Berlin, tschuss! ")

    elif answer.lower() == "check-in":
            print("You look around and try to find the Airbeerlin check-in counter, after a few minutes you finally find it. There are 4 people head of you which is not bad. You patiently wait for your turn and right before it's your time, the airberlin computers stop working. You decide to head back to all gates entrance for departure, but now the line is 5 times as long. It takes you 50 minutes to pass through TSA and you end up missing your flight. Sorry, you lost! ")

    else:
        print("Not a valid optiom. You missed your plane! 😢")   

elif answer == "left":
    answer = input("You choose the left path, which takes you to a sign that says 'Airport Lounges.' As you approach the lounges, a friendly attendant offers you a complimentary pass to a luxurious lounge. Do you want to accept the pass and enter the lounge or decline and continue exploring the terminal? Please type accept or decline. ").lower()

    if answer.lower() == "accept":
        answer = input("You accept the complimentary lounge pass and step into the luxurious airport lounge. Inside, you find comfortable leather chairs, soft ambient music, and a wide selection of complimentary snacks and beverages. A friendly lounge attendant approaches you and informs you of two amenities available: a buffet with international cuisine or a well-stocked bar. Please type: cuisine or bar, to continue. ")

    if answer.lower() == "bar":
        answer =  input("You can choose from beer or tequila. Please type: Beer or Tequila, to continue. ")

        if answer.lower() == "beer":
            answer = input("You got a beer, then headed out the lounge to the TSA check point to enter to the departuree hall where you quickly found gate number 3 and caught the flight to Berlin! Enjoy your time visitng die Museumsinsel!  ")

        elif answer.lower() == "tequila":
            answer = input("Your start hammering down shots of tequila with this famous actor and actress. The conversations were so amazing that you ended up missing your flight and never made it to berlin! Sorry, you lost! But atleast you got to take tequila shots with two famous peole :) ")

    if answer.lower() == "cuisine":
        answer =  input("You decide to indulge in the gourmet meal at the buffet in the airport lounge. As you approach the buffet area, the enticing aroma of freshly prepared dishes wafts through the air. Since your arrived almost at closing, they only have two options pasta or a grilled cheese sandwhich. Please type: pasta or grilled cheese, to continue. ")

        if answer.lower() == "pasta":
            answer = input("You picked the pasta, but 5 minutes after eating it. Your stomach starts to ramble, sending straight to the bathroom. It's food poisining, you are too sick to enter a plane. Sorry, you missed the flight to Berlin!")

        elif answer.lower() == "grilled cheese":
            answer = input("Your start eating this simple but yet so flavourful cheese sandwhich. You are enjoying so much that you lose track of time. You quickly finish it cheese sandwhich and headed out the lounge to the TSA check point to enter to the departuree hall where you quickly found gate number 3 and caught the flight to Berlin! Enjoy your time visitng die Museumsinsel!")
    
    else:
        print("Not a valid optiom. You missed your plane! 😢")   

if answer.lower() == "decline":
        answer =  print("You turn around and headed towards the sign that says TSA check point to enter to the departuree hall where you quickly found gate number 3 and caught the flight to Berlin! Enjoy your time visitng die Museumsinsel!")

print("Thank you for trying to help", characterName, "reach Berlin")