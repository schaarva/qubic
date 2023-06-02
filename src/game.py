"""
Qubic
~~~~~

Author: 
Description: Game loop
"""
import pygame

import core
import gui.field
import gui.infos


class Game:
    """The main game class."""

    def __init__(self):

        # Engine init

        self.screen = pygame.display.set_mode((1280, 720))

        self.maxfps = 100
        self.clock = pygame.time.Clock()

        # GUI init

        self.field = gui.field.Field()
        self.infos = gui.infos.Infos()

        # Loop init

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

        # Reset GUI

        self.screen.fill((0, 0, 0))

        # Render GUI

        surfaces = []
        
        surfaces += self.field.render()
        surfaces += self.infos.render()

        # Show GUI

        self.screen.blits(surfaces)
        pygame.display.flip()

    def wait(self):
        """Wait for next frame."""
        self.clock.tick(self.maxfps)
    
    def run(self):
        """Run game loop."""

        self.running = True

        pygame.init()
        pygame.font.init()

        while self.running:

            self.handle_inputs()
            self.update()
            self.render()
            self.wait()
        
        pygame.quit()