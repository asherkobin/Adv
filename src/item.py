class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

class InventoryItem(Item):
  def __init__(self, name, description):
    super().__init__(name, description)

  def pickup(self, player):
    player.add_item(self)

  def drop(self, player):
    player.remove_item(self)

class RoomItem(Item): # maybe rename to RoomObject
  def __init__(self, name, description):
    super().__init__(name, description)