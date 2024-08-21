from game_data import MONSTER_DATA

# class only stores data so no need for pygame imports

class Monster:
  def __init__(self, name, level):
    self.name, self.level = name, level
    
    # stats
    self.element = MONSTER_DATA[name]['stats']['element']
    self.base_stats = MONSTER_DATA[name]['stats']