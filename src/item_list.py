from item import InventoryItem, RoomItem

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

class Padlock(RoomItem):
  def __init__(self):
    super().__init__("padlock", "A 'Master' brand lock.  On its face, 'Mineshaft 23-C' is written on a piece of tape.")

class SteelKey(InventoryItem):
  def __init__(self):
    super().__init__("steel-key", "Engraved on they key is 'Mineshaft 23-C'. It looks like it hasn't been used in a while.")

class Gravel(InventoryItem):
  def __init__(self):
    super().__init__("gravel", "The gravel shows flecks of what looks like gold.  With your luck, it's probably just pyrite.")

class KeyForEntranceChest(InventoryItem):
  def __init__(self):
    super().__init__("key", "An ordinary key for a ordinary lock.")

class EntranceChest(RoomItem):
  def __init__(self):
    super().__init__("chest", "The chest is banded in bronze has a keyhole on the front.")

class MysticStone(InventoryItem):
  def __init__(self):
    super().__init__("stone", "Mysterious rune carvings surround the stone.")

class DarkGlassPool(RoomItem):
  def __init__(self):
    super().__init__("pool", "The pool surface is looks like dark glass.")