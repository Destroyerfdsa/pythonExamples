#Nicholaus Whites
#Deck of cards
#12/6/2018
import random

deck = []
player1_hand = []
player2_hand = []

def makedeck(deck):
    """ populate the deck of cards """
    #making deck of cards
    SUITS = ["Hearts","Diamonds","Clubs","Spades"]
    VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)

def shuffledeck(deck):
    #random.shuffle(deck)
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp


def dealcard(deck,player1_hand,player2_hand):
    #taking the card from the top of the deck and adding it to the players hands
    for i in range(5):
        card = deck.pop()
        player2_hand.append(card)
        card = deck.pop()
        player1_hand.append(card)
        




#before deck is shuffled
makedeck(deck)
print(len(deck))
print(deck)

#shuffling deck and showing it
print("\n\n\n")
shuffledeck(deck)
print(deck)

#dealing to  players hands
dealcard(deck,player1_hand,player2_hand)

#showing players hands
print("\n\n\n")
print(player1_hand)
print(player2_hand)

#showing amount of cards left in deck
print(len(deck))
