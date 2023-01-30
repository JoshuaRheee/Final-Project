import time
import random

speed = 1

"""
Class Stat Setup
Stats are listed in an array as HP, MP, Defense, Magic Defense, Attack, Magic Attack, Health Regen, and Critical Srike, Experience Gain, and Dodge Chance
"""

Class = "" #Class will later be assigned via user  input
Wizard = [80, 120, 8, 12, 6, 12, 2, 6, 0, 100, 0]
Paladin = [120, 100, 12, 8, 10, 8, 2, 4, 0, 100, 0]
Berserker = [110, 80, 8, 8, 12, 6, 2, 6, 5, 100, 0]
Hunter = [90, 80, 8, 8, 12, 6, 2, 6, 5, 100, 0]
stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0]
moveset = []
itemcheck = []

#moves

StaffBash = [
    "StaffBash", "Deals low physical damage to the enemy.", "Atk", .8, 1
]
Fireball = [
    "Fireball", "Deals high magical damage to the enemy.", "Matk", 1.5, 1
]
PreciseStrike = [
    "PreciseStrike", "Deals medium physical damage to the enemy.", "Atk", 1, 1
]
Blessing = [
    "Blessing", "Deals medium magical damage to the enemy.", "Matk", 1.5, 1
]
EnragedStrike = [
    "EnragedStrike", "Deals medium physical damage to the enemy.", "Atk", 1.2,
    1
]
FlurryStrike = [
    "FLurryStrike", "Deals low physical damage repeatedly to the enemy.",
    "Atk", .4, 6
]
PreciseShot = [
    "PreciseStrike", "Deals high physical damage to the enemy.", "Atk", .8, 1
]
FlurryShots = [
    "FlurryShots", "Deals low physical damage repeatedly to the enemy.", "Atk",
    .4, 4
]

#movesets

Wizardmoves = [StaffBash, Fireball]
Paladinmoves = [PreciseStrike, Blessing]
Berserkermoves = [EnragedStrike, FlurryStrike]
Huntermoves = [PreciseShot, FlurryShots]

statnames = [
    "Hp", "Mp", "Def", "Mdef", "Atk", "MAtk", "HpRegen", "MpRegen", "Crit",
    "Xpgain", "Dodge"
]
Hp = stats[0]
Mp = stats[1]
Def = stats[2]
Mdef = stats[3]
Atk = stats[4]
MAtk = stats[5]
HpRegen = stats[6]
MpRegen = stats[7]
Crit = stats[8]
Xpgain = stats[9]
Dodge = stats[10]

#Leveling
level = 1
levelreq = 30
xp = 0


def levelup():
    for i in range(len(stats)):
        stats[i] += 1


# Common Items
Chainmail = ["Chainmail", "Gives 4 Def", "Def", 4]
Cloak = ["Cloak", "Gives 4 Mdef", "Mdef", 4]
CrookedSword = ["CrookedSword", "Gives 11 Attack", "Atk", 11]
FrugalStaff = ["FrugalStaff", "Gives 10 MAtk", "MAtk", 10]
Bandages = ["Bandages", "Gives 3 HpRegen", "HpRegen", 3]
BookofKnowledge = [
    "BookofKnowledge", "Gives 150% increase in xpgain", "Xpgain", 150
]
HealthInfusion = ["HealthInfusion", "Gives 40 hp", "Hp", 40]
HandofHatred = ["HandofHatred", "Gives 5 Crit chance", "Crit", 5]

# Uncommon Items
ObsidianScroll = ["ObsidianScroll", "Gives 25 MAtk", "MAtk", 25]
MantleofMalady = ["MantleofMalady", "Gives 10 Mdef", "Mdef", 10]
PrimalNecklace = ["PrimalNecklace", "Gives 10 Crit chance", "Crit", 11]
GemofOrigins = ["GemofOrigins", "Gives 8 HpRegen", "HpRegen", 8]
ValorAmulet = ["ValorAmulet", "Gives 100 Hp", "Hp", 100]
SpikedClub = ["SpikedClub", "Gives 25 Atk", "Atk", 25]
Catalyst = ["Catalyst", "Gives 300% Xpgain", "Xpgain", 300]
Shield = ["Shield", "Gives 10 Def", "Def", 10]

