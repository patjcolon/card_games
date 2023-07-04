"""
Contains the code for Deck_Cards
will be used in many card games in parent folder (eventually)
by: patjcolon
Last updated: 6/28/2023
"""
from random import shuffle, choice
from helper_modules import styl

rst = styl.unstyl()
yB = styl.styl("Yellow", "Bold")
gB = styl.styl("Yellow", "Bold")

# ysw:      "Red Bold White"
reds = styl.styl("Red", "Bold", "White")
# ysw:      "Black Bold White"
blks = styl.styl("Black", "Bold", "White")


class Deck_Cards():  # WIP : error handling, card object creation
    """Handles creation, management and deletion of all decks and their contents"""

# ====================================================================
# || Object Initialization, Deletion, and asString Functions:       ||
# ====================================================================
    def __init__(self, starting_decks: int = 1):
        """Creates starting_decks amount of decks, minimum 1.
        Creates self.card_count and self.number_of_sets for tracking purposes."""
        self.card_count = 0
        self.number_of_sets = 0
        self.external_sets_added = 0
        self.new_deck()

        # Additional starting decks created only at initialization.
        self.starting_decks = starting_decks
        extra_decks_left = starting_decks - 1
        if extra_decks_left > 0:
            extra_decks_left -= 1
            self.combine_decks(False, extra_decks_left, False, True)
            # resetting this value changed by combine decks, as initial decks don't count as external
            self.external_sets_added = 0
            extra_decks_left = 0

    def __del__(self):
        del self.diamonds, self.clubs, self.hearts, self.spades
        del self.deck
        del self.card_count
        del self.number_of_sets
        del self

    def __str__(self) -> str:
        return f"This is a deck containing {self.card_count} cards."

