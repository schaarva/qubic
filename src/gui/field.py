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

        pygame.draw.line(grid, "orange", (340, 260), (940, 260), 8) # Top
        pygame.draw.line(grid, "orange", (340, 460), (940, 460), 8) # Bot
        pygame.draw.line(grid, "orange", (540, 60), (540, 660), 8) # Left
        pygame.draw.line(grid, "orange", (740, 60), (740, 660), 8) # Right

        # Render crosses and circles

        

        return [(grid, (0, 0))]