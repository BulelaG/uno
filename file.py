import random
from termcolor import colored # pyright: ignore[reportMissingImports]
"""
Generate uno deck of 108 cards
parameters: none
Return values: deck->list
"""

def buildDeck():
    deck = []                                    
    colours = ["Red","Green","Blue", "Yellow"]                         
    values = [0,1,2,3,4,5,6,7,8,9, "Draw Two","Skip","Reverse"]
    wilds = ["Wild","Wild Draw Four"]
    
    for colour in colours:
        for value in values:                                            ##nested forloop for deck
            cardValue = "{} {}".format(colour, value)
            deck.append(cardValue)
            if value != 0:
                deck.append(cardValue)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])                                            ## adding wild cards on the index 1&2
    # print(deck)
    return deck


"""
Shuffles a list of items passed into it
Parameters : deck->list
Return values: deck ->list
"""

def shuffleDeck(deck):
        random.shuffle(deck)
        return deck

"""
Draw card function that specifies a number of cards off the top of the deck
Parameters: numCards >   list
"""
def drawCards(numCards):
     cardsDrawn = []
     
     for x in range(numCards):
          cardsDrawn.append(unoDeck.pop(0))
     return cardsDrawn

"""
Print formatted list of player's hand
Parameter: player -> list, playerHand->list
Return: None
"""

def showHand(player, playerHand):
     print(colored("Player {}'s Turn".format(player+1), "green", "on_black"))
     print(colored("Your Hand", "green", "on_black"))
     print("__________________________")
     
     y = 1
     for card in playerHand:
          print("{}) {}".format(y,card))
          y+=1
          
     print("__________________________")

"""
Check wehether a player is able to play a card, or not
Parameters: colour->string, value->string, playerHand->list
Return: Boolean
"""
def canPlay(colour, value, playerHand):
     for card in playerHand:
         if "Wild" in card:
              return True
         elif colour in card or value in card:
              return True
     return False


unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck)
discards = []
# print(unoDeck)



players = []
colours = ["Red","Green","Blue", "Yellow"]
numPlayers = int(input("How many players?"))
while numPlayers<2 or numPlayers>4:
     numPlayers = int(input("Invalid . Please enter a number between 2-4. How many players?"))
for player in range(numPlayers):
     players.append(drawCards(7))


playersTurn  = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ",1)
currentColour = splitCard[0]
if currentColour != "Wild":
     cardVal = splitCard[1]
else:
     cardVal = "Any"

while playing:
     showHand(playersTurn,players[playersTurn])
     print(colored("Card on top of discard pile: |{}|\n".format(discards[-1]), "green", "on_grey"))
     if canPlay(currentColour, cardVal, players[playersTurn]):
          cardChosen =  int(input("Which card do you want to play?"))
          while not canPlay(currentColour,cardVal,[players[playersTurn][cardChosen-1]]):
               cardChosen =int(input("Not a valid card. Which card do you want to play?"))
          print("You played {}.".format(players[playersTurn][cardChosen-1]))
          discards.append(players[playersTurn].pop(cardChosen-1))
          #check if player won
          if len(players[playersTurn]) == 0:
              playing = False
              winner = "Player {}".format(playersTurn + 1)
          else:
              
                #check for special cards 
                splitCard = discards[-1].split(" ",1)
                currentColour = splitCard[0]
                if len(splitCard) == 1:
                    cardVal == "Any"
                else:
                    cardVal = splitCard[1]
                if currentColour == "Wild":
                    for x in range(len(colours)):
                            print("{}) {}".format(x+1,colours[x]))
                    newColour = int(input("What colour would you like to choose?"))
                    while newColour <1 or newColour > 4:
                            newColour =int(input("Invalid option. What colour would you like to choose?"))
                    currentColour = colours[newColour-1]   
                if cardVal == "Reverse":
                    playDirection = playDirection * -1
                elif cardVal == "Skip":
                    playersTurn  += playDirection
                    if playersTurn == numPlayers:
                        playersTurn == 0
                    elif playersTurn < 0:
                        playersTurn = numPlayers-1
                elif cardVal == "Draw 2":
                    playerDraw = playersTurn+playDirection
                    if playerDraw == numPlayers:
                        playerDraw = 0
                    elif playerDraw < 0:
                        playerDraw = numPlayers-1
                    players[playerDraw].extend(drawCards(2))
                elif cardVal == "Draw 4":
                    playerDraw = playersTurn+playDirection
                    if playerDraw == numPlayers:
                        playerDraw = 0
                    elif playerDraw < 0:
                        playerDraw = numPlayers-1
                    players[playerDraw].extend(drawCards(4))
                print("")
     else:
            print("You can not play. You have to draw a card")
            players[playersTurn].extend(drawCards(1))
          
           
     playersTurn += playDirection
     if playersTurn >= numPlayers:
         playersTurn = 0
     elif playersTurn < 0:
               playersTurn = numPlayers-1

print("Game Over")
print("{} is the won the game!").format(winner)