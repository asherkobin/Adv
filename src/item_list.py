from item import InventoryItem, RoomItem
from termcolor import colored, cprint

class ItemList():
  def __init__(self):
    self.items = dict()

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
      return True
    else:
      return False

class Padlock(RoomItem):
  def __init__(self):
    super().__init__("padlock", "A 'Master' brand lock. On its face, 'Mineshaft 23-C' is written on a piece of tape.")

class SteelKey(InventoryItem):
  def __init__(self):
    super().__init__("steel-key", "Engraved on they key is 'Mineshaft 23-C'. It looks like it hasn't been used in a while.")
  def use(self, target, state):
    if target is state.items.get_item("padlock"):
      if target.opened == True:
        cprint("\nThe padlock has already been broken open.")
      else:
        cprint("\nAs you turn the steel-key, it crumbles before you into a cloud of rust.", "white")
        cprint("\nThe padlock remains locked.", "magenta")
        state.player.remove_item(self)
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

class MysticStone(InventoryItem):
  def __init__(self):
    super().__init__("peculiar-stone", "Mysterious rune carvings surround the stone.", True)

class DarkGlassPool(RoomItem):
  def __init__(self):
    super().__init__("pool", "Beyond the dark surface, you see several rocks settled on the floor of the pool.  You scatter the rocks and see a peculiar-stone, distinct from the others.")

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

