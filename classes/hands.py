"""WIP - contains classes for hands. Hands are used in card games in conjuction with card_decks, minimum. styl and suitr recommended
By: patjcolon
Last updated 6/28/2023"""


from . import Deck_Cards
from helper_modules.styl import suitr
from helper_modules.typr import typr

class Hand():   # unfinished
    """Hand class used by Player/Dealer/Opponents for holding cards. Can draw/return cards from/to decks"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        return suitr(self.cards)

    def take(self, deck: Deck_Cards, draw_from_where: str = "TOP"):
        draw_from = Deck_Cards.draw
        card = draw_from(deck, draw_from_where)
        self.cards.append(card)
        return [card]

    def toss(self, *cards):
        if not self.cards: return print("Hand is empty.")
        cards_tossed = []
        for card in cards:
            if card in self.cards:
                cards_tossed.append(card)
                self.cards.remove(card)
            else: print(f"{card} not in hand.")
        return cards_tossed
        

    def put_in_deck(self,deck: Deck_Cards, *cards):
        # Put card(s) in deck, hand, or table
        if not self.cards: return print("Hand is empty.")
        selection_valid = False
        for card in cards:
            if card in self.cards:
                selection_valid = True
                self.cards.remove(card)
            else: print(f"{card} not in hand.")
        if not selection_valid: return print("Cards were not in hand.")
        put_in_deck = Deck_Cards.combine_decks
        put_in_deck(deck, cards)

    def check_hand(self):
        return typr(f"Your hand is: {suitr(self.cards)}")


class Dealer(Hand):   # unfinished
    """Child class of Hand, can draw/return cards as well as deal cards and take cards from/to decks.
    Can deal cards face down. Will have some AI/algorithms to play games"""
    #? Can dealer have own personal deck? Will size of deck depend on game?
    pass