from item_list import *

def init_items(state):
  state.items.add_item("brick", Brick())
  state.items.add_item("padlock", Padlock())
  state.items.add_item("steel-key", SteelKey())
  state.items.add_item("gravel", Gravel())
  state.items.add_item("key-for-entrance-chest", KeyForEntranceChest())
  state.items.add_item("entrance-chest", EntranceChest())
  state.items.add_item("mystic-stone", MysticStone())
  state.items.add_item("dark-glass-pool", DarkGlassPool())


# #### BRICK ####

# brick = InventoryItem("brick", "An ordinary red brick.  This may be useful to smash rats in the tunnels ahead.")

# def brick_on_use(self, target, player):
#   if target == items["padlock"]:
#     if target.opened == True:
#       cprint("\nThe padlock has already been broken open.")
#     else:
#       target.opened = True
#       target.locked = False
#       cprint("\nThe brick destroys the rusty padlock and the entrance to the mine is opened.", "white")
#    #   rooms["outside"].description = "North of you, the mine entrance is opened."
#     #  rooms["outside"].n_to = rooms["mine-entrance"]
#     return True
#   else:
#     return False

# brick.use = MethodType(brick_on_use, brick)
# items["brick"] = brick

# #### STEEL-KEY ####

# steel_key = InventoryItem("steel-key", "Engraved on they key is 'Mineshaft 23-C'. It looks like it hasn't been used in a while.")

# def steel_key_on_use(self, target, player):
#   if target == items["padlock"]:
#     cprint("\nAs you turn the steel-key, it crumbles before you into a cloud of rust.", "white")
#     cprint("\nThe padlock remains locked.", "magenta")
#     player.remove_item(self)
#     return True
#   else:
#     return False

# steel_key.use = MethodType(steel_key_on_use, steel_key)
# items["steel-key"] = steel_key