# ====================================================================
# || Object Testing Functions:                                      ||
# ====================================================================
    def test_deck(self, test_selection: str = "ALL", test_cycles: int = 1, deck_combining_test: object = False):
        """Tests variables and methods to ensure deck is functioning as intended. Defaults: Running "ALL" tests, 1 time, with a random new deck used in the combination
        test_selection Options: "ALL", "CURRENT", "NEW", "CLEAR", "COMBINE"
        "ALL":      Performs all tests
        "CURRENT":  Performs tests on deck as is
        "NEW":      Runs self.new_deck and performs tests on new deck
        "CLEAR":    Runs self.clear_deck and performs tests on cleared deck
        "COMBINE":  Runs self.combine_decks and performs tests on combination deck
        "SHUFFLE":  Runs self.shuffle_deck and performs tests on shuffled deck
        test_cycles: Runs iterates through test this many times
        deck_combining_test = deck that will be used in self.combine_decks. If true: use new_deck in combination. False will not combine a deck; default False"""
        test_selection = test_selection.upper()
        self.test_cycles = test_cycles
        self.tests_ran = 0
        self.deck_combining_test = deck_combining_test
        done_testing = False

        def tests_performed():
            """Tests performed in every deck test"""
            print(f"{gB}(Test #1){yB}   ----->   {rst}" +
                  f"Sets: {self.number_of_sets} Cards: {self.card_count} Starting Decks: {self.starting_decks}")

            print(f"{gB}(Test #2){yB}   ----->   {rst}" +
                  f"Diamonds: {self.diamonds}, Clubs: {self.clubs} Hearts: {self.hearts} Spades: {self.spades}")

            print(f"{gB}(Test #3){yB}   ----->   {rst}" +
                  f"Deck: {self.deck}")
            self.tests_ran += 1
            print(f"\n{yB}+-{gB}< Test Cycle #{self.tests_ran} DONE >{yB}--------------------------------------+{rst}\n\n")

        def current_deck_tests():
            """Performs tests on current deck as is"""
            print(
                f"{yB}--------------------------------------------------------------------")
            print(
                f"| -{rst}(CURRENT DECK STATS){yB}-----                                       |")
            print(
                f"--------------------------------------------------------------------{rst}")
            tests_performed()

        def new_deck_tests():
            """Runs self.new_deck and performs tests on new deck"""
            print(
                f"{yB}--------------------------------------------------------------------")
            print(
                f"| -{rst}(NEW DECK STATS){yB}-----                                           |")
            print(
                f"--------------------------------------------------------------------{rst}")
            self.new_deck()
            tests_performed()

        def clear_deck_tests():
            """Runs self.clear_deck and performs tests on cleared deck"""
            print(
                f"{yB}--------------------------------------------------------------------")
            print(
                f"| -{rst}(CLEAR DECK STATS){yB}-----                                         |")
            print(
                f"--------------------------------------------------------------------{rst}")
            self.clear_deck()
            tests_performed()

        def combine_decks_tests(deck_combining_test: object = self.deck_combining_test):
            """Runs self.combine_decks and performs tests on combination deck"""
            print(
                f"{yB}--------------------------------------------------------------------")
            print(
                f"| -{rst}(COMBINE DECKS STATS){yB}-----                                      |")
            print(
                f"--------------------------------------------------------------------{rst}")
            self.combine_decks(deck_combining_test)
            tests_performed()

        def shuffle_deck_tests():
            """Runs self.shuffle_deck and performs tests on shuffled deck"""
            print(
                f"{yB}--------------------------------------------------------------------")
            print(
                f"| -{rst}(SHUFFLE DECK STATS){yB}-----                                       |")
            print(
                f"--------------------------------------------------------------------{rst}")
            self.shuffle_deck()
            tests_performed()

        def random_deck_test():
            """Runs any style test at random"""
            choice(self.all_tests_list)()

        def run_all_tests():
            """Performs all tests in random order"""
            print(
                f"{yB}====================================================================")
            print(
                f"|| ={gB}[ RUNNING ALL DECK TESTS ]{yB}=====                               ||")
            print(
                f"===================================================================={rst}")
            all_tests_list = self.all_tests_list
            number_of_tests = len(all_tests_list)

            while number_of_tests > 0:
                number_of_tests -= 1
                random_test = choice(all_tests_list)
                random_test()
                all_tests_list.remove(random_test)

        # Used in run_all_tests and random_deck_test
        self.all_tests_list = [current_deck_tests, new_deck_tests,
                               clear_deck_tests, combine_decks_tests, shuffle_deck_tests]
        # Runs test selected for as many intervals as specified:
        while test_cycles > 0:
            test_cycles -= 1
            done_testing = False
            if test_selection == "ALL":         # Runs all deck tests in random order
                run_all_tests()
            elif test_selection == "CURRENT":   # Runs current deck tests
                current_deck_tests()
            elif test_selection == "NEW":       # Runs new deck tests
                new_deck_tests()
            elif test_selection == "CLEAR":     # Runs clear deck tests
                clear_deck_tests()
            elif test_selection == "COMBINE":   # Runs combine decks tests
                combine_decks_tests()
            elif test_selection == "SHUFFLE":   # Runs shuffle deck tests
                shuffle_deck_tests()
            elif test_selection == "RANDOM":    # Runs a randomly selected deck tests function
                random_deck_test()
            else:   # test_selection not listed - breakout of cycles loop
                print("Test selection invalid. Terminating testing objects.")
                test_cycles = 0
            # Testing complete, call objects cleanup
            done_testing = True

        # Testing objects cleanup
        if done_testing:
            del self.test_cycles
            del self.tests_ran
            del self.deck_combining_test
            return print("Testing completed. Testing objects deleted.")
        # Testing cleanup failed
        return print("Testing cleanup failed to run.")


