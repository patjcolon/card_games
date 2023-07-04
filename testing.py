"""For testing purposes only"""
from os import system

from classes import *
from helper_modules.styl import styl, suitr, testr
from helper_modules.typr import typr
from main import get_user_input, hide_unhide

def cashyr(cash_amount: float = 0, words_before_payout: str = "Here is your payout: "):
    """cashyr is designed to turn a float/int into its value as a set of bills and coins"""

    # cashyr() presets for colorzing dollars and coins
    cashz = styl("Black", "Bold", "Green")
    coinz = styl("Black", "Bold", "White")

    # early exception handling
    try:
        cash_amount = float(cash_amount)
    except ValueError:
        typr(f"I can't pay you '{cash_amount}'... That's not even a number!")
        return False
    if not cash_amount:
        typr(f"Cool. Here's your {coinz}(0\u00A2){rst}! You gonna keep wasting my time?", "slow")
        return False



    unpaid_dollars = int(cash_amount)
    unpaid_cents = int((cash_amount - unpaid_dollars + 0.000001) * 100)

    def get_bills(unpaid_dollars):
        cashyr_payout = ""
        hundreds = 0
        fiftys = 0
        twentys = 0
        tens = 0
        fives = 0
        ones = 0
        total_dollars = []
        
        if unpaid_dollars // 100:
            hundreds = unpaid_dollars // 100
            unpaid_dollars -= hundreds * 100
        if unpaid_dollars // 50:
            fiftys = unpaid_dollars // 50
            unpaid_dollars -= fiftys * 50
        if unpaid_dollars // 20:
            twentys = unpaid_dollars // 20
            unpaid_dollars -= twentys * 20
        if unpaid_dollars // 10:
            tens = unpaid_dollars // 10
            unpaid_dollars -= tens * 10
        if unpaid_dollars // 5:
            fives = unpaid_dollars // 5
            unpaid_dollars -= fives * 5
        if unpaid_dollars // 1:
            ones = unpaid_dollars // 1
            unpaid_dollars -= ones
        total_dollars = [hundreds, fiftys, twentys, tens, fives, ones]
        bills_out = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            1: 0,
        }
        bill_type_counter = 0
        for bill in bills_out:
            bills_out[bill] = total_dollars[bill_type_counter]
            bill_type_counter += 1

        for dollar_amount in bills_out:
            number_of_bills = bills_out[dollar_amount]
            while number_of_bills:
                cashyr_payout += (f"{cashz}[" + f"${dollar_amount}".center(4, " ")) + f"]{rst}, "
                number_of_bills -= 1
        cashyr_payout = cashyr_payout[:-2]
        typr(f"Here is your cash: {cashyr_payout}\033[0K")
    
    def get_coins(unpaid_cents, as_change: bool = False):
        cashyr_payout = ""
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        total_coins = []

        if unpaid_cents // 25:
            quarters = unpaid_cents // 25
            unpaid_cents -= quarters * 25
        if unpaid_cents // 10:
            dimes = unpaid_cents // 10
            unpaid_cents -= dimes * 10
        if unpaid_cents // 5:
            nickels = unpaid_cents // 5
            unpaid_cents -= nickels * 5
        if unpaid_cents // 1:
            pennies = unpaid_cents // 1
            unpaid_cents -= pennies * 1
        
        total_coins = [quarters, dimes, nickels, pennies]
        coins_out = {
            25: 0,
            10: 0,
            5: 0,
            1: 0
        }

        coin_type_counter = 0
        for coin in coins_out:
            coins_out[coin] = total_coins[coin_type_counter]
            coin_type_counter += 1

        for coin_amount in coins_out:
            number_of_coins = coins_out[coin_amount]
            while number_of_coins:
                cashyr_payout += (f"{coinz}(" + f"{coin_amount}\u00A2".center(3, " ")) + f"){rst}, "
                number_of_coins -= 1
        cashyr_payout = cashyr_payout[:-2]
        
        # if the user received cash first (entry was at least $1.01)
        if as_change:
            # checking if it is only 1 penny
            if sum(total_coins) == 1:
                return typr(f"And here is your lucky penny: {cashyr_payout}\033[0K")
            return typr(f"And here is your change: {cashyr_payout}\033[0K")
        
        # if the user user only withdrew coins:
        # checking if it is only 1 penny
        if sum(total_coins) == 1:
                return typr(f"Welp, here is your unlucky penny: {cashyr_payout}\033[0K")
        return typr(f"Here are your coins: {cashyr_payout}\033[0K")


    if cash_amount == unpaid_dollars:
        get_bills(unpaid_dollars)
        print()
        return True
    if cash_amount < 1:
        get_coins(unpaid_cents)
        print()
        return True
    get_bills(unpaid_dollars)
    get_coins(unpaid_cents, True)
    print()
    return True
    
# if cash only get_bills()
# if coins only get_coiuns() "Here's your coins: "
# if cash and coins getbills, getcoins - "And here's your change: "

def play_cashr():
    system('cls')
    hide_unhide()
    typr("Welcome to cashyr! ", "slow", False)
    while True:
        typr("How much would you like to witdraw?", "slow")
        player_payout = get_user_input("$")
        if not cashyr(player_payout):
            continue
        typr(f"That was ${float(player_payout):.2f}. Would you like to withdraw some more?")
        while True:
            typr("'y': replay, 'n': quit")
            replay_cashr = get_user_input().lower()
            if replay_cashr == 'y':
                break
            if replay_cashr == 'n':
                return
            
play_cashr()
typr("Thanks for playing!")



# \u00A2 is cents symbol ¢ b on w or b on , u0024 is dollar $ (dont need code...)