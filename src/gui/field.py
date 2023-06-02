"""
Qubic
~~~~~

Author: Valentin
Description: Status bar
"""

import pygame

import const


class Field:
    """
    A class for the game field.

    Field:
         0 _
        +1 x
        -1 o

    Coordinates:
        field[z][y][x]
    """

    def __init__(self):
        
        self.field = [[[0, 0, 0]*3]*3]
        self.layer = 0
    
    def set_field(self, field):
        self.field = field
    
    def set_layer(self, layer: int):
        
        self.layer = layer

        if layer > 2:
            self.layer = 2
        
        if layer < 0:
            self.layer = 0
    
    def render(self):

        # Render grid
        
        surface_grid = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_grid.fill((0, 0, 0, 0))

        pygame.draw.rect(
            surface_grid, "black", pygame.Rect(320, 40, 640, 640), 15)
            # Border
        
        pygame.draw.line(
            surface_grid, "black", (340, 260), (940, 260), 8) # Top
        pygame.draw.line(
            surface_grid, "black", (340, 460), (940, 460), 8) # Bot
        pygame.draw.line(
            surface_grid, "black", (540, 60), (540, 660), 8) # Left
        pygame.draw.line(
            surface_grid, "black", (740, 60), (740, 660), 8) # Right

        # Render crosses and circles

        surface_signs = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_signs.fill((0, 0, 0, 0))

        for x in range(3):
            for y in range(3):
                
                if self.field[self.layer][y][x] == const.CROSS:
                    
                    pygame.draw.line(
                        surface_signs, "blue", (340+x*200+20, 60+y*200+20),
                        (340+x*200+180, 60+y*200+180), 8)
                    pygame.draw.line(
                        surface_signs, "blue", (340+x*200+180, 60+y*200+20),
                        (340+x*200+20, 60+y*200+180), 8)
                
                elif self.field[self.layer][y][x] == const.CIRCLE:
                    
                    pygame.draw.circle(
                        surface_signs, "red", (340+x*200+100, 60+y*200+100), 80, 8)

        return [(surface_grid, (0, 0)), (surface_signs, (0, 0))]