class Room():
  def __init__(self, name, description, inventory_items = [], room_items = []):
    self.name = name
    self.description = description
    self.inventory_items = inventory_items
    self.room_items = room_items
    self.north_room = None
    self.south_room = None
    self.east_room = None
    self.west_room = None
    self.map_row = -1
    self.map_col = -1
    self.uid = None

  def can_go_north(self):
    return self.north_room is not None

  def can_go_south(self):
    return self.south_room is not None

  def can_go_east(self):
    return self.east_room is not None

  def can_go_west(self):
    return self.west_room is not None

  def get_dirs(self):
    dirs = []
    if self.can_go_north():
      dirs.append("north")
    if self.can_go_south():
      dirs.append("south")
    if self.can_go_east():
      dirs.append("east")
    if self.can_go_west():
      dirs.append("west")
    return dirs

  def has_inventory_item(self, item_name):
    found_item = False
    for item in self.inventory_items:
      if item.name == item_name:
        found_item = True
        break
    return found_item

  def get_inventory_item(self, item_name):
    found_item = None
    for item in self.inventory_items:
      if item.name == item_name:
        found_item = item
        break
    return found_item

  def has_room_item(self, item_name):
    found_item = False
    for item in self.room_items:
      if item.name == item_name:
        found_item = True
        break
    return found_item

  def get_room_item(self, item_name):
    found_item = None
    for item in self.room_items:
      if item.name == item_name:
        found_item = item
        break
    return found_item