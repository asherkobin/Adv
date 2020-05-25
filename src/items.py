from item_list import *

# Unique identifiers for objects that may have the same name

def init_items(state):
  state.items.add_item("brick", Brick())
  state.items.add_item("padlock", Padlock())
  state.items.add_item("steel-key", SteelKey())
  state.items.add_item("gravel", Gravel())
  state.items.add_item("key-for-entrance-chest", KeyForEntranceChest())
  state.items.add_item("entrance-chest", EntranceChest())
  state.items.add_item("mystic-stone", MysticStone())
  state.items.add_item("dark-pool", DarkPool())
  state.items.add_item("stone", MysticStone())
  state.items.add_item("equipment-locker", EquipmentLocker())
  state.items.add_item("rock-pick", RockPick())
  state.items.add_item("shovel", Shovel())
