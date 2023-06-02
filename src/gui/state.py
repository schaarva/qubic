"""
Qubic
~~~~~

Author: Valentin
Description: Start and end screen
"""

import pygame


class State:
    """A class for info screens."""

    def __init__(self):

        self.state = 0
        self.win = 0
        
        self.image_welcome = pygame.image.load(
            "./assets/images/welcome.png").convert_alpha()
        self.image_loss = pygame.image.load(
            "./assets/images/loss.png").convert_alpha()
        self.image_win = pygame.image.load(
            "./assets/images/win.png").convert_alpha()
        self.image_draft = pygame.image.load(
            "./assets/images/draft.png").convert_alpha()
    
    def set_state(self, state: int):

        self.state = state

        if not state in (-1, 0, 1):
            self.state = 0
    
    def set_win(self, win: int):

        self.win = win

        if not win in (-1, 0, 1):
            self.win = 0
    
    def render(self):

        surface_state = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_state.fill((0, 0, 0, 0))

        if self.state == -1:

            if self.win == -1:
                surface_state = self.image_loss
            
            elif self.win == 0:
                surface_state = self.image_draft
            
            elif self.win == 1:
                surface_state = self.image_win
        
        elif self.state == 1:
            surface_state = self.image_welcome

        return [(surface_state, (0, 0))]