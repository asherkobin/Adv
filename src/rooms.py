from room import Room

def init_rooms(state):
  state.rooms.add_room(
    "outside",
    Room(
      "Outside Mine Entrance",
      "North of you, the mine entrance is blocked by a grid of thick steel. The grid is locked by a padlock that looks rather new.",
      [state.items.get_item("brick"), state.items.get_item("steel-key"), state.items.get_item("gravel")],
      [state.items.get_item("padlock")]
    ))

  state.rooms.add_room(
    "mine-entrance",
    Room(
      "Mine Entrance",
      "The entrance is framed by thick wooden support beams. Chiseled out of stone are narrow passageways to the west, north, and east.",
      [state.items.get_item("key-for-entrance-chest")],
      [state.items.get_item("entrance-chest")]
    ))

  state.rooms.add_room(
    "east-passageway",
    Room(
      "East Passageway",
      "The hard-packed earthen floor has been heavily traveled by miners. It must lead to somewhere interesting.",
      [],
      []
    ))
  
  state.rooms.add_room(
    "equipment-room",
    Room(
      "Equipment Room",
      "The room is looks like it was used by the miners to prepare for work. You see shovels and picks scattered around. On the south wall, there are a row of heavily damaged lockers but one locker is undamaged.",
      [state.items.get_item("rock-pick"), state.items.get_item("shovel")],
      [state.items.get_item("equipment-locker")]
    ))

  state.rooms.add_room(
    "cool-room",
    Room(
      "Open Area west of the Mine Entrance",
      "Entering the area, the cool air suggests to you that the elevation has lowered. To the west, you hear a periodic tapping sound.",
      [],
      []
    ))

  state.rooms.add_room(
    "narrow-corridor",
    Room(
      "Narrow Corridor",
      "The air is getting cooler as the corridor decends. On the north wall, someone painted an arrow pointing west with a red slash through it. The sound of water dripping echos to the west.",
      [],
      []
    ))

  state.rooms.add_room(
    "barrel-shaped-room",
    Room(
      "Barrel-Shaped Room",
      "The corridor ends into a cold empty area. The ceiling is covered in moisture, the walls converging into a circle. You have found the source of the dripping sound: a small pool being filled from codensation.",
      [state.items.get_item("peculiar-stone")],
      [state.items.get_item("dark-pool")]
    ))

def init_room_connections(state):
  num_map_rows = 3
  num_map_columns = 6
  game_map = [
    [None,                    None,                   None,                   state.rooms.tunnel().uid,    None,                   None                   ],
    ["barrel-shaped-room",    "narrow-corridor",      "cool-room",            "mine-entrance",             "east-passageway",      "equipment-room"       ],
    [None,                    None,                   None,                   "outside",                   None,                   None                   ]
  ]

  if len(game_map) != num_map_rows:
    raise Exception("Invalid Map")
  for row in game_map:
    if len(row) != num_map_columns:
      raise Exception("Invalid Map")

  for rowIdx in range(num_map_rows):
    for colIdx in range(num_map_columns):
      room = None
      room_name = game_map[rowIdx][colIdx]
      if room_name == "outside":
        print("Debug")
      if room_name is not None:
        room = state.rooms.get_room(room_name)
        if room is None:
          raise Exception("Room Not Found: " + room_name)
      if room is not None:
        room.map_row = rowIdx
        room.map_col = colIdx
        if rowIdx > 0:
          room.north_room = state.rooms.get_room(game_map[rowIdx - 1][colIdx])
        if rowIdx < num_map_rows - 1:
          room.south_room = state.rooms.get_room(game_map[rowIdx + 1][colIdx])
        if colIdx < num_map_columns - 1:
          room.east_room = state.rooms.get_room(game_map[rowIdx][colIdx + 1])
        if colIdx > 0:
          room.west_room = state.rooms.get_room(game_map[rowIdx][colIdx - 1])