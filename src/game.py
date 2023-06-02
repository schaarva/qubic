"""
Qubic
~~~~~

Author: 
Description: Game loop
"""
import pygame
import core 

class Game:
    """The main game class."""

    def __init__(self):
        width = 1280 
        height = 720 

        #window 
        screen = pygame.display.set_mode((width, height))
        

        self.running = False
        self.eventqueue = []

    def handle_inputs(self):
        """Collect events."""
        """handle inputs from player"""
        
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        """adding events to eventqueue"""

        for event in events: 
            #Layers
            if keys[pygame.K_UP]:
                self.eventqueue += [(core.INDEPTH)]
        
            if keys[pygame.K_DOWN]: 
                self.eventqueue += [(core.OUT)]
            
            #placement 
            if keys[pygame.MOUSEBUTTONDOWN]: 
                self.eventqueue += [(core.PLACE)]
    
    def update(self):
        """React to events."""
        ...
    
    def render(self):
        """Update GUI images."""
        pygame.display.flip()

    def wait(self):
        """Wait for next frame."""
        ...
    
    def run(self):
        """Run game loop."""

        self.running = True

        # pygame.init()

        while self.running:

            self.handle_inputs()
            self.update()
            self.render()
            self.wait()
        
        # pygame.quit()