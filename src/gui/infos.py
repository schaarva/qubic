"""
Qubic
~~~~~

Author: 
Description: Status bar
"""

import pygame


class Infos:
    """A class for a status bar."""

    def __init__(self):
        
        self.fps = 0
        self.turn = 0
        self.time = (0, 0)
        self.player = True
    
    def render(self):
        return [pygame.surface.Surface((1280, 720))]