#Rare Items
RuneofRage = ["RuneofRage", "Gives 15 Crit chance", "Crit", 15]
FountainofLuminosity = [
    "FountainofLuminosity", "Gives 12 HpRegen", "HpRegen", 12
]
SpellboundHorn = ["SpellboundHorn", "Gives 40 MAtk", "MAtk", 40]
ManaInfusion = ["ManaInfusion", "Gives 200 Hp", "Hp", 200]
Exilesandals = ["Exilesandals", "Gives 20 Mdef", "Mdef", 20]
Spikedgloves = ["Spikedgloves", "Gives 40 Atk", "Atk", 40]
GuardVesture = ["GuardVesture", "Gives 20 Def", "Def", 20]
CrownofInsight = ["CrownofInsight", "Gives 500% Xpgain", "Xpgain", 500]

# special interaction items

#Epic Items
InsanityHorn = ["InsanityHorn", "Gives 30 Crit", "Crit", 30]
TomeofDemolition = ["TomeofDemolition", "Gives 150 MAtk", "MAtk", 150]
AlchemyHand = ["AlchemyHand", "Gives 20 HpRegen", "HpRegen", 20]
PlateofCourage = ["PlateofCourage", "Gives 150 Atk", "Atk", 150]
CubeofResistance = ["CubeofResistance", "Gives 80 Mdef", "Mdef", 80]
DivinityGauntlet = ["DivinityGauntlet", "Gives 80 Def", "Def", 80]
TextsofSight = ["TextsofSight", "Gives 1000% Xpgain", "Xpgain", 1000]
VitalityFountain = ["VitalityFountain", "Gives 300 Hp", "Hp", 300]

# special interaction items

#Legendary Items
InscriptionofStorms = ["InscriptionofStorms", "Gives 500 MAtk", "MAtk", 500]
HeroesChalice = ["HeroesChalice", "Gives 100 HpRegen", "HpRegen", 1000]
GrimoireofWishes = ["GrimoireofWishes", "Gives 500 Atk", "Atk", 500]
DoorofDreams = ["DoorofDreams", "Gives 20000 Xpgain", "Xpgain", 20000]
ImmortalCirclet = ["ImmortalCirclet", "Gives 6666 Hp", "Hp", 6666]
FortitudeMask = ["FortitudeMask", "Gives 500 Def", "Def", 500]
RuneoftheCosmos = ["RuneoftheCosmos", "Gives 80 Crit chance", "Crit", 80]
StormTiara = ["StormTiara", "Gives 500 Mdef", "Mdef", 500]

# special interaction items

#Item Rarity Sorting
common = [
    Chainmail, Cloak, CrookedSword, FrugalStaff, Bandages, BookofKnowledge,
    HealthInfusion, HandofHatred
]

uncommon = [
    ObsidianScroll, MantleofMalady, PrimalNecklace, GemofOrigins, ValorAmulet,
    SpikedClub, Catalyst, Shield
]

rare = [
    RuneofRage, FountainofLuminosity, SpellboundHorn, ManaInfusion,
    Exilesandals, Spikedgloves, GuardVesture, CrownofInsight
]

epic = [
    InsanityHorn, TomeofDemolition, AlchemyHand, PlateofCourage,
    CubeofResistance, DivinityGauntlet, TextsofSight, VitalityFountain
]

legendary = [
    InscriptionofStorms, HeroesChalice, GrimoireofWishes, DoorofDreams,
    ImmortalCirclet, FortitudeMask, RuneoftheCosmos, StormTiara
]


def ShowStats():
    print("\nHp = " + str(stats[0]) + "\n")
    print("Def = " + str(stats[2]) + "\n")
    print("Mdef = " + str(stats[3]) + "\n")
    print("Atk = " + str(stats[4]) + "\n")
    print("MAtk = " + str(stats[5]) + "\n")
    print("HpRegen = " + str(stats[6]) + "\n")
    print("MpRegen = " + str(stats[7]) + "\n")
    print("Crit = " + str(stats[8]) + "%\n")
    print("Xp Gain = " + str(stats[9]) + "%\n")

    time.sleep(speed * 3)


def DescribeMoves():
    time.sleep(speed)
    print("\n" + moveset[0][0] + ": " + moveset[0][1])
    print("\n" + moveset[1][0] + ": " + moveset[1][1])


