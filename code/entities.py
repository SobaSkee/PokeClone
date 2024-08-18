from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = pygame.Surface((100, 100))
    self.image.fill('red')
    self.rect = self.image.get_frect(center=pos)

    self.direction = vector()
  
  def input(self):
    keys = pygame.key.get_pressed()
    input_vector = vector() # gives a blank vector of 0 and 0
    if keys[pygame.K_UP]:
      input_vector.y -= 1
    if keys[pygame.K_DOWN]:
      input_vector.y += 1
    if keys[pygame.K_LEFT]:
      input_vector.x -= 1
    if keys[pygame.K_RIGHT]:
      input_vector.x += 1
    self.direction = input_vector

  def move(self, dt):
    self.rect.center += self.direction * 1000 * dt # change to 250 default later

  def update(self, dt):
    self.input()
    self.move(dt)