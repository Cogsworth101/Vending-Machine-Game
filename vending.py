from random import *
from time import *
from sys import *
from termcolor import *

myfile = open("FullVendingGame\save.txt", "r+")
filecontents = myfile.read()

# Vending machine

    ########
################
#              #
#              #
#              #
################
#     ####     #
#     ####     #
################

Sword = "Sword"
Axe = "Axe"
Common = "Common"
Uncommon = "Uncommon"
Rare = "Rare"
SuperRare = "Super Rare"
Randomrank = "Random"
Blue = "Blue"
Gray = "Gray"
Club = "Club"
Daggertag = "Dagger"
dogpetname = ""
Dog = "Dog"
Physical = "Physical"
Green = "Green"
rngsworddamage = randint(0, 300)

class Player:
    def __init__(self, Level, Experience, Attack, Maxhealth, CurrentHealth, helditem):
        self.Level = Level
        self.Experience = Experience
        self.Attack = Attack
        self.Maxhealth = Maxhealth
        self.CurrentHealth = CurrentHealth
        self.helditem = helditem

class Heal:
    def __init__(self, Name, Description, Level, Value, Rarity, Quantity):
        self.Name = Name
        self.Description = Description
        self.Level = Level
        self.Value = Value
        self.Rarity = Rarity
        self.Quantity = Quantity

class Weapon:
    def __init__(self, Name, Description, Level, Type, Damage, Rarity, Speed, Quantity):
        self.Name = Name
        self.Description = Description
        self.Level = Level
        self.Type = Type
        self.Damage = Damage
        self.Rarity = Rarity
        self.Speed = Speed
        self.Quantity = Quantity

class Creature:
    def __init__(self, Name, Description, Level, Type, Damage, MaxHealth, Experience, Item, CurrentHealth):
        self.Name = Name
        self.Description = Description
        self.Level = Level
        self.Type = Type
        self.Damage = Damage
        self.MaxHealth = MaxHealth
        self.Experience = Experience
        self.Item = Item
        self.CurrentHealth = CurrentHealth

class Pet:
    def __init__(self, Name, Nickname, Description, Level, Species, Maxhealth, Trait, CurrentHealth, Damage, Experience, Quantity, isHeld):
        self.Name = Name
        self.Nickname = Nickname
        self.Description = Description
        self.Level = Level
        self.Species = Species
        self.Maxhealth = Maxhealth
        self.Trait = Trait
        self.CurrentHealth = CurrentHealth
        self.Damage = Damage
        self.Experience = Experience
        self.Quantity = Quantity
        self.isHeld = isHeld

# Weapons
BossItem = "Boss Item"
Ultimate = "Ultimate"
BasicSword = Weapon("Basic Sword", "Pathetic little blade, probably couldn't cut human flesh if it tried.", 1, Sword, 10, Common, 3, 1)
GreaterSword = Weapon("Greater Sword", "It still couldn't cut flesh but it is a bit better now.", 2, Sword, 20, Common, 3.5, 0)
Dagger = Weapon("Dagger", "Small device, very quick with less attack power...", 2, Daggertag, 20, Uncommon, .1, 0)
RNGsword = Weapon("Random Sword", "Wow! What a gamer! Congrats on finding this!", 10000, Sword, rngsworddamage, Randomrank, randint(0, 5), 0)
GrayClub = Weapon("Gray Club", "You have this in the dream world alone...", 5, Club, 75, Rare, 10, 0)
BasicAxe = Weapon("Basic Axe", "It is a heavy old axe for cutting logs. It's dull but it gets the job done.", 1, Axe, 50, Common, 10, 0)
BlackClaw = Weapon("Black Claw", "The claw that takes so many...", 1000, BossItem, 1000000, Ultimate, 0, 0)