def ShowMoveset():
    print("Your moves are: \n")
    print("1: " + moveset[0][0])
    print("\n\n2: " + moveset[1][0])


def getItem():
    rarity = ""
    randVal = random.randrange(10000)
    rand2 = 0
    if randVal > 9995:
        rarity = (" Legendary")
        itemStatus = legendary
        rand2 = random.randrange(len(legendary))
    elif randVal > 9494:
        rarity = (" Epic")
        itemStatus = epic
        rand2 = random.randrange(len(epic))
    elif randVal > 8494:
        rarity = (" Rare")
        itemStatus = rare
        rand2 = random.randrange(len(rare))
    elif randVal > 5494:
        rarity = ("n Uncommon")
        itemStatus = uncommon
        rand2 = random.randrange(len(uncommon))
    else:
        rarity = (" Common")
        itemStatus = common
        rand2 = random.randrange(len(common))
    print(
        "\nYou rummage through the remains of the enemy. Within it you find a"
        + rarity + " item called " + itemStatus[rand2][0] +
        ". It's description is: \n\n" + itemStatus[rand2][1])
    item1 = 0
    itemGet = input(
        "\nGet item? (For yes type Yes or yes. For no type anything else)\n")
    if itemGet == "Y" or itemGet == "y" or itemGet == "Yes" or itemGet == "yes":
        item1 += 1

    if item1 > 0:
        print("\nYou pick up and equip the item")
        temp = statnames.index(itemStatus[rand2][2])
        stats[temp] += itemStatus[rand2][3]
        ShowStats()
    else:
        print("\nYou choose to leave the item")

def speedset():
    speedset = input("""Select the speed you would like to experience the game:
1. Normal           2. Slow             3. Fast             4. ZOOM ZOOM\n""")
    newloopmade = 1
    while newloopmade > 0:
        if speedset == "1" or speedset == "2" or speedset == "3" or speedset == "4":
            newloopmade -= 1
        else:
            print("Please select a valid option(1,2,3, or 4)")
            speedset = input("""Select the speed you would like to experience the game:
1. Normal           2. Slow             3. Fast             4. ZOOM ZOOM\n""")
    if speedset == "1":
        time.sleep(speed)
        print("You have selected normal speed\nThe game will start now")
        time.sleep(speed*2)
        return (1)
    if speedset == "2":
        time.sleep(speed)
        print("You have selected slow speed\nThe game will start now")
        time.sleep(speed*2)
        return (2)
    if speedset == "3":
        time.sleep(speed)
        print("You have selected fast speed\nThe game will start now")
        time.sleep(speed*2)
        return(.5)
    if speedset == "4":
        time.sleep(speed)
        print("You have selected ZOOM ZOOM speed\nThe game will start now")
        time.sleep(speed*2)
        return(.25)

### Introduction ###
def Intro():
    intro = input(
        """The last thing you remember is entering a portal to another dimension. You wake up groggy facing an old man seemingly full of wisdom. He asks you, \"Are you willing to take this journey?\"\n"""
    )
    if intro == "yes" or intro == "Yes":
        print("\"Good!\"")
        time.sleep(speed)
        print("\"Off you go now.\"")

        return classChoose()
    else:
        print(
            "\"I see. Well only death awaits.\" The old man proceeds to stab you."
        )
        exit()


