from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

# imports
def import_image(*path, alpha=True, format='png'):
  full_path = join(*path) + f'.{format}'
  surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
  return surf

# only stores surface
def import_folder(*path):
  frames = []
  for folder_path, sub_folders, image_names in walk(join(*path)):
    for image_name in sorted(image_names, key=lambda name: int(name.split('.')[0])):
      full_path = join(folder_path, image_name)
      surf = pygame.image.load(full_path).convert_alpha()
      frames.append(surf)
  return frames

# stores surface and name
def import_folder_dict(*path):
  frames = {}
  for folder_path, sub_folders, image_names in walk(join(*path)):
    for image_name in image_names:
      full_path = join(folder_path, image_name)
      surf = pygame.image.load(full_path).convert_alpha()
      frames[image_names.split('.')[0]] = surf
  return frames

# 
def import_sub_folders(*path):
  