from room import Room
from item import Item
from target import Target
from termcolor import colored, cprint

items = {
  "brick":
    Item("brick", "An ordinary red brick.  This may be useful to break things.", True, "brick_for_steel_gate"),
  "steel-key":
    Item("steel-key", "Engraved on they key is 'Mineshaft 23-C'. It looks like it hasn't been used in a while.", True, None, True),
  "gravel":
    Item("gravel", "The gravel shows flecks of what looks like gold.  Probably just pyrite.", True, None, True),
  "mystic_stone":
    Item("stone", "Mysterious rune carvings surround the stone.", True),
  "key_for_chest":
    Item("key", "An ordinary key for a ordinary lock.", True, "key_for_chest")
}

def padlock_use_success(player, item, target):
  if (target.opened == True):
    cprint("\nThe padlock has already been broken open.")
  else:
    target.opened = True
    target.locked = False
    cprint("\nThe brick destroys the rusty padlock and the entrance to the mine is opened.", "magenta")
    rooms["outside"].description = "North of you, the mine entrance is opened."
    rooms["outside"].n_to = rooms["mine-entrance"]

def padlock_use_fail(player, item, target):
  if (item.name == "steel-key"):
    cprint("\nAs you turn the steel-key, it crumbles before you into a cloud of rust.", "white")
    player.remove_item(item)
  cprint("\nThe padlock remains locked.", "magenta")

def padlock_open_action(player, target):
  if (target.opened == True):
    cprint("\nThe padlock is already opened.")

def chest_unlocked(player, target):
  if (target.locked == False):
    cprint("\nThe chest is already unlocked.")
  else:
    target.locked = False
    cprint("\nYou unlocked the chest, unfortunately the chest was trapped and poison gas caused 10 damage.")

def chest_opened(player, target):
  if (target.opened == True):
    cprint("\nThe chest is empty.")
  else:
    target.opened = True
    cprint("\nYou find 100 twenty-dollar bills wrapped in a currency strap! $2000 is added to your loot bag.")
    player.add_cash(2000)

targets = {
  "padlock":
    Target("padlock", "brick_for_steel_gate", padlock_use_success, padlock_use_fail, padlock_open_action),
  "chest":
    Target("chest", "key_for_chest", chest_unlocked, None, chest_opened, True),
  "pool":
    Target("pool", None, None, None, None, True)
}

rooms = {
  "outside":
    Room(
      "Outside Mine Entrance",
      "North of you, the mine entrance is blocked by a grid of thick steel.  The grid is locked by a " + colored("padlock", "cyan") + colored(" that looks rather new.", "white"),
      [items["steel-key"], items["brick"], items["gravel"]],
      [targets["padlock"]]),

  "mine-entrance":
    Room(
      "Mine Entrance",
      "The entrance is framed by thick wooden support beams.  Chiseled out of stone are narrow passageways to the west, north, and east.",
      [items["key_for_chest"], items["mystic_stone"]],
      [targets["chest"]]),

  "cool-room":
    Room(
      "Open Area east of the Mine Entrance",
      "Entering the area, the cool air suggests to you that the elevation has lowered.  To the east, you hear the sound of water dripping.", #corridor
      [],
      []),

  "narrow-corridor":
    Room(
      "Narrow Corridor",
      "The air is getting cooler as the corridor decends.  On the north wall, someone painted an arrow pointing east with a red slash through it.",
      [],
      []),
  
  "barrel-shaped-room":
    Room(
      "Barrel-Shaped Room",
      "The corridor ends into a cold empty area.  The ceiling is covered in moisture, the walls converging into a circle.  You have found the source of the dripping sound: a small pool being filled from codensation.",
      [],
      [targets["pool"]]),
}