### Classes###
def classChoose():
    loopcheck = 1

    print("""
  You wake up suddenly in an armorshop to a man yelling at you. \"What apparel do you need?! HelloOOoooo. Are you going to answer me?\"
  """)
    time.sleep(speed * 3)
    print(""""
  Quick! Choose a class so you know what gear to buy!
  """)
    time.sleep(speed * 2)
    print("""
  Choose a class from the following:
  Wizard:
  A class which trades off high magic damage for low physical and defensive stats.
  Stats:
  Hp: 80
  MP: 120
  Def: 8
  Mdef: 12
  Atk: 6
  MAtk: 12
  Hp Regen: 2
  Crit: 0
  """)
    time.sleep(speed * 2)
    print("""
  Paladin:
  A warrior guided by the light bringing blessings upon himself. He has tankier stats with a self heal and damage buff.
  Hp: 120
  MP: 100
  Def: 12
  Mdef: 8
  Atk: 10
  MAtk: 6
  Hp Regen: 2
  Crit: 0
  """)
    time.sleep(speed * 2)
    print("""
  Berserker:
  A warrior with hell bent rage seeking revenge. His high atk and atk speed allows him to attack his enemies quickly.
  Hp: 110
  MP: 80
  Def: 8
  Mdef:8
  Atk: 12
  MAtk: 6
  Hp Regen: 2
  Crit: 5
  """)
    time.sleep(speed * 2)
    print("""
  Hunter:
  A ranged high physical dps archer. High physical dps and mid tier defenses.
  Hp: 90
  MP: 80
  Def: 8
  Mdef: 8
  Atk: 12
  MAtk: 6
  Hp Regen: 2
  Crit: 5
  """)
    while loopcheck < 2:
        ask = input("Pick a class by typing out the name:\n")
        if ask == "Wizard" or ask == "wizard":
            time.sleep(speed)
            print("You have chosen the Wizard! Your stats are: \n")
            time.sleep(speed)
            return (Wizard, Wizardmoves)

        if ask == "Paladin" or ask == "paladin":
            time.sleep(speed)
            print("You have chosen the Paladin! Your stats are:\n")
            time.sleep(speed)
            return (Paladin, Paladinmoves)

        if ask == "Berserker" or ask == "berserker":
            time.sleep(speed)
            print("You have chosen the Berserker! Your stats are:\n")
            time.sleep(speed)
            return (Berserker, Berserkermoves)

        if ask == "Hunter" or ask == "Hunter":
            time.sleep(speed)
            print("You have chosen the Hunter! Your stats are:\n")
            time.sleep(speed)
            return (Hunter, Huntermoves)


#format
#    [Hp,Atk,Matk,Def,Mdef,Xp,chance]

#mobs
goblin = [25, 16, 8, 3, 3, 20, 5]
wolf = [40, 20, 12, 4, 4, 30, 30]
ogre = [60, 26, 18, 8, 8, 40, 15]
thief = [80, 28, 28, 10, 10, 80, 60]
gremlin = [100, 36, 30, 16, 8, 120, 45]
orc = [120, 24, 30, 20, 15, 150, 45]
skeleton = [150, 60, 50, 15, 15, 220, 50]
giant = [180, 70, 60, 35, 25, 250, 30]
vampire = [200, 84, 90, 25, 45, 300, 70]
witch = [220, 60, 100, 35, 45, 500, 70]
phantom = [250, 60, 140, 65, 25, 700, 85]
wereman = [400, 140, 140, 5, 5, 1200, 50]
mimics = [50, 10, 5, 5, 5, 40, 50]

#bosses
LargeWolf = [60, 30, 30, 5, 5, 100, 40]
ChiefThief = [100, 50, 50, 10, 10, 200, 40]
MutantOrc = [150, 80, 80, 25, 15, 300, 40]
Cyclops = [200, 150, 150, 25, 35, 400, 40]
Dracula = [250, 160, 240, 45, 45, 500, 40]
CrimsonMary = [500, 200, 300, 60, 60, 1500, 40]
Xayrraiss = [1000, 300, 300, 100, 100, 2000, 50]

#Floors
floor1 = [goblin, wolf, LargeWolf]
floor2 = [ogre, thief, ChiefThief]
floor3 = [gremlin, orc, MutantOrc]
floor4 = [skeleton, giant, Cyclops]
floor5 = [vampire, witch, Dracula]
floor6 = [phantom, wereman, CrimsonMary]
floor7 = [Xayrraiss]


def damage(atk, matk, crit, type, multiplier, edef, emdef, ehp, strikes,
           accumulation, basehp):
    if type == "Atk":
        dmgtype = atk
        edeftype = edef
    if type == "Matk":
        dmgtype = matk
        edeftype = emdef

    willcrit = random.randrange(100)
    if willcrit <= crit:
        multiplier * 2

    dealt = round(dmgtype * multiplier - edeftype, 1)

    b = accumulation
    c = ehp

    for i in range(strikes):
        time.sleep(speed / 2)
        willcrit = random.randrange(100)
        if willcrit <= crit:
            multiplier = multiplier * 2
        dealt = dmgtype * multiplier - edeftype
        if dealt < 0:
            dealt = dmgtype * multiplier
        dealt = round(dealt, 1)
        b = round(b + dealt, 1)
        c = round(c - dealt, 1)
        print("You've dealt " + str(b) + " damage (+" + str(dealt) +
              ") damage to the mob.           Mob Hp = " + str(c) + "/" +
              str(basehp))
    return (b)


