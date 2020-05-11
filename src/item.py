class Item():
  def __init__(self, name, description, can_be_pickedup = True, used_for = None, show_description_on_pickup = False):
    self.name = name
    self.description = description
    self.inspect_description = "Show Secret Hints" #TBD
    self.can_be_pickedup = can_be_pickedup
    self.used_for = used_for
    self.show_description_on_pickup = show_description_on_pickup
