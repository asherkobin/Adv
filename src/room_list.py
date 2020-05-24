from room import Room
import uuid


class RoomList():
  def __init__(self):
    self.rooms = dict()

  def add_room(self, uid, room):
    room.uid = uid
    self.rooms[uid] = room

  def get_room(self, uid):
    if uid in self.rooms.keys():
      return self.rooms[uid]
    else:
      return None

  def tunnel(self):
    tunnel_room = Room("Mine Tunnel", "")
    uid = str(uuid.uuid4())
    tunnel_room.uid = uid
    self.add_room(uid, tunnel_room)
    return tunnel_room