def taken(defense, mdef, eatk, ematk, mchance, myhp):
    edmgchance = random.randrange(100)
    if edmgchance <= mchance:
        edmg = ematk
        deftype = mdef
        printtype = "magic"
    else:
        edmg = eatk
        deftype = defense
        printtype = "physical"
    taken = edmg - deftype
    if taken < 0:
        taken = 0
    newhp = myhp - taken
    print("")
    print("")
    print("\nThe enemy retaliates, doing " + str(taken) + " " +
          str(printtype) + " damage.          You have " + str(newhp) + "/" +
          str(stats[0]) + " hitpoints remaining.")
    print("")
    print("")
    return (newhp)


"""
"""


def combat(mob):
    Looop = 1
    print("You enter into combat\n")
    print("")

    time.sleep(speed)
    myhp = float(Hp)
    enemybasehp = float(mob[0])
    enemyhp = float(mob[0])
    overtime = float(0)
    while Looop > 0:
        ShowMoveset()
        laaap = 0
        while laaap < 1:
            print("")
            time.sleep(speed)
            print("Choose your attack:\n")
            print("")
            chooseatk = input("")
            if chooseatk == "1" or chooseatk == "2":
                laaap += 1
        if chooseatk == "1":
            change1 = damage(stats[4], stats[5], stats[8], moveset[0][2],
                             moveset[0][3], mob[3], mob[4], enemyhp,
                             moveset[0][4], overtime, mob[0])
            enemyhp = enemybasehp - change1
            overtime = change1
            if enemyhp <= 0:
                print(
                    "\nYou have successfully defeated the enemy! Your xp is now "
                    + str((xp + mob[5]) *
                          (stats[9] / 100)) + "/" + str(levelreq))
                return (mob[5], myhp)
            takechange1 = taken(stats[2], stats[3], mob[1], mob[2], mob[6],
                                myhp)
            myhp = takechange1
        if chooseatk == "2":
            change2 = damage(stats[4], stats[5], stats[8], moveset[1][2],
                             moveset[1][3], mob[3], mob[4], enemyhp,
                             moveset[1][4], overtime, mob[0])
            enemyhp = enemybasehp - change2
            overtime = change2
            if enemyhp <= 0:

                print(
                    "\nYou have successfully defeated the enemy! Your xp is now "
                    + str((xp + mob[5]) *
                          (stats[9] / 100)) + "/" + str(levelreq))
                return (mob[5], myhp)
            takechange2 = taken(stats[2],stats[3],mob[1],mob[2],mob[6],myhp)
            myhp = takechange2
        if myhp < 0:
            print("You have died. Try again")
            return ("death", 0)
        if myhp + stats[6] > stats[0]:
            time.sleep(speed)
            print("You regen to max hp")
            myhp = stats[0]
        else:
            time.sleep(speed)
            print("You regenerate " + str(stats[6]) + " HP\n")
            myhp += stats[6]
        time.sleep(speed)
        print("Your hp is now: " + str(myhp) + "/" + str(stats[0]) + "\n")
        print("")


###STUFF FOR LATER

#    [Hp,Atk,Matk,Def,Mdef,Xp]

#atk,matk,crit,type,multiplier,regen,mpregen,edef,emdef,ehp,strikes

#defense,mdef,eatk,ematk,mchance
    """
  Hp = stats[0]
  Mp = stats[1]
  Def = stats[2]
  Mdef = stats[3]
  Atk = stats[4]
  MAtk = stats[5]
  HpRegen = stats[6]
  MpRegen = stats[7]
  Crit = stats[8]
  Xpgain = stats[9]
  Dodge = stats[10]

  defense,mdef,eatk,ematk,mchance
  [Hp,Atk,Matk,Def,Mdef,Xp,chance]

  """


