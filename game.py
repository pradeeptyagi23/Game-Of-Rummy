#! /usr/bin/python

#-------------
# This is the main script that starts the game for a single instance of a Player.
# The game continues until the player wins or looses or the deck of cards gets empty.
# Each time the players current cards are shown in order to know the progress of the game.
# The player can pick only from the top of the Remaining cards or discard pile.
# The player can discard or submit any card he may wish.
# The current cards of the player are shown in the form of a list such as
# [{1:('Heart','Ace')}, {2:('Heart',2), ........}]


from random import shuffle
from Functions import Player

import sys

if __name__ == "__main__":
    person = Player.Player()
    while True:
        player_cards = person.showcards()
        print "----- Player 1 has following cards -------"
        print player_cards
        if person.show_status():
            print "WIN"
            sys.exit(0)
        elif person.showscore() > 101:
            print "LOOSE"
            sys.exit(0)

        if len(player_cards) < 7:
            print "Card count less than 7. Picking a card "
            if person.isempty():
                print "Deck is empty"
                sys.exit(0)
            person.pick_card()
            print person.showcards()
            if person.show_status():
                print "WIN"
                sys.exit(0)
            elif person.showscore() > 101:
                print "LOOSE"
                sys.exit(0)

        player1_choice = int(raw_input(" [ 1: Discard card 2: Pick a card ]"))
        if player1_choice == 1:
            discard_choice = int(raw_input("Please enter card to discard"))

            for mycard in player_cards:
                for key,value in mycard.iteritems():
                    if key == discard_choice:
                        person.submit_card(key,*value)

            if len(person.showcards()) < 7:
                print "--- Picking a card --- "
                if person.isempty():
                    print "Deck is empty"
                    sys.exit(0)
                person.pick_card()
                if person.show_status():
                    print "WIN"
                    sys.exit(0)
                elif person.showscore() > 101:
                    print "LOOSE"
                    sys.exit(0)

        else:
            if len(person.showcards()) == 7:
                person.showcards()
                discard_choice = int(raw_input("Please enter card to discard"))

                for mycard in player_cards:
                    for key,value in mycard.iteritems():
                        if key == discard_choice:
                            person.submit_card(key,*value)


            print "--- Picking a card --- "
            if person.isempty():
                print "Deck is empty"
                sys.exit(0)

            person.pick_card()
