from options import *
from battle import Mob
from npc import NPC

def world():
    start_room = bedroom = Rolodex("bedroom", "home")
    closet = Rolodex("closet", "home")
    hallway = Rolodex("hallway", "home")
    livingroom = Rolodex("livingroom", "home")
    garden = Rolodex("your home", "home")
    road = Rolodex("town road", "town")
    neighbour = Rolodex("miss tover's house", "home")
    tover_house = Rolodex("tover house", "home")
    inn = Rolodex("inn", "shop")
    alley = Rolodex("dark alley", "tension")
    town_center = Rolodex("town square", "town")
    bakery = Rolodex("bakery", "shop")
    magicshop = Rolodex("magicshop", "shop")
    armory = Rolodex("armory", "shop")
    training = Rolodex("training", "shop")
    castle_gate = Rolodex("castle gate", "town")
    bank = Rolodex("bank", "shop")
    castle = Rolodex("castle","tension")
    town_bridge = Rolodex("town bridge", "forrest")
    crossroads = Rolodex("crossroads", "forrest")
    long_road = Rolodex("long road", "forrest")
    dunes = Rolodex("dunes", "forrest")
    sea = Rolodex("sea", "forrest")
    harbor = Rolodex("the harbor", "tension")
    forrest_path = Rolodex("forrest path", "forrest")
    river = Rolodex("river", "forrest")
    forrest = Rolodex("forrest", "forrest")
    lake = Rolodex("the lake", "forrest")
    clearing = Rolodex("clearing", "forrest")
    waterfall = Rolodex("waterfall", "forrest")
    cave = Rolodex("cave", "tension")
    bonfire = Rolodex("bonfire", "tension")
    tower = Rolodex("wizard tower", "tension")
    forrest_cabin = Rolodex("cabin", "forrest")
    in_forrest_cabin = Rolodex("cabin", "tension")
    deep_forrest = Rolodex("deep forrest", "forrest")
    strange_rock = Rolodex("strange rock", "tension")
    candy_house = Rolodex("candy house", "tension")
    ufo = Rolodex("crashlanded ufo")
    mountain_path = Rolodex("canyon path", "forrest")
    canyon_path = Rolodex("mountain path", "forrest")
    mountain_cabin = Rolodex("cabin")
    in_mountain_cabin = Rolodex("cabin")
    mines = Rolodex("the mines", "tension")

    #BEDROOM
    looker(bedroom, "bed", "It is not very soft.")
    bedroom_livingroom_door = bedroom.add(Door(
        name="door", destination=livingroom, 
        description="a damaged wooden door"))
    bedroom_closet_door = bedroom.add(Door(
        name="closet", destination=closet, 
        description ="The dark oak closet holding your wardrobe."))
        # CLOSET
    closet.add(Door(destination=bedroom, mimic=bedroom_closet_door))
    closet.add(Item("plain clothes", "made from very cheap cloth"))
        # DESK
    desk = Rolodex("writing desk")
    bedroom.add(Move("writing desk", desk, "you inspect the writing desk."))
    looker(desk, "quill", "There's no ink to write with")
    looker(desk, "paper", "There's no ink on them")
    looker(desk, "paperweight", "It's useless.")
    desk.add(Nevermind(bedroom, "You stop touching the writing desk."))
    # LIVINGROOM
    looker(livingroom, "window", "you bathe in the sun's warmth")
    front_door = livingroom.add(Door(garden, "front door"))
    front_door.locked = "It won't open. It's locked."
        # WALL HOOKS
    hooks = Rolodex("wall hooks")
    livingroom.add(Move("wall hooks", hooks, "you inspect the wall hooks."))
    hat = hooks.add(Item("hat")).add(Return("feel", "a stitson hat."))
    looker(hooks, "wet spot", "there's a wet spot on the wall here")
    hooks.add(Nevermind(livingroom, "You stop inspecting the wall hooks."))
        # FRONT DOOR AND KEY
    def unlock_front_door(activated, activator):
        if front_door.locked:
            front_door.locked = None
            base.interface.say("You unlock the door with a satisfying click.")
        else:
            base.interface.say("It's already unlocked.")
    key = hooks.add(Item("key"))
    key.add(Return("feel", "It's a bit rusty."))
    key.add(Use(
        "use", "That doesn't work.", 
        front_door, unlock_front_door))
    livingroom_chair = livingroom.add(Menu("chair"))
    livingroom_chair.add(Return("look", "your trusty chair"))
    livingroom_chair.add(Return("sit", "You sit down for a few, and stand up again."))
    livingroom.add(Door(destination=bedroom, name="door", mimic=bedroom_livingroom_door))
    livingroom_bookcase = livingroom.add(Menu("bookcase"))
    livingroom_bookcase.add(Return("look", "All the books you've ever read."))
    livingroom_bookcase.add(Return("read", "you've read all of these already."))
    # GARDEN
    looker(garden, "flowerbed", "they smell so good", verb="smell")
    garden.add(Door(destination=livingroom, name="front door", mimic=front_door))
    looker(garden, "shrub", "a fresh smelling shrubbery", verb="smell")
    make_path(road, garden)
    make_path(town_bridge, road)   
    make_path(road, neighbour)
    # MISS TOVER
    looker(neighbour, "flowers", "Miss Tover likes flowers almost as much as you do")
    make_open_door(neighbour, tover_house, "front door")
    looker(neighbour, "small tree", "a very dry old pine tree.")
    tover_house.add(NPC("miss tover", [
        "Hello young man. Can I get you anything?",
        "I haven't left the city in over 30 years.",
        "How are things outside of the city?",
        "My son David works in the mines.",
    ]))
    # TOWN CENTER
    make_open_door(town_center, bakery, "bakery door")
    bakery.add(NPC("baker", [
        "Good day, friend. What will it be?",
        "Take a look...euh smell around!",
        "I start baking at 4AM.",
        "Don't you just love the smell of bread?",
    ]))
    make_path(town_center, road)
    make_open_door(town_center, armory, "armory door")
    armory.add(NPC("smith", [
        "What will it be, huh?",
        "Finest steel in the land!",
        "Bending steel is hard work.",
        "We have a special offer on wooden swords today.",
    ]))
    looker(town_center, "well", "dank stones. the town's water supply.")
    make_path(town_center, alley)
    make_open_door(town_center, inn, "inn door")
    inn.add(NPC("innkeeper", [
        "Come in! Have a seat!",
        "What can I get you?",
        "A room is 25 gold a night.",
        "This mead comes all the way from Albaden.",
    ]))
    make_open_door(town_center, magicshop, "magicshop door")
    magicshop.add(NPC("magician", [
        "Spells and curses for sale.",
        "Careful, that's very unstable!",
        "I can tell you have a good ear for magic.",
        "Magic, ladies and gentlemen.",
    ]))
    make_open_door(town_center, training, "trainer door")
    training.add(NPC("trainer", [
        "Need some training?",
        "Just walk up to the equipment!",
        "Don't you want to feel the burn?",
        "Are you pumped yet?",
    ]))
    # CASTLE
    make_open_door(castle_gate, bank, "banker door") 
    bank.add(NPC("banker", [
        "Need someone to hold on to your money?",
        "Interest makes the world go round.",
        "Sorry, we're all out of loans.",
        "Life insurance perhaps?",
    ]))
    make_path(castle_gate, town_center)
    make_open_door(castle_gate, castle, "castle door") 
    castle.add(NPC("castle guard", [
        "You can't just walk into the castle like that.",
        "The king is too busy to see the likes of you.",
        "What makes you think you can just barge in here?",
    ]))
    # BRIDGE
    looker(town_bridge, "river", "the river flows under the bridge", verb="listen")
    make_path(town_bridge, crossroads)
    looker(town_bridge, "river", "the river flows under the bridge", verb="listen")
    # CROSSROADS
    make_path(crossroads, forrest_path)
    make_path(crossroads, long_road)
    make_path(crossroads, mountain_path)
    make_path(long_road, forrest_cabin)
    make_path(long_road, dunes)
    looker(long_road, "street lantern", "should provide illumination at night, not that you need it")
    # SEA DIRECTION
    looker(dunes, "seashell", "it emulates the ocean sound", verb="listen")
    make_path(dunes, sea)
    looker(dunes, "grass patch", "a patch of grass surrounded by warm sand")
    # SEA
    looker(sea, "seaweed", "a bit of seaweed washed ashore")
    looker(sea, "sea", "you hear crashing ocean waves", verb="listen")
    looker(sea, "seagul", "a seagul squeeks at you", verb="listen")
    # HARBOR
    make_path(dunes, harbor)
    looker(harbor, "the harbor", "You smell a lot of fish! All ashore!", verb="listen")
    # MOUNTAIN DIRECTION
    looker(mountain_path, "canyon view", "You throw a pebble. Long way down.", verb="listen")
    make_path(mountain_path, canyon_path)
    looker(mountain_path, "cliff face", "an vertical, cold cliff face")
    looker(canyon_path, "stack of rocks", "someone has stacked some rocks on top of eachother")
    make_path(canyon_path, mountain_cabin)
    make_open_door(mountain_cabin, in_mountain_cabin, "cabin door")
    looker(in_mountain_cabin, "broken table", "this table is missing two legs")
    looker(in_mountain_cabin, "hole in floor", "the hole exposes a crack in the foundation")
    looker(in_mountain_cabin, "torn wallpaper", "there's a tear in the wallpaper here")
    make_path(canyon_path, mines)
    mines.add(NPC("miner", [
        "Sorry, but this mine is off limits."
    ]))
    # FORREST DIRECTION
    looker(forrest_path, "big tree", 
        "you can't quite put your arms around it")
    make_path(forrest_path, lake)
    looker(forrest_path, "bench", "A park bench for the resting of tired legs.")
    # FORREST CABIN
    looker(forrest_cabin, "birdhouse", "No birds.", verb="listen")
    make_path(forrest_path, forrest_cabin)
    make_open_door(forrest_cabin, in_forrest_cabin, "cabin door")
    looker(in_forrest_cabin, "dresser", "probably contains the old man's clothes")
    in_forrest_cabin.add(NPC("old man", [
        "Who's there?",
        "Get out of my house!",
        "Who do you think you are?",
        "...scaring an old man like that.",
        "Wait, what was I talking about?",
    ]))
    looker(in_forrest_cabin, "grandfather clock", "that's quite a clock. It's not ticking.")
    looker(in_forrest_cabin, "bunk bed", "three beds stacked on top of eachother.")
    # LAKE
    make_path(lake, river)
    looker(lake, "lake", "the water is very cold, but not deep.")
    make_path(lake, forrest)
    looker(lake, "walnut tree", "The fruit feel like wallnuts.")
    make_path(lake, tower)
    looker(lake, "berry bush", "better leave them alone, might be poisonous.", verb="taste")
    make_path(forrest, deep_forrest)
    # WIZARD TOWER
    tower_door = looker(tower, "tower entrance", "the seams betrays a large stone door")
    tower_door.add(Return("open", "it is magically sealed"))
    # LIGHT FORREST
    looker(forrest, "tree", "Not quite sure what kind of tree this is.")
    make_path(forrest, candy_house)
    looker(forrest, "mushrooms", "a small group of mushrooms")
    make_path(forrest, waterfall) 
    looker(forrest, "boulder", "a decently sized boulder sticking out of the dirt")
    looker(river, "river", "Riverrun, past Eve and Adam's, from swerve of shore to bend of bay")
    # DEEP FORREST
    looker(deep_forrest, "foliage", "a cluster of trees and shrubs")
    looker(deep_forrest, "foliage", "a cluster of trees and shrubs")
    make_path(river, deep_forrest)
    looker(deep_forrest, "foliage", "a cluster of trees and shrubs")
    looker(deep_forrest, "foliage", "a cluster of trees and shrubs")
    make_path(deep_forrest, clearing)
    looker(deep_forrest, "foliage", "a cluster of trees and shrubs")
    looker(deep_forrest, "foliage", "a cluster of trees and shrubs")
    # STRANGE ROCK
    make_path(clearing, strange_rock)
    looker(strange_rock, "strange rock", "An enormous strange, vibrating stone")
    # BONFIRE
    make_path(clearing, bonfire)
    looker(bonfire, "bonfire", "there's a fire here, someone must have been here only recently")
    # CANDY HOUSE
    make_path(clearing, candy_house)
    looker(candy_house, "candy mailbox", "it tastes like candy", verb="taste")
    looker(candy_house, "candy house", "A house made of candy. You don't taste an entrance.", verb="taste")
    looker(candy_house, "candy fence", "a picket fence made of candy", verb="taste")
    # WATERFALL
    #make_path(waterfall, cave) # TODO: Cave is behind the waterfall
    looker(waterfall, "puddle", "you go splish splash", verb="splash")
    looker(waterfall, "waterfall", "A fog of water tickles your face. sparkles!")
    looker(waterfall, "wet boulder", "water from the waterfall moistens this boulder")
    return start_room