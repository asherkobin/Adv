from room import Room
from player import Player
from item import InventoryItem, RoomItem
from termcolor import colored, cprint
import textwrap
import time

#
# Items can be used on Targets
# Targets can be opened
# Targets cannot be pickedup
#

class Actions():
  def __init__(self, state):
    self.state = state

  def help(self):
    cprint("""
  Movement Commands: n (north), s (south), e (east), w (west)

  Room Commands:
  - look (describe your current location)
  - search (search your nearby location for objects of interest)
  - inspect [object_of_interest] (look closely at something nearby)

  Item Commands:
  - take [item_name] (take an item that you have found)
  - open [item_name] (opens an object, if possible)

  Inventory Commands:
  - loot (displays your inventory)
  - inspect [item_name] (inspect an item for a closer look)
  - use [item_name] on [target] (use an item from your inventory on an object)
  - use [item_name] (uses an object is self-operable)
  - drop [item_name] (drop an item from your inventory)
  
  Other Commands:
  - q (quit)
  - hint (show a hint that might help if you are stuck)""")

############# Helper Methods #############

  def print_room_description(self, room):
    if room.name == "Mine Tunnel":
      room_dirs = room.get_dirs()
      if len(room_dirs) == 0:
        cprint("\nYou have no where to go!", "red")
      elif len(room_dirs) == 1:
        cprint(f"\nYou have reached the dead end of a tunnel. You can move {room_dirs[0]}.", "white")
      elif len(room_dirs) == 2:
        cprint(f"\nYou are in a mine tunnel. You can move {room_dirs[0]} or {room_dirs[1]}.", "white")
      else:
        tmp_str = ""
        for i in range(len(room_dirs) - 1):
          tmp_str += room_dirs[i] + ", "
        tmp_str += f"or {room_dirs[len(room_dirs) - 1]}"
        cprint(f"\nYou are in a mine tunnel. You can walk {tmp_str}.", "white")
    else:
      cprint(f"\nYou are in the {room.name}\n", "green", attrs=["bold"]) 
      for line in textwrap.wrap(room.description, 80):
        cprint(line, "white")

  def print_room_directions(self, room):
    room_dirs = room.get_dirs()
    if len(room_dirs) == 0:
      cprint("\nYou have no where to go!", "red")
    else:
      cprint("\nYou can walk: " + ", ".join(room_dirs), "white")

