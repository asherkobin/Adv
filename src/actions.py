from item import Item
from room import Room
from player import Player
from termcolor import colored, cprint
import textwrap

#
# Items can be used on Targets
# Targets can be opened
# Targets cannot be pickedup
#

class Actions():
  def __init__(self, player):
    self.player = player

  def list_commands(self):
    cprint("""
  Movement Commands: n (north), s (south), e (east), w (west), q (quit)

  Room Commands:
  - look (describe your current location)
  - survey (survey your nearby location for objects of interest)
  - search [area_of_interest] (look further at something nearby)

  Item Commands:
  - pickup [item_name] (pickup an item that you have found)
  - drop [item_name] (drop an item from your inventory)
  - open [item_name] (opens an object)

  Inventory Commands:
  - loot (displays your inventory)
  - inspect [item_name] (inspect an item)
  - use [item_name] on [target] (use an item on an object)""")

  def print_room_description(self, room):
    cprint(f"\nYou are in the {room.name}\n", "green") 
    for line in textwrap.wrap(room.description, 80):
      cprint(line, "white")

  def north(self):
    if self.player.room.n_to != None:
      self.player.room = self.player.room.n_to
      self.print_room_description(self.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def south(self):
    if self.player.room.s_to != None:
      self.player.room = self.player.room.s_to
      self.print_room_description(self.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def east(self):
    if self.player.room.e_to != None:
      self.player.room = self.player.room.e_to
      self.print_room_description(self.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def west(self):
    if self.player.room.w_to != None:
      self.player.room = self.player.room.w_to
      self.print_room_description(self.player.room)
    else:
      cprint("\n** Blocked **", "red")

  def survey(self):
    num_items_and_targets = 0
    cprint("\nYou survey the area and see...\n", "white")
    for item in self.player.room.items:
      print("- " + colored(item.name, "yellow"))
      num_items_and_targets += 1
    for target in self.player.room.targets:
      if (target.include_in_survey == True):
        print("- " + colored(target.name, "cyan"))
        num_items_and_targets += 1
    if num_items_and_targets == 0:
      cprint("Nothing of interest.", "magenta")

  def open(self, target_name):
    found_target = None
    for target in self.player.room.targets:
      if target.name == target_name:
        found_target = target
        break
    if found_target == None:
      cprint("\nNo such target.")
    else:
      if (found_target.locked == False):
        found_target.open_action(self.player, found_target)
      else:
        cprint("\nThe " + found_target.name + " is locked.", "red")

  def look(self):
    self.print_room_description(self.player.room)

  def pickup(self, item_name):
    found_item = None
    found_target = None
    for item in self.player.room.items:
      if item.name == item_name:
        found_item = item
        break
    for target in self.player.room.targets:
      if target.name == item_name:
        found_target = item
        break
    if (found_target is not None):
      cprint("\nThe " + item_name + " is too heavy to pickup.")
    elif (found_item is None):
      cprint("\nThere is no " + item_name + " here.")
    elif found_item.can_be_pickedup == False:
      cprint("\nYou cannot pickup the " + colored(item_name, "yellow") + ".")
    else:
      cprint("\nYou picked up the " + colored(item_name, "yellow") + ".")
      if found_item.show_description_on_pickup:
        cprint("\n" + found_item.description, "magenta")
      self.player.room.items.remove(item)
      self.player.add_item(item)

  def drop(self, item_name):
    found_item = None
    for item in self.player.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nYou do not possess a \033[93m" + item_name)
    else:
      cprint("\nYou dropped the \033[93m" + item_name)
      self.player.room.items.append(item)
      self.player.remove_item(item)

  def show_inventory(self):
    cprint("\nIn your loot bag you have:\n")
    if len(self.player.items) == 0:
      cprint("Nothing", "red")
    else:
      cprint(f"You have ${self.player.get_cash_amount()}")
      for item in self.player.items:
        cprint("- \033[93m" + item.name)

  def inspect(self, item_name):
    found_item = None
    for item in self.player.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nYou do not possess a \033[93m" + item_name)
    else:
      cprint("\n" + found_item.description, "magenta")

  def search(self, target_name):
    found_target = None
    for target in self.player.room.targets:
      if target.name == target_name:
        found_target = target
        break
    if (found_target is None):
      cprint("\nThere is no " + colored(target_name, "cyan") + " present.")
    else:
      found_target.search()
  
  def use(self, item_name, function, target_name):
    found_item = None
    found_target = None
    for item in self.player.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nYou do not possess a \033[93m" + item_name)
    else:
      for target in self.player.room.targets:
        if target.name == target_name:
          found_target = target
          break
      if (found_target is None):
        cprint("\nThis room does not have a " + colored(target_name, "cyan"))
      elif (found_target.item_used_for == found_item.used_for):
        found_target.success_action(self.player, found_item, found_target)
      elif (found_target.fail_action != None):
        found_target.fail_action(self.player, found_item, found_target)
      else:
        cprint("\nNo Effect", "magenta")