# Healing items
HealingPotionRank1 = Heal("Basic Healing Potion", "Heals almost nothing, 20 - 30", 1, randint(20, 30), Common, 1)
HealingPotionRank2 = Heal("Rank 2 Healing Potion", "Heals a bit more than Basic. 15 - 50", 2, randint(15, 50), Common, 0)
HealingPotionRank3 = Heal("Rank 3 Healing Potion", "Heals more consistently than rank 2. 30 - 40", 3, randint(30, 40), Uncommon, 0)

# Creatures
clawboss = "Claw Boss"
BlueCreature = Creature("Blue Creature", "It is a basic blue creature. Doesn't do much damage", 1, Blue, randint(1, 5), 20, 30, HealingPotionRank1, 20)
GrayGiant = Creature("Gray Giant", "Big Scary Dream Beast...", 5, Gray, 50, 100, 100, GrayClub, 100)
GreenCreature = Creature("Green Creature", "It is a green creature, a bit harder.", 3, Green, 20, 70, 200, BasicAxe, 70)
Claw = Creature("The Black Claw", "The claw that took his son...", 1000, clawboss, 1000000, 1500, 10000, BlackClaw, 1500)

# Pets
Doggy = Pet("Doggy", dogpetname, "Dependable little doggy!!! So CUTE!!!", 1, Dog, 150, Physical, 150, 50, 0, 0, False)

# Variables
EquippedWeapon = BasicSword
placeholder = "PlaceHolder"
CurrentEnemy = placeholder
done = 0
x = 0
playerhealth = 30
playerhealthmax = 30
playerlevel = 1
playerexperience = 0
playerattack = 0

# Player
Player1 = Player(playerlevel, playerexperience, playerattack, playerhealth, playerhealthmax, EquippedWeapon)

# THE TWO TS ARE PURPOSEFUL
def healpointt():
    healpoint = input("Do you want to heal? y or n: ")
    if healpoint == "y" or healpoint == "Y":
        typepot = input("What rank of potion do you want to use: ")
        if typepot == "1":
            if HealingPotionRank1.Quantity > 0:
                print("You used a healing potion")
                HealingPotionRank1.Quantity = HealingPotionRank1.Quantity - 1
                print("You have", HealingPotionRank1.Quantity, HealingPotionRank1.Name)
            elif HealingPotionRank1.Quantity == 0:
                print("You have none left...")
        elif typepot == "2":
            if HealingPotionRank2.Quantity > 0:
                print("You used a healing potion")
                HealingPotionRank2.Quantity = HealingPotionRank2.Quantity - 1
                print("You have", HealingPotionRank2.Quantity, HealingPotionRank2.Name)
            elif HealingPotionRank2.Quantity == 0:
                print("You have none left...")
    elif healpoint == "n" or healpoint == "N":
        print("Ok then, you have", HealingPotionRank1.Quantity, HealingPotionRank1.Name + ".", HealingPotionRank2.Quantity, HealingPotionRank2.Name + ".", HealingPotionRank3.Quantity, HealingPotionRank3.Name)

expincrease = 10

def ExperienceAdder(Curenemy):
    global expincrease
    print("You earned", Curenemy.Experience, "experience.")
    Player1.Experience = Player1.Experience + Curenemy.Experience
    input()
    while expincrease - Player1.Experience <= 0:
        if expincrease - Player1.Experience <= 0:
            Player1.Level = Player1.Level + 1
            expincrease = expincrease * 2
            Player1.Maxhealth = Player1.Maxhealth + 5
            Player1.CurrentHealth = Player1.Maxhealth
            Player1.Attack = Player1.Attack + 3
    print("Your current level is", Player1.Level)

def printbl(text):
    input("")
    cprint(text, "blue")

def printgr(text):
    input("")
    cprint(text, "green")

opt1 = input("What will you do? To look into the vending machine enter l. To stop playing enter d. ")

done1 = 0