# ====================================================================
# || Deck Management Functions:                                     ||
# ====================================================================

    def new_deck(self):
        """Declares/Resets self.deck and a self.suit for diamonds, clubs, hearts, and spades.
        Declares: Used when initialized to create values and new deck.
        Resets: Can be manually called at any point to reset deck to 1 fresh, unshuffled deck of 52 cards."""
        self.deck = []
        self.diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
                      "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        self.clubs = ["AC", "2C", "3C", "4C", "5C", "6C",
                      "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
        self.hearts = ["AH", "2H", "3H", "4H", "5H", "6H",
                       "7H", "8H", "9H", "10H", "JH", "QH", "KH"]
        self.spades = ["AS", "2S", "3S", "4S", "5S", "6S",
                       "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
        self.deck.extend(self.diamonds + self.clubs +
                         self.hearts + self.spades)
        self.card_count = 52
        self.number_of_sets = 1

    def clear_deck(self):
        """Clears every list and sets every value to 0.  Does not delete object."""
        self.deck.clear()
        self.diamonds.clear()
        self.clubs.clear()
        self.hearts.clear()
        self.spades.clear()
        self.card_count = 0
        self.number_of_sets = 0

    def shuffle_deck(self):
        """Shuffles self.deck using random.shuffle()"""
        shuffle(self.deck)

    def combine_decks(self, other_deck: object = False, extra_decks: int = 0, shuffle_decks: bool = True, create_new_deck: bool = False):
        """Takes other_deck.deck and combines it to this deck.

        For every 1 in extra_decks: runs combine_decks again (defaulting to new_deck)
        Ex: combine_decks(deck2, 3) will first combine self.deck and deck2, then it will add 3 more new decks, shuffling each time.

        Will shuffle_deck() if shuffle_decks is True, otherwise will add new decks to bottom.

        If create_new_deck True, creates a new deck to combine instead.
        Default is False. If no deck is entered, switches to True"""
        if not other_deck:
            create_new_deck = True
        if create_new_deck == True:
            del other_deck
            other_deck = Deck_Cards()

        self.deck.extend(other_deck.deck)
        self.diamonds.extend(other_deck.diamonds)
        self.clubs.extend(other_deck.clubs)
        self.hearts.extend(other_deck.hearts)
        self.spades.extend(other_deck.spades)

        self.card_count = len(self.deck)
        self.number_of_sets += 1
        self.external_sets_added += 1
        del other_deck

        if shuffle_decks:
            self.shuffle_deck()
        if extra_decks > 0:
            extra_decks -= 1
            self.combine_decks(False, extra_decks, shuffle_decks, True)

#   def combine_hands()             #   <===================== TEST TESTING TEMPORARY 123============================

# ====================================================================
# || Card Management Functions:                                     ||
# ====================================================================
    def remove_card(self, card_removed: str):
        """Helper function to update self.deck and suits"""
        self.deck.remove(card_removed)
        self.card_count -= 1

        card_suit = card_removed[-1]
        if card_suit == 'D':
            self.diamonds.remove(card_removed)

        elif card_suit == 'C':
            self.clubs.remove(card_removed)

        elif card_suit == 'H':
            self.hearts.remove(card_removed)

        elif card_suit == 'S':
            self.spades.remove(card_removed)

    def draw(self, draw_type: str = "TOP", peek: bool = False):
        """Contains all draw functions."""
        draw_type = draw_type.upper()

        def specific_card(specific_card: str = '') -> str:
            """Returns specific card if in deck, updates self.deck and suits
            Returns False if card not in deck."""
            if self.card_count == 0:
                print("There are no cards left.")
                return False
            elif specific_card in self.deck:
                if self.card_count == 1:
                    print(f"This is the last card in the deck.")
                self.remove_card(specific_card)
                return specific_card
            elif specific_card:
                print("Card is not in deck.")
                return False
            print("What card would you like?")
            return False

        def from_top(peek: bool = False) -> str:
            """Returns card from top of deck, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            if self.card_count == 0:
                print("There are no cards left.")
                return False
            drawn_card = self.deck[0]
            if self.card_count == 1:
                print(f"This is the last card in the deck.")
            if not peek:
                self.remove_card(drawn_card)
            return drawn_card

        def from_bottom(peek: bool = False) -> str:
            """Returns card from bottom of deck, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            if self.card_count == 0:
                print("There are no cards left.")
                return False
            drawn_card = self.deck[-1]
            if self.card_count == 1:
                print(f"This is the last card in the deck.")
            if not peek:
                self.remove_card(drawn_card)
            return drawn_card

        def from_random(peek: bool = False) -> str:
            """Returns card from random location in deck, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            if self.card_count == 0:
                print("There are no cards left.")
                return False
            drawn_card = choice(self.deck)
            if self.card_count == 1:
                print(f"This is the last card in the deck.")
            if not peek:
                self.deck.remove(drawn_card)
            return drawn_card

        def from_diamonds(peek: bool = False) -> str:
            """Returns card from random location in diamonds, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            if self.card_count == 0:
                print("There are no cards left.")
                return False
            drawn_card = choice(self.diamonds)
            if not peek:
                self.remove_card(drawn_card)
            return drawn_card

        def from_clubs(peek: bool = False) -> str:
            """Returns card from random location in clubs, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            drawn_card = choice(self.clubs)
            if not peek:
                self.remove_card(drawn_card)
            return drawn_card

        def from_hearts(peek: bool = False) -> str:
            """Returns card from random location in hearts, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            drawn_card = choice(self.hearts)
            if not peek:
                self.remove_card(drawn_card)
            return drawn_card

        def from_spades(peek: bool = False) -> str:
            """Returns card from random location in spades, updates self.deck and suits
            peek: Does not remove card if True (default False)"""
            drawn_card = choice(self.spades)
            if not peek:
                self.remove_card(drawn_card)
            return drawn_card

        from_where = {
            "TOP": from_top,
            "BOTTOM": from_bottom,
            "RANDOM": from_random,
            "DIAMONDS": from_diamonds,
            "CLUBS": from_clubs,
            "HEARTS": from_hearts,
            "SPADES": from_spades
        }

        if draw_type not in from_where:
            return specific_card(draw_type)
        return from_where[draw_type]()
