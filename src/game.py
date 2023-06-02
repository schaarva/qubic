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
import gui.view
import gui.help


class Game:
    """The main game class."""

    def __init__(self):
        
        # Engine init

        pygame.font.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Qubic")

        self.maxfps = 100
        self.clock = pygame.time.Clock()
        
        # GUI init

        self.field = gui.field.Field()
        self.infos = gui.infos.Infos()
        self.view = gui.view.View()
        self.help = gui.help.Help()

        # Loop init
        
        self.layer = 0
        self.player = True
        self.state = 1 # 1 - Ready, 0 - Play, -1 - End

        self.running = False
        self.eventqueue = [] # Besteht aus einem KEY (sagt, welcher Bereich) 
                             # und einer INFO (was soll in dem Bereich gemacht 
                             # werden)

    def handle_inputs(self):
        """Collect events."""
        
        # Handle inputs from player
        
        keys = pygame.key.get_pressed()
        events = pygame.event.get() 

        # Adding events to eventqueue

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
    
    def update(self):
        """React to events."""
        
        # Update by events

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
                    
                    self.layer = self.layer + 1 
                    
                    if self.layer > 2: 
                        self.layer = 0

                elif info == const.OUT: 
                    
                    self.layer = self.layer - 1
                    
                    if self.layer < 0: 
                        self.layer = 2

            # Placement 
            if key == const.LAYER: 
                if info == const.PLACE: 
                    ...

        # Update by time or state
        
        elapsed_time = self.clock.get_time() / 1_000

        self.view.set_layer(self.layer)

        self.field.set_layer(self.layer)

        curr_millis = pygame.time.get_ticks()
        curr_minutes, curr_millis = divmod(curr_millis, 60_000)
        curr_seconds, curr_millis = divmod(curr_millis, 1_000)
        self.infos.set_time(curr_minutes, curr_seconds)

        fps = self.clock.get_fps()
        self.infos.set_fps(int(fps))

        self.field.set_field([
            [
                [-1, 0, -1],
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
        ]) # DEBUG
    
    def render(self):
        """Update GUI images."""

        # Reset GUI

        self.screen.fill((255, 255, 255))
        surfaces = []

        # Render GUI

        surfaces += self.infos.render()
        surfaces += self.help.render()
        surfaces += self.field.render()
        surfaces += self.view.render()

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

        while self.running:

            self.handle_inputs()
            self.update()
            self.render()
            self.wait()
        
        pygame.quit()