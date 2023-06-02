"""
Qubic
~~~~~

Author: Arne
Description: Error message
"""
import pygame 

class Error_:
    """A class for an error message window."""

    def show(self, err: Exception):
        """Show the message window."""
        self.errorScreen = pygame.display.set_mode((500, 100))
        pygame.display.flip()
        