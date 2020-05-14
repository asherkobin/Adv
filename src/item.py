class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

class InventoryItem(Item): # Source
  def __init__(self, name, description, hidden = False):
    super().__init__(name, description)
    self.hidden = hidden

  def pickup(self, state):
    state.player.add_item(self)

  def drop(self, state):
    state.player.remove_item(self)

  def use(self, target, state):
    return False

  def is_hidden(self):
    return self.is_hidden

class RoomItem(Item): # Target
  def __init__(self, name, description):
    super().__init__(name, description)
    self.locked = False
    self.opened = False