"""
Qubic
~~~~~

Author: Valentin
Description: Help icon
"""

import pygame


class Help:
    """A class for a help icon."""

    def __init__(self):
        """Initializes a new help icon."""

        self.image = pygame.image.load("./assets/images/book.png").convert_alpha()
    
    def render(self) -> list:
        """Render the help icon."""

        surface_help = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_help.fill((0, 0, 0, 0))

        pygame.draw.rect(surface_help, "black", pygame.Rect(90, 290, 140, 140), 4)

        return [
            (surface_help, (0, 0)),
            (self.image, (112, 312))
        ]