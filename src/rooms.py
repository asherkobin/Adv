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
      [state.items.get_item("dark-glass-pool")]
    ))

def init_room_connections(state):
  state.rooms.get_room("mine-entrance").south_room = state.rooms.get_room("outside")
  state.rooms.get_room("mine-entrance").west_room = state.rooms.get_room("cool-room")
  state.rooms.get_room("cool-room").east_room = state.rooms.get_room("mine-entrance")
  state.rooms.get_room("cool-room").west_room = state.rooms.get_room("narrow-corridor")
  state.rooms.get_room("narrow-corridor").east_room = state.rooms.get_room("cool-room")
  state.rooms.get_room("narrow-corridor").west_room = state.rooms.get_room("barrel-shaped-room")
  state.rooms.get_room("barrel-shaped-room").east_room = state.rooms.get_room("narrow-corridor")



# rooms['mine-entrance'].e_to = rooms['cool-room']
# rooms['mine-entrance'].w_to = None
# rooms['cool-room'].n_to = None
# rooms['cool-room'].s_to = None
# rooms['cool-room'].e_to = rooms['narrow-corridor']
# rooms['cool-room'].w_to = rooms['mine-entrance']
# rooms['narrow-corridor'].n_to = None
# rooms['narrow-corridor'].s_to = None
# rooms['narrow-corridor'].e_to = rooms['barrel-shaped-room']
# rooms['narrow-corridor'].w_to = rooms['cool-room']
# rooms['barrel-shaped-room'].n_to = None
# rooms['barrel-shaped-room'].s_to = None
# rooms['barrel-shaped-room'].e_to = None
# rooms['barrel-shaped-room'].w_to = rooms['narrow-corridor']