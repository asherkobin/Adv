from state import State
from termcolor import colored, cprint
from actions import Actions
from inspect import signature
import textwrap
from items import init_items
from rooms import init_rooms, init_room_connections

state = State()

init_items(state)
init_rooms(state)
init_room_connections(state)

import sys
from item import RoomItem
unlock_all_items = False
start_flag = None
if len(sys.argv) > 1:
  start_flag = sys.argv[1]
if start_flag == "-u":
  unlock_all_items = True
if unlock_all_items:
  for item in state.items:
    if isinstance(item, RoomItem) and item.locked:
      item.locked = False
      state.rooms.get_room("outside").north_room = state.rooms.get_room("mine-entrance")

actions = Actions(state)

options = {
  "n": actions.north,
  "s": actions.south,
  "e": actions.east,
  "w": actions.west,
  "?": actions.list_commands,
  "look": actions.look,
  "take": actions.take,
  "drop": actions.drop,
  "loot": actions.show_inventory,
  "inspect": actions.inspect,
  "examine": actions.examine,
  "use": actions.use,
  "open": actions.open,
  "search": actions.search,
  "hint": actions.hint
}

cash_needed_to_win = 10000

state.player.set_room(state.rooms.get_room("outside"))

cprint(f"\n Welcome {state.player.name}!  This is story so far... ", "yellow", attrs=['reverse'])

print()

intro = """You have accumulated a sports gambling debt of $10,000.
Your petulant bookie is looking for you to collect his money.
You must find the money needed within 24 hours.
You decide to explore an abandoned mine hoping to find anything of value to pay your debt."""

for line in textwrap.wrap(intro, 80):
  cprint(line, "cyan")

options["hint"]()

cprint("\nType '?' to list player commands", "green")

actions.print_room_description(state.player.room)

if unlock_all_items:
  cprint("\nEVERYTHING IS UNLOCKED", "red")

while (True):
  user_action = input("\nAction: ")

  decontructed_command = user_action.split(" ")

  if (len(decontructed_command) == 2):    # eg: take key, search pond
    action = decontructed_command[0]
    subject = decontructed_command[1]
    function = None
    target = None
  elif (len(decontructed_command) == 4):  # eg: use key on door
    action = decontructed_command[0]
    subject = decontructed_command[1]
    function = decontructed_command[2]
    target = decontructed_command[3]
  else:
    action = decontructed_command[0]      # eg: search
    subject = None

  if (action == "q"):
    break

  try:
    fn_sig = signature(options[action])
    if (subject is None):
      if len(fn_sig.parameters) > 0:
        cprint("\n" + action + " what?", "red")
      else:
        options[action]()
    elif (function is None and target is None):
      if len(fn_sig.parameters) == 0:
        cprint("\nInvalid syntax.  Type '?' for proper usage.", "red")
      else:
        try:
          options[action](subject)
        except TypeError:
          cprint(f"\n{action} {subject} on what?", "red")
    else:
      options[action](subject, function, target)
  except KeyError:
    print("\nInvalid Action: Type '?' to get list of actions.")
