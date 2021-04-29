'''
Step 1: Prepare our classes:
We will have three classes. A class Card, class Deck and class Player .
Each of these will inherit from the object.
We create an init method for each class.

Step 2: Create our class Card:
The Card is going to take a suit and value self.
We’re going to create the attributes suit, value
and set them equal to whatever we pass in when we create a card.

We create another method to show the card.
Everything takes self so we have access it’ s attribute self.
In the show method we want to print out the card,
so we make a string that will print out the value and the suit.

'''

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {} ".format(self.suit, self.value))

card = Card("Card", 6)
card.show()
'''
Step 3: Create our class Deck:
When we create a deck what do we want to do?
Well we might first want to build our deck with 52
cards of 4 suits from Ace to King. We start with the
init method and we initialize an attribute called cards
with an empty list which we will append to and a build
method to create our deck.

'''

import random
class Deck:
    def __init__(self):
        self.cards =[]
        self.build()

    def build(self):
        for s in ["spades", "Clubs", "Diamonds","Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for each_card in self.cards:
            each_card.show()
        '''
        Step 4: Create a Shuffle method:
        Now what do we want to do next? Well we would probably like to shuffle our deck.
        To do this we “import random” to use the Fisher Yates shuffle which is a
        very neat shuffling algorithm that makes sure that each card has an equal
        likelihood of ending up in every other position.

        '''
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    '''
    Step 5: Create a Draw Card method:
    We would like to draw a card from our shuffled deck.
    To do this we simply create a drawCard method that takes in self.
    The method will return self.cards.pop() which will remove the last card
    from the top of the deck and return that card. Lets test this out.
    '''

    def drawCard(self):
        return self.cards.pop()

# Lets test our method by calling shuffle and show to display our deck!
deck = Deck()
deck.show()
deck.shuffle()
deck.show()
card = deck.drawCard()
card.show()

# '''
# Step 6: Create Player:
# Lastly, we create a class Player with a name attribute
# set to name and a hand attribute set to an empty list.
# Next we create a draw method that takes in self and a
# deck in which we will pass in a deck. We append Deck.drawCard()
# to the self.hand and return self for the card drawn.
# '''
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.hand = []
#
#     def draw(self, deck):
#         self.hand.append(deck.drawCard())
#         return self
#     '''
#     We then create a showHand method to show the hand of the player.
#     We create a for loop that will loop card in self.hand.
#     It will then show our hand with card.show(). Now lets test our code!
#     '''
#     def showHand(self):
#         for card in self.hand:
#             card.show()
#
# bob = Player("Bob")
# bob.draw(deck)
# bob.showHand()