#スクリーン初期化
import sys
import pygame
from pygame.locals import *
import numpy as np
import scipy as sc

screen_height = 1500
screen_width = 1000

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))
white = (255,255,255)
black = (0,0,0)

screen.fill(white)

def draw_diamond(size_diagonal, center_point, angle_rad, color_rgb):
    """ひし形描画"""
    point1 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (1/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (1/4) * np.pi) + center_point[1])

    point2 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (3/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (3/4) * np.pi) + center_point[1])

    point3 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (5/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (5/4) * np.pi) + center_point[1])

    point4 = (np.sqrt(2) * (size_diagonal / 2) * np.cos(angle_rad + (7/4) * np.pi) + center_point[0],
              np.sqrt(2) * (size_diagonal / 2) * np.sin(angle_rad + (7/4) * np.pi) + center_point[1])

    print(point1, point2, point3, point4)

    pygame.draw.polygon(screen, color_rgb, [point1, point2, point3, point4])

draw_diamond(50,(screen_height/2,screen_width/2),np.pi * 0.125,black)

#計算処理

#描画処理
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
