import random
import math

suits = ["♥", "♦️", "♣️", "♠️"]

def randomSuit(name):
       name = (name + " " + str(random.choice(suits)))
       
class Card():
    def __init__(self, name, dealers):
        self.name = name;
        self.isAce = round(random.uniform(1, 52));
        self.value = round(random.uniform(1, 13));
        self.dealer = dealers

    def init(self):
        if self.isAce == 1 or self.isAce == 2 or self.isAce == 3 or self.isAce == 4:
            while True:
              aceChoice = input("[ACE!]: 11 or 1? >> ")
              x = int(aceChoice)
              if x == 11 or x == 1:
                print("updated to " + str(x))
                self.value = round(x)
                self.name = randomSuit("ACE")
                break
        if self.value == 11:
            self.name = randomSuit("J")
        elif self.value == 12:
            self.name = randomSuit("Q")
        elif self.value == 13:
            self.name = randomSuit("K")

card = Card("Card", False)
card2 = Card("Card", False)

dealercard = Card("Card", True)
dealercard2 = Card("Card", True)

card.init()
card2.init()

dealercard.init()
dealercard2.init()

print("Dealer's Hand: " + str(dealercard.value) + "\n" + str(dealercard.name) + "\n [UNKNOWN..]")
print("Your Hand: " + str(int(card.value) + int(card2.value)) + "\n" + str(card.name) + "\n" + str(card2.name) + "\n Hit or Stay?")

def checkResult(card: Card):
   if card.dealer == True:
      dealerTotal = dealercard.value + dealercard2.value
      dealerDis = math.dist(dealerTotal, 21)

      userTotal = card.value + card2.value
      userDis = math.dist(userTotal, 21)

      if userDis < dealerDis:
        print("I think this means u win \n dealer: " + str(dealerTotal) + "\n  yours:" + str(userTotal))
      elif userDis == dealerDis:
        print("draw lol \n dealer: " + str(dealerTotal) + "\n  yours:" + str(userTotal))
      elif userDis > dealerDis:
        print("I think this means u LOST \n dealer: " + str(dealerTotal) + "\n  yours:" + str(userTotal))
 
def hit():
   card3 = Card("Card", False)
   checkResult(card3)
   print("hit function")

def stay():
   dealercard3 = Card("Card", True)
   checkResult(dealercard3)
   print("stay function")

def ask():
    while True:
        user_input = input("Hit/Stay >> ")
        if user_input.lower() == "hit":
         hit()
         break
        elif user_input.lower() == "stay":
         stay()
         break
        else: user_input = input("Hit/Stay >> ")
ask()
