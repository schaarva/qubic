"""
Qubic
~~~~~

Author: Valentin
Description: View perspective
"""

import pygame


class View:
    """A class for a status bar."""

    def __init__(self):
        
        self.fps = 0
        self.turn = 0
        self.time = (0, 0)
        self.player = True
    
    def render(self, layer: int):

        view = pygame.surface.Surface((1280, 720)).convert_alpha()
        view.fill((0, 0, 0, 0))

        return [(view, (0, 0))]