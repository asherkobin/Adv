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

  def list_commands(self):
    cprint("""
  Movement Commands: n (north), s (south), e (east), w (west)

  Room Commands:
  - look (describe your current location)
  - search (search your nearby location for objects of interest)
  - inspect [object_of_interest] (look further at something nearby)

  Item Commands:
  - pickup [item_name] (pickup an item that you have found)
  - drop [item_name] (drop an item from your inventory)
  - open [item_name] (opens an object)

  Inventory Commands:
  - loot (displays your inventory)
  - inspect [item_name] (inspect an item for a closer look)
  - use [item_name] on [target] (use an item from your inventory on an object)
  
  Other Commands:
  - q (quit)
  - hint (show a hint that might help if you are stuck)""")

  def print_room_description(self, room):
    cprint(f"\nYou are in the {room.name}\n", "green", attrs=["bold"]) 
    for line in textwrap.wrap(room.description, 80):
      cprint(line, "white")

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
      self.state.player.room = self.state.player.west_room
      self.print_room_description(self.state.player.room)
    else:
      cprint("\n** Blocked **", "red")

############# HINT #############

  def hint(self):
    hint = colored("HINT: ", "white")\
    + "You can "\
    + colored("inspect", "green", attrs=["bold", "underline"])\
    + " sepcific areas of interest.  Also, you can "\
    + colored("inspect", "green", attrs=["bold", "underline"])\
    + " items\nin your inventory.  You may learn more about an item and discover possible clues."\
    + "\nIf you feel stuck, use the " + colored("look", "green", attrs=["bold", "underline"]) + " command as the description may provide help."
    
    print()
    print(hint)

############# SEARCH #############

  def search(self):
    num_items = 0
    cprint("\nYou search the area and see...\n", "white")
    for item in self.state.player.room.inventory_items:
      time.sleep(0.25)
      print("- " + colored(item.name, "yellow"))
      num_items += 1
    if num_items == 0:
      cprint("Nothing of interest.", "magenta")

############# INSPECT #############

  def inspect(self, item_name):
    if self.state.player.has_item(item_name):
      cprint("\n" + self.state.player.get_item(item_name).description, "magenta")
    elif self.state.player.room.has_room_item(item_name):
      cprint("\n" + self.state.player.room.get_room_item(item_name).description, "magenta")
    elif self.state.player.room.has_inventory_item(item_name):
      cprint("\nYou must pickup the " + colored(item_name, "yellow") + " to examine it.")
    else:
      cprint("\nAnything of that description is unremarkable.")

############# OPEN #############

  def examine(self):
    cprint("\nNot Implemented!", "red")
  
############# OPEN #############

  def open(self, target_name):
    found_target = None
    for target in self.state.player.room.targets:
      if target.name == target_name:
        found_target = target
        break
    if found_target == None:
      cprint("\nNo such target.")
    else:
      if (found_target.locked == False):
        found_target.open_action(self.state.player, found_target)
      else:
        cprint("\nThe " + found_target.name + " is locked.", "red")

  def look(self):
    self.print_room_description(self.state.player.room)

############# PICKUP #############

  def pickup(self, item_name):
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
      cprint("\nThe " + item_name + " is too heavy to pickup.")
    elif found_inventory_item is None:
      cprint("\nThere is no " + item_name + " here.")
    elif found_inventory_item is not None:
      cprint("\nYou added the " + colored(item_name, "yellow") + " to your loot bag.")
      found_inventory_item.pickup(self.state.player)
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
      found_inventory_item.drop(self.state.player)
      self.state.player.room.inventory_items.append(found_inventory_item)

############# LOOT #############

  def show_inventory(self):
    cprint("\nIn your loot bag you have:\n")
    cprint("- " + colored("$" + str(self.state.player.get_cash_amount()), "yellow"))
    for item in self.state.player.items:
      cprint("- " + colored(item.name, "yellow"))
  
############# USE #############

  def use(self, inventory_item, function, room_item):
    found_item = None
    found_target = None
    
    found_item = self.state.player.get_item(inventory_item)
    if not found_item:
      cprint("\nYou do not possess a " + colored(inventory_item, "yellow") + ".")
      return

    found_target = self.state.player.room.get_room_item(room_item)
    if not found_target:
      cprint("\nThis room does not have a " + colored(room_item, "cyan") + ".")
      return

    if not found_item.use(found_target, self.state.player):
      cprint("\nNo effect...", "magenta")