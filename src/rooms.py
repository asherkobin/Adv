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
      "The room is looks like it was used by the miners to prepare for work. You see shovels and picks scattered around. On the south wall, there are a row of busted open lockers but one locker is undamaged.",
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
      [state.items.get_item("dark-glass-pool")]
    ))

def init_room_connections(state):
  state.rooms.get_room("outside").north_room = state.rooms.get_room("mine-entrance") #TEMP
  state.rooms.get_room("mine-entrance").south_room = state.rooms.get_room("outside")
  state.rooms.get_room("mine-entrance").west_room = state.rooms.get_room("cool-room")
  state.rooms.get_room("mine-entrance").east_room = state.rooms.get_room("east-passageway")
  state.rooms.get_room("cool-room").east_room = state.rooms.get_room("mine-entrance")
  state.rooms.get_room("cool-room").west_room = state.rooms.get_room("narrow-corridor")
  state.rooms.get_room("narrow-corridor").east_room = state.rooms.get_room("cool-room")
  state.rooms.get_room("narrow-corridor").west_room = state.rooms.get_room("barrel-shaped-room")
  state.rooms.get_room("barrel-shaped-room").east_room = state.rooms.get_room("narrow-corridor")
  state.rooms.get_room("east-passageway").west_room = state.rooms.get_room("mine-entrance")
  state.rooms.get_room("east-passageway").east_room = state.rooms.get_room("equipment-room")
  state.rooms.get_room("equipment-room").west_room = state.rooms.get_room("east-passageway")
