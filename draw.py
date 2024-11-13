import sys
import pygame
from pygame.locals import *
import numpy as np
import scipy as sc
import main

main.screen.fill(main.black)

def draw_diamond(size_diagonal, center_point, angle_rad, color_rgb):
    point1 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (1/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (1/4) * np.pi) + center_point[1])

    point2 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (3/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (3/4) * np.pi) + center_point[1])

    point3 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (5/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (5/4) * np.pi) + center_point[1])

    point4 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (7/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (7/4) * np.pi) + center_point[1])

    print(point1, point2, point3, point4)

    pygame.draw.polygon(main.screen, color_rgb, [point1, point2, point3, point4])

draw_diamond(1.4,(0,0),0,main.black)