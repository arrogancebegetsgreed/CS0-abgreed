#Programmer Information: Caine Mayhew/arrogancebegetsgreed
#Program Info: prints 4 playing card of multiple values in different suits (#'s and cards in spades, hearts, diamonds, clubs)
#: Store and print 4 different pieces of ASCII Art
import random


num = random.randrange(0,100)
name = input("Please state your name dear customer.")
print("Wonderful to have you here,", name, ". A cool-toned bodiless voice greets you. Please comfortably seat yourself.")
print("You pull back a rickety wooden chair at an equally rickety wooden table. You observe the table")

cardback1: str = " ________"
cardback2: str = "|~~~~~~~~|"
cardback3: str = "|<><><><>|"
cardback4: str = "|********|"
cardback5: str = "|IIIIIIII|"
cardback6: str = "|<><><><>|"
cardback7: str = "|~~~~~~~~|"
cardback8: str = "|________|"

print(cardback1)
print(cardback2)
print(cardback3)
print(cardback4)
print(cardback5)
print(cardback6)
print(cardback7)
print(cardback8)



card1a: str = " ___________"
card1b: str = "|K        /\|"
card1c: str = "|         \/|"
card1d: str = "|  * * * *  |"
card1e: str = "|  \ ||| /  |"
card1f: str = "|/\ _____   |"
card1g: str = "|\/       K |"
card1h: str = "|___________|"


card2a: str= " ___________"
card2b: str="|J  _____ <3|"
card2c: str="|  |* * *|  |"
card2d: str="|  |  +  |  |"
card2e: str="|  |* * *|  |"
card2f: str="|  |_____|  |"
card2g: str="|<3       J |"
card2h: str="|___________|"



card3a: str= " ___________"
card3b: str="|A        ^ |"
card3c: str="|     /\    |"
card3d: str="|    (  )   |"
card3e: str="|    ----   |"
card3f: str="|           |"
card3g: str="|^         A|"
card3h: str="|___________|"

card4a: str= " ___________"
card4b: str="|8         *|"
card4c: str="|  *     *  |"
card4d: str="|     *     |"
card4e: str="|  *     *  |"
card4f: str="|     *     |"
card4g: str="|8 *     * *|"
card4h: str="|___________|"

print("There lays in front of you a singluar card, facedown on the table. It seems to whisper to you to turn it over and reveal its secrets. Flip the card Y/N?")
choice = input()

if choice == "Y" or choice == "Yes":
    if num < 10:
        print(card3a)
        print(card3b)
        print(card3c)
        print(card3d)
        print(card3e)
        print(card3f)
        print(card3g)
        print(card3h)
    elif num < 35:
        print(card4a)
        print(card4b)
        print(card4c)
        print(card4d)
        print(card4e)
        print(card4f)
        print(card4g)
        print(card4h)
    elif num < 65:
        print(card2a)
        print(card2b)
        print(card2c)
        print(card2d)
        print(card2e)
        print(card2f)
        print(card2g)
        print(card2h)
    elif num <100:
        print(card1a)
        print(card1b)
        print(card1c)
        print(card1d)
        print(card1e)
        print(card1f)
        print(card1g)
        print(card1h)
      
if choice == "N" or choice == "No":
      print("You cower away from the card, and the card reshuffles itself back into a deck you had not seen on the table before.")
      print("The clock sounds. Time is up; there is nothing left for you to do here.")
      quit
