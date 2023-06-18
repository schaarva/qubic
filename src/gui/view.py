"""
Qubic
~~~~~

Author: Valentin
Description: View perspective
"""

import pygame


class View:
    """A class for the view perspective."""

    def __init__(self):
        """Initialize a new view perspective."""

        self.layer = 0
    
    def set_layer(self, layer: int) -> None:
        """
        Set the layer to show.

        layer: The z-coordinate of the layer.        
        """
        
        self.layer = layer

        if layer > 2:
            self.layer = 2
        
        if layer < 0:
            self.layer = 0
    
    def render(self) -> list:
        """Render the view perspective."""

        surface_view = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_view.fill((0, 0, 0, 0))
        
        # Render marker

        if self.layer == 0:

            pygame.draw.polygon(surface_view, "red", (
                (1070, 310),
                (1082, 298),
                (1182, 298),
                (1182, 398),
                (1170, 410),
                (1070, 410)
            ))
        
        elif self.layer == 1:

            pygame.draw.polygon(surface_view, "red", (
                (1082, 298),
                (1094, 286),
                (1194, 286),
                (1194, 386),
                (1182, 398),
                (1182, 298)
            ))
        
        elif self.layer == 2:

            pygame.draw.polygon(surface_view, "red", (
                (1094, 286),
                (1105, 275),
                (1205, 275),
                (1205, 375),
                (1194, 386),
                (1194, 286)
            ))

        # Render cube

        pygame.draw.rect(
            surface_view, "black", pygame.Rect(1070, 310, 100, 100), 4)
            # Front

        pygame.draw.line(surface_view, "black", (1105, 275), (1205, 275), 4)
            # Back top
        pygame.draw.line(surface_view, "black", (1205, 275), (1205, 375), 4)
            # Back right
        pygame.draw.line(surface_view, "black", (1070, 310), (1105, 275), 4)
            # Angled left
        pygame.draw.line(surface_view, "black", (1170, 310), (1205, 275), 4)
            # Angled middle
        pygame.draw.line(surface_view, "black", (1170, 410), (1205, 375), 4)
            # Angled right
        
        return [(surface_view, (0, 0))]