def floor(floorandnumber, floorlore1, floorlore2, floorlore3, congratulation,
          xp, levelreq):
    time.sleep(speed)
    print(floorlore1)
    var = combat(floorandnumber[0])
    time.sleep(speed * 5)
    if var[0] == "death":
        return ("death", 0, 0)
    else:
        xp += round(var[0] * (stats[9] / 100))
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                print("You leveled up! Gained 1 of every stat.")
                levelup()
            print("Your updated stats are: \n")
            ShowStats()
    getItem()
    time.sleep(speed)
    print(floorlore2)
    time.sleep(speed * 5)
    var = combat(floorandnumber[1])
    if var[0] == "death":
        return ("death", 0, 0)
    else:
        xp += round(var[0] * (stats[9] / 100))
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                print("You leveled up! Gained 1 of every stat.")
                levelup()
            print("Your updated stats are: \n")
            ShowStats()
    getItem()

    print(congratulation)
    return ("Passed", xp, levelreq)


#STORY WRITING SECTION
floor1 = [goblin, wolf, LargeWolf]
floor2 = [ogre, thief, ChiefThief]
floor3 = [gremlin, orc, MutantOrc]
floor4 = [skeleton, giant, Cyclops]
floor5 = [vampire, witch, Dracula]
floor6 = [phantom, wereman, CrimsonMary]
floor7 = [Xayrraiss]

floor1lore1 = """
You enter the first floor. As you are about to leave, you see a green ear popping out of the floors. Oh No! You encounter a goblin!
"""
floor1lore2 = """
You continue ahead. As you are walking through the dark trip, you get stopped by a wolf!
"""
floor1lore3 = """
You finally step ahead and find the boss waiting with its red teeth: A  Large Wolf
"""
floor1pass = """
Past the boss you see a staircase peeking ahead. You ascend up the stairs
"""
floor2lore1 = """
You enter the second floor. You hear a loud noise... You hear something loud coming towards you. You encounter an ogre!
"""
floor2lore2 = """
You continue ahead. You feel someone reaching into your bag, you get stopped by a thief 
"""
floor2lore3 = """
You finally step ahead and find the boss waiting: A  Chief Thief
"""
floor2pass = """
Past the boss you see a staircase peeking ahead. You ascend up the stairs
"""
floor3lore1 = """
You enter the third floor. You see something ugly and disgusting. You encounter a gremlin
"""
floor3lore2 = """
You continue ahead. However you get stopped by an orc
"""
floor3lore3 = """
You finally step ahead and find the boss waiting: A  Mutant Orc
"""
floor3pass = """
Past the boss you see a staircase peeking ahead. You ascend up the stairs
"""
floor4lore1 = """
You enter the fourth floor. You hear things moving around, almost like a clicking noise. It's the noise of bones hitting against each other. You encounter a skeleton
"""
floor4lore2 = """
You continue ahead. But you encounter another monster, you think to yourself if this will be easier, however you get stopped by a giant
"""
floor4lore3 = """
You finally step ahead and find the boss waiting with its one eye staring right at you: A  Cyclops
"""
floor4pass = """
Past the boss you see a staircase peeking ahead. You ascend up the stairs
"""
floor5lore1 = """
You enter the fifth floor. You realize that you did not bring any garlic as you see a tall creature with sharp teeth. You encounter a vampire
"""
floor5lore2 = """
You continue ahead. But then you smell something digusting. You get stopped by a witch
"""
floor5lore3 = """
You finally step ahead and find the boss waiting: A  Dracula
"""
floor5pass = """
Past the boss you see a staircase peeking ahead. You ascend up the stairs
"""
floor6lore1 = """
You enter the sixth floor. You encounter a phantom
"""
floor6lore2 = """
You continue ahead. You are tired but will not give up. As you continue your adventure, you get stopped by a wereman
"""
floor6lore3 = """
You finally step ahead and find the boss waiting: Mary Crimson
"""
floor6pass = """
Past the boss you see a grand staircase showing ahead. You are lost in sight before you start your journey up your final flight of stairs
"""


def finalboss():
    print(
        "You enter into the chamber of Xayrraiss. He is a large ice blue dragon. You travel over mountains of coins and wealth to face him. \"You dare come and face me mortal?\" You take a stance"
    )
    FINALFIGHT = combat(Xayrraiss)
    if FINALFIGHT[0] == "death":
        return ("death",0,0)
    else:
        print("You have done it. In relief you lay down your weapon beside you. You have finally cleared the tower. But what next? You peer out the only window to the outside and smile")
        quit()

