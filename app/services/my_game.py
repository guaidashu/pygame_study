"""
author songjie
"""
import time

import pygame

from tool.lib.function import debug

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


class MyGame(object):
    def __init__(self):
        self.game = pygame
        self.game.init()
        self.game.font.init()
        self.screen = self.game.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.game.display.set_caption("这是标题")

    def __del__(self):
        pass

    def run(self):
        debug("ok")
