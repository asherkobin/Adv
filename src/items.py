from item import InventoryItem, RoomItem

items = {
  "brick":
    InventoryItem("brick", "An ordinary red brick.  This may be useful to smash rats in the tunnels ahead."),
  "steel-key":
    InventoryItem("steel-key", "Engraved on they key is 'Mineshaft 23-C'. It looks like it hasn't been used in a while."),
  "gravel":
    InventoryItem("gravel", "The gravel shows flecks of what looks like gold.  With your luck, it's probably just pyrite."),
  "mystic_stone":
    InventoryItem("stone", "Mysterious rune carvings surround the stone."),
  "key_for_chest":
    InventoryItem("key", "An ordinary key for a ordinary lock."),
  "padlock":
    RoomItem("padlock", "A 'Master' brand lock.  On its face, 'Mineshaft 23-C' is written on a piece of tape."),
  "chest":
    RoomItem("chest", "The chest is banded in bronze has a keyhole on the front."),
  "pool":
    RoomItem("pool", "The pool surface is looks like dark glass.")
}