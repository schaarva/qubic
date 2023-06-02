"""
Qubic
~~~~~

Author: Valentin
Description: Start and end screen
"""

import pygame


class State:
    """A class for info screens."""

    def __init__(self):
        
        self.image = pygame.image.load("./assets/book.png").convert_alpha()
        self.state = 0
    
    def set_state(self, state: int):

        self.state = state

        if not state in (-1, 0, 1):
            self.state = 0
    
    def render(self):

        surface_state = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_state.fill((0, 0, 0, 0))

        

        return [(surface_state, (0, 0))]