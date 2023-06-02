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
        self.field = [[[0, 0, 0]*3]*3]
    
    def render(self, layer_num: int):

        # pygame.surface.Surface((1280, 720)

        # Render grid
        
        grid = pygame.surface.Surface((1280, 720)).convert_alpha()
        grid.fill((0, 0, 0, 0))

        pygame.draw.rect(grid, "orange", pygame.Rect(320, 40, 640, 640), 15)
            # Border

        # pygame.draw.line(grid, "green", (320, 40), (960, 40), 8)

        return [(grid, (0, 0))]