from pygame import Surface, Rect, draw, image, transform, sprite
from config import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, BLACK, WHITE, LIGHT_GREY
from config import ROAD_IMAGES, PATH_ROAD_IMAGES, GRID_SIZE, GRID_WIDTH
import random
# from random import random.randint

import pygame

from app import window



class Grid(Surface):
    pos = (0, - GRID_SIZE)

    offset_y = 0

    def __init__(self):
        super().__init__((GRID_WIDTH * GRID_SIZE, (GRID_HEIGHT + 1) * GRID_SIZE))
        random.seed(3)

        
        self.roads = []


        self.floor_end = GRID_WIDTH//2

        self.fill(LIGHT_GREY)

        for i in ROAD_IMAGES:
            s, e = int(i[2]), int(i[3])
            for j in range(4):
                sj, ej = (s+j)%4, (e+j)%4
                if not (sj == 1 or ej == 3):    
                    new_dict = {'image': transform.rotate(image.load(PATH_ROAD_IMAGES + i).convert_alpha(), -90*j), 'start': sj, 'end': ej}
                    self.roads.append(new_dict)
                sj, ej = ej, sj
                if not (sj == 1 or ej == 3):    
                    new_dict = {'image': transform.rotate(image.load(PATH_ROAD_IMAGES + i).convert_alpha(), -90*j), 'start': sj, 'end': ej}
                    self.roads.append(new_dict)

        
        while 1:
            i = random.randint(0, len(self.roads)-1)
            if self.roads[i]['end'] == 1 and self.roads[i]['start'] == 3: 
                self.blit(self.roads[i]['image'], (GRID_WIDTH//2 * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
                break

        floor_end = GRID_WIDTH//2
        for j in range(GRID_HEIGHT-1, -1, -1):
                self.create_one_floor(j)


    def draw(self, y=0):
        y = -y
        if y - self.offset_y >= GRID_SIZE:
            self.offset_y = y
            self.update()

        window.blit(self, (0, y - self.offset_y - GRID_SIZE))


    def update(self):
        self.blit(self,(0, GRID_SIZE))
        self.fill(LIGHT_GREY, pygame.Rect(0, 0, GRID_WIDTH * GRID_SIZE, GRID_SIZE))

        self.create_one_floor(0)


    def create_one_floor(self, floor = 0):
        start = 3
        left, right = False, False
        while 1:
            i = random.randint(0, len(self.roads)-1)
            if self.roads[i]['start'] != start or (right and self.roads[i]['end'] == 0) or (left and self.roads[i]['end'] == 2): continue
            self.blit(self.roads[i]['image'], (self.floor_end * GRID_SIZE, floor * GRID_SIZE))


            if self.roads[i]['end'] == 1: break


            if not ((self.floor_end == 0 and self.roads[i]['end'] == 0) or (self.floor_end == GRID_WIDTH - 1 and self.roads[i]['end'] == 2)): 
                start = (self.roads[i]['end'] + 2) % 4
                self.floor_end += self.roads[i]['end'] - 1
                left, right = False, False
                if self.roads[i]['end'] == 2:
                    right = True
                if self.roads[i]['end'] == 0:
                    right = False


