from item import Item

class Room():
  def __init__(self, name, description, items, targets):
    self.name = name
    self.description = description
    self.items = items
    self.targets = targets