speed = speedset()
classstuff = []
classstuff = Intro()
time.sleep(speed)
stats = classstuff[0]
time.sleep(speed)
moveset = classstuff[1]
time.sleep(speed)
ShowStats()
time.sleep(speed)
ShowMoveset()
time.sleep(speed)
loopcheck = 1

while loopcheck > 0:
    seemoves = input(
        "\nWould you like to see your move details?(Yes/yes or no)\n")
    if seemoves == "Yes" or seemoves == "yes":
        DescribeMoves()
        loopcheck -= 1
    else:
        print("You chose not to view your moves")
        loopcheck -= 1

Hp = stats[0]
Mp = stats[1]
Def = stats[2]
Mdef = stats[3]
Atk = stats[4]
MAtk = stats[5]
HpRegen = stats[6]
MpRegen = stats[7]
Crit = stats[8]
Xpgain = stats[9]
Dodge = stats[10]

journeybegin = input("\nAre you ready to begin your journey?\n")
if journeybegin == "No" or journeybegin == "no":

    print("Nothing happens and you go to sleep")
    quit()
else:
    print(
        "Then away we go! You trump towards a dark looming tower. The citizens of the city have always feared it, and the legendaary dragon Xayrraiss has been keeping his reign, forcing the humans to pay him taxes as well as human servants every month. No one knows where they go. His giant tower has 7 floors filled with creatures of different kinds and only the brave challenge him. You trudge the path towards it."
    )
    time.sleep(speed * 8)
alive = 1
while alive > 0:
    time.sleep(speed * 3)
    first = floor(floor1, floor1lore1, floor1lore2, floor1lore3, floor1pass,
                  xp, levelreq)
    if first[0] == "death":
        print("You met your end... Try again")
        quit()
    else:
        xp += first[1]
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                levelreq = first[2] + 30
                print("You leveled up! Gained 1 of every stat.")
                level += 1
                levelup()
            time.sleep(speed / 4)
            ShowStats()
    second = floor(floor2, floor2lore1, floor2lore2, floor2lore3, floor2pass,
                   xp, levelreq)
    if second[0] == "death":
        print("You met your end... Try again")
        quit()
    else:
        xp += second[1]
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                levelreq += 30
                print("You leveled up! Gained 1 of every stat.")
                level += 1
                levelup()
            time.sleep(speed / 4)
            ShowStats()
    third = floor(floor3, floor3lore1, floor3lore2, floor3lore3, floor3pass,
                  xp, levelreq)
    if third[0] == "death":
        print("You met your end... Try again")
        quit()
    else:
        xp += third[1]
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                levelreq += 30
                print("You leveled up! Gained 1 of every stat.")
                level += 1
                levelup()
            time.sleep(speed / 4)
            ShowStats()
    fourth = floor(floor4, floor4lore1, floor4lore2, floor4lore3, floor4pass,
                   xp, levelreq)
    if fourth[0] == "death":
        print("You met your end... Try again")
        quit()
    else:
        xp += fourth[1]
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                levelreq += 30
                print("You leveled up! Gained 1 of every stat.")
                level += 1
                levelup()
            time.sleep(speed / 4)
            ShowStats()
    fifth = floor(floor5, floor5lore1, floor5lore2, floor5lore3, floor5pass,
                  xp, levelreq)
    if fifth[0] == "death":
        print("You met your end... Try again")
        quit()
    else:
        xp += fifth[1]
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                levelreq += 30
                print("You leveled up! Gained 1 of every stat.")
                level += 1
                levelup()
            time.sleep(speed / 4)
            ShowStats()
    sixth = floor(floor6, floor6lore1, floor6lore2, floor6lore3, floor6pass,
                  xp, levelreq)
    if sixth[0] == "death":
        print("You met your end... Try again")
        quit()
    else:
        xp += sixth[1]
        if xp > levelreq:
            while xp > levelreq:
                xp -= levelreq
                levelreq += 30
                print("You leveled up! Gained 1 of every stat.")
                level += 1
                levelup()
            time.sleep(speed / 4)
            ShowStats()
    bossfight = finalboss()
    if bossfight[0] == "death":
        print(
            "You were the exalted and chosen one, generations of people have waited for one like you to come... Your existence fades."
        )
        quit()
