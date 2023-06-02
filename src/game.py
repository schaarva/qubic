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
        self.eventqueue = [] # --> besteht aus einem KEY (sagt welcher Bereich) und einer INFO (was soll in dem Bereich gemacht werden)

    def handle_inputs(self):
        """Collect events."""
        """handle inputs from player"""
        
        keys = pygame.key.get_pressed()
        events = pygame.event.get() 

        """adding events to eventqueue"""

        for event in events: 
            #quit

            if event.type == pygame.QUIT: 
                self.eventqueue += [(core.SCREEN, core.QUIT)]



            #Layers
            if keys[pygame.K_UP]:
                self.eventqueue += [(core.LAYER, core.INDEPTH)]
        
            if keys[pygame.K_DOWN]: 
                self.eventqueue += [(core.LAYER, core.OUT)]
            
            #placement 
            if keys[pygame.MOUSEBUTTONDOWN]: 
                self.eventqueue += [(core.LAYER, core.PLACE)]
        print(self.eventqueue)
    
    def update(self):
        """React to events."""
        

        for event in self.eventqueue: 
            
            key, info = event

            #window quit
            if key == core.SCREEN: 
                if info == core.QUIT: 
                    self.running = False    
                    return 

            #Layer
            if key == core.LAYER: 
                if info == core.INDEPTH:
                    ...

            if key == core.LAYER: 
                if info == core.OUT: 
                    ...

            #placement 
            if key == core.LAYER: 
                if info == core.PLACE: 
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