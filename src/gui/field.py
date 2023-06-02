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
        
        grid = pygame.surface.Surface((1280, 720))
        grid.convert_alpha()
        grid.fill((0, 0, 0, 0))

        pygame.draw.line(grid, "orange", (320, 40), (960, 40), 10)
            # Border top
        pygame.draw.line(grid, "orange", (320, 680), (960, 680), 10)
            # Border bot
        pygame.draw.line(grid, "orange", (320, 40), (320, 680), 10)
            # Border left
        pygame.draw.line(grid, "orange", (960, 40), (960, 680), 10)
            # Border right

        return [(grid, (0, 0))]