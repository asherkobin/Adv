from termcolor import colored, cprint

class PawnShop():
  def __init__(self):
    self.state = None

  def enter(self, state):
    self.state = state

    cprint("\nWelcome to the Pawn Shop. You can sell your items or gold for cash.", "white")

    options = {
        "exit": self.leave,
        "leave": self.leave,
        "bye": self.leave,
        "sell": self.sell,
        "appraise": self.appraise,
        "look": self.look,
        "loot": self.show_inventory,
        "inspect": self.inspect,
        "help": self.help,
        "?": self.help,
        "hint": self.hint
      }

    options["help"]()

    while (True):
      user_action = input("\nPawn Shop Command: ")
      decontructed_command = user_action.split(" ")
      if len(decontructed_command) == 1:
        action = decontructed_command[0]
        item = None
      elif len(decontructed_command) == 2:
        action = decontructed_command[0]
        item = decontructed_command[1]
      else:
        options["help"]()

      try:
        result = True
        if item is None:
          result = options[action]()
        else:
          result = options[action](item)
      except KeyError:
        print("\nInvalid Action: Type '?' to get list of actions.")
      
      if (result == False):
        break
    
  def help(self):
    cprint("""
  Pawn Shop Commands:
  - look (describe your current location)
  - loot (displays your inventory)
  - inspect [item] (describe an inventory item)
  - sell [item] (sells the item)
  - appraise [item] (gives the amount you get for selling this item)
  - leave (returns you to the mine)""")

  def hint(self):
    hint = colored("HINT: ", "white")\
    + "You can "\
    + colored("sell", "green", attrs=["bold", "underline"])\
    + " an item in your loot bag.  You, might want to "\
    + colored("appraise", "green", attrs=["bold", "underline"])\
    + " that item before selling it."\
    + "\nUse the " + colored("help", "green", attrs=["bold", "underline"]) + " command to list your actions."
    print()
    print(hint)
  
  def leave(self):
    cprint("\nIn a blink of an eye, you are back in the mine.", "cyan")
    return False

  def sell(self, item):
    cprint(f"\nYou sell the {item} for $20.", "white")
    return True

  def appraise(self, item):
    cprint(f"\nThe {item} is worth $20.", "white")
    return True

  def look(self):
    cprint("\nYou are in a Pawn Shop.", "white")
    return True

  def show_inventory(self):
    cprint("\nIn your loot bag you can sell:\n")
    if self.state.player.num_gold_ounces > 0:
      cprint("- " + colored(f"gold ({self.state.player.num_gold_ounces} ounces)", "yellow"))
    for item in self.state.player.items:
      cprint("- " + colored(item.name, "yellow"))
    cprint(colored(f"\nYou have ${self.state.player.get_cash_amount()}", "white"))
    return True

  def inspect(self):
    return False