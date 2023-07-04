""" WIP. Not for use yet. 
The goal is for the card class is to act as a supporting coordinator between decks and hands.
The card class is meant to be able to increase the features of the cards, such as being facedown or faceup
By: patjcolon
Last updated 6/28/2023"""

class Card():   #unfinished
    """Card object created everytime a card is removed from a Deck_Cards
    Card object Destroyed when returned to a deck or trashed.
    Can be face up or face down. Can be flipped"""
    def __init__(self, card_face: str = "KH", face_up: bool = True):
        self.face = card_face
        self.face_up = face_up

    def __del__(self):
        del self.face
        del self.face_up
        del self

    def flip(self):
        self.face_up = not self.face_up
        if self.face_up:
            return f"{self.face} has been revealed."
        return "Putting card face down."

    def view_card(self):
        if self.face_up:
            return self.face
        return "??"