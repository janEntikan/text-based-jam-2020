from random import randint
from battle import Mob


def _bunny():
    creature = Mob(
        "bomber bunny", 
        "you can hear sizzles and maniacal laughter...a bomber bunny!", 
        "it's completely mangled"
    )
    creature.hp = 3
    creature.ap = 1
    creature.xp = 25
    creature.cash = randint(2, 12)
    creature.attack = 2
    creature.sensitivity = "green"
    if randint(0,2)==1:
        return creature

def _crab():
    creature = Mob(
        "giant crab", 
        "it makes a click-clacking noise, almost like...a giant crab!", 
        "a pile of cans, claws and shells"
    )
    creature.hp = 5
    creature.ap = 5
    creature.xp = 100
    creature.cash = randint(25, 75)
    creature.attack = 4
    creature.sensitivity = "blue"
    if randint(0,1)==1:
        return creature

def _goat():
    creature = Mob(
        "demon goat", 
        "you can hear hoves on rocks...a demon goat!", 
        "a human chest and the body of a goat, weird"
    )
    creature.hp = 5
    creature.ap = 2
    creature.xp = 50
    creature.cash = randint(15, 50)
    creature.attack = 3
    creature.sensitivity = "red"
    if randint(0,1)==1:
        return creature
    return creature

def _robber():
    creature = Mob(
        "robber", 
        "a bag of money and the chewing of knives...a robber!", 
        "a crumpled heap of humanoid flesh"
    )
    creature.hp = 15
    creature.ap = 5
    creature.xp = 150
    creature.cash = randint(50, 100)
    creature.attack = 5
    creature.sensitivity = "green"
    return creature

def _wizard():
    creature = Mob(
        "wizard", 
        "you can hear sparkles and magic...a wizard!", 
        "some dust and intestines under a robe"
    )
    creature.hp = 15
    creature.ap = 5
    creature.xp = 250
    creature.cash = randint(100, 200)
    creature.attack = 10
    creature.sensitivity = None
    return creature

def _unicorn():
    creature = Mob(
        "unicorn", 
        "you can hear hoves, sparkles and magic...a unicorn!", 
        "the blood is sticky and warm"
    )
    creature.hp = 50
    creature.ap = 50
    creature.xp = 1000
    creature.cash = randint(300, 500)
    creature.attack = 10
    creature.sensitivity = "green"
    if randint(0,5):
        return creature
