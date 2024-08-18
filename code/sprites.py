from settings import *

# inherits from the pygame.sprite module, Sprite class
class Sprite(pygame.sprite.Sprite):
  def __init__(self, pos, surf, groups):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(topleft=pos) # get floating point rectangle