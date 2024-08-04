import pygame
import sys
from config import WINDOW_SIZE, CARS_NUMBER

import neat

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Drag and Drop')

from app.objects.fps import draw_fps, draw_score
from app.objects.grid import Grid
from app.car.main import Car, is_somebody_alive





# group_roads = pygame.sprite.Group()
# from app.objects.road_block import RoadBlock
# RoadBlock(0, (WINDOW_SIZE[0]//(2*128),WINDOW_SIZE[1]//(256)), True, [0])

clock = pygame.time.Clock()

# from app.genoms import Checkpointer
# a=Checkpointer() 
import app.neat