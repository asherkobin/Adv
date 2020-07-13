from room_list import RoomList
from item_list import ItemList
from player import Player
from game_map import GameMap
from pawn_shop import PawnShop

class State():
  def __init__(self):
    self.player = Player()
    self.rooms = RoomList()
    self.items = ItemList()
    self.game_map = GameMap()
    self.pawn_shop = PawnShop()