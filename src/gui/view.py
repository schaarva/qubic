"""
Qubic
~~~~~

Author: Valentin
Description: View perspective
"""

import pygame


class View:
    """A class for the view perspective."""
    
    def render(self, layer: int):

        view = pygame.surface.Surface((1280, 720)).convert_alpha()
        view.fill((0, 0, 0, 0))
        
        # Render marker

        if layer == 0:

            pygame.draw.polygon(view, "red", (
                (1070, 310),
                (1082, 298),
                (1182, 298),
                (1182, 398),
                (1170, 410),
                (1070, 410)
            ))
        
        elif layer == 1:

            pygame.draw.polygon(view, "red", (
                (1082, 298),
                (1094, 286),
                (1194, 286),
                (1194, 386),
                (1182, 398),
                (1182, 298)
            ))
        
        elif layer == 2:

            pygame.draw.polygon(view, "red", (
                (1094, 286),
                (1105, 275),
                (1205, 275),
                (1205, 375),
                (1194, 386),
                (1194, 286)
            ))

        # Render cube

        pygame.draw.rect(view, "black", pygame.Rect(1070, 310, 100, 100), 4)
            # Front

        pygame.draw.line(view, "black", (1105, 275), (1205, 275), 4)
            # Back top
        pygame.draw.line(view, "black", (1205, 275), (1205, 375), 4)
            # Back right
        pygame.draw.line(view, "black", (1070, 310), (1105, 275), 4)
            # Angled left
        pygame.draw.line(view, "black", (1170, 310), (1205, 275), 4)
            # Angled middle
        pygame.draw.line(view, "black", (1170, 410), (1205, 375), 4)
            # Angled right
        
        return [(view, (0, 0))]