def Maingame():
    global done
    global x
    global BlueCreature
    global Heal
    global HealingPotionRank1
    global __init__
    global playerhealth
    global EquippedWeapon
    global rngsworddamage
    global myfile
    global filecontents
    global done1
    myfile.seek(0)
    while done1 != 1:
        if myfile.read():
            print("You have a saved file...")
            input()
            continuequer = input("Restart or continue: ")
            if continuequer == "Restart":
                myfile.truncate(0)
                myfile.seek(0)
                done1 = 1
            elif continuequer == "continue" or continuequer == "Continue":
                print(myfile.readlines(-1))
            else:
                print("What?")

    print("""

     ________  ___       ________      ___    ___ ________      
    |\   __  \|\  \     |\   __  \    |\  \  /  /|\_____  \     
    \ \  \|\  \ \  \    \ \  \|\  \   \ \  \/  / ||____|\  \    
     \ \   ____\ \  \    \ \   __  \   \ \   / /      \ \__\   
      \ \  \___|\ \  \____\ \  \ \  \   \/  / /        \|__|   
       \ \__\    \ \_______\ \__\ \__\__/  / /           ____
        \|__|     \|_______|\|__|\|__|\___/ /           |\__/|

    """)
    print()
    input()
    print("You put your hand on the handle and fingers on the buttons")
    input()
    print("You see little figures moving in the machine")
    input()
    print("You feel a tugging sensation in the small of your back and you fly into the vending machine.")
    input()
    print("Shrinking as you go in.")
    input()
    print(".")
    input()
    print(".")
    input()
    print(".")
    input()
    print("You hear a voice.")
    input()
    printbl("Get up kid!")
    print("You feel that same tugging sensation, but this time you aren't shrinking.")
    input()
    print("You are being pulled up onto a cart by a middle aged man.")
    input()
    print("He is bald and has worry lines.")
    input()
    print("He has a blue scar over his eye.")
    input()
    print("He looks vaguely familiar...")
    input()
    printgr("Do I know you?")
    printbl("Nope... Nobody does. There is nobody left...")
    printgr("What do you mean?")
    printbl("They've all been taken up... By the black claw...")
    printgr("What's that? Black claw...? Well alright then, I don't really believe you yet...")
    printbl("Well you'd better start...")
    printbl("I'll be your only guide...")
    printbl("It's a cruel world out there bud...")
    printgr("Ok that's nice but do you got fooooood?")
    printgr("I'm so hungry! Haven't eaten since yesterday!!!")
    printbl("*Mumbles* Why did I pick this idiot up...")
    printgr("I heard that!!")
    printgr("You wake with a start...")
    printgr("Ahhhhhh when did I go to sleep?")
    printbl("You are fine.")
    printbl("Calm down. You are scaring the horses.")
    printgr("Alright sorry, can I sleep more?")
    printbl("Sure! I'll just eat alone!")
    printgr("Oh no it's alright I'm not tired.")
    printbl("*Chuckles*")
    input()
    print("*Snoring*")
    input()
    printbl("WAKE UP BOY!")
    printgr("What....? I'm tir-")
    printbl("YOU HAVE A SWORD!! USE IT AGAINST THIS BEAST.")
    print("You are being attacked by a blue creature.")
    CurrentEnemy = BlueCreature
    while done != 1:
        fightchoice = input("Fight or Items: ")
        if fightchoice == "Fight" or fightchoice == "f" or fightchoice == "F" or fightchoice == "fight":

            rngsworddamage = randint(0, 300)
            input("You attacked the creature...")
            print("You did", (EquippedWeapon.Damage + playerattack), "damage")
            input()
            CurrentEnemy.CurrentHealth = CurrentEnemy.CurrentHealth - EquippedWeapon.Damage
            if CurrentEnemy.CurrentHealth <= 0:
                print("The enemy is dead.")
                input()
                print("You recieved", CurrentEnemy.Item.Name, "and", CurrentEnemy.Experience, "experience.")
                CurrentEnemy.Item.Quantity = CurrentEnemy.Item.Quantity + 1
                input()
                print("You have", CurrentEnemy.Item.Quantity, CurrentEnemy.Item.Name)
                input()
                ExperienceAdder(CurrentEnemy)
                done = 1
            else:
                print("The enemy has", CurrentEnemy.CurrentHealth, "health")
                input()
                print("The enemy attacked")
                input()
                playerhealth = playerhealth - CurrentEnemy.Damage
                print("The enemy did", CurrentEnemy.Damage, "damage")
                if playerhealth <= 0:
                    playerhealth = 0
                    print("You are dead...")
                    Maingame()
                else:
                    playerhealth = playerhealth
                    print("Your health is", playerhealth)
        elif fightchoice == "Item" or fightchoice == "I" or fightchoice == "item" or fightchoice == "i":
            print("Looks like you would like to heal!")
            input()
            healpointt()
            x = x + 1
            if x == 10 and RNGsword.Quantity == 0:
                print("Congrats, you unlocked the secret code...")
                input("You obtained 1 RNG sword")
                print("                                ")
                print("                                ")
                print("      ₪₪₪₪§|(ΞΞΞΞΞΞΞΞΞΞΞΞ>      ")
                print("                                ")
                print("                                ")
                myfile.write("Rngsword")
                RNGsword.Quantity = RNGsword.Quantity + 1
            elif x == 11:
                print("You equipped the weapon")
                EquippedWeapon = RNGsword
            else:
                print("Get back to the battle!")
        elif fightchoice == "0" and RNGsword.Quantity == 0:
            print("Congrats, you unlocked the secret code...")
            input("You obtained 1 RNG sword")
            print("                                ")
            print("                                ")
            print("      ₪₪₪₪§|(ΞΞΞΞΞΞΞΞΞΞΞΞ>      ")
            print("                                ")
            print("                                ")
            myfile.write("Rngsword")
            RNGsword.Quantity = RNGsword.Quantity + 1
            print("You equipped the weapon")
            EquippedWeapon = RNGsword
        else:
            printbl("What are ya gonna do?!")
    print("SAVING...")
    myfile.write("\n")
    myfile.write("First battle")
    input()
    printbl("Good job!")
    printgr("???")
    printbl("There are monsters in this world...")
    printbl("It is dangerous...")
    printgr("What's a health potion?")
    printbl("If a competent enemy attacks, it will do you damage.")
    printgr("Huh. Ok. Will it hurt?")
    printbl("Of course it will hurt.")
    printgr("Do you need a health potion for your eye?")
    printbl("Whats wrong with my eye?")
    printgr("You have a blue scar over it...?")
    printbl("Oh... Right... Sure I'll take it...")
    input()
    print("You gave Old Man 1 health potion")
    HealingPotionRank1.Quantity = HealingPotionRank1.Quantity - 1
    input()
    print("You have", HealingPotionRank1.Quantity, "healing potions")
    input()
    printbl("Ok so to use a healing potion, you wait for a healpoint.")
    printbl("You'll see a healpoint now.")
    healpoint = input("Heal (y, n): ")
    if healpoint == "y" or healpoint == "Y":
        if HealingPotionRank1.Quantity > 0:
            print("You used a healing potion")
            HealingPotionRank1.Quantity = HealingPotionRank1.Quantity - 1
            print("You have", HealingPotionRank1.Quantity, HealingPotionRank1.Name)
        elif HealingPotionRank1.Quantity == 0:
            print("You have none left...")
    elif healpoint == "n" or healpoint == "N":
        printbl("Why don't you heal?")
        printgr("I don't want to.")
    if RNGsword.Quantity == 1:
        printbl("You are a smart person... You got the sword...")
        printbl("Do you want to see the legendary description of the sword...?")
        descrng = input("y or n: ")
        if descrng == "y" or descrng == "Y":
            print(RNGsword.Description)
        else:
            print("Loser...")
    else:
        o = 2
        o + 2
    printbl("Ok now we are done with formalities.")
    printgr("When are we gonna stop moving?")
    printbl("Have patience...")
    printgr("Ok...")
    print("You have fallen asleep")
    input()
    print("You are concious in your dream...")
    input()
    print("You see a gray giant...")
    input()
    print("He looks at you...")
    input()
    print("You scream but hold your ground")
    input()
    print("You.")
    sleep(.3)
    print("Can't.")
    sleep(.3)
    print("Move.")
    input()
    print("You scream again...")
    input()
    print("You go into battle...")
    input() 
    done = 0
    x = 0
    CurrentEnemy = GrayGiant
    while done != 1:
        fightchoice = input("Fight or Items: ")
        if fightchoice == "Fight" or fightchoice == "f" or fightchoice == "F" or fightchoice == "fight":
            if EquippedWeapon.Name == "Random Sword":
                EquippedWeapon.Damage = randint(0, 300)
            else:
                EquippedWeapon = EquippedWeapon
            input("You attacked the creature...")
            print("You did", EquippedWeapon.Damage, "damage")
            input()
            CurrentEnemy.CurrentHealth = CurrentEnemy.CurrentHealth - EquippedWeapon.Damage
            if CurrentEnemy.CurrentHealth <= 0:
                print("The enemy is dead.")
                input()
                print("You recieved", CurrentEnemy.Item.Name)
                CurrentEnemy.Item.Quantity = CurrentEnemy.Item.Quantity + 1
                input()
                print("You have", CurrentEnemy.Item.Quantity, CurrentEnemy.Item.Name)
                input()
                ExperienceAdder(CurrentEnemy)
                print("You wake with a start")
                done = 1
            else:
                print("The enemy has", CurrentEnemy.CurrentHealth, "health")
                input()
                if x != 3:
                    print("The enemy is charging...")
                    x = x + 1
                elif x == 3:
                    print("The enemy attacks!")
                    input()
                    print("The enemy does", CurrentEnemy.Damage, "damage.")
                    playerhealth = playerhealth - CurrentEnemy.Damage
                    if playerhealth <= 0:
                        playerhealth = 0
                        print("You wake with a start...")
                        done = 1
                    else:
                        print("You have", playerhealth, "health")
        elif fightchoice == "Item" or fightchoice == "I" or fightchoice == "item" or fightchoice == "i":
            print("Looks like you would like to heal!")
            input()
            healpointt()
    printbl("WHAT?!?!?")
    printgr("What?")
    printbl("What?")
    printgr("Why'd you say what")
    printbl("You were screaming...")
    if playerhealth == 0:
        printgr("Oh... Yeah I just died in my dream...")
        Player1.CurrentHealth = Player1.Maxhealth
    else:
        printgr("I just killed something in my dream...")
        Player1.CurrentHealth = Player1.Maxhealth
    printbl("Hmmmm...")
    printbl("That's not great...")
    printbl("*Mumbles* guess he's a shadow fighter then... *Mumbles*")
    printgr("What?")
    printbl("You are a shadow fighter, you can fight monsters on the dream plane...")
    printgr("Oh yeah I saw a gray monster...")
    printgr("It was huge... I couldn't move, only attack it...")
    printgr("It was a giant... It had a huge gray club...")
    printbl("Mmmmmmmm... interesting...")
    printbl("My son had that ability...")
    printgr("What happened?")
    printbl("He was taken... *Head turns*")
    printbl("*Tears form in his eyes...*")
    printgr("Oh.....")
    printgr("I'm sorry...")
    printgr("I'll stop that claw... Just tell me what to do...")
    printbl("You can't...")
    printbl("Eventually i'll be taken... I've been hiding out...")
    print("Suddenly you remember a green tinted image... Two adults standing next to you...")
    input()
    print("A little girl, you feel like you are trying to grasp an invisible string...")
    input()

if opt1 == "l":
    print("You look into the vending machine")
    input()
    Maingame()
elif opt1 == "d":
    print("Too bad")
    input()
    Maingame()
