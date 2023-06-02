"""
Qubic
~~~~~

Author: Arne
Description: Game loop
"""
import pygame

import const
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
        
        self.layer = 1

        self.running = False
        self.eventqueue = [] # --> besteht aus einem KEY (sagt welcher Bereich) und einer INFO (was soll in dem Bereich gemacht werden)

    def handle_inputs(self):
        """Collect events."""
        """handle inputs from player"""
        
        keys = pygame.key.get_pressed()
        events = pygame.event.get() 

        """adding events to eventqueue"""

        for event in events: 
            
            # Quit

            if event.type == pygame.QUIT: 
                self.eventqueue += [(const.SCREEN, const.QUIT)]

            # Layers

            if keys[pygame.K_UP]:
                self.eventqueue += [(const.LAYER, const.INDEPTH)]
        
            if keys[pygame.K_DOWN]: 
                self.eventqueue += [(const.LAYER, const.OUT)]
            
            # Placement
            
            if keys[pygame.MOUSEBUTTONDOWN]: 
                self.eventqueue += [(const.LAYER, const.PLACE)]
        
        # print(self.eventqueue)
    
    def update(self):
        """React to events."""
        

        for event in self.eventqueue: 
            
            key, info = event

            # Window quit
            if key == const.SCREEN: 
                if info == const.QUIT: 
                    self.running = False    
                    return 

            # Layer
            if key == const.LAYER: 
                if info == const.INDEPTH:
                    new = self.layer + 1 
                    if new > 3: 
                        new = 0
                    self.layer = new

             
                elif info == const.OUT: 
                    n = self.layer - 1
                    if n < 0: 
                        n = 3
                    self.layer = n

            # Placement 
            if key == const.LAYER: 
                if info == const.PLACE: 
                    ...
        
        ### Test ###

        self.field.setField([
            [
                [1, 0, -1],
                [0, 0, 1],
                [1, 0, 0]
            ],
            [
                [1, -1, -1],
                [1, -1, 1],
                [1, -1, 0]
            ],
            [
                [1, 0, 1],
                [0, -1, 1],
                [1, 0, -1]
            ]
        ])
            
    
    def render(self):
        """Update GUI images."""

        # Reset GUI

        self.screen.fill((255, 255, 255))

        # Render GUI

        surfaces = []
        
        # surfaces += self.infos.render()
        surfaces += self.field.render(self.layer)

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