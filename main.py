import random

class Card():
    def __init__(self, name):
        self.name = name;
        self.isAce = round(random.uniform(1, 52));
        self.value = round(random.uniform(1, 10));
    def checkForAce(self):
        if self.isAce == 1 or self.isAce == 2:
            while True:
              aceChoice = input("[ACE!]: 11 or 1? >> ")
              x = int(aceChoice)
              if x == 11 or x == 1:
                print("updated to " + str(x))
                self.value = round(x)
                break

card = Card("Card")
card2 = Card("Card")

dealercard = Card("Card")
dealercard2 = Card("Card")

card.checkForAce()
card2.checkForAce()

dealercard.checkForAce()
dealercard2.checkForAce()

print("Dealer has " + str(dealercard.value) + ", UNKNOWN")
print("Hit or stay? " + str(card.value) + ", " +  str(card2.value) + " : " + card.value + card2.value)

user_input = input(">> ")

def checkResult():
   pass

def hit():
   print("hit function")

def stay():
   print("stay function")

def ask():
    while True:
        if user_input.lower() == "hit":
         print("Player hit")
         hit()
         break
        elif user_input.lower == "stay":
         print("Player pass")
         stay()
         break
        else: print("Hit or stay..")

ask()
