from room import Room

def init_rooms(state):
  state.rooms.add_room(
    "outside",
    Room(
      "Outside Mine Entrance",
      "North of you, the mine entrance is blocked by a grid of thick steel.  The grid is locked by a padlock that looks rather new.",
      [state.items.get_item("brick")],
      [state.items.get_item("padlock")]
    ))

  state.rooms.add_room(
    "mine-entrance",
    Room(
      "Mine Entrance",
      "The entrance is framed by thick wooden support beams.  Chiseled out of stone are narrow passageways to the west, north, and east.",
      [state.items.get_item("key-for-entrance-chest")],
      [state.items.get_item("entrance-chest")]
    ))

def init_room_connections(state):
  state.rooms.get_room("outside").north_room = state.rooms.get_room("mine-entrance")
# def chest_unlocked(player, target):
#   if (target.locked == False):
#     cprint("\nThe chest is already unlocked.")
#   else:
#     target.locked = False
#     cprint("\nYou unlocked the chest, unfortunately the chest was trapped and poison gas caused 10 damage.")

# def chest_opened(player, target):
#   if (target.opened == True):
#     cprint("\nThe chest is empty.")
#   else:
#     target.opened = True
#     cprint("\nYou find 100 twenty-dollar bills wrapped in a currency strap! $2000 is added to your loot bag.")
#     player.add_cash(2000)

# rooms = {
#   "outside":
#     Room(
#       "Outside Mine Entrance",
#       "North of you, the mine entrance is blocked by a grid of thick steel.  The grid is locked by a padlock that looks rather new.",
#       [items["steel-key"], items["brick"], items["gravel"]],
#       [items["padlock"]]),

#   "mine-entrance":
#     Room(
#       "Mine Entrance",
#       "The entrance is framed by thick wooden support beams.  Chiseled out of stone are narrow passageways to the west, north, and east.",
#       [items["key_for_chest"], items["mystic_stone"], items["chest"]]),

#   "cool-room":
#     Room(
#       "Open Area east of the Mine Entrance",
#       "Entering the area, the cool air suggests to you that the elevation has lowered.  To the east, you hear the sound of water dripping.", #corridor
#       []),

#   "narrow-corridor":
#     Room(
#       "Narrow Corridor",
#       "The air is getting cooler as the corridor decends.  On the north wall, someone painted an arrow pointing east with a red slash through it.",
#       []),
  
#   "barrel-shaped-room":
#     Room(
#       "Barrel-Shaped Room",
#       "The corridor ends into a cold empty area.  The ceiling is covered in moisture, the walls converging into a circle.  You have found the source of the dripping sound: a small pool being filled from codensation.",
#       [items["pool"]])
# }
