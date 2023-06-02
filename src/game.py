"""
Qubic
~~~~~

Author: 
Description: Game loop
"""

import pygame

class Game:
    """The main game class."""

    def __init__(self):
        
        self.running = False
        self.eventqueue = []

    def handle_inputs(self):
        """Collect events."""
        ...
    
    def update(self):
        """React to events."""
        ...
    
    def render(self):
        """Update GUI images."""
        ...

    def wait(self):
        """Wait for next frame."""
        ...
    
    def run(self):
        """Run game loop."""

        self.running = True

        pygame.init()

        while self.running:

            self.handle_inputs()
            self.update()
            self.render()
            self.wait()
        
        pygame.quit()