from item import InventoryItem, RoomItem
from termcolor import colored, cprint

class ItemList():
  def __init__(self):
    self.items = dict()

  def __iter__(self):
    return iter(self.items.values())

  def add_item(self, name, item):
    self.items[name] = item

  def get_item(self, name):
    return self.items[name]

class Brick(InventoryItem):
  def __init__(self):
    super().__init__("brick", "An ordinary red brick.  This may be useful to smash rats in the tunnels ahead.")
  def use(self, target, state):
    if target is state.items.get_item("padlock"):
      if target.opened == True:
        cprint("\nThe padlock has already been broken open.")
      else:
        target.opened = True
        target.locked = False
        cprint("\nThe brick destroys the rusty padlock and you remove the steel grid.  The entrance to the mine is opened!", "white")
        state.rooms.get_room("outside").north_room = state.rooms.get_room("mine-entrance")
        state.rooms.get_room("outside").description = "North of you, the mine entrance is opened."
        target.description = "Only a pile of rust remains."
      return True
    else:
      return False

class Padlock(RoomItem):
  def __init__(self):
    super().__init__("padlock", "A 'Master' brand lock. On its face, 'Mineshaft 23-C' is written on a piece of tape.", True)

class SteelKey(InventoryItem):
  def __init__(self):
    super().__init__("steel-key", "Engraved on they key is '23-C'. It looks like it hasn't been used in a while.")
  def use(self, target, state):
    if target is state.items.get_item("padlock"):
      if target.opened == True:
        cprint("\nThe padlock has already been broken open.")
      else:
        cprint("\nAs you turn the steel-key, it crumbles before you into a cloud of rust.", "white")
        cprint("\nThe padlock remains locked.", "magenta")
        state.player.remove_item(self)
      return True
    if target is state.items.get_item("equipment-locker"):
      if target.opened == True:
        cprint("\nThe locker is already unlocked.")
      else:
        target.locked = False
        cprint("\nYou unlock the locker with the steel-key", "white")
      return True
    else:
      return False

class Gravel(InventoryItem):
  def __init__(self):
    super().__init__("gravel", "The gravel shows flecks of what looks like gold. With your luck, it's probably just pyrite.")

class KeyForEntranceChest(InventoryItem):
  def __init__(self):
    super().__init__("key", "An ordinary key for a ordinary lock.")

class EntranceChest(RoomItem):
  def __init__(self):
    super().__init__("chest", "The chest is banded in bronze has a keyhole on the front.")

class MysticStone(InventoryItem): # Lets your pawn off any gold or items for cash
  def __init__(self):
    super().__init__("stone", "Mysterious rune carvings surround the stone.", True)
  def take(self, state):
    super().take(state)
    state.items.get_item("dark-pool").description = "Beyond the dark surface, you see several rocks settled on the floor of the pool."
  def use(self, target, state):
    cprint("\nYou are instantly transported to somewhere outside the mine...", "magenta")
    state.pawn_shop.enter(state)
    return True

class DarkPool(RoomItem):
  def __init__(self):
    super().__init__("pool", "Beyond the dark surface, you see several rocks settled on the floor of the pool.  You scatter the rocks and see a peculiar looking stone, distinct from the others.")

class RockPick(InventoryItem):
  def __init__(self):
    super().__init__("pick", "A tool used for breaking rock.")

class Shovel(InventoryItem):
  def __init__(self):
    super().__init__("shovel", "A tool used for digging.")
  def use(self, target, state):
    if state.player.room.num_gold_ounces > 0:
      print(colored("\nYou hit paydirt and find ", "white") + colored(str(state.player.room.num_gold_ounces) +  " ounces of gold!", "yellow") + colored(" You put the gold in your loot sack.", "white"))
      state.player.num_gold_ounces += state.player.room.num_gold_ounces
      state.player.room.num_gold_ounces = 0
    else:
      cprint("\nThere is nothing to be found here.", "white")
    return True

class EquipmentLocker(RoomItem):
  def __init__(self):
    super().__init__("locker", "There is a keyhole with a nameplate that reads '23-C'.", True)
  def can_open(self, state):
    return True
  def open(self, state):
    if self.locked:
      cprint("\nYou cannot open it. Is there a keyhole?")
    elif self.looted:
      cprint("\nThe locker is empty.")
    else:
      super().open(state)
      cprint("\nYou find a bag containing $1000!", "yellow")
      state.player.add_cash(1000)
      self.looted = True

# def chest_unlocked(player, target):
#   if (target.locked == False):
#     cprint("\nThe chest is already unlocked.")
#   else:
#     target.locked = False
#     cprint("\nYou unlocked the chest, unfortunately the chest was trapped and poison gas caused 10 damage.")

# def chest_opened(player, target):
#   if (target.opened == True):
#     cprint("\nThe chest is empty.")
#   else:
#     target.opened = True
#     cprint("\nYou find 100 twenty-dollar bills wrapped in a currency strap! $2000 is added to your loot bag.")
#     player.add_cash(2000)

