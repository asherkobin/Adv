class RoomList():
  def __init__(self):
    self.rooms = dict()

  def add_room(self, name, room):
    self.rooms[name] = room

  def get_room(self, name):
    if name in self.rooms.keys():
      return self.rooms[name]
    else:
      return None