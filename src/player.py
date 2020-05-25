class Player():
  def __init__(self, name = "Player"):
    self.name = name
    self.room = None
    self.items = []
    self.cash = 0
    self.num_gold_ounces = 0

  def set_name(self, name):
    self.name = name

  def set_room(self, room):
    self.room = room
  
  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    self.items.remove(item)

  def add_cash(self, cash):
    self.cash += cash

  def get_cash_amount(self):
    return self.cash

  def has_item(self, item_name):
    found_item = False
    for item in self.items:
      if item.name == item_name:
        found_item = True
        break
    return found_item

  def get_item(self, item_name):
    found_item = None
    for item in self.items:
      if item.name == item_name:
        found_item = item
        break
    return found_item