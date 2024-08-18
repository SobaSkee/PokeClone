from settings import *

class AllSprites(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.offset = vector(100, 20)
  

  def draw(self, player_center):
    self.offset.x = player_center[0]
    self.offset.y = player_center[1]
    for sprite in self:
      self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)