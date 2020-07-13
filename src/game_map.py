class GameMap():
  def __init__(self):
    self.__room_matrix__ = None
    self.num_rows = None
    self.num_cols = None

  def initialize(self, room_matrix, num_rows, num_cols, start_uid):
    self.__room_matrix__ = room_matrix
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.start_uid = start_uid

  def get_room_uid_at(self, row_idx, col_idx):
    return self.__room_matrix__[row_idx][col_idx]

  def get_all_room_uids(self):
    uid_list = []
    for row_idx in range(self.num_rows):
      for col_idx in range(self.num_cols):
        room_uid = self.get_room_uid_at(row_idx, col_idx)
        if room_uid is not None:
          uid_list.append(room_uid)
    return uid_list

def init_map(state):
  num_map_rows = 4
  num_map_columns = 6
  room_matrix = [
    [None,                    None,                   None,                   state.rooms.tunnel().uid,    state.rooms.tunnel().uid,  None                   ],
    [None,                    None,                   None,                   state.rooms.tunnel().uid,    None,                      None                   ],
    ["barrel-shaped-room",    "narrow-corridor",      "cool-room",            "mine-entrance",             "east-passageway",         "equipment-room"       ],
    [None,                    None,                   None,                   "outside",                   None,                      None                   ]
  ]

  state.game_map.initialize(room_matrix, num_map_rows, num_map_columns, "outside")

  if len(room_matrix) != num_map_rows:
    raise Exception("Invalid Map")
  for row in room_matrix:
    if len(row) != num_map_columns:
      raise Exception("Invalid Map")

  for rowIdx in range(num_map_rows):
    for colIdx in range(num_map_columns):
      room = None
      room_uid = room_matrix[rowIdx][colIdx]
      if room_uid is not None:
        room = state.rooms.get_room(room_uid)
        if room is None:
          raise Exception("Room Not Found: " + room_uid)
        room.map_row = rowIdx
        room.map_col = colIdx
        if rowIdx > 0:
          room.north_room = state.rooms.get_room(room_matrix[rowIdx - 1][colIdx])
        if rowIdx < num_map_rows - 1:
          room.south_room = state.rooms.get_room(room_matrix[rowIdx + 1][colIdx])
        if colIdx < num_map_columns - 1:
          room.east_room = state.rooms.get_room(room_matrix[rowIdx][colIdx + 1])
        if colIdx > 0:
          room.west_room = state.rooms.get_room(room_matrix[rowIdx][colIdx - 1])

  setup_map(state)

def setup_map(state):
  state.rooms.get_room("outside").north_room = None
  
  for rowIdx in range(state.game_map.num_rows):
    for colIdx in range(state.game_map.num_cols):
      room_uid = state.game_map.get_room_uid_at(rowIdx, colIdx)
      if room_uid is not None:
        room = state.rooms.get_room(room_uid)
        if room.is_tunnel:
          pass

# TODO: do something random with the tunnels