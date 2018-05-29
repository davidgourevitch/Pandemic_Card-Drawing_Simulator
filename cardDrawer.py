import sys
import random
#Make all the lists
emergencyEvents = ["CDC Planes Grounded", "Containment Failure", "Disease Hotspot", "Disease Zones Expand", "Limited Options", "Logistics Failure", "Patient Zero", "Sanitation Breakdown", "Time Runs Out", "WideSpread Panic"]
deck = ["Algiers", "Atlanta", "Baghdad", "Bangkok", "Beijing", "Bogota", "Buenos Aries", "Cairo", "Chennai", "Chicago", "Delhi", "Essen", "Ho Chi Minh City", "Hong Kong", "Istanbul", "Jakarta", "Johannesburg", "Karachi", "Khartoum", "Kinshasa", "Kolkata", "Lagos", "Lima", "London", "Los Angeles", "Madrid", "Manila", "Mexico City", "Miami", "Milan", "Montreal", "Moscow", "Mumbai", "New York", "Osaka", "Paris", "Riyadh", "San Francisco", "Santiago", "Sao Paulo", "Seoul", "Shanghai", "St. Petersburg", "Sydney", "Taipei", "Tehran", "Tokyo", "Washington"]
events = ["Goverment Grant", "Forecast", "Airlift", "Special Orders", "Remote Treatment", "Borrowed Time", "Re-examined Research", "Rapid Vaccine Delivery", "Mobile Hospital"]
epidemics = ["Chronic Effect", "Complex Molecular Structure", "Slippery Slope", "Uncounted Populations", "Unacceptable Loss", "Government Interference"]
roles = ["Scientist", "Researcher", "Medic", "Quarintine Specialist", "Operations Expert", "Dispatcher", "Contingency Planner", "Field Director", "Virologist", "Pilot", "Local Liason", "Field Operator", "Epidemiologist", "Generalist", "Archivist", "Containment Specialist"]

print("Welcome to Pandemic!\n")

eventsDecision = "a"
while ((eventsDecision != "y") and (eventsDecision != "Y") and (eventsDecision != "n") and (eventsDecision != "N")):
	eventsDecision = input("Would you like to play with Emergency Events? Y/N\n")
	if ((eventsDecision != "y") and (eventsDecision != "Y") and (eventsDecision != "n") and (eventsDecision != "N")):
		print("I did not understand that...")
epidemDecision = "a"
while ((epidemDecision != "y") and (epidemDecision != "Y") and (epidemDecision != "n") and (epidemDecision != "N")):
	epidemDecision = input("Would you like to play with the Virulent Strain? Y/N\n")
	if ((epidemDecision != "y") and (epidemDecision != "Y") and (epidemDecision != "n") and (epidemDecision != "N")):
		print("I did not understand that...")

#Establish all the sizes
eventsDecision = (eventsDecision == "Y" or eventsDecision == "y")
epidemDecision = (epidemDecision == "Y" or epidemDecision == "y")
numCities = len(deck)
numEmergencies = 6
numEpidemics = numEmergencies 
numEvents = 5
turn = 0
handSize = 4
finalDeckSize = len(deck) + numEpidemics + numEvents + eventsDecision*(numEmergencies)

print("Num cities = " + str(numCities) + "Num events = " + str(eventsDecision*numEmergencies))
#Welcome
print("Starting hands are...\nPlayer 1 (" + roles.pop(random.randint(0, len(roles) - 1)) + "):\n")

#add events to deck - working
for i in range(numEvents):
	index = random.randint(0, len(deck)-1)
	card = events.pop(random.randint(0, len(events)-1))
	deck.insert(index, card)

#Make hands - Working
hand1 = []
for i in range(handSize):
	hand1.append(deck.pop(random.randint(0, len(deck)-1)))
	print(" " + hand1[len(hand1)-1] + "\n")
print("\nPlayer 2 (" + roles.pop(random.randint(0, len(roles) - 1)) + "):\n")
hand2 = []
for i in range(handSize):
	hand2.append(deck.pop(random.randint(0, len(deck)-1)))
	print(" " + hand2[len(hand2)-1] + "\n")
#print them - done
for i in range(0):
	print("")

#Shuffle the remaining cards...
for i in range(1000):
	random.shuffle(deck)

#Fill the deck
#Emergency events
sizeOfDeck = len(deck)
if (eventsDecision):
	numAlreadyUsed = (numEmergencies-sizeOfDeck%numEmergencies)*(sizeOfDeck//numEmergencies+1) #iterations * values used in each iteration
	for i in range (sizeOfDeck%numEmergencies):
		#decks with an extra card
		card = "Emergency Event: " + emergencyEvents.pop(random.randint(0, len(emergencyEvents) - 1))
		index = random.randint((i*((sizeOfDeck//numEmergencies) + i)), ((i + 1)*(sizeOfDeck//numEmergencies) + i))
		deck.insert(index, card)
		
	for i in range (numEmergencies - sizeOfDeck%numEmergencies):
		#deck with normal card
		card = "Emergency Event: " + emergencyEvents.pop(random.randint(0, len(emergencyEvents) - 1))
		index = random.randint((numAlreadyUsed + i*(sizeOfDeck//numEmergencies)), (numAlreadyUsed + (i+1)*(sizeOfDeck//numEmergencies)))
		deck.insert(index, card)

#do epidemics 17chars
sizeOfDeck = len(deck)
numAlreadyUsed = (numEmergencies-sizeOfDeck%numEmergencies)*(sizeOfDeck//numEmergencies+1) #iterations * values used in each iteration
for i in range(sizeOfDeck%numEpidemics):
	if (epidemDecision):
		card = "Epidemic: " + epidemics.pop(random.randint(0, len(epidemics)-1))
	else:
		card = "EPIDEMIC!"
	index = random.randint((i*((sizeOfDeck//numEpidemics) + i)), ((i + 1)*(sizeOfDeck//numEpidemics) + i))
	deck.insert(index, card)

for i in range(numEpidemics - sizeOfDeck%numEpidemics):
	if (epidemDecision):
		card = "Epidemic: " + epidemics.pop(random.randint(0, len(epidemics)-1))
	else:
		card = "EPIDEMIC!"
	index = random.randint((numAlreadyUsed + i*(sizeOfDeck//numEpidemics)), (numAlreadyUsed + (i+1)*(sizeOfDeck//numEpidemics)))
	deck.insert(index, card)

#print("Printing deck..")
#for i in range(len(deck)):
#	print(deck[i] + "\n")

#Start the game
print("Press enter anytime you wish to draw a hand. Do so now to end turn 1\n")
input("...")
while(1 == 1):
	turn = turn + 1
	print("End of turn " + str(turn) + ".")
	draw1 = deck.pop(0)
	draw2 = deck.pop(0)
	if (len(deck) > 1 and draw1[:4] == "Epi" and draw2[:4] == "Eme"):
		temp = draw1
		draw1 = draw2
		draw2 = temp
	if (len(deck) > 1):
		input(" Draw 1: " + draw1 + "...")
		print(" Draw 2: " + draw2)
	else:
		if (len(deck) > 0):
			print(" The last card was " + deck.pop(0))
		print("\nThe game is over. Thank you for playing! :^)")
		input("Press enter to quit.")
		break
	input(" There are " + str(len(deck)) + " remaining card(s)...\n")