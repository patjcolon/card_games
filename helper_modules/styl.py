"""
Contains text stylization features for text color, style, and background
styl for all text style/color/background needs and unstyl to go back to default
suitr is for use in card games. input list of cards ['AD', 'KH'] and it will return them as playing cards
By patjcolon
Last updated 6/28/2023
"""


def unstyl():
    """Resets text style, color, and highlight to default AKA unstyl!
    Currently same in practicality as the defaults of styl(). Will add more unstyl resets as features are added."""
    return "\033[0;39;49m"


def styl(color_choice: str = "Default", style_choice: str = "Reset", highlight_choice: str = "Default") -> str:
    """
    Stylizes text color, style, and highlight. Returns a stylization escape command string.
    Custom variable presets can be made as well as custom print functions
    color_choice and highlight_choice options: 'Default', 'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', Cyan', 'White'
    style_choice options: 'Reset', 'Bold', 'Dim', 'Italic', 'Underline', 'Blinking', 'Inverse', 'Invisible', 'Strikethrough'
    Style choices can be stacked. must be reset to clear. Default setting resets style.
    """
    text_colors = {"Default": ";39", "Black": ";30", "Red": ";31", "Green": ";32", "Yellow": ";33",
                   "Blue": ";34", "Magenta": ";35", "Cyan": ";36", "White": ";37", }

    text_styles = {"Reset": "\033[0", "Bold": "\033[1", "Dim": "\033[2", "Italic": "\033[3", "Underline": "\033[4",
                   "Blinking": "\033[5", "Inverse": "\033[7", "Invisible": "\033[8", "Strikethrough": "\033[9"}

    text_highlight = {"Default": ";49m", "Black": ";40m", "Red": ";41m", "Green": ";42m", "Yellow": ";43m",
                      "Blue": ";44m", "Magenta": "1;45m", "Cyan": ";46m", "White": ";47m", }

    if not color_choice.isalpha() or not style_choice.isalpha() or not highlight_choice.isalpha():
        return "\033[4;31m \nstylError: styl() argument cannot contain characters outside of the alphabet.\033[0;39m\n"
    color_code = text_colors[color_choice]
    style_code = text_styles[style_choice]
    highlight_code = text_highlight[highlight_choice]

    color_style_code = style_code + color_code + highlight_code
    return color_style_code


def suitr(cards: list = ["LiveD", "LaughC","CodeH"]):
    """suitr is a cardgame helper function that uses styl. it can take any card like 'AD' and turn it into
    a white background card with red/black values and suit"""

    # styl() presets for colorizing cards with a white background
    rst = unstyl()                             # rst:   Reset unstyl()
    reds = styl("Red", "Underline", "White")        # reds:  Red Suits      "Red Bold White"
    blks = styl("Black", "Underline", "White")      # blks:  Black Suits    "Black Bold White"
    # Unicode for suit symbols
    suits = {
    "D": "\u2666",
    "C": "\u2663",
    "H": "\u2665",
    "S": "\u2660",
    }
    
    # turning card input into a card
    card_art = ""
    for card in cards:
        card_value = card[:-1]
        card_suit = card[-1]
        card_color = reds if card_suit == 'D' or card_suit == 'H' else blks
        card_art += f"{card_color} {card_value} {suits[f'{card_suit}']} {rst}, "
    card_art = card_art[:-2]
    return f" {card_art}\033[0K"

def testr():
    # rst:      Resets text stylization
    rst = unstyl()
    # ysw:      "Red Bold White"
    reds = styl("Red", "Bold", "White")
    # ysw:      "Black Bold White"
    blks = styl("Black", "Bold", "White")


    # You can assign styl options to variables. Great if a certain style is repeatedly used throughout code.
    # shortcut variable examples:
    # rst:      Resets text stylization
    rst = unstyl()
    # _b_:      Underlined "Blue"
    _b_ = styl("Blue", "Underline")
    # ysw:      "Yellow Strikethrough White"
    ysw = styl("Yellow", "Strikethrough", "White")
    # err:      Error! Eye catching; utilizes style stacking
    err = styl("Default", "Bold") + styl("Red", "Underline")
    # hurt:     Looks like an alarming damage taken notification
    hurt = styl("White", "Bold", "Red")
    # pangramity:   Contains every letter in the alphabet for testing
    pangramity = "The quick brown fox jumps over the lazy dog."

    # You can use the styl() function or styl varibales with the print() function to create a custom print function.
    # custom print function examples:


    # error():  prints red, bold and underlined text
    def error(error_message: str = "Error!") -> str:
        print(err + error_message + rst)


    # damage(): prints numbers as HP lost using bold white text on a bright red background
    def damage(damage_amount: int) -> str:
        print(hurt + " -" + str(damage_amount) + " HP! " + rst)


    def test_line():
        print(f"{styl('Yellow','Bold')}-+=+=+=+=========================<{rst} {styl('Green')}Test {styl('Yellow','Bold')}>=========================+=+=+=+-{rst}")


    # Testing different style options using styl(), shortcut variables, and custom print function
    test_line()
    print(
        f"Testing out f-string {styl('Cyan', 'Blinking')} testing testing WHOAA!!!{styl()}")
    print(
        f"Let's see {ysw}if it works{rst} \033[1;31;42m with {_b_}variables{rst}. Wowza!!!\n\n\n")

    test_line()
    print(f"_b_:    {_b_}{pangramity}{rst}\n")
    print(f"ysw:    {ysw}{pangramity}{rst}\n")
    print(f"err:    {err}{pangramity}{rst}\n")
    print(f"hurt:   {hurt}{pangramity}{rst}\n\n\n")

    test_line()
    error("Error: Ruh-roh Raggy!\n")
    damage(100)

    # list of cards for testing suitr
    hearts = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]
    print(suitr(hearts))
    print(suitr())


def cashyr(cash_amount: float):
    """cashyr is designed to turn a float/int into its value as a set of bills and coins"""
    
    # cashyr() presets for colorzing dollars and coins
    dollars = styl("Black", "Underline", "Green")
    cents = styl("Black", "Underline", "White")
    
    if cash_amount // 100:
        hundreds = cash_amount // 100
        cash_amount -= hundreds * 100
    if cash_amount // 50:
        fiftys = cash_amount // 50
        cash_amount -= fiftys * 20
    if cash_amount // 20:
        twentys = cash_amount // 20
        cash_amount -= twentys * 20
    if cash_amount // 10:
        tens = cash_amount // 10
        cash_amount -= tens * 10
    if cash_amount // 5:
        fives = cash_amount // 5
        cash_amount -= fives * 5
    if cash_amount // 1:
        ones = cash_amount // 1
        cash_amount -= ones
    


# u2620 is skull ☠ w on b, u2622 is radiation ☢ b on y, 2728 is sparkles for win ✨ 2B50⭐
# \u00A2 is cents symbol ¢ b on w or b on , u0024 is dollar $ (dont need code...), 
# u23F4 for hourglass ⏳, u23f0 is alarmclock ⏰, 
# 270A-C is rock-paper-scissors ✊ ✋ ✌