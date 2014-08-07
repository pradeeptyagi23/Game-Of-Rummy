#! /usr/bin/python

# -------------------------
# This is a library of functions that define 3 class :
# Card - Which is a simple class to store the card
# Deck - Which provides various functions to peform operations on the cards
# Player - This class is instantiated by the main Game.py script to start the game. This class  provides various functions to be performed on the current
# hand of cards of the player. This class inherits the Deck class.


from random import shuffle

import sys

deck = [
    {1: ('Heart','Ace')},
    {2: ('Heart',2)},
    {3: ('Heart',3)},
    {4: ('Heart',4)},
    {5: ('Heart',5)},
    {6: ('Heart',6)},
    {7: ('Heart',7)},
    {8: ('Heart',8)},
    {9: ('Heart',9)},
    {10: ('Heart',10)},
    {11: ('Heart','Jack')},
    {12: ('Heart','Queen')},
    {13: ('Heart','King')},
    {14: ('Diamond','Ace')},
    {15: ('Diamond',2)},
    {16: ('Diamond',3)},
    {17: ('Diamond',4)},
    {18: ('Diamond',5)},
    {19: ('Diamond',6)},
    {20: ('Diamond',7)},
    {21: ('Diamond',8)},
    {22: ('Diamond',9)},
    {23: ('Diamond',10)},
    {24: ('Diamond','Jack')},
    {25: ('Diamond','Queen')},
    {26: ('Diamond','King')},
    {27: ('Club','Ace')},
    {28: ('Club',2)},
    {29: ('Club',3)},
    {30: ('Club',4)},
    {31: ('Club',5)},
    {32: ('Club',6)},
    {33: ('Club',7)},
    {34: ('Club',8)},
    {35: ('Club',9)},
    {36: ('Club',10)},
    {37: ('Club','Jack')},
    {38: ('Club','Queen')},
    {39: ('Club','King')},
    {40: ('Club','Ace')},
    {41: ('Spade',2)},
    {42: ('Spade',3)},
    {43: ('Spade',4)},
    {44: ('Spade',5)},
    {45: ('Spade',6)},
    {46: ('Spade',7)},
    {47: ('Spade',8)},
    {48: ('Spade',9)},
    {49: ('Spade',10)},
    {50: ('Spade','Jack')},
    {51: ('Spade','Queen')},
    {52: ('Spade','King')},
    ]


'''
deck = [
    {1: ('Diamond',4)},
    {2: ('Diamond',5)},
    {3: ('Diamond',6)},
    {20: ('Diamond',7)},
    {21: ('Diamond',8)},
    {22: ('Diamond',9)},
    {23: ('Diamond',10)},
    {24: ('Heart','Ace')},
    {24: ('Spade','Ace')},
    {24: ('Club','Ace')}
    ]

'''

value_map = {'Ace':1,'Jack':11,'Queen':12,'King':13}

class Card(object):
    def __init__(self,*args):
		self.card = args


class Deck(Card):
    def __init__(self):
        self.deck = deck
        self.discardPile = []
        super(Deck, self).__init__(self.deck)


    def getDeck(self):
        return self.deck

    def get_discard_pile(self):
        return self.discardPile

    def discard_card(self,card_no,set,value):
        self.discardPile.append({card_no:(set,value)})

    def shufflecards_deck(self):
        shuffle(self.deck)

    def shufflecards_discardPile(self):
        shuffle(self.discardPile)

    def drawcard_deck(self):
        self.shufflecards_deck()
        return self.deck.pop()

    def drawcard_discardPile(self):
        self.shufflecards_discardPile()
        return self.discardPile.pop()

    def isempty(self):
        return len(self.deck) == 0




class Player(Deck):
    def __init__(self):
        self.hand = []
        super(Player,self).__init__()
        self.__init_player_cards__()

    def __init_player_cards__(self):
        count = 0
        while count < 7:
            self.hand.append(self.drawcard_deck())
            count = count + 1

    def pick_card(self):
        self.hand.append(self.drawcard_deck())

    def submit_card(self,no,set,value):
        self.discard_card(no,set,value)
        count = -1
        for card in self.hand:
            count = count + 1
            for key,value in card.iteritems():
                if(key == no):
                    self.hand.pop(count)

    def showcards(self):
        return self.hand

    def showscore(self):
        sum = 0
        for value in self.hand:
            for value in value.values():
                if isinstance(value[1],basestring):
                    card_value = value_map[value[1]]
                else:
                    card_value = value[1]

                if card_value == 1:
                    sum = sum + 1
                else:
                    sum = sum + 10
        return sum

    def show_status(self):
    	non_empty_buckets = {}
    	Diamond_bucket = []
    	heart_bucket = []
    	spade_bucket = []
    	club_bucket = []
    	face_value = []
    	win_flag = False

        for card in self.hand:
            if isinstance(card.values()[0][1], basestring):
                card_value = value_map[card.values()[0][1]]
            else:
                card_value = card.values()[0][1]

            if card.values()[0][0] == 'Diamond':
                Diamond_bucket.append(card_value)
            elif card.values()[0][0] == 'Heart':
                heart_bucket.append(card_value)
            elif card.values()[0][0] == 'Club':
                club_bucket.append(card_value)
            else:
                spade_bucket.append(card_value)

    	if Diamond_bucket:
        	non_empty_buckets['Diamond'] = Diamond_bucket
    	if heart_bucket:
        	non_empty_buckets['Heart'] = heart_bucket
    	if spade_bucket:
        	non_empty_buckets['spade'] = spade_bucket
    	if club_bucket:
        	non_empty_buckets['club'] = club_bucket


    	if len(non_empty_buckets.keys()) == 1:
            face_value =  sorted(non_empty_buckets.values()[0])
            if (face_value == (range(face_value[0],face_value[-1]+1))):
                win_flag = True

    	elif len(non_empty_buckets.keys()) == 2 or len(non_empty_buckets.keys()) == 4:
            newdict = sorted(non_empty_buckets.items() , key = lambda x : len(x[1]))
            if( len(newdict[-1][1]) == 4 or len(newdict[-1][1]) == 3 ):
                if len(non_empty_buckets.keys()) == 2:
                    if(len(newdict[-1][1]) == 4) and ( sorted(newdict[-1][1]) == range(sorted(newdict[-1][1])[0], sorted(newdict[-1][1])[-1]+1)) and ( sorted(newdict[-2][1]) == range(sorted(newdict[-2][1])[0], sorted(newdict[-2][1])[-1]+1)):
                        win_flag = True

                elif len(non_empty_buckets.keys()) == 4:
       	            if(len(newdict[-1][1]) == 4):
                        if (sorted(newdict[-1][1]) == range(sorted(newdict[-1][1])[0], sorted(newdict[-1][1])[-1]+1)):
                            comp_list = list(zip(newdict[-2][1],newdict[-3][1],newdict[-4][1])[0])
                            if comp_list[1:] == comp_list[:-1]:
                                win_flag = True
    	return win_flag
