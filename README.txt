Card Games Project by patjcolon
This project is a portfolio project for my nucamp backend bootcamp.
I am trying to create card games. This is very much a WIP.

Info on /classes:
I will create a number of classes in order to play card games like Blackjack.
The classes folder will contain all of the classes necessary for playing these games.
Some classes excamples are "Deck_Cards" and "Hand".
More classes will be added like "Table" and "BlackjackTable(Table)"
I plan to have most of the game play out through the interaction of classes.

Info on /helper_modules:
I have created some helper functions to stylize the game or impact other functions and classes.
One such function is named "styl" which offers all basic text coloration and style options.
Another function is named "suitr" which turns card face strings like "AD" into stylized cards with
  their appropriate suits and colors on a white background.
I also have a function called "cashyr" which is what I will use for handing the player their money

Future Plans include:
- Add dealers and dealer hands
- Create Table class and subclasses like Blackjack_Table
- Create a way to get the value of the cards in a Hand
- Create simple AI for opponents that decides what they will do based on their hand and your hand
- Create a Card class that can be face up or face down, and is created on Draw events
  - It will be destroyed on toss or turn-in events
  - It will either be held directly within a Hand or:
  - It will be held within a book keeper object's dictionary and the index will be given to the hand,
      when card is deleted, the book keeper's reopened_slots list will now include the index/key for
      the destroyed card. new cards will pull index number from this list first, then overwrite
      deleted card values from these keys.
- Create a BookKeeper class to maintain/track certain objects like cards as well as other values.


Gameplay Plan:
Main room contains an ATM, a Casino Teller, and several Card Tables (Ex: BlackjackTable).
Player can withdraw cash from ATM, take cash to Casino Teller to exchange for chips, then play
  at a table and bet chips. After playing, the player can take chips to Casino Teller in exchange
  for cash, and then deposit the cash back into the ATM.
The ATM account logins and balances will be saved, so as of now, that is how the player will "logout"
Eventually the main room will include other casino and arcade games, many of which do not require
  chips to play. 
Games that do not require chips to play will isntead print out receipts which can be exchanged for
  cash/chips at a teller or deposited directly into the ATM. Big wins over x amount of $ will 
  require a cash-in-hand payout event.
