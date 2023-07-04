from os import system

from classes import *
from helper_modules.styl import styl, suitr, testr
from helper_modules.typr import typr

deck1 = Deck_Cards()



my_hand = Hand()
deck1.shuffle_deck()


# turn this into one of them typrs!
def hide_unhide(hide:bool = True):
    if hide:
        return print('\033[?25l',end="")
    print('\033[?25h',end="")


# here is a rough codeup of the above idea in action:
def get_user_input(symbol_shown: str = "> "):
    hide_unhide(False)
    user_input = input(typr(symbol_shown, "slow", False))
    hide_unhide()
    return user_input


# just a silly game i came up with lol
# I should call the game "X 52!"
# can have the player draw one card each round "Here, take this!"
# says special things depending on how many cards the player has
# "woah 1 card. nice, real nice... here check out 104!"
# "10 cards? guess you have nothing better to do..."
# "Wow, you have 52 cards now. Maybe it's time for you to host..."
# then the game switches to you handing out cards (well saying its you)
# then the computer has a hand instead, and when they get 52 cards...
# 52 counter starts at 0 and goes up to 52, so 52 rounds of playing 52 rounds
# also, when you reach 52, the computer asks for them back "gimme those back!"
# and you have to press enter, each time you do it removes 1 card from your hand and sends it to them
# which they then secretly put in a deck and start playing with that deck

# maybe some games they secretly give you 1 of every card in a deck, and at the end of that special round you get something cool
# special messages for havin 4 of a kind, a full set of a suit, etc

# maybe the game starts with 51 cards and one golden card!! if the player gets the golden card they win?
# maybe create a lucky card, death cards, and other cards? if 1 lucky 3 death, one value from each suit can be swapped 
#    (no 'AD', 'AC', 'AH' 'AS') instead 'AL' x3 , 'AW' ? 
# death: U+2620, trophy: 1F3C6, 4leaf: 1F340(these large ones dont work)
# also dice values are 2680-2685. squared key is 26BF
def never_ending_cards():
    deck52 = Deck_Cards()
    deck2 = Deck_Cards()
    player_hand = Hand()
    hide_unhide()
    typr("Welcome to the never ending cards dance! HAHAHA!")
    typr("Buckle up... Go:", "slow")
    rounds = 1
    deck_s = ""
    while True:
        deck2.shuffle_deck()
        typr(f"{suitr(deck2.deck)}", "fastest")
        typr(f"Yay! Time to play {deck2.card_count} card pickup...", "medium")
        system('cls')
        typr(f"And take this!", "slow")
        player_hand.take(deck52, "TOP")
        deck2.draw(player_hand.cards[-1])
        system('cls')
        player_hand.check_hand()
        typr(f"That was only {deck2.number_of_sets} deck{deck_s}...")
        typr("Let's add another!")
        deck2.combine_decks()
        deck_s = "s"
        rounds += 1
        typr(f"Time for round {rounds}! Go:")


# original CC: Diamonds game
def diamonds_game():
    while deck1.diamonds:    
        hide_unhide()
        typr("Press enter to play or 'Q' and then enter to quit.")
        player_choice = get_user_input().upper()
        if player_choice == 'Q':
            typr("Thank you for playing!")
            exit()
        typr(f"You drew: {suitr(my_hand.take(deck1, 'DIAMONDS'))}")
        typr(f"Remaining diamonds: {suitr(deck1.diamonds)}")
        my_hand.check_hand()

    print("\nDeck's remaining cards: ", end="")
    typr(f"{suitr(deck1.deck)}", "fastest")
    typr("Thank you for playing!")


never_ending_cards()