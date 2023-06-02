"""
Qubic
~~~~~

Author: 
Description: Error message
"""
import pygame 

class Error:
    """A class for an error message window."""

    def show(self):
        """Show the message window."""
        self.errorScreen = pygame.display.set_mode(500, 100)
        