############# Player Movements #############

  def north(self):
    if self.state.player.room.can_go_north():
      self.state.player.room = self.state.player.room.north_room
      self.print_room_description(self.state.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def south(self):
    if self.state.player.room.can_go_south():
      self.state.player.room = self.state.player.room.south_room
      self.print_room_description(self.state.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def east(self):
    if self.state.player.room.can_go_east():
      self.state.player.room = self.state.player.room.east_room
      self.print_room_description(self.state.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def west(self):
    if self.state.player.room.can_go_west():
      self.state.player.room = self.state.player.room.west_room
      self.print_room_description(self.state.player.room)
    else:
      cprint("\n** Blocked **", "red")

############# HINT #############

  def hint(self):
    hint = colored("HINT: ", "white")\
    + "You can "\
    + colored("inspect", "green", attrs=["bold", "underline"])\
    + " sepcific areas of interest. Also, you can "\
    + colored("inspect", "green", attrs=["bold", "underline"])\
    + " items\nin your inventory. You may learn more about an item and discover possible clues."\
    + "\nIf you feel stuck, use the " + colored("look", "green", attrs=["bold", "underline"]) + " command as the description may provide help."
    print()
    print(hint)

############# SEARCH #############

  def search(self):
    num_items = 0
    cprint("\nYou search the area and see...\n", "white")
    for item in self.state.player.room.inventory_items:
      if item.hidden is False:
        time.sleep(0.25)
        print("- " + colored(item.name, "yellow"))
        num_items += 1
    if num_items == 0:
      cprint("Nothing of interest.", "white")

############# INSPECT #############

  def inspect(self, item_name):
    if self.state.player.has_item(item_name):
      msg = self.state.player.get_item(item_name).description
      print()
      for line in textwrap.wrap(msg, 80):
        cprint(line, "magenta")
    elif self.state.player.room.has_room_item(item_name):
      print()
      msg = self.state.player.room.get_room_item(item_name).description
      for line in textwrap.wrap(msg, 80):
        cprint(line, "magenta")
    elif self.state.player.room.has_inventory_item(item_name):
      cprint("\nYou must take the " + colored(item_name, "yellow") + " to examine it.")
    elif item_name in self.state.player.room.keywords.keys():
      cprint("\n" + self.state.player.room.keywords[item_name], "magenta")
    else:
      cprint("\nAnything of that description is unremarkable.", "white")

############# EXAMINE #############

  def examine(self, target):
    if target == "room":
      self.print_room_directions(self.state.player.room)
    else:
      cprint("Examine what?", "white")
  
############# OPEN #############

  def open(self, target_name):
    found_target = None
    for target in self.state.player.room.room_items:
      if target.name == target_name:
        found_target = target
        break
    if found_target == None:
      cprint("\nNo such target.")
    else:
      if found_target.locked == True:
        cprint("\nThe " + found_target.name + " is locked.", "red")
      else:
        found_target.open(self.state)

############# LOOK #############
  
  def look(self, target = None):
    if target is None:
      self.print_room_description(self.state.player.room)
    elif target == "up":
      cprint("\nYou see rough brown stone veined with white quartz.", "white")
    elif target == "down":
      cprint("\nYou see hard-packed earth, well traveled.", "white")
    elif target in ["north", "south", "east", "west"]:
      cprint("\nYou see darkness", "white")
    else:
      cprint("\nlook where?", "white")

############# TAKE #############

  def take(self, item_name):
    found_inventory_item = None
    found_room_item = None
    for item in self.state.player.room.inventory_items:
      if item.name == item_name:
        found_inventory_item = item
        break
    for item in self.state.player.room.room_items:
      if item.name == item_name:
        found_room_item = item
        break
    if found_room_item is not None:
      cprint("\nWhy would you want to do that?")
    elif found_inventory_item is None:
      cprint("\nThere is no " + item_name + " here.")
    elif found_inventory_item is not None:
      cprint("\nYou added the " + colored(item_name, "yellow") + " to your loot bag.")
      found_inventory_item.take(self.state)
      self.inspect(item_name)
      if found_inventory_item.hidden:
        found_inventory_item.hidden = False
      else:
        self.state.player.room.inventory_items.remove(found_inventory_item)


############# DROP #############

  def drop(self, item_name):
    found_inventory_item = None
    for item in self.state.player.items:
      if item.name == item_name:
        found_inventory_item = item
        break
    if found_inventory_item is None:
      cprint("\nYou do not possess a " + colored(item_name, "yellow"))
    else:
      cprint("\nYou dropped the " + colored(item_name, "yellow"))
      found_inventory_item.drop(self.state)
      self.state.player.room.inventory_items.append(found_inventory_item)

############# LOOT #############

  def show_inventory(self):
    cprint("\nIn your loot bag you have:\n")
    cprint("- " + colored(f"${self.state.player.get_cash_amount()}", "yellow"))
    if self.state.player.num_gold_ounces > 0:
      cprint("- " + colored(f"gold ({self.state.player.num_gold_ounces} ounces)", "yellow"))
    for item in self.state.player.items:
      cprint("- " + colored(item.name, "yellow"))
  
############# USE #############

  def use(self, inventory_item, function = None, room_item = None):
    found_item = None
    found_target = None

    found_item = self.state.player.get_item(inventory_item)
    if not found_item:
      cprint("\nYou do not possess a " + colored(inventory_item, "yellow") + ".")
      return

    if room_item is not None:
      found_target = self.state.player.room.get_room_item(room_item)
      if not found_target:
        cprint("\nThis room does not have a " + colored(room_item, "cyan") + ".")
        return

    if not found_item.use(found_target, self.state):
      cprint("\nNo effect...", "magenta")

############# DEBUG #############

  def debug(self):
    print()
    for uid in self.state.game_map.get_all_room_uids():
      cprint(f"- {uid}", "blue")