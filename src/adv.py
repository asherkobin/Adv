from item_old import Item
from room import Room
from player import Player
from termcolor import colored, cprint
from actions import Actions
from rooms import rooms
from inspect import signature
import roomsetup
import textwrap

player = Player("Adventurer", rooms["outside"])
actions = Actions(player)

# def move_to(dir, cur_loc):
#   attribute = dir + "_to"

#   if hasattr(cur_loc, attribute):
#     return getattr(cur_loc, attribute)
#   else:
#     print("Can't Go That Way!")
#     return cur_loc

options = {
  "n": actions.north,
  "s": actions.south,
  "e": actions.east,
  "w": actions.west,
  "?": actions.list_commands,
  "look": actions.look,
  "pickup": actions.pickup,
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

cprint(f"\n Welcome {player.name}!  This is story so far... ", "yellow", attrs=['reverse'])

print()

intro = """You have accumulated a sports gambling debt of $10,000.
 Your petulant bookie is looking for you to collect his money.
 You must find the money needed within 24 hours.
 You decide to explore an abandoned mine hoping to find anything of value to pay your debt."""

for line in textwrap.wrap(intro, 80):
  cprint(line, "cyan")

options["hint"]()

cprint("\nType '?' to list player commands", "green")

actions.print_room_description(player.room)

while (True):
  user_action = input("\nAction: ")

  decontructed_command = user_action.split(" ")

  if (len(decontructed_command) == 2):    # eg: pickup key, search pond
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
    action = decontructed_command[0]      # eg: survey
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
