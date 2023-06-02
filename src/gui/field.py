"""
Qubic
~~~~~

Author: 
Description: Status bar
"""

import pygame


class Field:
    """A class for a status bar."""

    def __init__(self):
        
        self.field = [[[None]*3]*3]
    
    def render(self):
        return [(pygame.surface.Surface((1280, 720)), (0, 0))]