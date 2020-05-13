class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

class InventoryItem(Item): # Source
  def __init__(self, name, description):
    super().__init__(name, description)

  def pickup(self, player):
    player.add_item(self)

  def drop(self, player):
    player.remove_item(self)

  def use(self, target, player):
    return False

class RoomItem(Item): # Target
  def __init__(self, name, description):
    super().__init__(name, description)
    self.locked = False
    self.opened = False